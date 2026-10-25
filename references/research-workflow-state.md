# Persistent Research Workflow State

Use this layer for multi-session mathematical research, theorem discovery, nontrivial proof development, or a requested persistent research audit. It is **not** a prerequisite for language-only revision.

## Placement and ownership

The reusable `theory-writing-skill` contains the protocol and a blank template. Each real research project stores its **own** `research-state.json` beside the manuscript, plus the proofs, source PDFs, and notes referenced by the state. Do not put project-specific claims or confidential content into this reusable skill. Start by copying `assets/research-state.template.json` into that project's repository. Read local `AGENTS.md`, manuscript context, the state snapshot, and relevant Git diff at the start of each session.

The state file is a structured **index of evidence**, not the proof itself. A path and a high confidence statement are insufficient if the underlying proof is absent. If source files disagree with a saved status, report the discrepancy and correct the state instead of silently proceeding.

## Orthogonal state axes

`workflow_state` tells us *what activity is taking place*: `framing`, `falsification`, `derivation`, `audit`, `literature`, `writing`, `blocked`, or `complete`.

`epistemic_state` tells us *what is justified*: `conjectured`, `stress_tested`, `proof_in_progress`, `conditional`, `proof_drafted`, `audited`, `refuted`, or `superseded`.

A proof-shaped document is not a proof. A passed syntactic validator is not a mathematical guarantee. A successful self-review is not an independent audit. A novelty check is distinct from mathematical verification.

## Main objects

- `project`: research question, primitive model, target, and asymptotic regime.
- `claims`: persistent IDs (`T1`, `L1`), **revision numbers**, verbatim statements, claim role, both states, assumption and proof-obligation IDs, audit, novelty, and an actionable next step.
- `assumptions`: one condition per ID, typed by role; necessity is separately classified.
- `obligations`: load-bearing mathematical claims, dependency IDs, status (`open`, `proved_here`, `verified_source`, `assumed_explicitly`, `refuted`), evidence IDs, and any formal assumption ID.
- `evidence`: stable IDs and exact source locators, with a type (`stress_test`, `derivation`, `source_proof`, `counterexample`, `review`, `literature_comparison`), associated claim revision, and concise factual finding.
- `events`: append-only journal of each epistemic transition and revision change, with rationale and evidence IDs.

Evidence for old revisions stays in the history, but does **not** certify a modified theorem. An obligation marked `assumed_explicitly` must refer to an **actual assumption stated in the theorem**, not an unspoken missing lemma. If an anchor paper's proof has not been read and its hypotheses checked, the obligation cannot be `verified_source`.

## Transition gates

The common path is `conjectured -> stress_tested -> proof_in_progress -> proof_drafted -> audited`, but it is **not** a compulsory linear checklist: research may go directly to derivation, return to conditional after finding a gap, or be refuted at any time.

- `stress_tested`: a located `stress_test` evidence item records the test and its outcome; negative tests do not prove the theorem.
- `proof_in_progress`: some actual derivation evidence exists, but the proof is not yet closed.
- `conditional`: one or more named `open` obligations blocks the intended result.
- `proof_drafted`: all listed obligations are `proved_here`, `verified_source`, or formally `assumed_explicitly`; no open or refuted obligation. Each discharged obligation has appropriate evidence for the current claim revision.
- `audited`: the proof-drafted requirements hold **and** a passing, located `review` matches this claim revision. The review must record a real separate-context agent or human reviewer, not just a self-assigned persona.
- `refuted`: a checked `counterexample` is linked and explicitly satisfies the claim's stated assumptions.
- `superseded`: a replacement claim is identified in the state.
- `workflow_state=complete`: requires `audited`; for a main result, also requires a source-checked `literature_comparison`. Supporting lemmas may be complete without novelty checking.

Changing statement, assumption set, or obligation set **increments revision**, resets stale audit, and requires a revision event. Never change status silently: append a transition event. Refuted claims remain recorded rather than being erased.

The provided validator checks these bookkeeping invariants and (with `--previous`) some cross-snapshot transition rules. It cannot read or establish the actual proof, establish original research novelty, or guarantee independent reasoning.

## Session protocol

1. **Orient**: open the actual primitive model, stated theorem, assumptions, existing proofs, anchor papers, current snapshot, and changed files. Mark conflicting or missing information explicitly.
2. **Select**: choose a single active claim and a `next_action` with a target ID and a falsifiable success criterion.
3. **Stress-test**: when informative, attempt simple observational-equivalence, weak-signal, boundary, or finite-dimensional counterexamples before expensive proof search.
4. **Derive**: start from an exact primitive identity at the required resolution. Create obligations and track local lemma dependencies. Never conceal an unidentified remainder.
5. **Referee**: run a targeted mathematical audit, preferably with an independently generated argument or a separate-context reviewer. Record reviewer provenance.
6. **Compare**: inspect the precise anchor results if claiming novelty or assumptions weaker than prior work.
7. **Persist**: reconcile the snapshot with source artifacts, append evidence and events, run the validator, and commit changes together if possible.
8. **Hand off**: report the strongest justified statement, blocking obligations, whether an assumption was added, and one testable next step.

If blocked, do not loop on the same failed derivation or silently add assumptions. Record the obstruction and choose a competing route, a counterexample, or a precisely conditional theorem.

## Running validation

From the installed skill root:

```bash
python scripts/validate_research_state.py /path/to/project/research-state.json
python scripts/validate_research_state.py /path/to/project/research-state.json --previous /path/to/old-research-state.json
```

No third-party Python packages are required. Passing this validator means the documented process is consistent; it does **not** mean the theorem is proved.
