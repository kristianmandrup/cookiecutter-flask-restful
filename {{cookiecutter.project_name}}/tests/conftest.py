import json
import pytest
from dotenv import load_dotenv

from {{cookiecutter.app_name}}.models import User
from {{cookiecutter.app_name}}.app import create_app
from {{cookiecutter.app_name}}.extensions import db as _db
from pytest_factoryboy import register
from tests.factories import UserFactory


register(UserFactory)


@pytest.fixture(scope="session")
def app():
    load_dotenv(".testenv")
    app = create_app(testing=True)
    return app


