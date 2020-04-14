from flask import Blueprint
from flask_restful import Api, Resource, reqparse

from .Api.Controller.WorldController import World_Controller as world
from .Api.Controller.WorldController import Generic_Object_Topology as generic_topology
from .Api.Controller.WorldController import Generic_Object_Readings as generic_reading

blueprint = Blueprint('Alarms', __name__)
api = Api(blueprint)

api.add_resource(world, '/hello')
api.add_resource(generic_topology, '/GenericObjectTopology')
api.add_resource(generic_reading, '/GenericObjectReadings')