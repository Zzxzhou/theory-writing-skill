# Prose and Architecture

## Reader-facing objective

Organize the manuscript around what the reader must understand and verify, not around the chronology of discovery. State the question, answer, mechanism, and scope in that order when the material permits.

- Prefer direct, idiomatic sentences.
- Prefer two short sentences to one sentence carrying several logical jobs.
- Keep transitions short. Name the reason for the next step rather than narrating algebra already visible in a display.
- Use ordinary mathematical language when specialized terminology adds no precision.
- Put the positive claim before limitations. State what the paper proves, why it matters, and where it applies.
- Remove throat-clearing, apology-like framing, inflated adjectives, and negotiation with an imagined referee.

## Theory-sensitive anti-defensive writing

Directness must not erase mathematical boundaries.

Preserve a qualification when it:

- changes a definition, assumption, implication, or theorem scope;
- distinguishes a pathwise, high-probability, or expected statement;
- separates the paper's object from an adjacent theory;
- explains why a tempting stronger statement is false;
- records a counterexample or a genuine boundary of the result;
- distinguishes a proved theorem, conditional interface, benchmark, diagnostic, or conjecture.

Rewrite or delete a qualification when it merely repeats formal scope, anticipates criticism without adding logic, or uses vague hedging instead of naming the source of uncertainty.

## Paragraph and section logic

- Give each paragraph one main job. Put that job in the opening sentence when possible.
- Map contributions to the questions or obstacles they resolve.
- State a theorem as soon as the reader has the objects needed to understand it.
- Interpret the theorem near its statement: identify the mechanism, comparison, and headline rate or qualitative implication.
- Place machinery after the result it serves unless the reader needs that machinery to parse the statement.
- Organize technical sections by logical dependency rather than discovery order.
- Give central assumptions, theorems, propositions, and lemmas descriptive titles when the local style permits.
- Use remarks for non-obvious interpretation, comparisons, or subtle boundaries, not to repeat the preceding display.

## Main text and appendix trigger

Do not assume every project uses a conference-style main-text/appendix split. First classify the document.

### Appendix-oriented mode

Use this mode only when at least one trigger is present:

- the user explicitly decides to create or expand an appendix;
- a venue, page limit, or submission plan requires a main-text/appendix split;
- the existing manuscript already assigns full proofs to an appendix;
- the current task explicitly reorganizes the paper around that split.

Then keep the main text focused on the contribution, mechanism, theorem statement, headline rate, and enough proof intuition to make the result usable. Put long verification, auxiliary concentration arguments, exact constants, and full calculations in the appendix. Moving a proof never authorizes compressing it. Give a long appendix a roadmap and align its sections with the main results.

### Inline-proof mode

Use this mode for a research note, technical note, early working draft, lecture note, or any document whose proof placement has not been decided. Keep a proof near its theorem when that helps the reader follow the developing argument. Do not create an appendix solely because the proof is long.

### Unclear mode

Preserve the existing placement. Flag the architectural choice only if it materially affects the requested revision.

## Scope and mathematical honesty

- Do not silently strengthen a claim while making it sound cleaner.
- Do not call a conditional-mean estimator an MLE unless the model supplies a likelihood interpretation.
- Do not describe separate lower-bound families as an additive direct sum when they yield only a maximum.
- Do not imply that upper and lower bounds form a common-class minimax sandwich unless they use the same class and quantifiers.
- Replace vague strength claims such as “very general” with the actual condition or comparison.
