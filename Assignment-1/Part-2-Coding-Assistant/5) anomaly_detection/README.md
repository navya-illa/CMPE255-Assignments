# Anomaly Detection — Server Telemetry

This experiment solves an anomaly-detection problem using synthetic server telemetry. It evaluates Isolation Forest with ranking metrics and an explicit anomaly-rate assumption.

## Method

The workflow audits the telemetry, keeps labels for evaluation only, scores observations with Isolation Forest, and reports PR-AUC and ROC-AUC. Alerts are signals for investigation, not proof of an incident.

## Reproduce

```bash
python src/run_experiment.py --data data/server_telemetry.csv --output artifacts
```

The notebook, report, prompt record, requirements, and exported artifacts are stored in this folder.

## References and disclosure

The reference example is [Data Science Examples](https://github.com/dlmastery/data_science_examples). scikit-learn anomaly-detection documentation was used. The AI assistant supported design, implementation, debugging, and documentation; results were checked against executed artifacts.
