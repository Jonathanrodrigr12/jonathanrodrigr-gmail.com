import json
from flask import Flask, jsonify
from flask_restful import Resource, Api
from ..Services.WorldService import WorldService
# api = WorldDto.api

class World_Controller(Resource):
    def get(self):
        service = WorldService()
        return service.GetWorld()

class Generic_Object_Topology(Resource):
      def get(self):
          return True

class Generic_Object_Readings(Resource):
      def get(self):
          return True
