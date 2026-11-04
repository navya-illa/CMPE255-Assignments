# SEMMA in Practice: Predicting Bank-Term-Deposit Subscriptions

SEMMA provides a practical modeling workflow: sample, explore, modify, model, and assess. I applied it to the Bank Marketing dataset to show how a campaign prediction problem can be organized without skipping the decisions between raw data and a final score.

The project makes the sample and class imbalance explicit, explores unknown values, performs leakage-safe modification, compares several models, and evaluates a campaign-oriented threshold. A SAS Enterprise Miner companion maps the Python work to a visual SEMMA flow.

The main lesson is that assessment is not just a final accuracy number. It must connect model behavior to the way a campaign can actually use ranked predictions.
