# Sample Inputs for Legal Document Generator

## Quick Reference

All requests use the same core structure with only these fields:
- `template_type` (required)
- `company_name` (required)
- `registration_number` (required)
- `registered_address` (required)
- `directors` (optional)
- `country` (optional - will be inferred from address if not provided)
- `corporate_context` (optional - but recommended for better results)

---

## 1. NDA (Non-Disclosure Agreement)

### Basic NDA
```json
{
  "template_type": "nda",
  "company_name": "TechCorp India Pvt Ltd",
  "registration_number": "U72900KA2020PTC123456",
  "registered_address": "123 Business Park, Whitefield, Bangalore, Karnataka 560066",
  "directors": ["John Doe"],
  "country": "India",
  "corporate_context": "SaaS AI Platform"
}
```

### NDA with Specific Counterparty (in corporate_context)
```json
{
  "template_type": "nda",
  "company_name": "Global Manufacturing Inc.",
  "registration_number": "DE987654",
  "registered_address": "456 Industrial Way, Detroit, Michigan 48201, USA",
  "directors": ["Robert Johnson"],
  "country": "USA",
  "corporate_context": "Frozen Food Manufacturing - NDA with ABC Supply Chain Solutions LLC for supply chain partnership and recipe sharing"
}
```

### NDA for Tech Company (UK)
```json
{
  "template_type": "nda",
  "company_name": "CloudSoft UK Ltd",
  "registration_number": "12345678",
  "registered_address": "789 Tech Street, London, UK, EC1A 1BB",
  "directors": ["Emma Wilson"],
  "country": "UK",
  "corporate_context": "Cloud Computing Services - NDA with XYZ Consulting for software development partnership"
}
```

---

## 2. Employment Agreement

### Basic Employment
```json
{
  "template_type": "employment",
  "company_name": "InnovateTech Inc.",
  "registration_number": "DE123456",
  "registered_address": "789 Silicon Valley Blvd, San Francisco, CA 94000",
  "directors": ["Jane Smith"],
  "country": "USA",
  "corporate_context": "Tech/SaaS"
}
```

### Employment with Specific Details (in corporate_context)
```json
{
  "template_type": "employment",
  "company_name": "Strategic Consulting Ltd",
  "registration_number": "87654321",
  "registered_address": "10 Downing Street, London, UK, SW1A 2AA",
  "directors": ["David Brown"],
  "country": "UK",
  "corporate_context": "Management Consulting - Hiring Sarah Williams as Senior Consultant for £75,000 per annum with health benefits and 25 days annual leave"
}
```

### Employment for Tech Company (India)
```json
{
  "template_type": "employment",
  "company_name": "IT Solutions India Pvt Ltd",
  "registration_number": "U74140MH2010PTC123456",
  "registered_address": "456 IT Park, Sector 18, Noida, Uttar Pradesh 201301",
  "directors": ["Priya Sharma"],
  "country": "India",
  "corporate_context": "Software Development - Hiring Rajesh Kumar as Senior Software Engineer for INR 15,00,000 per annum with stock options"
}
```

---

## 3. Service Agreement

### Basic Service Agreement
```json
{
  "template_type": "service",
  "company_name": "BuildRight Construction Ltd",
  "registration_number": "87654321",
  "registered_address": "789 London Street, London, UK, EC1A 1BB",
  "directors": ["David Brown"],
  "country": "UK",
  "corporate_context": "Construction Service"
}
```

### Service Agreement with Provider Details
```json
{
  "template_type": "service",
  "company_name": "TechCorp India Pvt Ltd",
  "registration_number": "U72900KA2020PTC123456",
  "registered_address": "123 Business Park, Bangalore, Karnataka 560066",
  "directors": ["John Doe"],
  "country": "India",
  "corporate_context": "IT Services - Master Service Agreement with ABC Tech Services for software development, maintenance, and technical support services"
}
```

### Service Agreement for Consulting (USA)
```json
{
  "template_type": "service",
  "company_name": "Business Solutions Inc.",
  "registration_number": "DE555666",
  "registered_address": "321 Corporate Avenue, New York, NY 10001",
  "directors": ["Michael Chen"],
  "country": "USA",
  "corporate_context": "Management Consulting - Service agreement with Strategic Advisors LLC for business consulting and advisory services"
}
```

---

## 4. Terms & Conditions

