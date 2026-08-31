# LaTeX Source Style

Follow a repository's explicit local guide when it conflicts with this reference. Otherwise use these conventions as the default personal profile.

## Math environments

- Use `$...$` for inline mathematics.
- Use `align*` for unnumbered displays and derivations.
- Use `equation` for a numbered one-line display.
- Use `equation` with nested `aligned` for a numbered multiline display.
- Avoid `$$...$$`, `\[...\]`, and `equation*` under this profile.
- Number a display row only when it is explicitly cross-referenced later in the manuscript with `\eqref{...}` or the manuscript's equivalent equation-reference command.
- Put every unreferenced display in `align*`. When an existing multirow `align` contains both referenced and unreferenced rows, retain numbers only on the referenced rows; remove each unused `\label{...}` and add `\notag` to the corresponding unreferenced row.
- Do not leave an automatic number on a row without a label.
- End displayed equations with the punctuation required by the surrounding sentence.

## Operator spacing in source

Put one source space on both sides of binary operators and relations, including `+`, binary `-`, `\times`, `\cdot`, `=`, `<`, `>`, `\leq`, `\geq`, and analogous symbols.

Prefer:

```tex
x + y, \qquad x - y, \qquad A \times B, \qquad u \cdot v,
```

and

```tex
\hat{\theta}_{t} = \theta_{0} + \Delta_{t}.
```

Avoid source such as `x+y`, `x-y`, or `A\times B`. Treat a unary sign differently: write `-x`, not `- x`. Do not insert spaces inside subscripts or superscripts solely to satisfy the binary-operator rule.

## Explicit braces for math commands and scripts

- Enclose the argument of every math-alphabet or font command in explicit braces, even when it is one token. Write `\mathsf{A}`, `\mathcal{F}`, `\mathrm{d}`, `\mathbf{x}`, `\mathbb{R}`, and analogous commands; never rely on next-token forms such as `\mathsf A`, `\mathcal F`, or `\mathrm d`.
- Apply the same rule to mathematical accents and decorators. Write `\hat{\theta}`, `\widehat{\theta}`, `\tilde{x}`, `\widetilde{x}`, `\bar{x}`, `\overline{x}`, `\vec{x}`, `\dot{x}`, and analogous commands, never `\hat \theta`, `\hat\theta`, or another unbraced next-token form.
- Always brace subscripts and superscripts, including one-token scripts: write `x_{i}`, `x^{2}`, and `\hat{\theta}_{t}`, not `x_i`, `x^2`, or `\hat{\theta}_t`.
- More generally, when a mathematical command takes an argument, delimit that argument explicitly with braces rather than relying on TeX's next-token parsing. This rule does not add braces to commands that take no argument in that position, such as relation symbols or named operators.
- Do not redefine standard commands such as `\hat`, `\tilde`, or `\bar`.
- Preserve the manuscript's established transpose, norm, support, probability, and expectation macros.

## Source-line discipline

- Keep one semantic mathematical row on one source line whenever it remains readable.
- A row should keep its left-hand side, relation, delimiters, conditions, and punctuation together.
- Never isolate `:=`, `=`, a brace, or a single summand on its own source line.
- Break a display for a genuine derivation, case split, matrix, or expression that cannot be read safely on one line.
- Align line breaks with mathematical operations.
- Keep closely related derivations in one `align` or `aligned` block instead of alternating displays and narrative paragraphs.

## Local explanations inside calculations

- When one assumption or identity licenses several rows, state it in a sentence before the display.
- When it licenses one row of an `align` derivation, use a compact annotation column such as `&& \text{by Assumption~\ref{ass:curvature}}`.
- Use `\underbrace{...}_{...}` only when the explanation belongs to a specific local term that is identified, bounded, or replaced immediately. For example, write `\underbrace{\langle u, v \rangle}_{= 0 \text{ by orthogonality}}` when that inner product vanishes at the current step.
- Name the exact assumption, lemma, identity, or condition; avoid vague annotations such as `\text{by assumptions}`.
- Keep annotations short and mathematical. If an annotation makes the row wide or requires a sentence, move the explanation before the display; do not embed a paragraph inside math.

## Cross-references and environments

- Use `\eqref{...}` for equations.
- Use nonbreaking spaces in references, such as `Theorem~\ref{...}` and `Appendix~\ref{...}`.
- Preserve valid labels when reorganizing a manuscript.
- Define notation before the assumption or theorem that uses it.
- Use `definition` for a central object, `assumption` for a substantive model condition, and `remark` for non-obvious interpretation or boundaries.

## Verification

After editing TeX:

1. compile the requested target with the project's build command;
2. check undefined and multiply defined references;
3. check package errors and relevant warnings;
4. inspect overfull and underfull boxes;
5. visually inspect affected pages when displays, annotations, tables, algorithms, or page breaks changed;
6. compare every actual numbered display row with the set of later equation cross-references, including rows inside `align`; convert fully unreferenced displays to `align*`, suppress unreferenced rows in mixed displays, and remove the corresponding unused labels;
7. review the diff for accidental notation, label, and scope changes.

If an unresolved mathematical issue is outside the authorized edit, mark the exact TeX location with `% TODO-MATH:` and report it to the user. Do not use a prose rewrite to conceal the issue.
