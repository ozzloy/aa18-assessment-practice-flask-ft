import os


class Configuration:
    SECRET_KEY = os.environ.get("SECRET_KEY", "default-key-for-devs")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "set DATABASE_URL in .env"
    )
