import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("diffusion_example", ROOT / "examples/steady_diffusion/run.py")
demo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(demo)


class DiffusionTests(unittest.TestCase):
    def test_uniform_limit_and_diffusion_bounds(self):
        run = demo.solve(16, 0)
        self.assertAlmostEqual(run["flux_m_per_s"], 1e-9, delta=1e-20)
        self.assertLess(run["max_concentration_error"], 1e-12)
        self.assertTrue(run["bounds_ok"])

    def test_analytic_error_converges_and_scales_with_units(self):
        coarse, fine = demo.solve(8, -1), demo.solve(16, -1)
        self.assertAlmostEqual(coarse["relative_flux_error"] / fine["relative_flux_error"], 4, delta=0.01)
        scaled = demo.solve(16, -1, d0=2e-9, length=2)
        self.assertAlmostEqual(scaled["flux_m_per_s"], fine["flux_m_per_s"], delta=1e-20)
        self.assertLess(fine["relative_flux_spread"], 1e-10)

    def test_real_governed_run_writes_note_and_bound_evidence(self):
        with tempfile.TemporaryDirectory() as td:
            result = demo.run(Path(td))
            self.assertTrue(result["protocol_ok"])
            self.assertGreater(result["summary"]["effect_fraction"], 0.4)
            self.assertTrue((Path(td) / "manuscript.md").is_file())
            self.assertTrue((Path(td) / "profile.svg").is_file())
            state = demo.rf.context(td)
            self.assertEqual(state["claims"]["flux-ranking"]["status"], "supported")
            self.assertNotIn("physical_validation", state["claims"]["flux-ranking"]["support"])


if __name__ == "__main__":
    unittest.main()
