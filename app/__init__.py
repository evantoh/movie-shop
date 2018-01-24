# from flask import Flask
# from flask_bootstrap import Bootstrap
# # from app import views
# from .config import DevConfig

# # Initializing application
# app = Flask(__name__, instance_relative_config = True)

# # Setting up configuration
# app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')

# bootstrap = Bootstrap(app)



# from app import views
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    #Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Will add the views and forms

    return app