### Basic Terms (E-commerce)
```json
{
  "template_type": "terms",
  "company_name": "ShopEasy India Pvt Ltd",
  "registration_number": "U74999DL2015PTC123456",
  "registered_address": "456 Market Street, Connaught Place, New Delhi, Delhi 110001",
  "directors": ["Priya Sharma"],
  "country": "India",
  "corporate_context": "E-commerce Platform"
}
```

### Terms for SaaS Platform (USA)
```json
{
  "template_type": "terms",
  "company_name": "CloudSoft Inc.",
  "registration_number": "DE555666",
  "registered_address": "321 Cloud Avenue, Austin, Texas 78701",
  "directors": ["Alex Martinez"],
  "country": "USA",
  "corporate_context": "SaaS Platform - Cloud-based project management software with subscription billing"
}
```

### Terms for EU/UK (with mandatory consumer rights)
```json
{
  "template_type": "terms",
  "company_name": "EuroShop Ltd",
  "registration_number": "98765432",
  "registered_address": "555 High Street, Manchester, UK, M1 1AA",
  "directors": ["James Anderson"],
  "country": "UK",
  "corporate_context": "E-commerce Platform - Online marketplace for consumer products"
}
```

---

## 5. Board Resolution

### Basic Board Resolution
```json
{
  "template_type": "board",
  "company_name": "FoodCorp India Pvt Ltd",
  "registration_number": "U15100MH2010PTC123456",
  "registered_address": "321 Industrial Area, Andheri East, Mumbai, Maharashtra 400069",
  "directors": ["Rajesh Kumar"],
  "country": "India",
  "corporate_context": "Frozen Food Manufacturing"
}
```

### Board Resolution with Specific Purpose
```json
{
  "template_type": "board",
  "company_name": "StartupTech Inc.",
  "registration_number": "DE111222",
  "registered_address": "100 Innovation Drive, Palo Alto, CA 94301",
  "directors": ["Mark Zuckerberg"],
  "country": "USA",
  "corporate_context": "Tech Startup - Board resolution for approval of Series A funding round of $5 million and issuance of preferred shares to investors"
}
```

### Board Resolution for Expansion
```json
{
  "template_type": "board",
  "company_name": "Manufacturing Corp India Pvt Ltd",
  "registration_number": "U24240GJ2010PTC123456",
  "registered_address": "789 Industrial Estate, Ahmedabad, Gujarat 380001",
  "directors": ["Vikram Singh"],
  "country": "India",
  "corporate_context": "Textile Manufacturing - Board resolution for approval of expansion of manufacturing facility and procurement of new machinery worth INR 50 crores"
}
```

---

## 6. Shareholder Resolution

### Basic Shareholder Resolution
```json
{
  "template_type": "shareholder",
  "company_name": "Service Excellence Ltd",
  "registration_number": "98765432",
  "registered_address": "555 Business Centre, Manchester, UK, M1 1AA",
  "directors": ["James Anderson"],
  "country": "UK",
  "corporate_context": "Professional Services"
}
```

### Shareholder Resolution for Dividends
```json
{
  "template_type": "shareholder",
  "company_name": "Manufacturing Corp India Pvt Ltd",
  "registration_number": "U24240GJ2010PTC123456",
  "registered_address": "789 Industrial Estate, Ahmedabad, Gujarat 380001",
  "directors": ["Vikram Singh"],
  "country": "India",
  "corporate_context": "Textile Manufacturing - Shareholder resolution for approval of dividend distribution of INR 10 per share for the financial year 2023-24"
}
```

### Shareholder Resolution for Director Appointment
```json
{
  "template_type": "shareholder",
  "company_name": "TechCorp India Pvt Ltd",
  "registration_number": "U72900KA2020PTC123456",
  "registered_address": "123 Business Park, Bangalore, Karnataka 560066",
  "directors": ["John Doe"],
  "country": "India",
  "corporate_context": "SaaS AI Platform - Shareholder resolution for appointment of Jane Smith as Independent Director and increase in authorized share capital"
}
```

---

## Advanced Examples

### Using Flexible Address Format (Object)
```json
{
  "template_type": "nda",
  "company_name": "FlexiCorp Pvt Ltd",
  "registration_number": "U12345KA2020PTC111111",
  "registered_address": {
    "line": "456 Corporate Tower",
    "city": "Bangalore",
    "postal_code": "560001",
    "country": "India"
  },
  "directors": ["Flexi Director"],
  "country": "India",
  "corporate_context": "General Business"
}
```

### Using Directors as String
```json
{
  "template_type": "employment",
  "company_name": "StringDirectors Corp",
  "registration_number": "U22222MH2020PTC222222",
  "registered_address": "789 Business Street, Mumbai, Maharashtra 400001",
  "directors": "Ali Khan, Onur Yilmaz, Maria Garcia",
  "country": "India",
  "corporate_context": "Tech Services - Hiring Bob Johnson as CTO for $200,000 per annum"
}
```

