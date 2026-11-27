# Mathematical Notation Discipline

Use this reference when selecting, introducing, transporting, revising, or auditing mathematical notation in chat, research notes, proofs, and LaTeX. It complements reader-verifiable-proofs.md and latex-source-style.md. The objective is not the fewest symbols or shortest display: it is the lowest reader effort compatible with an exact, verifiable argument.

## 1. Authority and mathematical contract

- Follow the user's explicit notation decisions and the current manuscript's canonical definitions, local guide, and macros. Inspect the relevant surrounding statements, proof dependencies, appendices, and recent changes. Field conventions are defaults for genuinely new objects, not permission to rename existing ones.
- Distinguish a choice of symbol from a change of object. Preserve domains, codomains, units, normalization, information sets, parameter classes, quantifiers, signs, rates, and scope. If sources conflict or a definition is ambiguous, identify the conflict before relying on it. Never resolve a substantive ambiguity through a silent stylistic edit.
- When importing a result, map the source objects to the current objects, including their assumptions and scaling. Use the current notation in the derivation; do not copy a source alphabet unless authorized. Maintain an explicit correspondence where a reader or reviewer needs it.
- Treat an authorized renaming as a coordinated migration: check all affected statements, proofs, macros, cross-references, figures, tables, captions, and supplementary material. If the requested scope does not permit that migration, preserve the notation and flag the conflict.

## 2. Introduction test: earn every new symbol

Before introducing a nonstandard auxiliary symbol, check:
1. Is this a genuinely distinct object, a recurring quantity, or a structural representation needed for the argument?
2. Is its role easier to understand with a name than by retaining the original expression?
3. Does the name preserve the object's origin, indices, arguments, and mathematical status?
4. Is it compatible with existing names and the discipline's conventions?
5. Can the definition be placed immediately before the reader needs it?

If the answer does not justify the name, retain the original expression or use words. An alias used once or twice is presumptively unnecessary, but a one-use symbol is legitimate if it is needed as a bound variable, witness, construction, or genuinely clarifying structural decomposition. Repeated use alone is not sufficient. Do not alias an already named quantity, relabel a subscripted component just to remove its index, or build a chain of aliases for a simple expression.

There is no universal numerical cap on new symbols. For a long proof, assess how many distinct meanings and conversions the reader must remember simultaneously, and remove redundant names. Retain meaningful abstractions such as a projection, influence function, filtration, or covariance matrix when the proof exploits their properties.

## 3. Declare the object, then use it

Introduce nonstandard notation in a complete mathematical statement before first use. Specify, as relevant:

- what it is and why it is needed (e.g. the conditional bias, the estimated Hessian, the error from truncating an expansion);
- mathematical type, domain/codomain or dimensions, and index ranges;
- whether it is known, unknown, observed, latent, deterministic, random, fixed, chosen, or optimized;
- relevant arguments, evaluation point, normalization, and conditioning information;
- what it depends on, what varies, and the scope in which the definition applies.

Do not turn every definition into a bureaucratic checklist in the prose. Ordinary notation and clearly bound dummy indices need no redundant declaration. A central object belongs in the model setup; a temporary object belongs in the proof near its first sustained use. If a definition is needed across a long interruption, recall its role and the critical formula or argument locally. A glossary or macro comment does not replace a mathematical definition in the document.

Make declarations, assumptions, identities, implications, and approximations distinguishable. Use definition language or := for a genuine definition, equality for an established identity, and approximation/order notation only when its meaning has been established. Do not use "equivalently" for a one-way implication or call an approximation an identity.

## 4. Preserve the identity of objects through the derivation

- Start from the original model, estimator, objective, moment, or other primitive object. Derive the exact expression in that notation before compressing it into auxiliary objects.
- Keep related quantities visibly related. Prefer recognizable component, derivative, increment, or indexed notation to independent names where that reveals the connection. Use a consistent index order, adornment convention, and typography. Preserve the existing distinction between an estimand and estimator, population and sample, true and candidate parameter, oracle and feasible object, original and normalized object, leading term and full remainder.
- At a change of coordinates, basis, scale, measure, or conditioning set, give the conversion equation, explain its purpose, and explain how it maps back to the object of interest when relevant. If a transformation is not invertible, state what information it preserves rather than claiming recovery.
- Expand an auxiliary quantity at the first load-bearing use when its definition is needed to see an index, cancellation, normalization, rate, or dependence. After a long estimate, identify terms by mathematical origin rather than a bare list of letters. Reconnect the conclusion to the original target.
- Do not hide mathematical work by inventing a symbol for an unresolved term. A remainder must have an exact defining difference and a justified bound or an explicitly open obligation at the required resolution.

