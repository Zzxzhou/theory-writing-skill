# Theory Research Modes

This reference is for exploratory mathematical research, not ordinary prose polishing. It complements `reader-verifiable-proofs.md`; it never relaxes derivation-first work, source verification, or the LaTeX conventions in the main skill.

## Routing and non-goals

Select the smallest mode or combination that meets the actual request:

| Request | Activate | Primary artifact |
| --- | --- | --- |
| Is this conjecture even true? | Conjecture Stress Testing | counterexamples, boundary cases, revised claim |
| Prove or extend a theorem | Proof Architecture & Search; Stress Testing where informative | exact derivation, obligation graph, strongest established statement |
| Can we weaken a condition? | Assumption Minimization | assumption-to-proof map, weakening attempts, necessity examples |
| Check this proof | Independent Referee; Proof Architecture for any repair | line-specific findings and open obligations |
| Compare with anchor papers / claim novelty | Literature & Novelty Audit | theorem-by-theorem comparison with verified locators |
| Polish a completed passage or TeX | **No research mode unless the math changes** | edited manuscript following writing references |

One task may legitimately activate several modes. Do not impose all five for every request. For an open research program or a multi-session proof search, also load `research-workflow-state.md` and persist state **in the project repository**, not inside this reusable skill. Never silently convert a prose-only request into mathematical changes.

## 1. Conjecture Stress Testing

**Goal:** disprove a plausible statement cheaply before investing in a long proof.

- Restate the exact model, observables, target, parameter class, information set, quantifiers, and asymptotic regime.
- Probe zero-signal and boundary cases, nuisance degeneracy, weak separation, non-identification pairs, local alternatives, and small-dimensional examples, as applicable.
- For identification, seek two observationally equivalent distributions with distinct target values. For uniform rates, vary the parameter along an adversarial sequence. For an algebraic lemma, look for a finite counterexample.
- Verify each proposed counterexample really satisfies **every** stated assumption; otherwise it is a diagnostic, not a refutation.
- Distinguish `counterexample confirmed`, `test passed without refutation`, and `open`. Failure to find a counterexample does not establish truth.

**Output:** tested cases and exact reason they matter; a verified counterexample, a narrowed conjecture, or a precise unresolved boundary.

## 2. Proof Architecture & Search

**Goal:** derive a valid theorem from primitives and expose all technical work.

- Start from the model equation, criterion, score, likelihood, estimating equation, or optimality condition. Write an **exact** decomposition before any approximation.
- Fix the target resolution: finite sample, uniform, first-order, second-order, conditional, or another explicit scale. Carry all terms at that scale.
- Construct a dependency graph of obligations: identification, localization, linearization, stochastic control, expectation/bias, dependence, nuisance residuals, CLT, feasibility, and so forth as applicable.
- Attach a precise goal and provenance to each load-bearing lemma or rate. Track whether it is proved here, verified against a primary source, formally assumed, still open, or refuted.
- Maintain an obstruction ledger in the project notes: failed proof route, blocking transition, attempted fix, and best next discriminating test. Do not repeatedly invent stronger assumptions to make the proof appear closed.
- Explore competing proof routes when an obstruction is structural. Formalize the strongest actually justified statement only after the chain closes.

**Output:** dependency graph/obligations, explicit derivation, open gaps, and one testable next step.

## 3. Assumption Minimization

**Goal:** separate identification requirements, estimator requirements, and proof artifacts.

- Map each assumption to exact proof transitions that use it. Classify model, identification, technical, and proof-device restrictions.
- Attempt to delete, localize, or weaken one assumption at a time while holding the target and other assumptions fixed.
- For each weakening, either prove the claim still holds, exhibit a compatible counterexample, or record an open obligation. Do not silently change the estimand or the data-generating class.
- Compare **formal** conditions, quantifiers, rates, and asymptotic regimes to the closest verified anchor result. Beware of comparing restrictions that play different roles (e.g. exact label recovery versus estimation of an invariant functional).
- Necessity requires an impossibility or counterexample argument on the **same target class**, not merely failure of a known proof.

**Output:** assumption matrix with role, use, proposed weakening, necessity evidence, and remaining rate/identification gaps.

## 4. Independent Referee

**Goal:** critically audit the **exact version** of a mathematical claim.

- Check the statement, assumptions, notation, conditioning, dimensions, inequalities, signs, constants, stochastic orders, and all cited external lemmas.
- Verify the legitimacy of interchanging expectations, suprema, derivatives, limits, and conditional operations; check the scale of each remainder.
- Check own-observation and own-cluster feedback, optimization residuals, nonsmooth scores, and triangular-array dependence when present.
- Try a short independent proof or counterexample in addition to line-by-line verification. A review must identify the location and consequence of each genuine gap.
- A critique by the same agent in the same context is **self-review**, not independent audit. Mark it accordingly. Only record a separate-context agent or human review as independent, and never pretend that changing roles inside one context guarantees independence.
- A successful review is fallible human/model evidence, not a Lean-style formal certificate.

**Output:** pass/fail/conditional verdict with claim revision, checked lines, severity, proof repairs, and evidence.

## 5. Literature & Novelty Audit

**Goal:** distinguish a new result from a familiar result written in new notation.

- Start with the user's specified anchor papers and the manuscript's references. Read the original theorem, assumptions, and proof (including supplement), not just a search excerpt.
- Construct a comparison with exact model class, observable information, target, nuisance structure, sampling regime, rate, conclusion, and dependencies.
- Classify the relationship: direct implication, special case, extension, incomparable, or not yet verified; give exact proof/theorem locators only if checked.
- Separate improvement in `assumptions`, `estimand`, `rate`, `algorithm`, and `proof technique`. A different method alone does not establish theoretical novelty.
- A negative or incomplete search supports only `novelty not established`, never an assertion that nobody has studied the problem.

**Output:** checked theorem-level comparison, status of the claimed contribution, and unresolved source questions.

## Research-to-writing handoff

Writing follows the logical theorem dependency, not the chronology of attempts. Keep conjectures and conditional results explicitly labeled; do not launder proof gaps or unverified source claims into polished prose. Keep proofs inline or in an appendix according to the existing prose-and-architecture reference. After writing, reconcile every formal claim with its state record and the actual manuscript.
