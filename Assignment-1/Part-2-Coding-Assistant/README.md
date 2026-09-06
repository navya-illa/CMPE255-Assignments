# Part 2 — Five Data-Mining Problems

This directory contains five separate data-mining problems solved with support from an AI coding assistant. The problems cover clustering, classification, association mining, regression, and anomaly detection. Each problem is maintained as an independent, reproducible experiment rather than as one combined model.

## Problems and selected methods

| Problem | Folder | Selected method | Primary evidence |
|---|---|---|---|
| Clustering | [`1) clustering/`](1%29%20clustering/) | K-Means, k = 6 | Silhouette 0.4274; 100% coverage |
| Classification | [`2) classification/`](2%29%20classification/) | Random forest | PR-AUC 0.9320; ROC-AUC 0.9624 |
| Association mining | [`3) association_mining/`](3%29%20association_mining/) | Apriori-style rules | 45 rules; top lift 0.9377 |
| Regression | [`4) regression/`](4%29%20regression/) | Random forest | Duration R² 0.9024; fare R² 0.5904 |
| Anomaly detection | [`5) anomaly_detection/`](5%29%20anomaly_detection/) | Isolation Forest | PR-AUC 0.9908; ROC-AUC 0.9995 |

The metrics above summarize separate problem types and are not directly comparable. Each folder contains the detailed results, visual evidence, notebook workflow, report, prompt record, and reproducibility instructions for that problem.

## Shared evidence standard

Every experiment includes:

- a dataset and schema audit;
- a comparison among appropriate baselines or algorithms;
- metrics appropriate to the problem type;
- exported CSV and JSON artifacts;
- generated visual evidence where useful;
- a non-empty Jupyter notebook showing audit, execution, comparison, and reconciliation;
- a report describing verified findings and limitations;
- reproducibility instructions;
- references and dataset-attribution notes; and
- an AI-assistance disclosure.

The command-line script and exported artifacts are authoritative. Narrative claims are checked against executed outputs rather than invented or manually estimated results.

## Repository structure

```text
Part-2-Coding-Assistant/
├── README.md
├── PROMPTS.md
├── requirements.txt
├── 1) clustering/
│   ├── README.md
│   ├── PROMPTS.md
│   ├── data/
│   ├── notebooks/
│   ├── src/
│   ├── artifacts/
│   └── reports/
├── 2) classification/
├── 3) association_mining/
├── 4) regression/
├── 5) anomaly_detection/
└── reports/
    └── five-problem-summary.md
```

## How to use the experiments

Open the README inside the relevant numbered folder first. It identifies the dataset, the selected method, the comparison criteria, the generated evidence, limitations, references, and the exact command used to reproduce the outputs.

The shared dependency file can be installed with:

```bash
pip install -r requirements.txt
```

Some raw datasets are intentionally not redistributed. Follow the `data/README.md` instructions in the applicable experiment folder when a download is required.

## Prompt records

[`PROMPTS.md`](PROMPTS.md) indexes the detailed prompt records. Each record documents role and constraints, data audit, experiment design, implementation contract, adversarial review, interpretation limits, visualization checks, reproducibility, and final consistency checks.

## References

1. [Data Science Examples](https://github.com/dlmastery/data_science_examples). Reference examples that informed the choice of data-mining problem types and workflow framing.
2. [scikit-learn documentation](https://scikit-learn.org/stable/). Primary technical documentation for the implemented models, preprocessing, metrics, and evaluation utilities.
3. Dataset-specific sources and attribution notes are listed in the References section of each numbered experiment README.

## AI-assistance disclosure

The AI coding assistant supported experiment planning, code generation, debugging, validation, visualization, notebook construction, report writing, and documentation review. The reported conclusions were checked against executed code and exported artifacts.
