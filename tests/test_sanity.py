from pathlib import Path

def test_ci_yml_exists():
    assert Path(".github/workflows/ci.yml").exists()