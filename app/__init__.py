import os
from datetime import timedelta
from pathlib import Path

from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.update(
        SECRET_KEY=os.environ.get("SECRET_KEY", "dev-key-change-this-before-deploying"),
        PERMANENT_SESSION_LIFETIME=timedelta(days=30),
        DATABASE_URL=os.environ.get("DATABASE_URL"),
        SMTP_HOST=os.environ.get("SMTP_HOST"),
        SMTP_PORT=int(os.environ.get("SMTP_PORT", "587")),
        SMTP_USERNAME=os.environ.get("SMTP_USERNAME"),
        SMTP_PASSWORD=os.environ.get("SMTP_PASSWORD"),
        MAIL_FROM=os.environ.get("MAIL_FROM"),
        PUBLIC_BASE_URL=(
            os.environ.get("PUBLIC_BASE_URL")
            or os.environ.get("RENDER_EXTERNAL_URL")
        ),
        DATABASE=os.environ.get(
            "DATABASE_PATH",
            str(Path(app.instance_path) / "grupo306.sqlite"),
        ),
    )

    if os.environ.get("RENDER") and not app.config["DATABASE_URL"]:
        raise RuntimeError(
            "Configura DATABASE_URL con la URL de una base PostgreSQL persistente."
        )

    if not app.config["DATABASE_URL"]:
        Path(app.config["DATABASE"]).parent.mkdir(parents=True, exist_ok=True)

    from app.routes import bp, close_db

    app.register_blueprint(bp)
    app.teardown_appcontext(close_db)

    with app.app_context():
        from app.routes import init_db

        init_db()

    return app
