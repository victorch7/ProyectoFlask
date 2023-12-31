import logging
from decouple import config
from flask import abort, render_template

import mysql.connector

from mysql.connector import errorcode

def get_connection():
    try:
        return mysql.connector.connect(
            host=config('MYSQL_HOST'),
            user=config('MYSQL_USER'),
            password=config('MYSQL_PASSWORD'),
            database=config('MYSQL_DATABASE'),
            port=config('MYSQL_PORT', default=3306, cast=int),
        )
    except mysql.connector.Error as e:
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            logging.error("Error de acceso a la base de datos")
        elif e.errno == errorcode.ER_BAD_DB_ERROR:
            logging.error("La base de datos no existe")
        elif e.errno == errorcode.CR_CONN_HOST_ERROR:
            logging.error("No se pudo conectar al servidor de la base de datos")
        else:
            logging.error(f"Error en la base de datos: {e}")
        return render_template('error500.html'), 500
