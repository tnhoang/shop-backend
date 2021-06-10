import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def zed():
    return "zed"


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c
