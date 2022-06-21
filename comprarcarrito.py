import string
from flask import current_app, Flask, request, render_template, jsonify, redirect
import json
import os
import requests

import pymysql.cursors
from pymysql.constants import CLIENT
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
        data = (username)
        #### PRIMERA QUERY --> RECOGE TODOS LOS PRODUCTOS DEL CARRITO EN UNA LISTA
        sql = "SELECT * FROM Carritos INNER JOIN Products WHERE Carritos.id_usuario=%s AND Carritos.id_product=Products.id;"
        cursor = conn.cursor()
        cursor.execute(sql, data)
        productList1 = []
        carritoList1 = cursor.fetchall()
        #### SEGUNDA QUERY --> RECORRE LA LISTA, SELECCIONA CADA PRODUCTO DE MANERA INDIVIDUAL Y SUMA LA CANTIDAD A LAS UNIDADES VENDIDAS
        for producto in carritoList1:
            data2 = (producto["id_product"])
            sql = "SELECT * FROM Products WHERE id=%s;"
            cursor.execute(sql, data2)
            productObject1 = []
            productObject = cursor.fetchone()
            nuevasUnidadesVendidas = (int(producto["cantidad"]) + int(productObject["soldUnits"]))
            #### TERCERA QUERY --> ACTUALIZA EN LA TABLA PRODUCTOS CADA PRODUCTO CON SUS UNIDADES VENDIDAS
            data3 = (productObject["soldUnits"], producto["id_product"])
            sql = "UPDATE Products SET soldUnits=%s WHERE id=%s;"
            cursor.execute(sql, data3)
        #### CUARTA QUERY --> BORRA EL CARRITO DE ESTE USUARIO PORQUE HA REALIZADO LA COMPRA
        sql = "DELETE FROM Carritos WHERE id_usuario=%s;"
        cursor.execute(sql, data)
        #### QUINTA QUERY --> DEVUELVE EL CARRITO QUE SE ESPERA QUE ESTÉ VACIO
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
