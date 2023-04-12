import pytest


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "html: mark test to generate HTML report"
    )
