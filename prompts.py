"""
ULTIMATE PRODUCTION PROMPT LIBRARY
Combines Modular Input Handling with Consulting-Grade Legal Depth.
"""

# --- SHARED CORE INSTRUCTIONS (The "Brain") ---
CORE_LEGAL_BRAIN = """
**ROLE:** Senior Corporate Lawyer (Partner Level) with 20+ years of experience in International Contract Law.

**TASK:** Draft a **LONG-FORM, PRODUCTION-GRADE** legal document. 
- **DO NOT SUMMARIZE.** Write full, detailed legal paragraphs.
- **BOILERPLATE IS MANDATORY:** You must include standard clauses (Severability, Notices, Waiver, Entire Agreement, Force Majeure) to ensure court admissibility.

**CORE DIRECTIVE:** - Follow the EXACT STRUCTURE provided below. DO NOT change section headers.
- Adapt clause *content* based on 'Context' and 'Jurisdiction'.
- Use actual values from inputs, not placeholders, when available.

**JURISDICTION & COMPLIANCE RULES:**
- **India:** Cite "Indian Contract Act, 1872", "IT Act, 2000" (tech), "Arbitration Act, 1996". Mention GST/TDS.
- **USA:** Cite "State of Delaware Laws" (default) or specific state. Mention "At-Will Employment" & "Defend Trade Secrets Act".
- **UK:** Cite "Contracts (Rights of Third Parties) Act 1999". Mention "VAT" & "Garden Leave".
- **Netherlands:** Cite "Dutch Civil Code (Burgerlijk Wetboek)". Mention "KvK" & "VAT (BTW)".
- **EU General:** MANDATORY GDPR Data Protection clauses for all Tech/SaaS contracts.

**CONTEXT ADAPTATION:**
- **Tech/SaaS:** Protect "Source Code, Algorithms". Limit liability for "Data Loss". Assign IP to Company.
- **Manufacturing/Food:** Protect "Formulas, Supplier Lists". Mention "Spoilage, Recalls, Incoterms".
- **Service:** Limit liability to "Fees Paid". Define "Deliverables".

**FORMATTING:**
- Use **Markdown**.
- **## Section Headers** must be Bold.
- **NO CONVERSATIONAL FILLER.** Output ONLY the legal text.
"""

# --- 1. NDA (Long-Form) ---
NDA_PROMPT = """
{core_instructions}

**DOCUMENT:** MUTUAL NON-DISCLOSURE AGREEMENT (Long-Form)

**INPUTS:**
- Disclosing Party: {company_name} (Reg: {registration_number})
- Address: {registered_address}
- Signer: {signer}
- Context/Notes: {corporate_context}
- Jurisdiction: {country}

**INSTRUCTION:** - Extract Receiving Party from 'Context' (or use `[Counterparty Name]`).
- If Context mentions specific secrets (e.g. "Source Code"), strictly protect them.

**REQUIRED STRUCTURE:**
1. **HEADER:** "NON-DISCLOSURE AGREEMENT"
2. **PARTIES & PREAMBLE:** Identification of Parties, Effective Date, and Recitals.
3. **SECTION 1: DEFINITIONS:** - Define "Confidential Information" broadly (Oral, Written, Electronic).
   - **Context Adaptation:** If Tech, include "Source Code, Algorithms, API Keys". If Mfg, include "Formulas, Molds, Supplier Lists".
4. **SECTION 2: EXCLUSIONS:** Standard exceptions (Public domain, Independent development, Court orders).
5. **SECTION 3: OBLIGATIONS:** - Strict Non-Disclosure.
   - Permitted Use (Solely for the Purpose).
   - Protection Standard (Reasonable Care).
6. **SECTION 4: RETURN OR DESTRUCTION:** Process for returning/destroying data upon termination.
7. **SECTION 5: NO LICENSE & NO WARRANTY:** Info provided "AS IS". No IP rights transferred.
8. **SECTION 6: REMEDIES:** - **Injunctive Relief Clause:** Acknowledge that money damages are insufficient and Disclosing Party is entitled to immediate court orders.
9. **SECTION 7: MISCELLANEOUS (BOILERPLATE):**
   - Severability, Waiver, Assignment, Notices, Entire Agreement.
10. **SECTION 8: GOVERNING LAW & DISPUTE RESOLUTION:** 
    - Laws of {country}
    - **Jurisdiction-Specific:** 
      - India: Prefer Arbitration (Arbitration and Conciliation Act, 1996)
      - USA: Court jurisdiction (specify state and federal courts)
      - UK/EU: Either Arbitration or Court (specify preference)
      - Netherlands: Court jurisdiction (specify competent court)
11. **SIGNATURES:** Blocks for both parties.
"""

