from flask import Blueprint
from flask_restful import Api, Resource, reqparse

from .Api.Controller.WorldController import WorldController as world

blueprint = Blueprint('Alarms', __name__)
api = Api(blueprint)

api.add_resource(world, '/hello')