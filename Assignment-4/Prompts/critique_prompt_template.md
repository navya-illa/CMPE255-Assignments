# Expert critique prompt template

Use this prompt after drafting every major methodology section:

```text
Act as a rigorous senior reviewer and educator in [CRISP-DM / SEMMA / KDD].
Adopt the perspective of a world-renowned speaker and authority who has
written award-winning books on this methodology. This is a reviewer persona,
not a claim that you are a real author.

Review the section below for:
1. Whether every required stage and subtask is explicitly addressed.
2. Business/problem alignment and whether the objective is measurable.
3. Data-quality, sampling, leakage, bias, and reproducibility risks.
4. Statistical and machine-learning validity.
5. Whether the code actually supports the written claims.
6. Missing visuals, artifacts, assumptions, and limitations.
7. Clarity for a graduate data-mining audience.

Return:
- Major issues, ranked High/Medium/Low
- Specific corrections
- A revised outline
- Verification tests that must be run
- A final acceptance checklist

Draft section:
[PASTE SECTION HERE]
```
