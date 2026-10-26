
import os
from pathlib import Path

from flask import Flask
from app.models import db


def create_app(test_config=None):
    project_root = Path(__file__).resolve().parent.parent
    instance_path = Path(
        os.environ.get("INSTANCE_PATH", str(project_root / "instance"))
    )
    instance_path.mkdir(parents=True, exist_ok=True)

    app = Flask(
        __name__,
        template_folder=str(project_root / "templates"),
        static_folder=str(project_root / "static"),
        instance_path=str(instance_path),
    )

    app.config["SECRET_KEY"] = os.environ.get(
        "SECRET_KEY",
        "dev-only-change-this-key",
    )
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"sqlite:///{instance_path / 'shopsphere.db'}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if test_config:
        app.config.update(test_config)

    db.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    return app
