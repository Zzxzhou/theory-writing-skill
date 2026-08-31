# Reader-Verifiable Proofs

Proofs are written for readers, not stored as certificates of correctness. A technically prepared reader should be able to verify each substantive transition without reconstructing omitted algebra.

## Context loop

Before writing:

1. Read the theorem, all assumptions it invokes, definitions of every object, and the preceding setup.
2. Read the paragraph after the theorem to learn which interpretation and scope the manuscript promises.
3. Locate earlier lemmas, notation, events, and analogous proofs. Reuse them when they fit.
4. Identify the logical spine from the original estimator, objective, model equation, or optimality condition to the claimed result.

For a long proof, repeat this context check after each major module. After writing, reread the same context once more. Verify that the proof uses the manuscript's current notation, information structure, assumptions, and claim rather than a remembered or stronger version.

## Proof roadmap

For a long proof, begin with a short roadmap that names the mathematical operations or dependent modules. Do not write a generic table of contents. Each roadmap item should tell the reader what the step accomplishes.

Useful patterns include:

- reduce the stochastic claim to a deterministic inequality;
- establish the high-probability certificate;
- derive the basic inequality and cone condition;
- profile a nuisance parameter;
- apply curvature and obtain the norm rate;
- derive the normal equation and risk decomposition.

Use named steps only when they help navigation. A short continuous argument does not need artificial headings.

## Derivation before theorem packaging

Use a derivation-first workflow whenever a result is being constructed, extended, or transported rather than merely typeset from an already verified proof. This rule governs the order of mathematical work, not necessarily the final order of exposition: the finished manuscript may place a theorem before its proof, but the theorem statement must be earned by a completed derivation before it is finalized.

### Construction pass

1. Fix the endpoint and required resolution. State the primitive object, the quantity to be derived, the conditioning or information structure, and whether the target is first order, second order, uniform, conditional, finite-sample, or another specified scale. A term may not be discarded until it is shown to be negligible relative to that scale.
2. Start from the model equation, estimator, objective, sample moment, estimating equation, or optimality condition. Write the first decomposition as an exact identity and state explicitly that no approximation has yet been made.
3. Separate the roles of the proof devices. Identify which step supplies localization, which supplies linearization, which controls stochastic fluctuations, which identifies an expectation or bias, and which makes the result feasible. Do not present a preliminary device as the main mechanism merely because it appears early in the proof.
4. Separate components by mathematical status. Mark exact identities, deterministic expansions with explicit remainders, stochastic bounds, conditional statements, and expectation calculations. Expand only objects for which the required smoothness has been established; in particular, do not Taylor-expand a discontinuous sample object merely because its population counterpart is smooth.
5. Derive the leading approximation from the linear part, substitute it back into the same exact decomposition, and expose every correction channel. Retain every term that can contribute at the target scale instead of absorbing it into a generic Bahadur, Taylor, or empirical-process remainder.
6. Before replacing an estimator or another random argument by its leading approximation inside a nonlinear term, display the algebraic difference and prove its order. State the rates of both factors whose product yields the claimed remainder; a shared first-order rate alone does not justify replacement.
7. Audit stochastic size and expectation separately. A term that is too large to discard in probability may have a smaller structured expectation, but that expectation requires its own calculation. An $O_p$ bound does not by itself imply a bias or conditional-expectation bound.
8. Resolve dependence, nonsmoothness, optimization residuals, and boundary effects at the point where they enter. Expose own-observation feedback before invoking leave-one-out or conditioning, and derive the relevant subgradient or KKT residual rather than replacing it by an unjustified zero.
9. Close the remainder calculation at the target scale. Give every load-bearing technical input exactly one honest status: proved here; invoked from a precise result after checking its conditions; imposed transparently as an assumption for a conditional theorem; or left explicitly open. Explanatory prose, a desired rate, or a structural analogy is not a proof.
10. Only after the chain closes, synthesize the result into lemmas, a theorem, and corollaries. Match every theorem assumption to the exact transition where it is used, and do not let theorem packaging erase the mechanism that produced the result.

### Transporting a method

When importing a method from another paper or model:

1. Derive the source mechanism line by line in the smallest setting in which it is valid.
2. Separate exact algebraic identities from smooth expansions, stochastic bounds, distributional assumptions, and source-specific dimension restrictions.
3. Identify the main engine and distinguish it from tools that provide only localization, regularity, or auxiliary control.
4. Give an object-by-object map from the source setting to the target setting.
5. Re-derive the target model's exact identity from its own primitive object. Structural similarity is a guide, not a proof.
6. State precisely which source steps survive unchanged and which become new technical obligations because of dimension growth, dependence, normalization, nuisance parameters, conditioning, or a different sampling structure.
7. Do not finalize the target theorem until those obligations have been proved or assigned one of the explicit statuses in the construction pass.