## 5. Statistical and econometric distinctions

Use the following checks whenever they affect a result; do not impose a new universal alphabet.

- Keep the unit, time, coordinate, treatment, sample-split, and approximation indices distinct. Check free and bound indices and summation ranges. Use an unambiguous diagonal entry such as $A_{jj}$ when $A_j$ would be unclear.
- State whether a probability, expectation, covariance, or variance is under a sampling law, experimental randomization, a posterior, or a conditional law when more than one is present. Specify the sigma-field and measurability when an adaptive argument requires them. Never replace local conditioning by full-design conditioning without verification.
- Distinguish pointwise and uniform rates, deterministic and stochastic orders, conditional and unconditional results, and finite-sample from asymptotic assertions. Identify the limit path when several dimensions grow.
- For a bound, identify relevant constants and their allowed dependencies. A claimed uniform constant must not depend on the variable over which uniformity is asserted. A generic constant may change from line to line only under a stated convention that preserves the required uniformity.
- Distinguish a scalar loss or risk from a vector error, the operator norm from other norms when ambiguous, and matrix multiplication from coordinatewise operations. Check matrix shapes, derivative orientation, transpose conventions, and norm domains.
- Do not suppress a parameter, sample size, network, design, evaluation point, or conditioning argument when the omission obscures which quantity is fixed, varies, is estimated, or is optimized. After explicitly establishing a convention, omit redundant arguments when the local context is unambiguous.
- Prefer standard mathematical nouns and field-recognizable symbols. Related objects should use harmonious names, and visually confusable glyphs should not denote distinct nearby objects. Avoid mechanically enforcing bold, calligraphic, or other font rules when the manuscript has its own consistent convention. Dummy indices may be reused in disjoint, unmistakable scopes; do not overload a persistent symbol with unrelated meanings.

## 6. Match notation density to the task

**Research / proof discovery / explanation:** Default to transparent calculations with the original objects, explicit conversions, dependencies, and intermediate identities. Use the user's requested pace; for a question about a particular equality, begin with that equality and expose its algebra instead of inventing a new setup. A new meaningful abstraction can be explored, but explain it before relying on it. Do not force a theorem-first presentation during discovery.

**Verified manuscript / publication polishing:** Compress routine material only when the underlying argument is established and the reader can still verify every substantive transition. Preserve the mathematical contract, local style, and proof placement. Remove obsolete notation and unused aliases; use descriptive references to identify the mathematical job of distant lemmas or equations. Keep important definitions and statement prerequisites accessible at point of use.

**Formatting-only revision:** Do not rename symbols or change mathematical meaning merely to normalize style. Follow latex-source-style.md and the local preamble. Prefer inline math for small expressions and existing align* conventions for important displays and derivations. A compiled document is not evidence that its notation is coherent.

## 7. Maintain continuity across sessions

At the start of substantial multi-session work, read the canonical manuscript and any existing notation guide or project state. For a long project with recurring ambiguity or several agents, maintain a compact project-local notation register only when useful or requested. Do not create extra files for a short proof or require a register for routine prose edits. An existing glossary or notation file can serve this purpose.

A register may have columns: Symbol (and macro if any), mathematical meaning, type/shape, range or domain, dependencies/conditioning, scope, canonical definition locator. Record persistent and potentially confusable objects, not every dummy variable. Keep proof-local abbreviations in their local scope. If an authorized change occurs, record the old/new correspondence and affected locations; update the canonical manuscript and register together. Do not store private project notation in this reusable skill.

Use the existing research-state workflow for claims, evidence, and mathematical revisions. A change of symbol alone does not establish a new theorem or invalidate a proof; a change in what the symbol denotes, its quantifiers, or information structure may change the mathematical claim and must follow the existing revision rules. No schema extension is required by this reference.

## 8. Notation audit (separate from proof correctness)

After a substantial proof, derivation, or notation edit, perform a separate reading pass before delivery. For an audit-only request, report issues without changing the manuscript.

