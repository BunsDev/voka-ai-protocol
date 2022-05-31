from entity.UserEntity import UserEntity
from exceptions.ExceptionEntity import NotFoundException
from orm.OrmEntities import db, UserTable
from typing import Dict

# Interact with databases, see http://www.pythondoc.com/flask-sqlalchemy/queries.html
class UserDao:
    # save user data and return user_id
    def saveUser(self, user: UserEntity) -> int:
        u = UserTable(user.username, user.passwd, user.email)
        db.session.add(u)
        db.session.commit()
        # orm will fill the id after the transcation has been committed
        return u.id

    def hasUser(self, u: UserEntity) -> int:
        result = UserTable.query.filter_by(passwd=u.passwd, email=u.email).first()
        if (not result.id):
            raise NotFoundException("Id Not Found")
        res = {}
        res["id"] = result.id
        res["username"] = result.username
        return res
    
    def getUser(self, username: str) -> UserEntity:
        res = UserTable.query.filter_by(username=username).first()
        if (not res):
            raise NameError("don' t have this username")
        return UserEntity(res.username, res.passwd, res.email, res.id)
    
    # get cover model
    def getCover(self, id: int) -> int:
        u = UserTable.query.filter_by(id=id).first()
        if (not u):
            raise NotFountException()
            
        return u.cover_model
    
    # set cover model
    def setCover(self, id: int, model_id: int):
        u = UserTable.query.filter_by(id=id).first()
        u.cover_model = model_id
        
        if (not u):
            raise NotFountException("user {0} doesn' t have this model {1}".format(id, model_id))

        return
        
