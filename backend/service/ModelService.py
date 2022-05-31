from entity.ModelEntity import ModelEntity, SaveModelRequest
from dao.ModelDao import ModelDao
from utils.avatarToHair import avatarToHair

class ModelService:
    def __init__(self):
        self.modelDao = ModelDao()
    
    def registerModel(self, user_id: int, gender: bool, avatar_id: int):
        res = {}
        id = self.modelDao.registerModel(user_id, gender, avatar_id)
        hair = avatarToHair[id]
        
        res["id"] = id
        res["hair_id"] = hair if hair else 1
        
        return res
    
    def getModel(self, user_id: int, model_id: int):
        return self.modelDao.getModel(user_id, model_id)
    

    def updateModel(self, user_id: int, model_id: int, req: SaveModelRequest):
        m = req.toEntity()
        m.id = model_id
        
        self.modelDao.updateModel(user_id, m)
        return
        
    def hideModel(self, user_id: int, model_id: int):
        self.modelDao.hideModel(user_id, model_id)
        return
    
    def getModels(self, user_id: int):
        return self.modelDao.getModels(user_id)
        
        
