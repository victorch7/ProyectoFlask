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
        logging.error(f"Error en la base de datos: {e}")
        return render_template('500.html'), 500
