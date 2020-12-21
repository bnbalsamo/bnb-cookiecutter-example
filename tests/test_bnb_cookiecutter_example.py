"""Tests for bnb-cookiecutter-example."""
import pytest

import bnb_cookiecutter_example


def test_version_available():
    """Test the version dunder is available on the module."""
    x = getattr(bnb_cookiecutter_example, "__version__", None)
    assert x is not None


if __name__ == "__main__":
    pytest.main()
