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


if __name__ == "__main__":
    unittest.main()
