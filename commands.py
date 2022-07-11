import click
import json
import pandas as pd
from flask import Blueprint
from models import Project, db
command_blueprint = Blueprint("commands", __name__)


@command_blueprint.cli.command("populatedb")
def populate_db():
    click.echo(
        f"Loading projectx.xlsx file"
    )
    data = json.loads(pd.read_excel('projectx.xlsx').fillna('').to_json(orient="records"))
    for dp in data:
        project = Project(topic=dp["topic"], year=dp["year"], student=dp["student"], supervisor=dp["supervisor"], matric_no=dp["matric_no"], submitted=dp["submitted"])
        db.session.add(project)
        db.session.commit()