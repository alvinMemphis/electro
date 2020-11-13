import os
basedir = os.path.abspath(os.path.dirname(__file__))
postgres_local_base = 'postgresql://postgres:123456@localhost/'
database_name = 'electro'
file_path = os.path.abspath(os.getcwd())+"/database.db"
DATABASE_NAME = os.environ.get('DATABASE_NAME') or database_name
DATABASE_USER =  os.environ.get('DATABASE_USER') or "rentpay"
DATABASE_PORT =  os.environ.get('DATABASE_PORT')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD') or "boystomen"
DATABASE_HOST  = os.environ.get('DATABASE_HOST') or "electro.carfdu5ojz3r.us-east-2.rds.amazonaws.com"
DATABASE_ENIGINE =  os.environ.get('DATABASE_ENIGINE')
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
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username=DATABASE_USER,
    password=DATABASE_PASSWORD,
    hostname=DATABASE_HOST,
    databasename=DATABASE_NAME,
)

config ={
        'development':Development,
        'testing':Testing,
        'production':Production,
        'default':Development
        }


