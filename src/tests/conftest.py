import pytest
from unittest.mock import MagicMock
from server import build_app


@pytest.fixture()
def session():
    session = MagicMock()
    return session


@pytest.fixture()
def app(session):
    flask_app = build_app(session)
    flask_app.config.update({
        "TESTING": True,
    })
    yield flask_app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()