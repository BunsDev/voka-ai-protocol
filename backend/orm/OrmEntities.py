from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# User database data format
class UserTable(db.Model):
    __tablename__ = 'user_info'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    passwd = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True, nullable=True)
    cover_model = db.Column(db.Integer)
    models = db.relationship('ModelTable',backref = db.backref('user'),lazy='dynamic')
    # models = db.relationship('ModelTable',secondary = hub,backref = db.backref('user'), lazy='dynamic')

    
    def __init__(self, username: str, passwd: str, email: str):
        self.username = username
        self.passwd = passwd
        self.email = email

    # return string when print it
    def __repr__(self):
        return '<User %r>' % self.username

# TODO: Other three tables in mysql: need to relate to user
# model database data format
class ModelTable(db.Model):
    __tablename__ = 'model'
    id = db.Column(db.Integer, primary_key=True,autoincrement = True)
    gender = db.Column(db.Boolean)
    avatar_id = db.Column(db.Integer)
    
    eye_id = db.Column(db.Integer)
    shoes_id = db.Column(db.Integer)
    hair_id = db.Column(db.Integer)
    hat_id = db.Column(db.Integer)
    coat_id = db.Column(db.Integer)
    pants_id = db.Column(db.Integer)
    glasses_id = db.Column(db.Integer)
    # hide or not
    hide = db.Column(db.Boolean)
    # set owner
    user_id = db.Column(db.Integer,db.ForeignKey('user_info.id'))

    def toJson(self): 
        res = {}
        keys = ['id', 'gender', 'avatar_id', 'eye_id', 'shoes_id', 'hair_id', 'hat_id', 'coat_id', 'pants_id', 'glasses_id']
        for key in keys:
            res[key] = self.__dict__[key]
            
        return res
# subscribe database data format: don't need to relate to user
class SubscribeTable(db.Model):
    __tablename__ = 'subscribe'
    id = db.Column(db.Integer, primary_key=True,autoincrement = True)
    email = db.Column(db.String(100), unique=True)
    valid = db.Column(db.Boolean)

# hub database data format: need to relate to user and model
# hub = db.Table('hub',
#     db.Column('user_info.id', db.Integer,db.ForeignKey('user_info.id'))
#     db.Column('model.id', db.Integer,db.ForeignKey('model.id'))
# )
