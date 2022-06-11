import string
from flask import current_app, Flask, request, render_template, jsonify, redirect
import json
import os
import requests
import pymysql.cursors
app = Flask(__name__)

def main():
    try:
        conn = pymysql.connect(
            host='10.64.1.8', 
            user='root',
            password='jaime',
            database='TFGJaime',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        datos = request.json
        sql = datos['sql']
        cursor = conn.cursor()
        cursor.execute(sql)
        productList = []
        productList = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify(productList)
    except:
        return "<h1>Algo salio mal en: getProducts</h1>"
