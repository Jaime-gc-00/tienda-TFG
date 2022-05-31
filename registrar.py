import string
from flask import current_app, Flask, request, render_template, jsonify, redirect
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
        email = datos['email']
        password = datos['password']
        rol = datos['rol']
        sql = "INSERT INTO Users (username, email, password, rol) VALUES (%s, %s, %s, %s)"
        data = (username,email,password, rol)
        cursor = conn.cursor()
        cursor.execute(sql,data)
        conn.commit()
        cursor.close()
        conn.close()
        #return "<h1>Usuario agregado correctamente</h1>"
    except:
        return "<h1>Algo salio mal en: postUser</h1>"
