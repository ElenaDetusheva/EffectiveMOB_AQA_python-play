import pytest

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        # "browser": "firefox",
        "viewport":{
            "width": 1920,
            "height": 960,
        }

    }
