import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True


    
    @staticmethod
    def init_app(app):
        pass



class Development(Config):
    DEBUG = True
    print('running in dev ')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
    



class Testing(Config):
    pass


class Production(Config):
    pass

config ={
        'development':Development,
        'testing':Testing,
        'production':Production,
        'default':Development
        }


