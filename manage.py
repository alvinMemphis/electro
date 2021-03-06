import os
from app import db,create_app
from flask_script import Manager
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand


app = create_app(os.getenv('FLASK_CONFIG') or 'default')


manager = Manager(app)
migrate = Migrate(app, db)




manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()

