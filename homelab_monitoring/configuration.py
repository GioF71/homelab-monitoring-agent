import os

def config(name, default = None):
    value = os.getenv(name)
    if not value:
        value = default
    return value

