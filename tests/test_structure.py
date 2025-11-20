import os

def test_readme_exists():
    """
    Test that the README.md file exists in the root directory.
    This simulates a project requirement that documentation must be present.
    """
    assert os.path.exists("README.md"), "README.md is missing! Documentation is required."
