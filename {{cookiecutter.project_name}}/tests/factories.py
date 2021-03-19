import factory
from {{cookiecutter.app_name}}.models import User


class {{cookiecutter.domain_name}}Factory(factory.Factory):

    name = factory.Sequence(lambda n: "user%d" % n)

    class Meta:
        model = {{cookiecutter.domain_name}}
