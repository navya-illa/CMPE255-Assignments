# From Business Question to Churn-Risk Deployment: A CRISP-DM Walkthrough

Customer churn projects are often presented as model-comparison exercises. CRISP-DM encourages a broader view: understand the business decision, understand the data, prepare it without leakage, model responsibly, evaluate against the decision, and plan deployment.

In this project, I used the Telco Customer Churn dataset to build a retention-oriented workflow. The key design choice was to define success around contacting a limited high-risk group rather than treating accuracy as the only objective.

The notebook walks through all six phases, including data-quality checks, a leakage-safe preprocessing pipeline, interpretable and nonlinear models, threshold evaluation, and a serialized scoring pipeline. The main lesson is that a model is only one component of a data-science solution; the surrounding business assumptions determine whether the result is useful.

**Artifacts:** notebook, report, critique log, scoring script, and figures.
