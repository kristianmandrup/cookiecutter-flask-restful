from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from {{cookiecutter.app_name}}.api.schemas import {{cookiecutter.domain_name|title}}Schema
from {{cookiecutter.app_name}}.models import {{cookiecutter.domain_name}}
from {{cookiecutter.app_name}}.commons.pagination import paginate


class {{cookiecutter.domain_name|title}}Resource(Resource):
    """Single object resource

    ---
    get:
      tags:
        - api
      parameters:
        - in: path
          name: id
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  user: {{cookiecutter.domain_name|title}}Schema
        404:
          description: {{cookiecutter.domain_name}} does not exists
    put:
      tags:
        - api
      parameters:
        - in: path
          name: id
          schema:
            type: integer
      requestBody:
        content:
          application/json:
            schema:
              {{cookiecutter.domain_name|title}}Schema
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: {{cookiecutter.domain_name}} updated
                  user: {{cookiecutter.domain_name|title}}Schema
        404:
          description: {{cookiecutter.domain_name}} does not exists
    delete:
      tags:
        - api
      parameters:
        - in: path
          name: id
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: {{cookiecutter.domain_name}} deleted
        404:
          description: {{cookiecutter.domain_name}} does not exists
    """

    method_decorators = [jwt_required()]

    def get(self, id):
        schema = {{cookiecutter.domain_name|title}}Schema()
        # get model
        # model = User.query.get_or_404(id)
        return {"model": schema.dump(model)}

    def put(self, id):
        schema = {{cookiecutter.domain_name|title}}Schema(partial=True)
        model = {{cookiecutter.domain_name|title}}.query.get_or_404(id)
        model = schema.load(request.json, instance=model)
        # put model
        return {"msg": "{{cookiecutter.domain_name}} updated", "model": schema.dump(model)}

    def delete(self, {{cookiecutter.domain_name}}_id):
        model = {{cookiecutter.domain_name|title}}.query.get_or_404(user_id)
        # delete model 
        return {"msg": "{{cookiecutter.domain_name}} deleted"}


class {{cookiecutter.domain_name|title}}List(Resource):
    """Creation and get_all

    ---
    get:
      tags:
        - api
      responses:
        200:
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginatedResult'
                  - type: object
                    properties:
                      results:
                        type: array
                        items:
                          $ref: '#/components/schemas/{{cookiecutter.domain_name|title}}Schema'
    post:
      tags:
        - api
      requestBody:
        content:
          application/json:
            schema:
              {{cookiecutter.domain_name|title}}Schema
      responses:
        201:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: {{cookiecutter.domain_name}} created
                  user: {{cookiecutter.domain_name|title}}Schema
    """

    method_decorators = [jwt_required()]

    def get(self):
        schema = {{cookiecutter.domain_name|title}}Schema(many=True)
        query = {{cookiecutter.domain_name|title}}.query
        return paginate(query, schema)

    def post(self):
        schema = {{cookiecutter.domain_name|title}}Schema()
        model = schema.load(request.json)
        # post
        return {"msg": "{{cookiecutter.domain_name}} created", "model": schema.dump(model)}, 201
