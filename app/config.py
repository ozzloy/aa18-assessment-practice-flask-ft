import os


class Configuration:
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"
    SECRET_KEY = (
        os.environ.get("SECRET_KEY") or "default-key-for-devs"
    )
