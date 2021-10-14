import os

from flask import Flask

from cryptocrunch import db
from cryptocrunch.config import Config
from cryptocrunch.scheduler import scheduler


def create_app(test_config=None):
    app = Flask("cryptocrunch", instance_relative_config=True)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, "cryptocrunch.db"),
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.update(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def hello():
        return "Hello, World!"

    # register the database commands
    from cryptocrunch import db
    db.init_app(app)
    scheduler.init_app(app)

    app.app_context().push()
    with app.app_context():
        from cryptocrunch import tasks
        scheduler.start()
        # from cryptocrunch import events
        from cryptocrunch.pricingstore import PricingStore

    return app
