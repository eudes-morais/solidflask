import sys
import importlib # For >= Python3.4 (extraído de https://stackoverflow.com/questions/961162/reloading-module-giving-nameerror-name-reload-is-not-defined)
from flask import app
from app import create_app
from config import app_config, app_active

config = app_config[app_active]
config.APP = create_app(app_active)

if __name__ == '__main__':
    config.APP.run(host=config.IP_HOST, port=config.PORT_HOST)
    importlib.reload(app) # For >= Python3.4, ao invés de reload(app)