### Using Directors as List of Objects
```json
{
  "template_type": "board",
  "company_name": "ObjectDirectors Corp",
  "registration_number": "U33333DL2020PTC333333",
  "registered_address": "321 Office Complex, New Delhi, Delhi 110001",
  "directors": [
    {"name": "Ali Khan", "designation": "CEO"},
    {"name": "Onur Yilmaz", "designation": "CTO"}
  ],
  "country": "India",
  "corporate_context": "Technology Services - Board resolution for strategic partnership agreement"
}
```

### Minimal Required Fields Only
```json
{
  "template_type": "terms",
  "company_name": "Minimal Corp",
  "registration_number": "MIN123456",
  "registered_address": "123 Main Street, City, Country 12345"
}
```

### Country Inference from Address
```json
{
  "template_type": "nda",
  "company_name": "InferTech India Pvt Ltd",
  "registration_number": "U72900KA2020PTC999999",
  "registered_address": "123 Tech Park, Hyderabad, Telangana 500081",
  "directors": ["Ravi Kumar"],
  "corporate_context": "Software Development - NDA with ABC Corp"
}
```
*Note: Country will be automatically inferred as "India" from the address*

---

## Using with cURL

### Example: Generate NDA
```bash
curl -X POST "http://localhost:8000/api/generate-legal-draft" \
  -H "Content-Type: application/json" \
  -d '{
    "template_type": "nda",
    "company_name": "TechCorp India Pvt Ltd",
    "registration_number": "U72900KA2020PTC123456",
    "registered_address": "123 Business Park, Bangalore, Karnataka 560066",
    "directors": ["John Doe"],
    "country": "India",
    "corporate_context": "SaaS AI Platform - NDA with ABC Consulting Services for software development partnership"
  }'
```

### Example: Generate Employment Agreement
```bash
curl -X POST "http://localhost:8000/api/generate-legal-draft" \
  -H "Content-Type: application/json" \
  -d '{
    "template_type": "employment",
    "company_name": "InnovateTech Inc.",
    "registration_number": "DE123456",
    "registered_address": "789 Silicon Valley Blvd, San Francisco, CA 94000",
    "directors": ["Jane Smith"],
    "country": "USA",
    "corporate_context": "Tech/SaaS - Hiring Bob Johnson as Senior Software Engineer for $150,000 per annum plus stock options"
  }'
```

---

## Using with Python

```python
import requests

# Example 1: NDA
response = requests.post("http://localhost:8000/api/generate-legal-draft", json={
    "template_type": "nda",
    "company_name": "TechCorp India Pvt Ltd",
    "registration_number": "U72900KA2020PTC123456",
    "registered_address": "123 Business Park, Bangalore, Karnataka 560066",
    "directors": ["John Doe"],
    "country": "India",
    "corporate_context": "SaaS AI Platform - NDA with ABC Consulting Services"
})

result = response.json()
print(result["draft_content"])

# Example 2: Employment with details in context
response = requests.post("http://localhost:8000/api/generate-legal-draft", json={
    "template_type": "employment",
    "company_name": "Strategic Consulting Ltd",
    "registration_number": "12345678",
    "registered_address": "10 Downing Street, London, UK, SW1A 2AA",
    "directors": ["David Brown"],
    "country": "UK",
    "corporate_context": "Management Consulting - Hiring Sarah Williams as Senior Consultant for £75,000 per annum"
})

result = response.json()
print(result["draft_content"])
```

---

## Tips for Best Results

1. **Be Specific in corporate_context**: Include details like:
   - Counterparty names
   - Employee names, job titles, salaries
   - Service provider names
   - Resolution details
   - Specific business purposes

2. **Country is Optional**: If not provided, it will be inferred from the address

3. **Directors Format**: You can use:
   - String: `"directors": "John Doe, Jane Smith"`
   - List: `"directors": ["John Doe", "Jane Smith"]`
   - List of objects: `"directors": [{"name": "John Doe"}]`

4. **Address Format**: You can use:
   - String: `"registered_address": "123 Main St, City, Country"`
   - Object: `"registered_address": {"line": "123 Main St", "city": "City", "postal_code": "12345", "country": "Country"}`

5. **EU/UK Compliance**: For Terms & Conditions in UK/EU, the system automatically includes the mandatory 14-day Right of Withdrawal

