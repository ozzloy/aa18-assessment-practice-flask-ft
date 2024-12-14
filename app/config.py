from os import environ


class Configuration:
    SECRET_KEY = environ.get("SECRET_KEY", "set SECRET_KEY in .env")
    SQLALCHEMY_DATABASE_URI = environ.get(
        "DATABASE_URL", "set DATABASE_URL in .env"
    )
