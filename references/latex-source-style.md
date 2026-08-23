# LaTeX Source Style

Follow a repository's explicit local guide when it conflicts with this reference. Otherwise use these conventions as the default personal profile.

## Math environments

- Use `$...$` for inline mathematics.
- Use `align*` for unnumbered displays and derivations.
- Use `equation` for a numbered one-line display.
- Use `equation` with nested `aligned` for a numbered multiline display.
- Avoid `$$...$$`, `\[...\]`, and `equation*` under this profile.
- Number only equations referenced later.
- End displayed equations with the punctuation required by the surrounding sentence.

## Operator spacing in source

Put one source space on both sides of binary operators and relations, including `+`, binary `-`, `\times`, `\cdot`, `=`, `<`, `>`, `\leq`, `\geq`, and analogous symbols.

Prefer:

```tex
x + y, \qquad x - y, \qquad A \times B, \qquad u \cdot v,
```

and

```tex
\hat{\theta}_t = \theta_0 + \Delta_t.
```

Avoid source such as `x+y`, `x-y`, or `A\times B`. Treat a unary sign differently: write `-x`, not `- x`. Do not insert spaces inside subscripts or superscripts solely to satisfy the binary-operator rule.

## Braces and accents

- Always write `\hat{...}` with explicit braces, even for one token: `\hat{\theta}`, not `\hat \theta` or `\hat\theta`.
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

- Use `\underbrace` only for a local block identified or replaced immediately.
- Keep annotations short and mathematical.
- When a condition justifies a transition, use a brief `\text{...}` annotation or a preceding sentence; do not embed a paragraph inside math.

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
6. review the diff for accidental notation, label, and scope changes.

If an unresolved mathematical issue is outside the authorized edit, mark the exact TeX location with `% TODO-MATH:` and report it to the user. Do not use a prose rewrite to conceal the issue.
