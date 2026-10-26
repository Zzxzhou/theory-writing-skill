import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_research_state import validate


class ResearchStateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = json.loads((ROOT / "assets/research-state.template.json").read_text())

    def test_template_is_valid(self):
        self.assertEqual(validate(self.base), [])

    def test_unearned_audit_is_rejected(self):
        state = copy.deepcopy(self.base)
        state["claims"][0]["epistemic_state"] = "audited"
        self.assertTrue(validate(state))

    def test_proof_without_evidence_is_rejected(self):
        state = copy.deepcopy(self.base)
        state["obligations"][0]["status"] = "proved_here"
        state["claims"][0]["epistemic_state"] = "proof_drafted"
        self.assertTrue(validate(state))

    def test_scope_changes_require_revision(self):
        new = copy.deepcopy(self.base)
        new["claims"][0]["statement"] = "A different assertion."
        self.assertTrue(any("revision" in x for x in validate(new, self.base)))

    def test_stress_test_requires_evidence(self):
        new = copy.deepcopy(self.base)
        new["claims"][0]["epistemic_state"] = "stress_tested"
        self.assertTrue(validate(new))

    def test_checked_counterexample(self):
        state = copy.deepcopy(self.base)
        state["evidence"].append({"id": "E1", "type": "counterexample", "claim_id": "T1", "claim_revision": 1,
                                  "locator": "notes/counterexample.md", "finding": "Same observables, distinct targets.",
                                  "assumptions_checked": True})
        state["claims"][0]["refutation_evidence_ids"] = ["E1"]
        state["claims"][0]["epistemic_state"] = "refuted"
        self.assertEqual(validate(state), [])


    def test_missing_scope_rejected(self):
        state = copy.deepcopy(self.base)
        del state["claims"][0]["scope_level"]
        self.assertTrue(any("scope_level" in x for x in validate(state)))

    def test_model_completion_requires_instantiation(self):
        state = copy.deepcopy(self.base)
        state["claims"][0]["workflow_state"] = "complete"
        self.assertTrue(any("model instantiation" in x for x in validate(state)))

    def test_model_verification_requires_evidence(self):
        state = copy.deepcopy(self.base)
        state["claims"][0]["primitive_model_verification"]["status"] = "verified"
        self.assertTrue(any("model verification requires" in x for x in validate(state)))

    def test_changed_scope_requires_revision(self):
        state = copy.deepcopy(self.base)
        state["claims"][0]["scope_level"] = "high_level"
        self.assertTrue(any("revision" in x for x in validate(state, self.base)))

    def test_event_history_is_append_only(self):
        previous = copy.deepcopy(self.base)
        previous["events"] = [{"claim_id": "T1", "to_revision": 1, "to_state": "conjectured"}]
        self.assertTrue(any("append-only" in x for x in validate(self.base, previous)))


if __name__ == "__main__":
    unittest.main()