For every substantive transition $A\to B$, the reader must be able to identify the immediately preceding expression, the single principal operation performed, the fact licensing that operation, the statement's mathematical status, and the remainder scale when applicable. If the reader must invent an intermediate identity, import an unstated rate, or guess why a target-order term disappears, the derivation is too compressed. Step-by-step exposition does not require displaying every formula; it requires showing every load-bearing transition.

## Continuous derivation

- Start from the original object, not from an unexplained intermediate formula.
- Keep related calculations in one continuous `align` chain when practical.
- Display each load-bearing expansion, substitution, cancellation, and inequality.
- Let formulas carry routine algebra. Use prose to state the assumption, identity, optimality condition, or certificate that licenses the next transition.
- Annotate an equality or inequality locally when the reader otherwise cannot tell which assumption justifies it.
- Do not replace several steps with “by a standard argument,” “after simplification,” “by calculation,” or “the result follows.”

For an optimization proof, show the following steps when present:

1. objective difference or optimality inequality;
2. model substitution;
3. quadratic expansion;
4. substitution of established Gram, score, or residual notation;
5. profiling or minimization over nuisance variables;
6. basic inequality;
7. cone implication;
8. curvature or compatibility step;
9. norm-rate calculation;
10. normal equation and risk decomposition.

Expand a quadratic before replacing it with compressed notation. When completing a square or profiling a variable, display the square, show why it is nonnegative, and identify the value at which it vanishes.

## Step granularity and justifications

The test is not whether a step is elementary. The test is whether the reader can verify the transition without reconstructing missing work. Display an intermediate line whenever a transition:

- performs more than one algebraic operation;
- expands, factors, rearranges, reindexes, or substitutes an expression in a way that changes its visible structure;
- invokes a definition, assumption, lemma, event, optimality condition, or probabilistic certificate;
- removes a term, declares a term nonnegative or zero, bounds a term, or changes an equality into an inequality;
- divides, cancels, normalizes, takes a norm, expectation, supremum, or probability, or otherwise changes the type of the mathematical object;
- contains a sign, factor, transpose, index, conditioning set, or constant that a compressed step could obscure.

In a multiline derivation, keep one principal transformation on each row. A mechanical row does not need a prose sentence when the displayed formulas make the operation evident, but it should still be shown when it exposes a quantity the reader must check. Do not compress $A \to B \to C$ into $A \to C$ merely because both omitted operations are individually simple.

Identify why each non-obvious equality or inequality is valid. Use the following order:

1. a sentence before the display when one assumption or identity licenses several rows;
2. a short annotation on the relevant row when it licenses one transition;
3. an `\underbrace{...}_{...}` when the explanation belongs to one specific term.

Name the exact assumption, lemma, identity, or condition instead of writing “by assumptions.” Keep local annotations short. If the explanation requires a sentence, put it before the display rather than forcing it inside the formula.

## Cancellations, conditioning, and edge cases

- Display a cross term before setting it to zero.
- Name the centering, orthogonality, independence, measurability, or optimality condition that removes it.
- When canceling a norm or denominator, handle the zero case before dividing unless nonzero status is already explicit.
- Track sigma-fields and the timing of random quantities when data are adaptive.
- State whether an event is pathwise, conditional, or high probability, and preserve its failure probability.
- Check boundary values and degenerate cases when the proof's algebra changes there.

## Notation gate

Do not introduce notation merely to shorten the current line. Before adding a symbol, ask:

1. Is the expression used repeatedly?
2. Does the new symbol reveal structure that the original notation hides?
3. Can the reader infer its type, dimension, and role at first use?
4. Will it remain useful after this proof step?
5. Does it conflict with notation elsewhere in the manuscript?

If the answers do not justify the symbol, keep the original expression. In complicated calculations, preserving the original notation may expose cancellations, block structure, or dependence that an alias would conceal. Remove stale notation after reorganizing a proof.

## Verification checklist

- Recompute every sign, factor, transpose, dimension, and inequality direction.
- Verify that all assumptions used are available at the exact step where they are invoked.
- Verify constants and probability allocations against the theorem statement.
- Check that every symbol is defined before use and has the same meaning in the main text and appendix.
- Check that prose claims exactly what the displayed calculation proves.
- If a gap remains, state it explicitly; do not bridge it with rhetoric.
