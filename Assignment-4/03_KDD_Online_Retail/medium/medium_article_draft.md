# From Transactions to Knowledge: Applying KDD to Online Retail

The KDD process is about more than fitting a model. It is a disciplined path from selecting meaningful data, cleaning it, transforming it into useful representations, mining patterns, and evaluating whether the resulting knowledge is credible.

Using the Online Retail dataset, I created customer-level RFM features for segmentation and invoice-level baskets for association-rule mining. The project documents cancellations and invalid transactions, compares cluster counts with silhouette scores, and filters product associations using support, confidence, and lift.

The most important lesson is interpretability: a segment or rule is not automatically knowledge. It becomes useful only after checking its stability, support, context, and possible business action.
