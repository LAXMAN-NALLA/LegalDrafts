"""
FastAPI Web API for Legal Document Generator
HOCEBRANCH Modular Legal Engine
"""

import os
from datetime import datetime
from typing import Optional, Union, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# Import the Prompt Library
from prompts import PROMPT_MAP, CORE_LEGAL_BRAIN

# Load environment variables from .env file
load_dotenv()

app = FastAPI(title="HOCEBRANCH Modular Legal Engine", version="2.0.0")

# Get configuration from environment variables
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")
OPENAI_TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE", "0.2"))

# Security: Use a low temperature for consistent, non-creative legal text
llm = ChatOpenAI(model=OPENAI_MODEL, temperature=OPENAI_TEMPERATURE)

# --- 1. DATA MODELS (Strict Input Validation) ---
class LegalRequest(BaseModel):
    template_type: str = Field(..., pattern="^(nda|employment|service|terms|board|shareholder)$", description="Type of legal document to generate")
    company_name: str = Field(..., description="Full legal name of the company")
    registration_number: str = Field(..., description="Company registration number")
    registered_address: Union[str, dict] = Field(..., description="Company registered address (string or object)")
    directors: Optional[Union[str, List[str], List[dict]]] = Field(None, description="Directors list (string, list of strings, or list of objects)")
    country: Optional[str] = Field(None, description="Jurisdiction/Country (e.g., 'India', 'USA', 'UK')")
    corporate_context: Optional[str] = Field(None, description="Business context (e.g., 'SaaS Platform', 'Frozen Food Mfg', 'Construction Service'). Additional details can be included here.")

    # Validators to clean up data before AI sees it
    @field_validator('registered_address')
    def normalize_address(cls, v):
        if isinstance(v, dict):
            # Convert {"city": "Hyd", "country": "IN"} -> "Hyd, IN"
            parts = [v.get('line'), v.get('city'), v.get('postal_code'), v.get('country')]
            return ", ".join([p for p in parts if p])
        return v

    @field_validator('directors')
    def normalize_directors(cls, v):
        # Convert [{"name": "Ali"}] -> ["Ali"]
        if isinstance(v, list) and len(v) > 0 and isinstance(v[0], dict):
            return [d.get('name') for d in v if d.get('name')]
        # Convert "Ali, Onur" -> ["Ali", "Onur"]
        if isinstance(v, str):
            return [d.strip() for d in v.split(',') if d.strip()]
        return v if v else []


# Prompt templates are now imported from prompts.py


@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "service": "HOCEBRANCH Modular Legal Engine",
        "version": "2.0.0",
        "endpoints": {
            "generate": "/api/generate-legal-draft",
            "health": "/health"
        },
        "supported_templates": ["nda", "employment", "service", "terms", "board", "shareholder"]
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "legal-document-generator"}


@app.post("/api/generate-legal-draft")
async def generate_draft(request: LegalRequest):
    """
    Generate a legal document based on the provided parameters.
    
    Returns a legally binding document tailored to the corporate context and jurisdiction.
    """
    try:
        # Check if OpenAI API key is set
        if not os.getenv("OPENAI_API_KEY"):
            raise HTTPException(
                status_code=500,
                detail="OPENAI_API_KEY environment variable is not set. Please set it in your .env file or as an environment variable."
            )

        # A. Logic Processing
        # 1. Signer Logic
        if isinstance(request.directors, list) and len(request.directors) > 0:
            signer = request.directors[0]
            directors_str = ", ".join(request.directors)
        else:
            signer = "Authorized Signatory"
            directors_str = "[Directors Listed in Registry]"

        # 2. Country Logic (Priority: Input > Address > Default)
        country = request.country
        if not country:
            # Try to infer from address
            address_str = str(request.registered_address).lower()
            if "india" in address_str or "bangalore" in address_str or "mumbai" in address_str or "delhi" in address_str:
                country = "India"
            elif "usa" in address_str or "united states" in address_str or "california" in address_str or "new york" in address_str:
                country = "USA"
            elif "uk" in address_str or "united kingdom" in address_str or "london" in address_str:
                country = "UK"
            elif "netherlands" in address_str or "amsterdam" in address_str:
                country = "Netherlands"
        
        if not country:
            country = "International Jurisdiction"

        # 3. Context Logic
        context = request.corporate_context or "General Business"

        # B. Select the Correct Prompt Template
        template_type_lower = request.template_type.lower()
        template_upper = request.template_type.upper()
        raw_prompt_template = PROMPT_MAP.get(template_type_lower)
        if not raw_prompt_template:
            raise HTTPException(status_code=400, detail=f"Invalid template type: {request.template_type}")

        # C. Inject User Data directly into the Prompt String using .format()
        # This makes the instructions to the AI incredibly clear and reduces hallucination
        # Note: We ONLY pass the core fields. AI will extract details from corporate_context or use placeholders
        formatted_system_prompt = raw_prompt_template.format(
            core_instructions=CORE_LEGAL_BRAIN,
            company_name=request.company_name,
            registration_number=request.registration_number,
            registered_address=request.registered_address,
            signer=signer,
            country=country,
            corporate_context=context,
            date_today=datetime.now().strftime("%B %d, %Y")
        )

        # D. Send to AI
        # Since we pre-formatted the prompt with data, we don't need complex variable inputs here
        prompt = ChatPromptTemplate.from_messages([
            ("system", formatted_system_prompt),
            ("human", "Generate the document now.")
        ])

        chain = prompt | llm | StrOutputParser()
        result = chain.invoke({})  # No variables needed, already baked into the prompt!

        return {
            "success": True,
            "draft_content": result,
            "metadata": {
                "template_type": template_upper,
                "applied_law": country,
                "applied_context": context,
                "company": request.company_name,
                "signer": signer
            }
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating document: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    # Render uses $PORT environment variable, fallback to 8000 for local development
    api_host = os.getenv("API_HOST", "0.0.0.0")
    api_port = int(os.getenv("PORT", os.getenv("API_PORT", "8000")))
    uvicorn.run(app, host=api_host, port=api_port)

