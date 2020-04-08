from flask import Blueprint
from flask_restful import Api, Resource, reqparse

from .Api.Controller.WorldController import World_Controller as world
from .Api.Controller.WorldController import Generic_Object_Topology as generic

blueprint = Blueprint('Alarms', __name__)
api = Api(blueprint)

api.add_resource(world, '/hello')
api.add_resource(generic, '/GenericObjectTopology')