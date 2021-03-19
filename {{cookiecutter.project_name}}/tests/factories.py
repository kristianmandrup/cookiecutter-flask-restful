import factory
from {{cookiecutter.app_name}}.models import {{cookiecutter.domain_name|title}}


class {{cookiecutter.domain_name|title}}Factory(factory.Factory):

    name = factory.Sequence(lambda n: "{{cookiecutter.domain_name}}%d" % n)

    class Meta:
        model = {{cookiecutter.domain_name|title}}
