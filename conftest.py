from gamersgrotto.__init__ import app
import pytest

@pytest.fixture
def api():
    client = app.test_client()
    return client