- Declaration and scope: can every nonstandard symbol be traced to its definition? Are free variables quantified, indices bound, and local aliases used only within their scope?
- Identity and drift: do the same persistent symbols refer to the same objects throughout the affected context? Are changes of representation explicitly linked?
- Mathematical contract: check dimensions, normalization, constants, conditioning, quantifiers, uniformity, rate and limit regimes; flag substantive ambiguity instead of guessing.
- Economy: remove aliases with no expository or mathematical payoff; restore meaningful arguments or indices that a shortcut concealed.
- Reader replay: read the argument in order using only the information introduced so far and declared prerequisites. At each load-bearing transition, check that a reader can identify the original object, the operation, its justification, and the resulting quantity without inventing a missing identity.
- Source fidelity: compare the revised passage to the canonical notation and macros, and check dependent locations when changes are authorized. Preserve existing labels unless the equation-numbering rule requires a change.
- Handoff: report significant conflicts, unresolved ambiguities, or authorized migrations with their locations and consequences. Do not add a ceremonial checklist to every answer. A self-audit is not independent proof verification.

A missing definition, incompatible dimension, or ambiguous conditioning that affects the claim blocks acceptance of the affected mathematical step. A merely cumbersome notation choice is an exposition issue, not evidence that a theorem is false. Treat the two separately.

## 9. Calibration examples (original synthetic examples)

These examples are behavioral checks, not rules to replace local notation or automatically rewrite a paper.

**Unnecessary alias.** Given a known scalar parameter $\theta_0$ and its estimator $\hat{\theta}_n$, prefer $\mathbb{E}[(\hat{\theta}_n-\theta_0)^2]$ to defining a new error and a new risk only to state the same quantity once. A repeated error in a lengthy expansion may merit a name.

**Recognizable derivatives.** If $g_i(\theta)$ is already defined, use $\nabla_\theta g_i(\theta)$ and $\nabla_\theta^2 g_i(\theta)$ at the first derivative calculation. A named Hessian is appropriate if its matrix properties or repeated use matter; define it as the derivative of $g_i$.

**Risk before compression.** For scalar outcomes with finite second moments and deterministic weights, expand the variance of $\sum_t w_t Y_t$ as $\sum_{t,s} w_t w_s\operatorname{Cov}(Y_t,Y_s)$. If spectral bounds follow, define the covariance matrix entry-by-entry and then write its quadratic form. Do not start with an unexplained covariance operator.

**Uniformity.** A bound with $C_\theta$ for each $\theta$ does not imply a bound with a common $C$ over $\Theta$. Verify the dependence and quantifier order before claiming a uniform rate.

**Conditional information.** $\mathbb{E}[Y_i\mid Z_i]$ and $\mathbb{E}[Y_i\mid Z_1,\ldots,Z_n]$ are not generally the same. Preserve the full argument until a compatibility condition or valid identity permits a reduction.

**Source mapping.** If a cited paper denotes a sum by $S_n$ and the current manuscript denotes its average by $S_n$, write the mapping in distinct temporary source notation and account for the factor $n$. Do not assert equal rates or copy the source symbol unmodified.

## Sources and design rationale

This reference is an original synthesis for mathematical statistics, econometrics, and related theory. It draws on the principles of symbol economy, coordinated names, linear presentation, and explicit mathematical declarations in:

- Paul R. Halmos, *How to Write Mathematics*, especially Sections 5 and 15: https://www.scott-nelson.net/readings/Halmos1973.pdf
- Dimitri P. Bertsekas, *Ten Simple Rules for Mathematical Writing*: https://web.mit.edu/dimitrib/www/Ten_Rules.html
- Keith Conrad, *Advice on Mathematical Writing*: https://kconrad.math.uconn.edu/blurbs/proofs/writingtips.pdf
- Amelie Loher and contributors, *Mathematics Paper Skills*, especially artisan-writing.md (CC BY 4.0): https://github.com/amelieloher/math-paper-skills
- *The Agentic Researcher*, mathematical research module: https://github.com/ZIB-IOL/The-Agentic-Researcher
- *Math Prose*, mathematical actions and preservation of claims: https://github.com/TianhuaGao/math-prose
- *Mathematical Academic Writing*, source and notation fidelity: https://github.com/JiahaoLi-creator/mathematical-academic-writing
- *AI4Math-Writing*, modular notation audit: https://github.com/VeryMath/AI4Math-Writing

The operational rules, statistical examples, project continuity mechanism, and audit are tailored to this skill. They are not a claim of formal verification or a benchmarked improvement in model performance.
