# SEMMA Report: Bank Marketing

## Objective

Estimate the probability that a contacted bank customer subscribes to a term deposit and support a campaign team with a ranked outreach list.

## Sample

The project uses a reproducible stratified train/test split. The population, target definition, unknown-value handling, and class imbalance are documented before modeling.

## Explore

Exploration covers target prevalence, numeric distributions, categorical levels, missing/unknown values, and candidate relationships. Exploration is used to form hypotheses, not to silently select features based on the test set.

## Modify

Numeric columns are imputed and standardized. Categorical columns are imputed and one-hot encoded. Transformations are placed inside a pipeline so cross-validation does not leak information between folds.

## Model

Logistic regression is the interpretable baseline. Random forest and histogram gradient boosting provide nonlinear comparisons. Each candidate uses the same evaluation split and cross-validation design.

## Assess

The project reports ROC-AUC, PR-AUC, classification metrics at an outreach threshold, and ROC/precision-recall curves. The final threshold should reflect campaign capacity and the relative cost of missed opportunities versus unnecessary contact.

## SAS companion

The Python pipeline maps to SAS Enterprise Miner nodes: Input Data → Sample → Explore → Metadata/Transform Variables → Model nodes → Model Comparison/Assessment. The SAS companion records equivalent roles, required screenshots, and differences between the two execution environments.