# --- 2. EMPLOYMENT (Long-Form / Executive) ---
EMPLOYMENT_PROMPT = """
{core_instructions}

**DOCUMENT:** EMPLOYMENT AGREEMENT (Comprehensive)

**INPUTS:**
- Employer: {company_name}
- Address: {registered_address}
- Signer: {signer}
- Context/Notes: {corporate_context}
- Jurisdiction: {country}

**INSTRUCTION:** - Extract Employee Name, Job Title, Salary from 'Context' if mentioned.
- **CRITICAL:** Include "Garden Leave" and "Non-Compete" clauses if Industry is Finance/Tech.
- **CRITICAL:** Include "At-Will" if USA. Include Statutory Notice if UK/India/NL.

**REQUIRED STRUCTURE:**
1. **HEADER:** "EMPLOYMENT AGREEMENT"
2. **PARTIES:** {company_name} (Reg: {registration_number}) ("Employer") AND [Employee Name] ("Employee").
3. **SECTION 1: APPOINTMENT & DUTIES:** - Title: [Job Title]. 
   - Reporting Line & Place of Work.
   - "Full Time and Attention" clause.
4. **SECTION 2: COMPENSATION & BENEFITS:** - Base Salary: [Salary Amount].
   - Expenses Reimbursement policy.
   - Holidays/Annual Leave (Cite local labor laws).
5. **SECTION 3: CONFIDENTIALITY:** Strict protection of trade secrets specific to {corporate_context}.
6. **SECTION 4: INTELLECTUAL PROPERTY:** - "Work Made for Hire".
   - Employee assigns ALL inventions/code to Company.
   - Waiver of Moral Rights (where applicable).
7. **SECTION 5: TERMINATION:** - Notice Period (e.g., 1-3 months).
   - Immediate Termination for Cause (Gross Misconduct).
   - **Garden Leave Clause:** Right to exclude employee from office during notice period.
8. **SECTION 6: RESTRICTIVE COVENANTS (Post-Termination):**
   - Non-Compete (Timebound, e.g. 6-12 months).
   - Non-Solicitation of Clients and Employees.
9. **SECTION 7: DATA PROTECTION:** Consent to process employee data (GDPR/Local Law).
10. **SECTION 8: GENERAL PROVISIONS:** Governing Law ({country}), Severability, Entire Agreement.
11. **SIGNATURES:** Blocks for Employer and Employee.
"""

# --- 3. MSA (Long-Form / B2B) ---
SERVICE_PROMPT = """
{core_instructions}

**DOCUMENT:** MASTER SERVICE AGREEMENT (MSA)

**INPUTS:**
- Client: {company_name}
- Address: {registered_address}
- Signer: {signer}
- Context/Notes: {corporate_context}
- Jurisdiction: {country}

**INSTRUCTION:** - Extract Provider Name from Context.
- Draft a robust B2B agreement including Indemnification and Liability Caps.

**REQUIRED STRUCTURE:**
1. **HEADER:** "MASTER SERVICE AGREEMENT"
2. **PARTIES & BACKGROUND:** 
   - Client: {company_name} (Reg: {registration_number})
   - Provider: [Service Provider Name or extract from Context]
3. **SECTION 1: SCOPE OF SERVICES:** - Reference to Statements of Work (SOWs).
   - Change Order Procedure (Mechanism for changing scope).
4. **SECTION 2: FEES, INVOICING & TAXES:** - Payment Terms (Net 30).
   - Taxes (GST for India, VAT for UK/EU, Sales Tax for USA).
5. **SECTION 3: OBLIGATIONS:** - Provider Warranties (Professional Standards).
   - Client Cooperation.
6. **SECTION 4: INTELLECTUAL PROPERTY:** - Client owns "Deliverables".
   - Provider retains "Background IP".
7. **SECTION 5: CONFIDENTIALITY:** Standard mutual protection.
8. **SECTION 6: INDEMNIFICATION (CRITICAL):** - Provider indemnifies Client against IP infringement and negligence.
9. **SECTION 7: LIMITATION OF LIABILITY:** - Cap liability at 12 months' fees.
   - Exclude indirect/consequential damages.
10. **SECTION 8: TERM & TERMINATION:** Convenience vs Cause. Effect of Termination.
11. **SECTION 9: BOILERPLATE:** Force Majeure, Independent Contractor status, Notices.
12. **SECTION 10: GOVERNING LAW:** Laws of {country}.
13. **SIGNATURES:** Both Parties.
"""

