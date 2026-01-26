# Phase 2: From Symptoms to Root Causes

## Interview Transcript (5 Whys)

**Interviewer (Auditor):** Arman, why are we prioritizing the new 'Travel Insurance' module when the 'Step Counter' we launched last quarter is losing 50% of users per week?

**Arman (Synthetic Persona):** The 'Travel Insurance' module is a key strategic initiative, fully approved and funded as part of our CAPEX roadmap for Q3. My primary focus is to ensure its on-time delivery, as per the Steering Committee's directives and budget allocation. Regarding the 'Step Counter,' we are aware of the churn data. However, any significant re-development or optimization would require a new budget allocation and a separate project initiative, which isn't currently approved for this quarter.

**Interviewer (Auditor):** Why can't we pause the Travel module for two sprints to fix the Step Counter onboarding bugs?

**Arman (Synthetic Persona):** Pausing development on the 'Travel Insurance' module, even for two sprints, isn't something we can do easily. That module has a committed CAPEX budget and a strict Q3 delivery timeline approved by the Steering Committee. Diverting our dedicated resources for two sprints would create significant delays, potentially jeopardize our funding, and would require a formal Change Request and re-approval process, which is quite extensive.

**Interviewer (Auditor):** Why is the budget rigidly locked to the 'Travel Module' scope defined 12 months ago?

**Arman (Synthetic Persona):** The budget for the 'Travel Insurance' module was approved last year based on a detailed business case and a defined scope, linking directly to our annual CAPEX plan. This upfront allocation ensures we have the necessary funding secured for specific strategic projects. Any deviation from that approved scope or timeline requires a new approval process and often impacts the overall CAPEX portfolio.

**Interviewer (Auditor):** Why does the Finance department classify 'fixing onboarding' as a cost (OPEX) while 'building a new module' is an investment (CAPEX)?

**Arman (Synthetic Persona):** Our financial guidelines categorize 'building new modules' as CAPEX because they represent new asset creation or significant functional expansions that drive future growth and are considered investments. Conversely, 'fixing onboarding' or similar improvements to existing features are generally classified as OPEX. These are seen as maintenance costs to ensure the current product operates effectively, rather than creating new value streams.

**Interviewer (Auditor):** Why does the organization value the creation of digital assets more than the performance of those assets?

**Arman (Synthetic Persona):** The organization's structure often links success to the delivery of approved strategic initiatives and the expansion of our digital footprint, which are funded through CAPEX. These new modules are tangible deliverables that align with the annual roadmap and receive significant visibility from the Steering Committee. While performance is important, the funding and approval processes are heavily geared towards launching these new "investment" projects. Iterating on existing features, though valuable, doesn't always have the same dedicated budget or a clear path for approval as a major new CAPEX project.

---

# Product Requirements Document (PRD)

## 1. Problem Statement
Kcell's Product Managers are structurally prevented from saving failing live products because internal financial governance rigidly locks resources to pre-planned "Capital Projects" (New Features), while classifying critical iteration and optimization as unfunded "Maintenance" (OPEX). This forces teams to continue building new features even when existing ones are hemorrhaging customers.

## 2. Job To Be Done (JTBD)
**When** I discover that a live critical feature is failing (high churn) while my team is fully booked on a new strategic CAPEX initiative, **I want to** instantly justify and execute a resource pivot using financial language **so that** I can save the customer base and asset value without triggering a 3-month "Change Request" bureaucracy or losing my funding.

## 3. Target User
**Arman, Senior Product Manager (SuperApp)**
*   **Role:** Responsible for delivering the "Digital Ecosystem" roadmap.
*   **Context:** Operates under strict "Project Governance"; his performance is judged by "On-Time Delivery" of new assets.
*   **Constraints:** Terrified of the "Change Request" process because it implies failure to plan; lacks the financial vocabulary to argue why "fixing a bug" is an "investment."

## 4. Current Pain Points
*   **The "Zombie Feature" Effect:** Managers are forced to let live features die (e.g., Step Counter losing 50% users/week) to birth new ones (Travel Insurance) because the budget dictates it.
*   **Administrative Paralysis:** "Change Requests" are viewed as extensive, punitive processes, effectively enforcing a Waterfall methodology where the plan is more important than reality.
*   **Misaligned Incentives:** Success is defined by the *Steering Committee* (Delivery of Assets) rather than the *Customer* (Retention/Value).
*   **Rigidity of "Business Case":** Budgets are locked to scopes defined 12 months prior, making them obsolete by the time development starts.

## 5. Proposed AI Agent — Purpose
**The "CAPEX-to-Value Bridge" Agent**
This AI agent exists to act as a real-time governance intermediary between Product Implementation and Financial Control. Its purpose is to automate the friction of re-allocation. It continuously monitors live product metrics against the committed project plan. When it detects that a live asset (product) is depreciating (churning) faster than a new asset can be created, it automatically generates a compliant, data-backed "Investment Pivot Request." This agent translates "product logic" (users are leaving) into "finance logic" (protecting asset value), empowering PMs to switch tracks legally and quickly.

## 6. Functional Requirements

### Inputs
*   **Strategic Roadmap:** Ingests the committed project plan, deadlines, and CAPEX codes for current initiatives (e.g., "Travel Insurance - Q3").
*   **Live Performance Data:** Connects to product analytics (mixpanel/database) to monitor "Asset Health" (Churn Rate, DAU, Onboarding Success) of live features.
*   **Financial Rulebook:** Ingests Kcell's internal capitalization policies (IAS 38 interpretation) and resource cost rates.

### Outputs
*   **"Asset Risk Alert":** A notification to the PM and Steering Committee when a live feature's performance drops below a critical threshold (e.g., >10% weekly churn).
*   **"Opportunity Cost Calculator":** A real-time dashboard showing the financial loss of *ignoring* the live bug vs. the value of *delaying* the new feature.
*   **A "Pivot Business Case" (Artifact):** An auto-generated, pre-formatted PDF memo. It populates the standard "Change Request" form with data proving that fixing the bug leads to higher Net Present Value (NPV) than sticking to the plan.

### Decisions & Recommendations
*   **Recommendation Engine:** "Recommend pausing [Project A] for [2 Sprints] to resolve [Critical Failure B]. Projected ROI impact: +15%."

### Integration
*   Integrates with **Jira** (to tag scope items) and the internal **ERP/Project Management System** (to flag the budget lines).

## 7. Non-Goals
*   The agent **does not** automatically re-assign developers or change their tasks (humans must decide).
*   The agent **does not** rewrite the company's accounting standards or violate IAS 38.
*   The agent **does not** write code to fix the actual product bugs.

## 8. Success Metrics (Outcome-Based)
*   **Pivot Velocity:** Time from identifying a critical market signal (churn) to official budget re-approval (Goal: < 48 hours, down from current status of weeks/months).
*   **Asset Health Maintenance:** percentage (%) of engineering budget successfully reallocated to optimization/iteration mid-year.
*   **Retention Impact:** Improvement in customer retention for "saved" features post-intervention.
*   **Reduction in "Failed Assets":** Decrease in the number of features that are launched and immediately abandoned.
