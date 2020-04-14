import json
from flask import Flask, jsonify
from flask_restful import Resource, Api
from ..Services.WorldService import WorldService
from ..Services.GenericObjectService import Generic_Object_Service
# api = WorldDto.api

class World_Controller(Resource):
    def get(self):
        service = WorldService()
        return service.GetWorld()

class Generic_Object_Topology(Resource):
      def get(self):
          genericObject = Generic_Object_Service().generic_Object_Response_Topology()
          response = jsonify(genericObject)
          return response

class Generic_Object_Readings(Resource):
      def get(self):
          genericObject = Generic_Object_Service().generic_Object_Response_Topology()
          response = jsonify(genericObject)
          return response
