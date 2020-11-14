from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_graphql import GraphQLView
from config import config
db = SQLAlchemy()
def create_app(config_name):
    app = Flask(__name__)
    CORS(app,resources={r"/graphql-api": {"origins": "http://localhost:3000"}})
    app.debug = True
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    print(config[config_name])

    from .schema import schema
    app.add_url_rule(
    '/graphql-api',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
      graphiql=True
    )
)
    db.init_app(app)
    return app



