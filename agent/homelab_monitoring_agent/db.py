import mysql.connector
from configuration import config
import config_keys

def connect(parameters : dict[str, str]):
    db_port = parameters[config_keys.KEY_DB_PORT] if config_keys.KEY_DB_PORT in parameters else 3306
    return mysql.connector.connect(
        host = parameters[config_keys.KEY_DB_HOST],
        port = db_port,
        user = parameters[config_keys.KEY_DB_USERNAME],
        passwd = parameters[config_keys.KEY_DB_PASSWORD])

