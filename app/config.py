from os import environ


class Configuration:
    SECRET_KEY = environ.get("SECRET_KEY", "set SECRET_KEY in .env")
