from typing import Dict, List
from exceptions.LackParamsException import LackParamsException

# request data format
class LoginRequest:
    def __init__(self, json: Dict):
        self.valid = True
        keys: List = ['passwd', 'email']
        
        # params check
        for key in keys:
            val = json.get(key)
            if val:
                self.__dict__[key] = val
            else:
                raise LackParamsException("lack of params {}".format(key))
        
class SignUpRequest:
    def __init__(self, json: Dict):
        self.valid = True
        keys: List = ['username', 'passwd', 'email']
        
        # params check
        for key in keys:
            val = json.get(key)
            if val:
                self.__dict__[key] = val
            else:
                raise LackParamsException("lack of params {}".format(key))

class UserEntity:
    def __init__(self, username: str, passwd: str, email: str, id: int = None, cover_model: int = None):
        self.username = username
        self.passwd = passwd
        self.email = email
        self.cover_mode = cover_model
        if (id):
            self.id = id
 
