# LaTeX Source Style

Apply the rule priority and task scope in `../SKILL.md`. Explicit project conventions fill choices not already settled by the user's current instructions or applicable standing preferences. These are personal formula-writing conventions, not journal requirements, and apply to formulas in chat as well as TeX.

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

## Emphasis of mathematical results

Do not use `\boxed{...}`, `\fbox{...}`, `\framebox{...}`, or analogous framed or colored boxes to emphasize mathematical results. Present conclusions in the usual mathematical environments and identify their significance in the surrounding prose. This restriction does not prohibit local explanatory annotations such as `\underbrace{...}_{...}`.

When removing a wrapper in an affected passage, preserve its mathematical content, punctuation, and labels. Existing boxed examples do not override the standing preference; a current explicit user exception does.

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

## Delimiter meaning and adaptive sizing

- Choose visible delimiters by mathematical meaning before considering algebraic nesting. Use parentheses for function arguments, probability, variance, covariance, estimator differences, ordinary grouping, and asymptotic notation. Use square brackets for expectations and extra outer algebraic grouping. Reserve visible braces for sets, events, indicators, and indexed collections; do not add braces merely because an expression has another nesting level.
- Keep an object's delimiter type fixed under nesting: write `\E\left[\left(Y_{i} - g\left(X_{i},\theta_{0}\right)\right)X_{i} \mid Z_{i}\right] = 0`, `\Pp\left(A\right)`, `\Var\left(X\right)`, and `O_{p}\left(n^{-1 / 2}\right)`. Repeated parentheses are acceptable. For purely algebraic nesting, use inner parentheses and outer square brackets without mechanically progressing to braces.
- Make visible mathematical delimiters adaptive throughout the affected formulas: pair `\left(` with `\right)`, `\left[` with `\right]`, and `\left\{` with `\right\}`. Size absolute values, norms, and inner products consistently with `\left|...\right|`, `\left\|...\right\|`, and `\left\langle...\right\rangle`. Preserve the meaning of interval endpoints, set cardinalities, conditional bars, and argument separators.
- Every `\left` and `\right` pair must close within one math group and one alignment row. If a derivation must continue on another row, use matching invisible delimiters `\right.` and `\left.` at the row boundary, then inspect the result. Do not create unmatched pairs across rows or across superscript/subscript groups.
- These rules concern visible mathematical delimiters. Preserve TeX argument braces, script braces, optional arguments, theorem titles, text punctuation, labels, citation keys, and bibliography metadata. Do not apply a blind document-wide character substitution.

## Explicit braces for math commands and scripts

- Enclose the argument of every math-alphabet or font command in explicit braces, even when it is one token. Write `\mathsf{A}`, `\mathcal{F}`, `\mathrm{d}`, `\mathbf{x}`, `\mathbb{R}`, and analogous commands; never rely on next-token forms such as `\mathsf A`, `\mathcal F`, or `\mathrm d`.
- Apply the same rule to mathematical accents and decorators. Write `\hat{\theta}`, `\widehat{\theta}`, `\tilde{x}`, `\widetilde{x}`, `\bar{x}`, `\overline{x}`, `\vec{x}`, `\dot{x}`, and analogous commands, never `\hat \theta`, `\hat\theta`, or another unbraced next-token form.
- Always brace subscripts and superscripts, including one-token scripts: write `x_{i}`, `x^{2}`, and `\hat{\theta}_{t}`, not `x_i`, `x^2`, or `\hat{\theta}_t`.
- More generally, when a mathematical command takes an argument, delimit that argument explicitly with braces rather than relying on TeX's next-token parsing. This rule does not add braces to commands that take no argument in that position, such as relation symbols or named operators.
- Do not redefine standard commands such as `\hat`, `\tilde`, or `\bar`.
- Preserve the manuscript's established transpose, norm, support, probability, and expectation macros.

## Source-line discipline

- Keep short definitions, notation introductions, routine identities, and short rate conditions inline. For example, write `Also require $\sqrt{NT}b^{m} \to 0$.` within its paragraph. Use displays for substantive results, long expressions, and derivations that benefit from alignment; do not display every formula.
- Keep a formula or equality/inequality chain on one mathematical row and one source line whenever it fits. Break it only when readability, a distinct derivation step, or the available page width requires it; do not put each equality or inequality on a separate row mechanically.
- Keep each row's left-hand side, relation, delimiters, conditions, and punctuation together. Never isolate `:=`, `=`, a brace, or a single summand on its own source line.
- Use multiple rows for genuine step-by-step derivations, matrices, or case splits. Align necessary breaks with mathematical operations and preserve every substantive intermediate expression.
- Keep actual successive calculations together in `align` or `aligned`. Connect distinct assertions with brief prose instead of collecting unrelated conclusions into one display.
- Preserve existing notation. Do not introduce auxiliary symbols merely to shorten a formula or make it fit on one line.

## Local explanations inside calculations

- When one assumption or identity licenses several rows, state it in a sentence before the display.
- When it licenses one row of an `align` derivation, use a compact annotation column such as `&& \text{by Assumption~\ref{ass:curvature}}`.
- Use `\underbrace{...}_{...}` only when the explanation belongs to a specific local term that is identified, bounded, or replaced immediately. For example, write `\underbrace{\left\langle u, v \right\rangle}_{= 0 \text{ by orthogonality}}` when that inner product vanishes at the current step.
- Name the exact assumption, lemma, identity, or condition; avoid vague annotations such as `\text{by assumptions}`.
- Keep annotations short and mathematical. If an annotation makes the row wide or requires a sentence, move the explanation before the display; do not embed a paragraph inside math.

## Cross-references and environments

- Use `\eqref{...}` for equations.
- Use nonbreaking spaces in references, such as `Theorem~\ref{...}` and `Appendix~\ref{...}`.
- Preserve valid labels when reorganizing a manuscript.
- Define notation before the assumption or theorem that uses it.
- Use `definition` for a central object, `assumption` for a substantive model condition, and `remark` for non-obvious interpretation or boundaries.

## Verification

After editing TeX, use the verification scope in `../SKILL.md`. Compile the requested target when available; inspect the changed material and affected pages, and distinguish new problems from pre-existing diagnostics. Once relevant checks pass, repeat or broaden them only if new changes or unresolved evidence justify it.

1. compile the requested target with the project's build command;
2. check undefined and multiply defined references;
3. check package errors and relevant warnings;
4. inspect overfull and underfull boxes;
5. visually inspect affected pages when displays, annotations, tables, algorithms, or page breaks changed;
6. compare affected numbered display rows with their later equation cross-references, including rows inside `align`; convert affected fully unreferenced displays to `align*`, suppress unreferenced rows in affected mixed displays, and remove the corresponding unused labels only after checking their uses throughout the manuscript;
7. review the diff for accidental notation, label, and scope changes.

If an unresolved mathematical issue is outside the authorized edit, mark the exact TeX location with `% TODO-MATH:` and report it to the user. Do not use a prose rewrite to conceal the issue.
