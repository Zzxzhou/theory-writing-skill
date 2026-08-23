---
name: theory-writing-skill
description: Draft, revise, structure, and audit reader-facing theoretical research prose, theorem statements, mathematical proofs, and LaTeX source in economics, econometrics, statistics, machine learning, and operations research. Use for theory papers, research notes, technical appendices, proof revisions, notation decisions, document architecture, or mathematical typesetting. Do not use for ordinary nontechnical prose or purely empirical reporting without mathematical exposition.
---

# Theory Writing

Write so that a technically prepared reader can locate the claim, understand its mechanism, and verify every substantive transition. Preserve mathematical correctness and local manuscript conventions over generic stylistic preferences.

## Route the task

Load only the references needed for the request:

- For abstracts, introductions, theorem interpretation, section organization, or prose revision, read `references/prose-and-architecture.md`.
- For any theorem, lemma, derivation, optimization argument, or proof audit, read `references/reader-verifiable-proofs.md` completely.
- For TeX creation or editing, read `references/latex-source-style.md` completely in addition to the substantive reference.
- When the user requests Dennis Shen's style, a style comparison, or an exemplar-based rewrite, read `references/style-exemplars.md`.
- When a manuscript provides local instructions or a private project profile, read those materials before applying the general defaults in this skill.

If the task spans multiple modes, load every applicable reference before editing.

## Establish context before writing

1. Read local instructions, manuscript guides, canonical examples, and the relevant Git diff when available.
2. Read the definitions, assumptions, theorem statement, preceding setup, following interpretation, and any proof that depends on the passage being edited.
3. Identify the document mode: submission manuscript, research note, technical note, early draft, lecture note, or appendix.
4. Determine whether the requested change is prose-only, formatting-only, exact author-supplied mathematics, or a substantive mathematical change.
5. Preserve established notation and placement unless the user or document structure authorizes a change.

For proof work, reread the surrounding context both before drafting and after completing the proof. Check that every object, condition, and claimed implication still matches the manuscript.

## Non-negotiable rules

- Preserve assumptions, events, constants, signs, inequality directions, conditioning information, probability allocations, and theorem scope.
- Make proofs reader-verifiable. Do not hide load-bearing algebra behind “standard,” “straightforward,” “by calculation,” or “the result follows.”
- Do not introduce notation casually. Add a symbol only when it reduces total reader burden or reveals a recurring structure.
- Treat proof placement as conditional. Move material to an appendix only after the document has entered an appendix-oriented mode or the user explicitly requests that split.
- In a note or an undecided draft, keep an existing inline proof inline unless there is a concrete reason to move it.
- Use direct, positive prose, but retain qualifications that define the mathematical claim or its boundary.
- Use external authors as structural exemplars only. Do not imitate distinctive wording or reproduce passages.

## Revise and verify

- Make the smallest coherent edit that satisfies the request; preserve unrelated user changes.
- After mathematical edits, independently check each sign, factor, dimension, equality, inequality, and cancellation.
- After TeX edits, compile the requested target and inspect warnings, references, overfull boxes, and affected pages when the environment permits.
- Review the diff for accidental changes to notation, assumptions, theorem scope, labels, and proof placement.
- If a substantive issue cannot be resolved within scope, identify it explicitly instead of smoothing it over with prose.
