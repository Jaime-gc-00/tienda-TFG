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
            cursorclass=pymysql.cursors.DictCursor,
        )
        datos = request.json
        username = datos['username']
        idProduct = datos['idProduct']
        #### PRIMERA QUERY
        data = (username, idProduct)
        sql = "DELETE FROM Carritos WHERE id_usuario=%s AND id_product=%s;"
        cursor = conn.cursor()
        cursor.execute(sql, data)
        #### SEGUNDA QUERY
        data = (username)
        sql = "SELECT * FROM Carritos INNER JOIN Products WHERE Carritos.id_usuario=%s AND Carritos.id_product=Products.id;"
        cursor.execute(sql, data)
        productList = []
        carritoList = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify(carritoList)
    except:
        return "<h1>Algo salio mal en: carrito_borrarelemento</h1>"
