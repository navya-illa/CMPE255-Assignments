# SEMMA deployment handoff

The SEMMA notebook produces ranked probabilities for a campaign. A deployment version should serialize the selected preprocessing/model pipeline, expose a batch-scoring job, and monitor campaign lift, precision at the contact budget, calibration, and drift. The threshold must be approved by the campaign owner rather than hard-coded without cost assumptions.
