from typing import Dict, List
from exceptions.LackParamsException import LackParamsException

class ModelEntity:
    def __init__(self, gender: bool = None, avatar_id: int = None , eye_id: int = None , hide: bool = False,
                shoes_id: int = None, hair_id: int = None, hat_id: int = None, user_id: int = None,
                coat_id: int = None, pants_id: int = None, glasses_id: int = None, id: int = None):
        self.id = id
        
        self.gender = gender
        self.avatar_id = avatar_id
        
        self.eye_id = eye_id
        self.shoes_id = shoes_id
        self.hair_id = hair_id
        self.hat_id = hat_id
        self.coat_id = coat_id
        self.pants_id = pants_id
        self.glasses_id = glasses_id
        
        self.hide = hide
        self.user_id = user_id

class AvatarRequest:
    def __init__(self, data: Dict):
        keys: List = ['gender', 'avatar_id']
        
        # params check
        for key in keys:
            val = data.get(key)
            if val:
                self.__dict__[key] = val
            else:
                raise LackParamsException("lack of params {}".format(key))

class SaveModelRequest:
    def __init__(self, data: Dict):
        keys: List = ['eye_id', 'shoes_id', 'hair_id', 'hat_id', 'coat_id', 'pants_id', 'glasses_id']
        
        # params check
        for key in keys:
            val = data.get(key)
            if val:
                self.__dict__[key] = val
            else:
                raise LackParamsException("lack of params {}".format(key))
    
    def toEntity(self):
        m = ModelEntity()
        
        m.eye_id = self.eye_id
        m.shoes_id = self.shoes_id
        m.hair_id = self.hair_id
        m.hat_id = self.hat_id
        m.coat_id = self.coat_id
        m.pants_id = self.pants_id
        m.glasses_id = self.glasses_id
        
        return m