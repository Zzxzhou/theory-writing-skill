#!/usr/bin/env python3
"""Structural checks for theory-writing-skill research snapshots; not a proof checker."""
import argparse
import json
from pathlib import Path

WORKFLOW = {"framing", "falsification", "derivation", "audit", "literature", "writing", "blocked", "complete"}
EPISTEMIC = {"conjectured", "stress_tested", "proof_in_progress", "conditional", "proof_drafted", "audited", "refuted", "superseded"}
CLOSED = {"proved_here": "derivation", "verified_source": "source_proof"}
TYPES = {"stress_test", "derivation", "source_proof", "counterexample", "review", "literature_comparison"}

def validate(state, previous=None):
    errors = []
    def error(s): errors.append(s)
    if state.get("schema_version") != 1: error("schema_version must equal 1")
    for key in ("project", "claims", "assumptions", "obligations", "evidence", "events"):
        if key not in state: error("missing " + key)
    if errors: return errors
    def index(key):
        vals = state[key]
        ids = [x.get("id") for x in vals]
        if len(ids) != len(set(ids)): error("duplicate ids in " + key)
        return {x["id"]: x for x in vals}
    claims, assumptions, obligations, evidence = map(index, ("claims", "assumptions", "obligations", "evidence"))
    if state.get("active_claim_id") not in claims: error("active claim absent")
    for o in obligations.values():
        if o.get("claim_id") not in claims: error(o["id"] + ": unknown claim")
        for dep in o.get("dependency_ids", []):
            if dep not in obligations: error(o["id"] + ": unknown dependency " + dep)
    def evidenced(cid, rev, eid, kind):
        e = evidence.get(eid)
        return e is not None and e.get("type") == kind and e.get("claim_id") == cid and e.get("claim_revision") == rev and bool(e.get("locator")) and bool(e.get("finding"))
    for c in claims.values():
        cid, rev = c["id"], c.get("revision")
        ep, wf = c.get("epistemic_state"), c.get("workflow_state")
        if not isinstance(rev, int) or rev < 1: error(cid + ": invalid revision")
        if ep not in EPISTEMIC or wf not in WORKFLOW: error(cid + ": unknown state")
        for a in c.get("assumption_ids", []):
            if a not in assumptions: error(cid + ": unknown assumption " + a)
        obs = [obligations[x] for x in c.get("obligation_ids", []) if x in obligations]
        if len(obs) != len(c.get("obligation_ids", [])): error(cid + ": missing obligation")
        for o in obs:
            if o.get("claim_id") != cid: error(cid + ": foreign obligation " + o["id"])
            st = o.get("status")
            if st in CLOSED:
                if not any(evidenced(cid, rev, x, CLOSED[st]) for x in o.get("evidence_ids", [])):
                    error(o["id"] + ": missing current evidence")
            elif st == "assumed_explicitly":
                if o.get("assumption_id") not in c.get("assumption_ids", []):
                    error(o["id"] + ": assumption not stated in claim")
            elif st not in {"open", "refuted"}: error(o["id"] + ": unknown status")
        closed = all(o.get("status") in set(CLOSED) | {"assumed_explicitly"} for o in obs)
        if ep == "stress_tested" and not any(evidenced(cid, rev, x, "stress_test") for x in c.get("stress_test_evidence_ids", [])):
            error(cid + ": stress test not documented")
        if ep == "proof_in_progress" and not any(e.get("claim_id") == cid and e.get("claim_revision") == rev and e.get("type") == "derivation" for e in evidence.values()):
            error(cid + ": no derivation evidence")
        if ep == "conditional" and not any(o.get("status") == "open" for o in obs):
            error(cid + ": conditional needs open obligation")
        if ep in {"proof_drafted", "audited"} and not closed:
            error(cid + ": proof obligations not closed")
        if ep == "refuted" and not any(evidenced(cid, rev, x, "counterexample") and evidence[x].get("assumptions_checked") is True for x in c.get("refutation_evidence_ids", [])):
            error(cid + ": refutation needs checked counterexample")
        if ep == "superseded" and c.get("supersedes") not in claims:
            error(cid + ": missing replacement link")
        audit = c.get("audit") or {}
        if ep == "audited" or wf == "complete":
            if not (audit.get("claim_revision") == rev and audit.get("verdict") == "pass" and audit.get("independent") is True and audit.get("reviewer_provenance") in {"human", "separate_context_agent"} and evidenced(cid, rev, audit.get("evidence_id"), "review")):
                error(cid + ": current independent passing review required")
            if not closed: error(cid + ": cannot complete open proof")
        if wf == "complete" and ep != "audited": error(cid + ": complete requires audited")
        if wf == "complete" and c.get("role") == "main_result":
            n = c.get("novelty", {})
            if n.get("status") != "verified" or not any(evidenced(cid, rev, x, "literature_comparison") for x in n.get("evidence_ids", [])):
                error(cid + ": verified anchor comparison required")
        if not c.get("next_action") or not c["next_action"].get("success_criterion") or not c["next_action"].get("target_id"):
            error(cid + ": actionable next step required")
    if previous:
        old = {x["id"]: x for x in previous.get("claims", [])}
        transitions = {(e.get("claim_id"), e.get("to_revision"), e.get("to_state")) for e in state["events"]}
        for cid, c in claims.items():
            if cid not in old: continue
            prior = old[cid]
            changed_scope = any(c.get(k) != prior.get(k) for k in ("statement", "assumption_ids", "obligation_ids"))
            if changed_scope and c["revision"] <= prior["revision"]:
                error(cid + ": changed scope without revision increment")
            if changed_scope and c.get("audit") and c["audit"].get("claim_revision") != c["revision"]:
                error(cid + ": stale audit")
            if c["revision"] < prior["revision"]: error(cid + ": revision regressed")
            if (c["revision"] != prior["revision"] or c["epistemic_state"] != prior["epistemic_state"]) and (cid, c["revision"], c["epistemic_state"]) not in transitions:
                error(cid + ": missing transition event")
    return errors

def main():
    p = argparse.ArgumentParser()
    p.add_argument("state", type=Path)
    p.add_argument("--previous", type=Path)
    args = p.parse_args()
    state = json.loads(args.state.read_text())
    previous = json.loads(args.previous.read_text()) if args.previous else None
    errors = validate(state, previous)
    for item in errors: print("ERROR:", item)
    if errors: raise SystemExit(1)
    print("State structure valid (not a mathematical proof).")

if __name__ == "__main__":
    main()
