# Executive Summary: Financial & Governance Feasibility Analysis

**To:** Executive Investment Committee, Kcell
**Date:** 26.01.2026
**Subject:** Go/No-Go Decision on "CAPEX-to-Value Bridge" AI Agent

This document evaluates the financial viability and regulatory compliance of deploying the proposed AI Agent designed to automate the strategic reallocation of resources (Product Pivot Requests).

---

## Section 1: Financial Reasoning (ROI Calculation)

### Step 1: Salary Assumptions (Kazakhstan Corporate Context)

To estimate the value of labor saved, we apply a conservative benchmark for a Mid-Senior Product Manager or Corporate Strategy Manager in the telecommunications sector in Kazakhstan.

*   **Gross Monthly Salary:** 1,200,000 KZT
    *   *assumption based on senior specialist/mid-management roles in Almaty/Astana.*
*   **Standard Working Hours:** 160 hours/month
*   **Fully Loaded Hourly Cost:** ~8,500 KZT
    *   *Base hourly rate (7,500 KZT) plus ~13% overhead for taxes/benefits/workspace.*

### Step 2: Time Savings Valuation

The AI agent automates data gathering, "Change Request" drafting, and financial justification, saving an estimated **10 hours per week** per Product Manager.

| Metric | Calculation | Value (KZT) |
| :--- | :--- | :--- |
| **Weekly Savings (Per Person)** | 10 hours * 8,500 KZT | **85,000 KZT** |
| **Monthly Savings (Per Person)** | 85,000 * 4 weeks | **340,000 KZT** |
| **Annual Savings (Per Person)** | 85,000 * 48 weeks | **4,080,000 KZT** |

**Scalability:**
*   **Single Pilot User:** 4.08 Million KZT / Year
*   **Digital Product Team (5 Managers):** 20.4 Million KZT / Year

### Step 3: Cost of AI Agent (Estimation)

Costs include internal development, enterprise API usage (to Ensure data privacy), and ongoing maintenance.

*   **Year 1 Development (One-off):** 6,000,000 KZT
    *   *Estimate: 2 months of Senior Developer time + Project Management.*
*   **Annual Infrastructure & API Costs:** 1,500,000 KZT
    *   *Enterprise-grade LLM tokens and secure hosting.*
*   **Annual Maintenance:** 1,200,000 KZT
    *   *10% of dev cost for updates/patches.*

**Total Year 1 Cost Benchmark:** ~8,700,000 KZT

### Step 4: ROI Summary (5-User Deployment)

*   **Total Year 1 Savings:** 20,400,000 KZT
*   **Total Year 1 Costs:** 8,700,000 KZT
*   **Net Year 1 Benefit:** **+11,700,000 KZT**

**Payback Period:** Approximately **5-6 Months**.

**Logic:** The project pays for itself in under two quarters comfortably. The primary value driver is not just the labor savings, but the *avoided opportunity cost* of continuing to fund failing features, which is likely 10x higher than the labor savings calculated here.

---

## Section 2: Governance & Legal Compliance (Kazakhstan AI Ethics Test)

### 1. Data Residency & Sovereignty
The agent processes internal strategic documents (Roadmaps, Budgets) and potentially user performance metrics.
*   **Risk:** Sending strategic trade secrets or user data to public US-based cloud endpoints violates internal security policies and potentially the Law of the Republic of Kazakhstan "On Personal Data and their Protection" if PII is mixed in.
*   **Requirement:** The solution must be deployed within a secure perimeter (Virtual Private Cloud) or utilize an Enterprise Agreement with the LLM provider that guarantees zero data retention for training.
*   **Risk Level:** **Medium**

### 2. Transparency & Explainability
The agent generates a "Pivot Business Case" (PDF Memo) which justifies the recommendation.
*   **Evaluation:** The output is text-based and cites specific financial inputs (Churn Rate vs. CAPEX Code). The logic is fully auditable by a human controller. It is a "White Box" determination, not a "Black Box" prediction.
*   **Risk Level:** **Low**

### 3. Human Accountability
The agent acts as a drafter and advisor. It does not have the authority to sign the Change Request or move funds.
*   **Evaluation:** Legal liability remains strictly with the Product Manager who reviews and submits the generated generated memo, and the Steering Committee that approves it. The AI is a tool, not an agent of authority.
*   **Risk Level:** **Low**

---

## Section 3: Final Go / No-Go Recommendation

### Verdict: **GO WITH CONDITIONS**

**Justification:**
*   The financial case is compelling with a payback period of <6 months on labor savings alone.
*   The strategic value (stopping "Zombie Projects") vastly outweighs the implementation cost.
*   The technical complexity is low (RAG architecture on structured internal data).

**Conditions for Approval:**
1.  **Enterprise Data Contract:** Must use an LLM provider with a "No Training on Customer Data" guarantee to protect corporate strategy.
2.  **PII Sanitization:** The agent must only ingest aggregated metrics (e.g., "15% Churn"), not raw user lists, to bypass severe data residency friction.
3.  **Human Tollgate:** The generated "Pivot Request" must require a digital signature from the human Manager before submission to Finance.
