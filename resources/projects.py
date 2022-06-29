from pagerank import get_document_scores
from serializers.projects import ProjectSchema, ProjectSearchSchema
from flask_apispec import marshal_with, use_kwargs
from utils import Resource, update_object_from_dict
import models
from models import db


class Projects(Resource):
    @marshal_with(ProjectSchema(many=True))
    def get(self):
        return models.Project.query.all()
    
    @use_kwargs(ProjectSchema())
    @marshal_with(ProjectSchema())
    def post(self, **kwargs):
        project = models.Project()
        update_object_from_dict(project, kwargs)
        db.session.add(project)
        db.session.commit()
        return project


class ProjectSearch(Resource):
    @marshal_with(ProjectSchema(many=True), apply=True)
    @use_kwargs(ProjectSearchSchema, location="query")
    def get(self, topic):
        projects = ProjectSchema(many=True).dump(models.Project.query.all())
        _, with_scores = get_document_scores(topic, projects)
        sorted_projects = sorted(with_scores, key=lambda p: p["score"], reverse=True )
        return sorted_projects