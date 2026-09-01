# Principal Prompts Used

## Master prompt

Help me create an advanced chatbot-assisted deep-learning project using the Intel Image Classification dataset from Kaggle. Follow CRISP-DM and produce a reproducible TensorFlow/Keras notebook suitable for a master's-level data-science assignment and Medium article.

Audit the dataset structure, image counts, labels, split integrity, and class balance. Create publication-quality examples and class-distribution figures. Use a fixed seed and preserve an untouched test set.

Build a custom convolutional neural network as a baseline. Then build a MobileNetV2 transfer-learning model using ImageNet weights, train its new classification head, and fine-tune an appropriate subset of upper layers. Use training-only augmentation, early stopping, learning-rate scheduling, and model checkpoints. Use both available Kaggle T4 GPUs safely.

Compare the models on the same untouched test set. Report accuracy, loss, class-level precision, recall, F1, macro averages, and a confusion matrix. Analyze the most confident errors and identify the principal class confusions. Generate Grad-CAM visualizations and explain their limitations.

Save figures, metrics, trained models, and a machine-readable results summary. Do not invent metrics. Make the workflow reproducible and discuss deployment, calibration, data drift, unknown classes, responsible use, and run-to-run GPU nondeterminism.

## Important follow-up prompts represented in the transcript

1. Verify that TensorFlow detects both Kaggle T4 GPUs and locate the exact dataset directories.
2. Audit the training and test image counts by class.
3. Create leakage-safe training, validation, and test pipelines.
4. Visualize training-only image augmentation.
5. Train and diagnose a custom CNN baseline.
6. Resolve the disabled-internet error when downloading MobileNetV2 weights.
7. Train the frozen transfer-learning head and fine-tune the final 30 layers.
8. Compare both models on the untouched test set.
9. Produce class-level metrics, confusion matrices, confident-error analysis, and Grad-CAM explanations.
10. Export all models, figures, CSVs, JSON summaries, and the final notebook.

