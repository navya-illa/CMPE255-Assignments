# CMPE 255 Assignments

This repository contains my assignments for coursework **CMPE 255: Data Mining** at San José State University.

## Assignment 1

### [Part 1 — Intel Scene Classification with Deep Learning](./Assignment-1/)

An end-to-end image-classification project comparing a custom CNN with a fine-tuned MobileNetV2 model on the Intel Image Classification dataset.

**Highlights:**

- Followed the CRISP-DM methodology
- Classified six natural-scene categories
- Built and evaluated a custom CNN
- Applied MobileNetV2 transfer learning and fine-tuning
- Achieved **90.27% test accuracy**
- Analyzed errors using confusion matrices and misclassification galleries
- Used Grad-CAM for model explainability
- Documented the AI-assisted prompt-engineering process

**Resources:**

- [Detailed project documentation](./Assignment-1/README.md)
- [Executed Kaggle notebook](https://www.kaggle.com/code/navyai9/intel-scene-classification-with-deep-learning)
- [Medium article](https://medium.com/@9navya9/teaching-a-neural-network-to-recognize-natural-scenes-from-a-custom-cnn-to-explainable-transfer-b404798e954a)

### Part 2 — Five Data-Mining Problems Solved with an AI Coding Assistant

This section presents five data-mining problems solved with the support of an AI coding assistant: classification, regression, clustering, anomaly detection, and association mining.

**Highlights:**

| Problem | Selected method | Primary result |
|---|---|---|
| Classification | Logistic regression | PR-AUC **0.6985** |
| Regression | Random forest | Duration R² **0.9024**; fare R² **0.5905** |
| Clustering | K-Means, k=6 | Silhouette **0.4274**; coverage **100%** |
| Anomaly detection | Isolation Forest | PR-AUC **0.9908** |
| Association mining | Apriori | **45** rules; top lift **0.9377** |

Each problem includes a data audit, model or algorithm comparison, executed metrics, visual artifacts, reproducibility instructions, limitations, references, and AI-assistance disclosure.

**Resources:**

- [Part 2 documentation](./Assignment-1/Part-2-Coding-Assistant/README.md)
- [Clustering experiment](./Assignment-1/Part-2-Coding-Assistant/1%29%20clustering/README.md)
- [Classification experiment](./Assignment-1/Part-2-Coding-Assistant/2%29%20classification/README.md)
- [Association-mining experiment](./Assignment-1/Part-2-Coding-Assistant/3%29%20association_mining/README.md)
- [Regression experiment](./Assignment-1/Part-2-Coding-Assistant/4%29%20regression/README.md)
- [Anomaly-detection experiment](./Assignment-1/Part-2-Coding-Assistant/5%29%20anomaly_detection/README.md)
- [Five-problem experiment summary](./Assignment-1/Part-2-Coding-Assistant/reports/five-problem-summary.md)
- [Coding-assistant prompts](./Assignment-1/Part-2-Coding-Assistant/PROMPTS.md)
## Author

**Navya Illa**  
San José State University
