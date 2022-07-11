from marshmallow import Schema, fields


class ProjectSchema(Schema):
    id = fields.Int(dump_only=True)
    topic = fields.Str(required=True)
    year = fields.Str(required=True)
    matric_no = fields.Str(required=True)
    submitted = fields.Str(required=True)
    student = fields.Str(required=True)
    supervisor = fields.Str(required=True)
    score = fields.Float(dump_only=True)


class ProjectSearchSchema(Schema):
    topic = fields.Str(required=True)