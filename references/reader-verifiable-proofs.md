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
