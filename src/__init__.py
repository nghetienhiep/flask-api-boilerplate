# coding=utf-8
import logging

from flask import Flask

__author__ = 'ThucNC'
_logger = logging.getLogger(__name__)


def create_app(config_name):
    import config
    import logging.config
    from src.api import init_api

    print("Starting in `{}` mode...".format(config_name))

    app = Flask(__name__)
    app.config.from_object(config.config_by_name[config_name])

    logging.config.fileConfig(app.config['LOGGING_CONFIG_FILE'], disable_existing_loggers=False)

    init_api(app)
    return app