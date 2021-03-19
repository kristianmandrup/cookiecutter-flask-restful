import json
import pytest
from dotenv import load_dotenv

from {{cookiecutter.app_name}}.models import User
from {{cookiecutter.app_name}}.app import create_app
from pytest_factoryboy import register
from tests.factories import {{cookiecutter.domain_name|title}}Factory


register({{cookiecutter.domain_name|title}}Factory)


@pytest.fixture(scope="session")
def app():
    load_dotenv(".testenv")
    app = create_app(testing=True)
    return app


