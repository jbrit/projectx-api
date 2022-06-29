from flask import Blueprint
from flask_apispec import FlaskApiSpec
from flask_restful import Api

from resources.projects import ProjectSearch, Projects

api_blueprint = Blueprint("api", __name__)
api = Api(api_blueprint)
docs = FlaskApiSpec()

def add_route(resource, url):
    api.add_resource(resource, url)
    docs.register(resource, blueprint="api")

# API routes -- start
add_route(Projects, "/projects/")
add_route(ProjectSearch, "/projects/search/")
# API routes -- end