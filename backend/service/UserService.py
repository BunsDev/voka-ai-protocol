from entity.UserEntity import LoginRequest, SignUpRequest, UserEntity
from dao.UserDao import UserDao

class UserService:
    def __init__(self):
        self.userDao = UserDao()

    def userLogin(self, req: LoginRequest):
        user = UserEntity("", req.passwd, req.email)
        return self.userDao.hasUser(user)

    # SignUp Service Logic and return user id
    def userSignUp(self, req: SignUpRequest) -> int:
        # convert request data entity to user entity
        user = UserEntity(req.username, req.passwd, req.email)
        # TODO: check username and emial has been in mysql
        return self.userDao.saveUser(user)
