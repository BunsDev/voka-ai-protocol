from entity.ModelEntity import ModelEntity
from exceptions.ExceptionEntity import NotFoundException
from orm.OrmEntities import db, ModelTable, UserTable
from typing import Dict

class ModelDao:
    def updateGender(self, id: int, gender: bool):
        result = ModelTable.query.filter_by(id=id).first()
        result.gender = gender
        db.session.add(result)
        db.session.commit()
    
    # create model by gender and avatar_id
    def registerModel(self, user_id: int, gender: bool, avatar_id: int) -> id:
        u = UserTable.query.filter_by(id=user_id).first()
        
        if (not u):
            raise NotFoundException("User {0} doesn' t exist".format(user_id))

        model = ModelTable()
        model.gender = gender
        model.avatar_id = avatar_id
        model.user_id = user_id
        model.hide = False
        
        db.session.add(model)
        db.session.commit()
        
        if (not u.cover_model):
            u.cover_model = model.id
            db.session.add(u)
            db.session.commit()
        
        return model.id
    
    # change model attribute
    def getModel(self, user_id: int, model_id: int):
        # find model
        m = ModelTable.query.filter_by(id=model_id, user_id=user_id).first()
        
        if (not m):
            raise NotFoundException("User {0} doesn' t have model {1}".format(user_id, model.id))
        
        return m.toJson()


    # change model attribute
    def updateModel(self, user_id: int, model: ModelEntity):
        # find model
        m = ModelTable.query.filter_by(id=model.id, user_id=user_id).first()
        
        if (not m):
            raise NotFoundException("User {0} doesn' t have model {1}".format(user_id, model.id))

        
        # change model attr
        m.eye_id = model.eye_id
        m.shoes_id = model.shoes_id
        m.hair_id = model.hair_id
        m.hat_id = model.hat_id
        m.coat_id = model.coat_id
        m.pants_id = model.pants_id
        m.glasses_id = model.glasses_id
        
        db.session.add(m)
        db.session.commit()
    
    # hide model
    def getModels(self, user_id: int):
        # find model
        m = ModelTable.query.filter_by(user_id=user_id, hide=False).all()
        
        res = []
        
        for model in m:
            res.append(model.toJson())
        # if (not m):
            # raise NotFoundException("User {0} doesn' t have models".format(user_id))
        
        return res
    
    # hide model
    def hideModel(self, user_id: int, model_id: int):
        # find model
        m = ModelTable.query.filter_by(id=model_id, user_id=user_id).first()

        if (not m):
            raise NotFoundException("User {0} doesn' t have model {}".format(user_id, model.id))
        
        m.hide = True
        
        db.session.add(m)
        db.session.commit()
        
        
        
        


