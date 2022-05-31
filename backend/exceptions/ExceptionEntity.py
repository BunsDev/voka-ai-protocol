from typing import Dict, List
import json

# The exception entity defination
class ExceptionEntity:
    def __init__(self, code: int, msg: str):
        self.code = code
        self.msg = msg

    def to_json(self):
        return json.dumps({
            "code": self.code,
            "msg": self.msg
        })
        
class LackParamsException(Exception):
    # init exception
    def __init__(self, value):
        self.value = value
    
    # explain message for exceptions
    def __str__(self):
        return "Lack Params Exception: {}".format(repr(self.value))
    
class NotFoundException(Exception):
    # init exception
    def __init__(self, value):
        self.value = value
    
    # explain message for exceptions
    def __str__(self):
        return "Not Found Exception: {}".format(repr(self.value))