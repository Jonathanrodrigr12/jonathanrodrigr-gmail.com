import json
from flask import Flask, jsonify
from flask_restful import Resource, Api
from ..Services.WorldService import WorldService
from ..Services.GenericObject import Generic_Object
# api = WorldDto.api

class World_Controller(Resource):
    def get(self):
        service = WorldService()
        return service.GetWorld()

class Generic_Object_Topology(Resource):
      def get(self):
          genericObject = Generic_Object().generic_Object_Response()
          response = jsonify(genericObject)
          return response
