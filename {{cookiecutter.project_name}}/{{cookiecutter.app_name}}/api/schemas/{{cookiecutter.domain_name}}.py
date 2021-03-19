from {{cookiecutter.app_name}}.models import {{cookiecutter.domain_name|title}}
from {{cookiecutter.app_name}}.extensions import ma, db


class {{cookiecutter.domain_name|title}}Schema():

    id = ma.Int(dump_only=True)

    class Meta:
        model = {{cookiecutter.domain_name|title}}
        load_instance = True
