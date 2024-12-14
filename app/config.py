import os


class Configuration:
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "set DATABASE_URL in .env"
    )
    SECRET_KEY = (
        os.environ.get("SECRET_KEY") or "default-key-for-devs"
    )