# --- 4. TERMS (Long-Form / SaaS) ---
TERMS_PROMPT = """
{core_instructions}

**DOCUMENT:** GENERAL TERMS & CONDITIONS

**INPUTS:**
- Issuer: {company_name} (Reg: {registration_number})
- Address: {registered_address}
- Context/Notes: {corporate_context}
- Jurisdiction: {country}
- Date: {date_today}

**INSTRUCTION:** - Draft Terms for a {corporate_context} business.
- **COMPLIANCE:** If EU/UK, MUST include "Right of Withdrawal" and GDPR references.

**REQUIRED STRUCTURE:**
1. **HEADER:** "GENERAL TERMS & CONDITIONS"
2. **SECTION 1: ACCEPTANCE OF TERMS:** Agreement binding upon use of site/service.
3. **SECTION 2: DESCRIPTION OF SERVICES:** - Define SaaS/Platform nature.
   - Service Level/Availability (uptime disclaimer).
4. **SECTION 3: USER ACCOUNTS:** Registration, Security, Password responsibility.
5. **SECTION 4: PAYMENT & SUBSCRIPTIONS:** Billing cycles, Auto-renewal, Taxes.
6. **SECTION 5: ACCEPTABLE USE POLICY:** Prohibited conduct (No reverse engineering, no illegal use).
7. **SECTION 6: INTELLECTUAL PROPERTY:** - Company owns Platform.
   - User owns User Data (License granted to Company to process).
8. **SECTION 7: DATA PROTECTION:** Reference Privacy Policy and GDPR/CCPA compliance.
9. **SECTION 8: DISCLAIMERS & LIABILITY:** - "AS IS" Warranty.
   - Liability Cap (Limit "Data Loss, Server Downtime").
10. **SECTION 9: TERMINATION:** Right to suspend access.
11. **SECTION 10: REFUNDS/CANCELLATION:** - **EU Specific:** 14-Day Right of Withdrawal (Mandatory for EU/UK).
12. **SECTION 11: BOILERPLATE:** Severability, Force Majeure, Assignment.
13. **SECTION 12: GOVERNING LAW:** Consumer laws of {country}.
14. **CONTACT INFO:** 
    - Support Email: Generate an appropriate support email based on {company_name} (e.g., support@companyname.com or contact@companyname.com)
    - Registered Address: {registered_address}
"""

# --- 5. BOARD RESOLUTION (Formal) ---
BOARD_PROMPT = """
{core_instructions}

**DOCUMENT:** BOARD RESOLUTION

**INPUTS:**
- Company: {company_name} (Reg: {registration_number})
- Address: {registered_address}
- Signer: {signer}
- Context/Notes: {corporate_context}
- Date: {date_today}

**INSTRUCTION:** - If Context implies Investment/Funding, draft a "Series A" style resolution (Issue of Shares).
- If Context is generic, draft "General Business Authorization".
- **CRITICAL:** Include Quorum declaration and filing authority (ROC/Companies House).

**REQUIRED STRUCTURE:**
1. **HEADER:** "BOARD RESOLUTION OF {company_name}"
2. **MEETING DETAILS:** 
   - Date: {date_today}
   - Time: [Meeting Time]
   - Location: {registered_address} or [Meeting Location]
   - Chairperson: {signer}
   - Quorum: [Number] directors present (meeting quorum requirements)
3. **BACKGROUND (PREAMBLE):** "The Chairperson informed the Board that..."
4. **RESOLUTIONS:** - "RESOLVED THAT..." (Draft specific text based on Context).
   - "RESOLVED FURTHER THAT..." (Approval of agreements/documents).
   - "RESOLVED FURTHER THAT..." (Authority to file forms with ROC/Companies House/KvK).
5. **CERTIFICATION:** Certified True Copy signed by Director.
6. **SIGNATURE:** {signer} (Director).
"""

# --- 6. SHAREHOLDER RESOLUTION (Formal) ---
SHAREHOLDER_PROMPT = """
{core_instructions}

**DOCUMENT:** SHAREHOLDER RESOLUTION

**INPUTS:**
- Company: {company_name} (Reg: {registration_number})
- Address: {registered_address}
- Context/Notes: {corporate_context}
- Date: {date_today}

**INSTRUCTION:** - If Context implies Dividends, include "Record Date" and "Solvency Statement".
- If Context is generic, draft "Approval of Financial Statements".

**REQUIRED STRUCTURE:**
1. **HEADER:** "SHAREHOLDER RESOLUTION OF {company_name}"
2. **COMPANY DETAILS:** 
   - Registration Number: {registration_number}
   - Registered Address: {registered_address}
3. **MEETING DETAILS:** 
   - Date: {date_today}
   - Location: {registered_address} or [Meeting Location]
   - Quorum: [Number] shareholders present (representing [X]% of share capital)
3. **BACKGROUND:** "The Board has recommended..."
4. **RESOLUTIONS:** - "RESOLVED THAT..." (Context specific).
   - **For Dividends:** Declare amount per share, Record Date, and Payment Date.
   - **Tax Compliance:** Mention deduction of Tax (TDS/Withholding) if applicable in {country}.
5. **APPROVAL:** Unanimous/Majority approval recorded.
6. **SIGNATURE:** 
   - [Shareholder Name] / [Chairperson Name]
   - Date: {date_today}
"""

# Map template types to their prompts
PROMPT_MAP = {
    "nda": NDA_PROMPT,
    "employment": EMPLOYMENT_PROMPT,
    "service": SERVICE_PROMPT,
    "terms": TERMS_PROMPT,
    "board": BOARD_PROMPT,
    "shareholder": SHAREHOLDER_PROMPT
}