# KDD Report: Online Retail Knowledge Discovery

## Knowledge objective

Discover actionable customer segments and product co-purchase patterns from transactional retail data.

## Selection

The project selects transactions with identifiable customers and products and defines two discovery tasks: customer-level RFM segmentation and invoice-level association discovery.

## Preprocessing

Cancelled invoices, nonpositive quantities, nonpositive prices, and records missing customer or product descriptions are excluded. Revenue is calculated as quantity times unit price. The resulting transaction table is checked for date and value integrity.

## Transformation

Customer records are transformed into Recency, Frequency, and Monetary features. Log transformation reduces skew and standardization makes distance-based clustering more meaningful. A binary invoice-product basket is created for association discovery.

## Data mining

K-means models are compared across candidate values of k using silhouette score. Apriori generates frequent itemsets, and association rules are ranked using support, confidence, and lift.

## Interpretation and evaluation

Segments are profiled using median RFM values and named only after examining the data. Rules are interpreted cautiously: association does not imply causation, and low-support rules are not operationally reliable. Stability checks and representative product review are required before business use.

## Limitations

The data reflects one retail context and may contain seasonal or geographic effects. Product descriptions require normalization, and customer identifiers may not represent unique individuals perfectly.

## Reproducible execution results

The corrected KDD flow was executed on the UCI Online Retail workbook. After removing cancellations, invalid quantities/prices, and rows without customer or product identifiers, 4,338 customers and 17,138 valid multi-item invoices were available for discovery. The strongest silhouette score occurred at k=2. Apriori produced 282 frequent itemsets and 96 filtered rules after applying support >= 0.02 and confidence >= 0.20.

## Reproducibility and artifacts

Run python notebook/KDD_Online_Retail.py. It downloads the UCI workbook, normalizes product descriptions, creates RFM features and basket data, and saves the preprocessing summary, cluster-selection table and chart, segment profiles, association rules, and knowledge summary under artifacts/. The inspected segment and rule tables are also copied into knowledge_artifacts/.

The association results should be treated as candidate merchandising hypotheses. They require temporal or holdout validation before production use.

