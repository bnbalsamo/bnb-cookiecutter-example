"""Tests for bnb-cookiecutter-example."""
import pytest

import bnb_cookiecutter_example


def test_version_available() -> None:
    """Test the version dunder is available on the module."""
    version_attr = getattr(bnb_cookiecutter_example, "__version__", None)
    assert version_attr is not None


if __name__ == "__main__":
    pytest.main()
