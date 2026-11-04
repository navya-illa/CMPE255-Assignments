# KDD critique and revision log

## Revision 1 — discovery framing

The initial draft jumped directly to clustering. The revision defines the population, valid transaction rules, RFM knowledge question, basket question, and interpretation criteria before mining.

## Revision 2 — preprocessing validity

The revision removes cancellations, nonpositive quantities/prices, and missing customer/product identifiers. It documents the snapshot date and creates customer-level features only after transaction validation.

## Revision 3 — knowledge validation

The revision uses silhouette analysis for cluster-count selection and support, confidence, and lift for association rules. Segment profiles and rules are exported as inspectable artifacts rather than presented as unexplained output.

## Manual verification

- Confirm exclusions and row counts at every preprocessing step.
- Confirm no cancellation invoices remain.
- Check cluster stability with a second random seed.
- Filter association rules for adequate support before interpretation.
- Manually inspect representative products for business plausibility.
