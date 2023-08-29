from marshmallow import Schema, fields, validate


class PromptCreateSchema(Schema):
    prompt_text = fields.Str(required=True, validate=validate.Length(min=3, max=100))


class PromptUpdateSchema(Schema):
    new_prompt = fields.Str(required=True, validate=validate.Length(min=3, max=100))
