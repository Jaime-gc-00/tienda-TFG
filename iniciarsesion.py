import string
from flask import current_app, Flask, request, render_template, jsonify, redirect, session
import json
import os
import requests
#from flaskext.mysql import MySQL
import pymysql.cursors
app = Flask(__name__)

def main():
    try:
        conn = pymysql.connect(
            host='10.64.3.7', 
            user='root',
            password='jaime',
            database='TFGJaime',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        datos = request.json
        username = datos['username']
        sql = 'SELECT * FROM Users WHERE username=%s'
        cursor = conn.cursor()
        cursor.execute(sql,(username))
        usuarioSeleccionado = []
        row = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        if row:
            return row
        else:
            return {}
    except:
        return "<h1>Algo salio mal seleccionando el usuario</h1>"
