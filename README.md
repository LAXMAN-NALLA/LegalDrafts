# Legal Document Generator

A LangChain-based application for generating legally binding documents tailored to specific corporate contexts and jurisdictions.

## 🚀 Quick Deploy to Render

**Deploy in 5 minutes:**
1. Push code to GitHub
2. Go to [Render Dashboard](https://dashboard.render.com)
3. Create new Web Service
4. Connect GitHub repo
5. Add `OPENAI_API_KEY` environment variable
6. Deploy!

See the Render Dashboard for deployment configuration. The service uses `render.yaml` for automatic configuration.

## Features

- **Multiple Document Types**: NDA, Employment, Service, Terms, Board Resolutions, Shareholder Resolutions
- **Context-Aware**: Adapts clauses based on corporate context (Tech/SaaS, Manufacturing, Service/Consulting, etc.)
- **Jurisdiction Compliance**: Cites appropriate laws based on country (India, USA, UK, etc.)
- **Strict Formatting**: Follows exact document structure while adapting content

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
   
   **Option A: Using .env file (Recommended)**
   ```bash
   # Copy the example file
   cp env.example .env
   
   # Edit .env and add your API key
   # OPENAI_API_KEY=your-actual-api-key-here
   ```
   
   **Option B: Using environment variables directly**
   ```bash
   # On Linux/Mac:
   export OPENAI_API_KEY='your-api-key-here'
   
   # On Windows (PowerShell):
   $env:OPENAI_API_KEY='your-api-key-here'
   
   # On Windows (CMD):
   set OPENAI_API_KEY=your-api-key-here
   ```
   
   The `.env` file is automatically loaded by the application. Make sure to add your actual API key to the `.env` file.

## Usage

### Option 1: FastAPI Web Service (Recommended for Production)

Start the API server:
```bash
uvicorn api:app --reload
```

The API will be available at `http://localhost:8000`

**API Endpoints:**
- `GET /` - API information
- `GET /health` - Health check
- `POST /api/generate-legal-draft` - Generate legal document

**Example API Request:**
```bash
curl -X POST "http://localhost:8000/api/generate-legal-draft" \
  -H "Content-Type: application/json" \
  -d '{
    "template_type": "nda",
    "company_name": "TechCorp India Pvt Ltd",
    "registration_number": "U72900KA2020PTC123456",
    "registered_address": "123 Business Park, Bangalore, Karnataka 560001",
    "directors": ["John Doe"],
    "country": "India",
    "corporate_context": "SaaS AI Platform - NDA with ABC Consulting Services for software development partnership"
  }'
```

**Note:** Additional details (like counterparty names, employee details, etc.) can be included in the `corporate_context` field. The AI will extract and use relevant information from this field.

**Python Client Example:**
```python
import requests

response = requests.post("http://localhost:8000/api/generate-legal-draft", json={
    "template_type": "nda",
    "company_name": "TechCorp India Pvt Ltd",
    "registration_number": "U72900KA2020PTC123456",
    "registered_address": "123 Business Park, Bangalore, Karnataka 560001",
    "directors": ["John Doe"],
    "country": "India",
    "corporate_context": "SaaS AI Platform - NDA with ABC Consulting Services for software development partnership"
})

result = response.json()
print(result["draft_content"])
```

### Option 2: Direct Python Function

```python
from main import generate_document

document = generate_document(
    template_type="NDA",
    corporate_context="SaaS AI Platform",
    country="India",
    company_name="TechCorp India Pvt Ltd",
    registered_address="123 Business Park, Bangalore, Karnataka 560001",
    reg_number="U72900KA2020PTC123456",
    signer="John Doe",
    counterparty_name="ABC Consulting Services"
)

print(document)
```

### Available Template Types

- **NDA**: Non-Disclosure Agreement
- **Employment**: Employment Agreement
- **Service**: Master Service Agreement
- **Terms**: General Terms & Conditions
- **Board**: Board Resolution
- **Shareholder**: Shareholder Resolution

### Parameters

#### Required Parameters:
- `template_type`: Type of document to generate (nda, employment, service, terms, board, shareholder)
- `company_name`: Full legal name of the company
- `registration_number`: Company registration number
- `registered_address`: Registered address of the company (string or object)

#### Optional Parameters:
- `directors`: Directors list (string, list of strings, or list of objects)
- `country`: Jurisdiction/Country (e.g., "India", "USA", "UK"). If not provided, will be inferred from address.
- `corporate_context`: Business context and additional details (e.g., "SaaS AI Platform", "Frozen Food Manufacturing - NDA with ABC Corp for supply chain partnership"). 
  - **Important:** You can include specific details here like counterparty names, employee details, job titles, salary information, resolution details, etc. The AI will extract and use relevant information from this field.

**Note:** The model is simplified to use only core fields. Additional details should be included in the `corporate_context` field, and the AI will intelligently extract and use them in the generated document.

## Examples

### Example 1: Employment Agreement

```python
import requests

response = requests.post("http://localhost:8000/api/generate-legal-draft", json={
    "template_type": "employment",
    "company_name": "InnovateTech Inc.",
    "registration_number": "DE123456",
    "registered_address": "456 Silicon Valley, CA 94000",
    "directors": ["Jane Smith"],
    "country": "USA",
    "corporate_context": "Tech/SaaS - Employment agreement for Bob Johnson as Senior Software Engineer with salary $150,000 per annum plus stock options"
})
```

### Example 2: Service Agreement

```python
import requests

response = requests.post("http://localhost:8000/api/generate-legal-draft", json={
    "template_type": "service",
    "company_name": "BuildRight Ltd",
    "registration_number": "12345678",
    "registered_address": "789 London Street, London, UK",
    "directors": ["David Brown"],
    "country": "UK",
    "corporate_context": "Construction Service - Master Service Agreement with Construction Services Pro Ltd for project management and construction services"
})
```

### Example 3: Board Resolution

```python
import requests

response = requests.post("http://localhost:8000/api/generate-legal-draft", json={
    "template_type": "board",
    "company_name": "FoodCorp India Pvt Ltd",
    "registration_number": "U15100MH2010PTC123456",
    "registered_address": "321 Industrial Area, Mumbai, Maharashtra 400001",
    "directors": ["Rajesh Kumar"],
    "country": "India",
    "corporate_context": "Frozen Food Manufacturing - Board resolution for approval of expansion of manufacturing facility and procurement of new cold storage equipment worth INR 50 crores"
})
```

## Document Structure

The generator follows strict document structures defined in the system prompt:

- **NDA**: 10 sections including Purpose, Confidential Information, Obligations, Duration, Governing Law
- **Employment**: 9 sections including Position, Compensation, Confidentiality, IP Assignment, Termination
- **Service**: 8 sections including Scope, Fees, Independent Contractor status, Liability
- **Terms**: 9 sections including Services, User Obligations, Payment & Taxes, Liability & Warranty
- **Board/Shareholder**: Resolution format with authorization clauses

## Context Adaptation

The generator automatically adapts clauses based on corporate context:

- **Tech/SaaS**: Protects Source Code, Algorithms, User Data; limits liability for Data Loss, Server Downtime
- **Manufacturing/Food**: Protects Recipes, Formulas, Supplier Lists; mentions Product Safety, Shipping Terms
- **Service/Consulting**: Limits liability to Professional Negligence; defines Deliverables vs Background IP

## Jurisdiction Compliance

The generator cites appropriate laws:

- **India**: Information Technology Act 2000, Indian Contract Act 1872, Arbitration and Conciliation Act 1996
- **USA**: State-specific laws (default: Delaware), At-Will Employment provisions
- **UK/EU**: GDPR, Contracts (Rights of Third Parties) Act 1999

## API Features

The FastAPI version (`api.py`) includes:

- **Input Validation**: Pydantic models ensure all inputs are validated
- **Flexible Address Format**: Accepts string or object format for addresses
- **Smart Director Handling**: Accepts string, list of strings, or list of objects
- **Country Inference**: Automatically infers country from address if not specified
- **Template-Specific Fields**: Handles optional fields based on document type
- **Error Handling**: Comprehensive error handling with meaningful messages

## Notes

- Always review generated documents with a qualified legal professional before use
- Documents are generated based on templates and may require customization
- Ensure all placeholders are filled before finalizing documents
- The system uses GPT-4o by default for higher quality output (in API) or GPT-4 (in main.py)
- The API version uses temperature 0.2 for more consistent legal text

## License

This project is provided as-is for educational and development purposes.

#   L e g a l _ D r a f t s  
 #   L e g a l _ D r a f t s  
 #   L e g a l _ D r a f t s  
 #   L e g a l D r a f t s  
 