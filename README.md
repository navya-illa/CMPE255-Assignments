# CMPE 255 Assignments

This repository contains my coursework and projects for **CMPE 255: Data Mining** at San José State University.

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

### [Part 2 — Customer Segmentation Using an AI Coding Assistant](./Assignment-1/Part-2-Coding-Assistant/)

A reproducible customer-segmentation experiment developed with an AI coding assistant using the Mall Customers dataset.

**Highlights:**

- Compared K-Means, Ward hierarchical clustering, and DBSCAN
- Selected six-cluster K-Means with a **0.4274 silhouette score**
- Assigned **100% of customers** to interpretable segments
- Audited the misleading effect of excluding DBSCAN noise points
- Generated customer profiles, PCA visualizations, and a hierarchical dendrogram
- Documented staged prompting, evidence requirements, and adversarial self-critique
- Included reproducible code, metrics, reports, and visual artifacts

**Resources:**

- [Part 2 documentation](./Assignment-1/Part-2-Coding-Assistant/README.md)
- [Coding-assistant prompts](./Assignment-1/Part-2-Coding-Assistant/PROMPTS.md)
- [Experiment notebook](./Assignment-1/Part-2-Coding-Assistant/notebooks/customer-segmentation.ipynb)
- [Experiment summary](./Assignment-1/Part-2-Coding-Assistant/reports/experiment-summary.md)

## Author

**Navya Illa**  
San José State University
