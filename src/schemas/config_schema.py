from typing import Any
from marshmallow import Schema, fields
from src.utils.exceptions import ApplicationException

class MySchema(Schema):

    def handle_error(self, error: fields.ValidationError, data: Any, *, many: bool, **kwargs):
        raise ApplicationException(422,"invalid request","huhuhuh")