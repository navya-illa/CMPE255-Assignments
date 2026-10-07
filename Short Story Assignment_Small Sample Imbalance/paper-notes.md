# Technical Review: Small-Sample Imbalance in Machine Learning

## Paper Information

**Title:** [A Survey on Small Sample Imbalance Problem: Metrics, Feature Analysis, and Solutions](https://arxiv.org/pdf/2504.14800)

**Authors:** Shuxian Zhao, Jie Gui, Minjing Dong, Baosheng Yu, Zhipeng Gui, Lu Dong, Yuan Yan Tang, and James Tin-Yau Kwok

**arXiv:** 2504.14800

**Submission date:** April 21, 2025

## Abstract and Scope

This paper examines the small-sample imbalance (S&I) problem, which occurs when a dataset contains relatively few training examples and the examples are distributed unevenly across classes. The problem becomes especially difficult when the classes overlap in feature space or when the minority class contains noisy, rare, or unrepresentative examples.

The survey presents a data-centric framework for understanding S&I datasets. It reviews imbalance metrics, feature-analysis methods, data-complexity measures, conventional resampling methods, complexity-aware solutions, and approaches for extreme imbalance. The authors also compare several classifiers and resampling methods on binary and multiclass datasets.

The central conclusion is that classifier capability and dataset characteristics can have a greater effect on performance than the choice of resampling method. Model selection and data analysis should therefore come before automatically applying oversampling or undersampling.

## Definition of the S&I Problem

A small-sample problem occurs when the available dataset is too limited for reliable generalization and may cause overfitting. A class-imbalance problem occurs when some classes have substantially more examples than others. The S&I problem combines both conditions, leaving the model with limited evidence and a strong bias toward the majority class.

The paper also discusses feature imbalance, sample-quality imbalance, temporal imbalance, and spatial imbalance. Class overlap, noise, missing values, small disjuncts, and outliers can further increase classification difficulty.

## Feature Analysis and Data Complexity

Table I identifies feature-analysis methods including mean and variance, skewness and kurtosis, Shannon entropy, t-SNE, PCA, LDA, KL divergence, the KS test, wavelet transforms, and Fourier transforms.

Table II groups data-complexity measures into four categories:

1. Feature-overlap measures: F1, F1v, F2, F3, F4, and IN.
2. Neighborhood measures: N1, N2, N3, N4, T1, and LSC.
3. Linear-separability measures: L1, L2, and L3.
4. Other imbalance-complexity measures: CM, wCM, and dwCM.

These analyses help determine whether poor performance is caused primarily by class proportions or by deeper characteristics such as overlap, noise, and feature separability.

## Datasets and Imbalance Statistics

The paper uses examples from the UCI Machine Learning Repository and the KEEL Data Repository. Table III reports the following dataset statistics:

| Task | Dataset | Samples | Features | Classes | Class distribution | IR | Complexity |
|---|---|---:|---:|---:|---|---:|---|
| Binary | Breast-Cancer | 569 | 30 | 2 | 357/212 | 1.68 | + |
| Binary | ecol | 336 | 7 | 2 | 35/301 | 8.60 | +++ |
| Binary | Wine | 178 | 13 | 2 | 71/107 | 1.51 | + |
| Binary | yeast | 1484 | 8 | 2 | 51/1433 | 28.10 | +++++ |
| Binary | Glass | 214 | 9 | 2 | 70/144 | 2.06 | ++++ |
| Multiclass | ecoli | 336 | 7 | 8 | 143/77/52/20/5/2/2 | 71.50 | ++++ |
| Multiclass | Wine | 178 | 13 | 3 | 71/59/48 | 1.48 | ++ |
| Multiclass | yeast | 1484 | 8 | 10 | 463/429/244/163/51/44/35/30/20/5 | 92.60 | +++++ |
| Multiclass | Glass | 214 | 9 | 6 | 76/70/29/17/13/9 | 8.44 | +++++ |

Table III also reports Gini, ID, LRID, IC, augmented R-value, adjusted IR, IBI³, IF, and MIR. A greater number of plus signs indicates higher dataset complexity. Some measures are not applicable to particular task types.

## Evaluation Metrics

Table IV summarizes the main evaluation metrics for S&I classification. Accuracy measures the proportion of all predictions that are correct. Precision measures the correctness of positive predictions, while recall measures how many positive examples are detected. F1-score combines precision and recall. AUC-ROC summarizes performance across classification thresholds. Matthews correlation coefficient uses all four confusion-matrix categories, and G-Mean combines the recalls of the positive and negative classes.

The paper notes that the precision-recall curve is often more informative than the ROC curve for imbalanced data because the ROC curve can appear overly optimistic when the minority class is small. Macro-average precision, recall, and F1-score are particularly useful for multiclass imbalanced classification.

## Solution Categories

### Conventional Solutions

Table V summarizes data-level methods such as SMOTE, Borderline-SMOTE, ADASYN, WK-SMOTE, MC-SMOTE, SUNDO, and WRO. It also includes augmentation methods based on traditional techniques, VAEs, GANs, and diffusion models.

Undersampling is used less frequently because removing majority-class examples can discard valuable information when the overall dataset is already small. The paper emphasizes that oversampling should be applied only to the training set to avoid overly optimistic evaluation.

### Data-Complexity Solutions

Table VII compares resampling methods for complex datasets using G-Mean, F1-score, and AUC.

| Method | G-Mean | F1-score | AUC |
|---|---:|---:|---:|
| No-sampling baseline | 57.18 | 48.32 | 70.22 |
| SMOTE-Tomek | 53.30 | 46.50 | 75.60 |
| SMOTE-ENN | 61.41 | 45.795 | 73.83 |
| SMOTE-IPF | 69.83 | 43.30 | 71.58 |
| SMOTE-WENN | 70.83 | 46.38 | 72.51 |
| FW-SMOTE | 80.75 | — | 86.40 |
| Re-SC | 77.60 | 60.10 | 81.00 |
| IA-SUWO | 79.44 | 71.67 | 80.12 |
| NI-MWMOTE | 75.21 | 63.23 | 77.41 |
| RBO | 78.80 | — | 83.95 |

Table VIII reports multiclass results using Recall, G-Mean, and F1-score. MC-RBO achieves the highest values shown: Recall 68.854%, G-Mean 78.196%, and F1-score 68.876%.

Table IX lists additional data-augmentation, feature-level, algorithm-level, and hybrid methods, including MoGAN, FAWGAN-GN, PCWGAN-GP, CFGAN, S2N, FAST, DBFS, Meta-learning, Class-Balanced Loss, RBBag, and PCA-SMOTE-SVM.

### Extreme S&I Solutions

For extreme imbalance, the paper discusses Sampling With the Majority, Few-shot GAN, UCML, DM-UCML, long-tail learning, invariant feature learning, representation calibration, and probabilistic contrastive learning. These methods may combine data generation, transfer learning, metric learning, class-aware losses, and specialized model architectures.

## Experimental Comparison

The main experiment compares Decision Tree, SVM, Random Forest, k-Nearest Neighbors, and AdaBoost. The authors evaluate no sampling, SMOTE, Borderline-SMOTE, ADASYN, and seven additional complexity-aware strategies using default parameters from the `imbalanced-learn` and `smote-variants` toolboxes.

### Table X: Binary Breast_cancer Dataset

With no sampling, the reported accuracy values are 0.9415 for DT, 0.9357 for SVM, 0.9708 for RF, 0.9591 for KNN, and 0.9766 for AdaBoost. The corresponding AUC values are 0.9438, 0.9931, 0.9968, 0.9953, and 0.9962.

The best AdaBoost F1-score shown is 0.9825 with SMOTE and SMOTE-IPF. The best G-Mean values shown include 0.9828 for AdaBoost with SMOTE and 0.9782 for KNN with SMOTE-ENN.

### Table XI: Multiclass Ecoli Dataset

With no sampling, the reported accuracy values are 0.7624 for DT, 0.8812 for SVM, 0.8218 for RF, 0.8812 for KNN, and 0.6535 for AdaBoost. The corresponding AUC values are 0.6967, 0.9141, 0.8386, 0.8577, and 0.6860.

The best F1-score shown is 0.8753 for RF with ADASYN, and the best G-Mean shown is 0.9266 for RF with ADASYN. The paper reports that, with SMOTE, SVM achieves 29.7% higher accuracy than AdaBoost on Ecoli.

The authors also report that RF's F1-score fluctuation across resampling methods on Breast_cancer is only 0.5 percentage points when the classifier is held constant. This supports the conclusion that classifier selection can matter more than resampling selection.

## Conclusions and Research Directions

The paper recommends a diagnostic workflow: measure imbalance, inspect feature and class distributions, evaluate data complexity, select a suitable classifier, and then test targeted data-processing methods. Resampling should not be treated as a universal fix.

The authors identify future research directions involving multiclass and dynamic imbalance, high-dimensional data, domain adaptation, few-shot and zero-shot learning, multimodal learning, large models, adaptive algorithms, interpretability, uncertainty, and task-specific evaluation metrics.

## Reference

Zhao, S., Gui, J., Dong, M., Yu, B., Gui, Z., Dong, L., Tang, Y. Y., and Kwok, J. T.-Y. “A Survey on Small Sample Imbalance Problem: Metrics, Feature Analysis, and Solutions.” arXiv:2504.14800, 2025. https://arxiv.org/abs/2504.14800

