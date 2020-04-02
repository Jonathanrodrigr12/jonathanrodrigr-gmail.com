from flask import Flask
from flask_restful import Resource, Api
from ..Services.WorldService import WorldService

# api = WorldDto.api

class WorldController(Resource):
    def get(self):
        service = WorldService()
        return service.GetWorld()
