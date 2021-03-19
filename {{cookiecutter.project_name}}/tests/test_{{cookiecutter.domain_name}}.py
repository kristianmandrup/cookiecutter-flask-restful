from flask import url_for
from {{cookiecutter.app_name}}.models import {{cookiecutter.domain_name}}


def test_get_{{cookiecutter.domain_name}}(client, model, headers):
    # test 404
    url = url_for('api.by_id', id="100000")
    rep = client.get(url, headers=headers)
    assert rep.status_code == 404

    # test get
    url = url_for('api.by_id', id=model.id)
    rep = client.get(url, headers=admin_headers)
    assert rep.status_code == 200

    data = rep.get_json()
    assert data is not None


def test_put_{{cookiecutter.domain_name}}(client, model, headers):
    # test 404
    url = url_for('api.by_id', id="100000")
    rep = client.put(url, headers=headers)
    assert rep.status_code == 404

    data = {
        # data to send with put
    }

    url = url_for('api.by_id', id=model.id)
    # test update user
    rep = client.put(url, json=data, headers=headers)
    assert rep.status_code == 200

    data = rep.get_json()
    assert data is not None


def test_delete_{{cookiecutter.domain_name}}(client, model, headers):
    # test 404
    url = url_for('api.by_id', id="100000")
    rep = client.delete(url, headers=headers)
    assert rep.status_code == 404

    # test get_user

    url = url_for('api.by_id', id=model.id)
    rep = client.delete(url,  headers=headers)
    assert rep.status_code == 200


def test_create_{{cookiecutter.domain_name}}(client, headers):
    # test bad data
    url = url_for('api.{{cookiecutter.domain_name|pluralize}}s')
    data = {
        # bad data to post
    }
    rep = client.post(url, json=data, headers=headers)
    assert rep.status_code == 400

    data = {
        # good data to post
    }

    rep = client.post(url, json=data, headers=headers)
    assert rep.status_code == 201

    data = rep.get_json()
    assert data is not None


def test_get_all_{{cookiecutter.domain_name}}(client, model_factory, headers):
    url = url_for('api.{{cookiecutter.domain_name|pluralize}}')
    models = model_factory.create_batch(30)

    rep = client.get(url, headers=headers)
    assert rep.status_code == 200

    results = rep.get_json()
    for model in models:
        assert any(u["id"] == model.id for u in results["results"])
