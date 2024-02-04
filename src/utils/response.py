from typing import Optional
from flask import jsonify

class SuccessResponse:
    success = True

    @classmethod
    def success_message(cls,status_code: int, message: str, data: Optional[list]= []):
        return jsonify({
            'success': cls.success,
            'code': status_code,
            'data': data,
            'message': message
         }
        )
    
class ErrorResponse:
    success = False

    @classmethod
    def error_message(cls,error) -> dict:
        return  jsonify(
                    {
                        "success" : cls.success,
                        'code': error.error_code,
                        "error" : error.error_description,
                        "message" : error.error_message
                    }
                )
