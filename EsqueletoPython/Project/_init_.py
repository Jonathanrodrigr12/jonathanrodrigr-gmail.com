from flask import Blueprint
from flask_restful import Api, Resource, reqparse

from .Api.Controller.WorldController import WorldController as world

blueprint = Blueprint('HelloWorld', __name__)
api = Api(blueprint)

api.add_resource(world, '/World')