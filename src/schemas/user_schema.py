from marshmallow import Schema, fields,validate
from src.config.app_config import AppConfig
from src.schemas.config_schema import MySchema

class LoginSchema(MySchema):
    username = fields.Str(required=True,validate=validate.Regexp(AppConfig.REGEX_NAME))
    password = fields.Str(required=True)

class LoginSuccessSchema(MySchema):
    access_token = fields.Str(dump_only=True)
    # refresh_token = fields.Str(dump_only=True)
    message = fields.Str(dump_only=True)

class UserCreateSchema(MySchema):
    username = fields.Str(required=True)
    role = fields.Str(required=True)

class UserDetailsSchema(MySchema):
    user_id = fields.Str(dump_only=True)
    username = fields.Str(dump_only=True)
    role = fields.Str(dump_only=True)

class UserPassword(MySchema):
    old_password = fields.Str(required=True)
    new_password = fields.Str(required=True)
    confirm_password = fields.Str(required=True)
    