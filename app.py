from logging import error
import string
import time
from flask import current_app, Flask, redirect, request, render_template, jsonify, session, flash
import json
import os
import requests
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
APP_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(APP_DIR, 'templates')
current_app.template_folder = TEMPLATE_DIR

def inicio():
    sessionU = ""
    sessionE = ""
    sessionR = ""
    if request.method == 'POST':
        sessionU = request.form['sessionU']
        sessionE = request.form['sessionE']
        sessionR = request.form['sessionR']
    return render_template('index.html', sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)

def lookbook():
    sessionU = ""
    sessionE = ""
    sessionR = ""
    if request.method == 'POST':
        sessionU = request.form['sessionU']
        sessionE = request.form['sessionE']
        sessionR = request.form['sessionR']
    url = 'http://router.fission.svc/getproducts'
    if request.method == "POST":
        if request.form['submit']=='completo':
            try:
                sentencia = "SELECT * FROM Products"
                data = {'sql': sentencia}
                productList = json.loads(requests.post(url, json=data).text) 
                return render_template('lookbook.html', productos=productList, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>Error en 'completo'</h1>"
        
        if request.form['submit']=='hombres':
            try:
                sentencia = "SELECT * FROM Products WHERE gender='hombre'"
                data = {'sql': sentencia}
                productList = json.loads(requests.post(url, json=data).text) 
                return render_template('lookbook.html', productos=productList, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>Error en 'hombres'</h1>"
        
        if request.form['submit']=='mujeres':
            try:
                sentencia = "SELECT * FROM Products WHERE gender='mujer'"
                data = {'sql': sentencia}
                productList = json.loads(requests.post(url, json=data).text) 
                return render_template('lookbook.html', productos=productList, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>Error en 'mujeres'</h1>"

        if request.form['submit']=='casual_hombres':
            try:
                sentencia = "SELECT * FROM Products WHERE gender='hombre' AND productStyle='casual'"
                data = {'sql': sentencia}
                productList = json.loads(requests.post(url, json=data).text) 
                return render_template('lookbook.html', productos=productList, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>Error en 'casual_hombres'</h1>"

        if request.form['submit']=='formal_hombres':
            try:
                sentencia = "SELECT * FROM Products WHERE gender='hombre' AND productStyle='formal'"
                data = {'sql': sentencia}
                productList = json.loads(requests.post(url, json=data).text) 
                return render_template('lookbook.html', productos=productList, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>Error en 'formal_hombres'</h1>"

        if request.form['submit']=='casual_mujeres':
            try:
                sentencia = "SELECT * FROM Products WHERE gender='mujer' AND productStyle='casual'"
                data = {'sql': sentencia}
                productList = json.loads(requests.post(url, json=data).text) 
                return render_template('lookbook.html', productos=productList, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>Error en 'casual_mujeres'</h1>"

        if request.form['submit']=='formal_mujeres':
            try:
                sentencia = "SELECT * FROM Products WHERE gender='mujer' AND productStyle='formal'"
                data = {'sql': sentencia}
                productList = json.loads(requests.post(url, json=data).text) 
                return render_template('lookbook.html', productos=productList, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>Error en 'formal_mujeres'</h1>"

        ######### CHAQUETAS ###########

        if request.form['submit']=='chaquetas':
            try:
                sentencia = "SELECT * FROM Products WHERE productType='chaqueta'"
                data = {'sql': sentencia}
                productList = json.loads(requests.post(url, json=data).text) 
                return render_template('lookbook.html', productos=productList, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>Error en 'chaquetas'</h1>"

        if request.form['submit']=='chaquetas_casual_hombres':
            try:
                sentencia = "SELECT * FROM Products WHERE gender='hombre' AND productStyle='casual' AND productType='chaqueta'"
                data = {'sql': sentencia}
                productList = json.loads(requests.post(url, json=data).text) 
                return render_template('lookbook.html', productos=productList, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>Error en 'chaquetas_casual_hombres'</h1>"

        if request.form['submit']=='chaquetas_casual_mujeres':
            try:
                sentencia = "SELECT * FROM Products WHERE gender='mujer' AND productStyle='casual' AND productType='chaqueta'"
                data = {'sql': sentencia}
                productList = json.loads(requests.post(url, json=data).text) 
                return render_template('lookbook.html', productos=productList, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>Error en 'chaquetas_casual_mujeres'</h1>"

        if request.form['submit']=='chaquetas_formal_hombres':
            try:
                sentencia = "SELECT * FROM Products WHERE gender='hombre' AND productStyle='formal' AND productType='chaqueta'"
                data = {'sql': sentencia}
                productList = json.loads(requests.post(url, json=data).text) 
                return render_template('lookbook.html', productos=productList, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>Error en 'chaquetas_formal_hombres'</h1>"

        if request.form['submit']=='chaquetas_formal_mujeres':
            try:
                sentencia = "SELECT * FROM Products WHERE gender='mujer' AND productStyle='formal' AND productType='chaqueta'"
                data = {'sql': sentencia}
                productList = json.loads(requests.post(url, json=data).text) 
                return render_template('lookbook.html', productos=productList, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>Error en 'chaquetas_formal_mujeres'</h1>"

        ######### CAMISETAS ###########

        if request.form['submit']=='camisetas':
            try:
                sentencia = "SELECT * FROM Products WHERE productType='camiseta'"
                data = {'sql': sentencia}
                productList = json.loads(requests.post(url, json=data).text) 
                return render_template('lookbook.html', productos=productList, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>Error en 'camisetas'</h1>"

        if request.form['submit']=='camisetas_casual_hombres':
            try:
                sentencia = "SELECT * FROM Products WHERE gender='hombre' AND productStyle='casual' AND productType='camiseta'"
                data = {'sql': sentencia}
                productList = json.loads(requests.post(url, json=data).text) 
                return render_template('lookbook.html', productos=productList, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>Error en 'camisetas_casual_hombres'</h1>"

        if request.form['submit']=='camisetas_casual_mujeres':
            try:
                sentencia = "SELECT * FROM Products WHERE gender='mujer' AND productStyle='casual' AND productType='camiseta'"
                data = {'sql': sentencia}
                productList = json.loads(requests.post(url, json=data).text) 
                return render_template('lookbook.html', productos=productList, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>Error en 'camisetas_casual_mujeres'</h1>"

        if request.form['submit']=='camisetas_formal_hombres':
            try:
                sentencia = "SELECT * FROM Products WHERE gender='hombre' AND productStyle='formal' AND productType='camiseta'"
                data = {'sql': sentencia}
                productList = json.loads(requests.post(url, json=data).text) 
                return render_template('lookbook.html', productos=productList, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>Error en 'camisetas_formal_hombres'</h1>"

        if request.form['submit']=='camisetas_formal_mujeres':
            try:
                sentencia = "SELECT * FROM Products WHERE gender='mujer' AND productStyle='formal' AND productType='camiseta'"
                data = {'sql': sentencia}
                productList = json.loads(requests.post(url, json=data).text) 
                return render_template('lookbook.html', productos=productList, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>Error en 'camisetas_formal_mujeres'</h1>"

        ######### PANTALONES ###########

        if request.form['submit']=='pantalones':
            try:
                sentencia = "SELECT * FROM Products WHERE productType='pantalon'"
                data = {'sql': sentencia}
                productList = json.loads(requests.post(url, json=data).text) 
                return render_template('lookbook.html', productos=productList, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>Error en 'pantalones'</h1>"
        
        if request.form['submit']=='pantalones_casual_hombres':
            try:
                sentencia = "SELECT * FROM Products WHERE gender='hombre' AND productStyle='casual' AND productType='pantalon'"
                data = {'sql': sentencia}
                productList = json.loads(requests.post(url, json=data).text) 
                return render_template('lookbook.html', productos=productList, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>Error en 'pantalones_casual_hombres'</h1>"

        if request.form['submit']=='pantalones_casual_mujeres':
            try:
                sentencia = "SELECT * FROM Products WHERE gender='mujer' AND productStyle='casual' AND productType='pantalon'"
                data = {'sql': sentencia}
                productList = json.loads(requests.post(url, json=data).text) 
                return render_template('lookbook.html', productos=productList, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>Error en 'pantalones_casual_mujeres'</h1>"

        if request.form['submit']=='pantalones_formal_hombres':
            try:
                sentencia = "SELECT * FROM Products WHERE gender='hombre' AND productStyle='formal' AND productType='pantalon'"
                data = {'sql': sentencia}
                productList = json.loads(requests.post(url, json=data).text) 
                return render_template('lookbook.html', productos=productList, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>Error en 'pantalones_formal_hombres'</h1>"

        if request.form['submit']=='pantalones_formal_mujeres':
            try:
                sentencia = "SELECT * FROM Products WHERE gender='mujer' AND productStyle='formal' AND productType='pantalon'"
                data = {'sql': sentencia}
                productList = json.loads(requests.post(url, json=data).text) 
                return render_template('lookbook.html', productos=productList, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>Error en 'pantalones_formal_mujeres'</h1>"

         ######### MAS VENDIDOS ###########

        if request.form['submit']=='masvendidos':
            try:
                sentencia = "SELECT * FROM Products ORDER BY soldUnits DESC"
                data = {'sql': sentencia}
                productList = json.loads(requests.post(url, json=data).text) 
                return render_template('lookbook.html', productos=productList, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>Error en 'masvendidos'</h1>"

         ######### MAS BARATOS ###########

        if request.form['submit']=='masbaratos':
            try:
                sentencia = "SELECT * FROM Products ORDER BY currentPrice ASC"
                data = {'sql': sentencia}
                productList = json.loads(requests.post(url, json=data).text) 
                return render_template('lookbook.html', productos=productList, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>Error en 'masbaratos'</h1>"

         ######### MAS CAROS ###########

        if request.form['submit']=='mascaros':
            try:
                sentencia = "SELECT * FROM Products ORDER BY currentPrice DESC"
                data = {'sql': sentencia}
                productList = json.loads(requests.post(url, json=data).text) 
                return render_template('lookbook.html', productos=productList, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>Error en 'mascaros'</h1>"

         ######### EN OFFERTA ###########
         
        if request.form['submit']=='enoferta':
            try:
                sentencia = "SELECT * FROM Products WHERE offer=1"
                data = {'sql': sentencia}
                productList = json.loads(requests.post(url, json=data).text) 
                return render_template('lookbook.html', productos=productList, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>Error en 'en offerta'</h1>"
         
    sentencia = "SELECT * FROM Products"
    data = {'sql': sentencia}
    productList = json.loads(requests.post(url, json=data).text)
    return render_template('lookbook.html', productos=productList, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)

def brand():
    sessionU = ""
    sessionE = ""
    sessionR = ""
    if request.method == 'POST':
        sessionU = request.form['sessionU']
        sessionE = request.form['sessionE']
        sessionR = request.form['sessionR']
    return render_template('brand.html', sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)

def product():
    sessionU = ""
    sessionE = ""
    sessionR = ""
    if request.method == 'POST':
        sessionU = request.form['sessionU']
        sessionE = request.form['sessionE']
        sessionR = request.form['sessionR']
    if request.method == 'POST':
        if request.form['submit']=='detallesproducto':
            try:
                idProucto = request.form['idProducto']
                #return str(idProucto)
                data = {'idProducto': str(idProucto)}
                url = 'http://router.fission.svc/getdetails'
                productoObtenido = json.loads(requests.post(url, json=data).text)
                #return productoObtenido
                return render_template('producto.html', productoObtenido=productoObtenido, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>AAAAAAAAAAAAAAAA</h1>"
    return redirect("http://34.69.19.98/inicio")

def login():
    sessionU = ""
    sessionE = ""
    sessionR = ""
    if request.method == 'POST':
        sessionU = request.form['sessionU']
        sessionE = request.form['sessionE']
        sessionR = request.form['sessionR']
    errorMessage =""
    if request.method == "POST":
        # Called when a new user is registered
        if request.form['submit']=='registrar':
            try:
                username = request.form['username']
                email = request.form['email']
                password = generate_password_hash(request.form['password'])
                rol = request.form['rol']
                data =  {'username': username, 'email': email, 'password': password, 'rol': rol}
                url = 'http://router.fission.svc/registrar'
                requests.post(url, json=data)
                return render_template('login.html', error=errorMessage, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE) 
            except:
                return "<h1>ALGO HA SALIDO MAL</h1>"

        if request.form['submit'] == 'iniciarsesion':
            try:
                username = request.form['username']
                password = request.form['password']
                data =  {'username': username}
                url = 'http://router.fission.svc/iniciarsesion'
                usuarioLogueado = json.loads(requests.post(url, json=data).text)
                if usuarioLogueado == {}:
                    errorMessage = "Usuario no encontrado"
                    return render_template('login.html', error=errorMessage, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)             
                else:
                    if check_password_hash(usuarioLogueado['password'], password):
                        sessionU = usuarioLogueado['username']
                        sessionE = usuarioLogueado['email']
                        sessionR = usuarioLogueado['rol']
                        return render_template('login.html', error=errorMessage, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
                    else:
                        errorMessage = "Contraseña incorrecta"
                        return render_template('login.html', error=errorMessage, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>ALGO HA SALIDO MAL</h1>"

        if request.form['submit'] == 'logout':
            try:
                sessionU = ""
                sessionE = ""
                sessionR = ""
                return render_template('login.html', error=errorMessage, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>ERROR CERRANDO SESION</h1>"

    return render_template('login.html', error=errorMessage, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)

def carrito():
    sessionU = ""
    sessionE = ""
    sessionR = ""
    if request.method == 'POST':
        sessionU = request.form['sessionU']
        sessionE = request.form['sessionE']
        sessionR = request.form['sessionR']
    if request.method == "POST":
        if request.form['submit'] == 'desdeNAVBAR':
            try:
                url = 'http://router.fission.svc/getcarrito'
                data = {'username': sessionU}
                carritoList = json.loads(requests.post(url, json=data).text)
                return render_template('carrito.html', productos=carritoList, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>ERROR GETCARRITO</h1>"
        if request.form['submit'] == 'agregarDesdeProduct':
            try:
                idProduct = request.form['idProducto']
                cantidad = request.form['cantidad']
                data = {'username': sessionU, 'idProduct': idProduct, 'cantidad': cantidad}
                url = 'http://router.fission.svc/agregarencarrito'
                carritoList = json.loads(requests.post(url, json=data).text)
                return render_template('carrito.html', productos=carritoList, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>ERROR AGREGAR DESDE PRODUCT</h1>"
        if request.form['submit'] == 'agregarDesdeLookbook':
            try:
                idProduct = request.form['idProducto']
                cantidad = 1
                data = {'username': sessionU, 'idProduct': idProduct, 'cantidad': cantidad}
                url = 'http://router.fission.svc/agregarencarrito'
                carritoList = json.loads(requests.post(url, json=data).text)
                return render_template('carrito.html', productos=carritoList, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>ERROR AGREGAR DESDE LOOKBOOK</h1>"
        if request.form['submit'] == 'borrarelemento':
            try:
                idProduct = request.form['idProducto']
                data = {'username': sessionU, 'idProduct': idProduct}
                url = 'http://router.fission.svc/borrarelemento'
                carritoList = json.loads(requests.post(url, json=data).text)
                return render_template('carrito.html', productos=carritoList, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>ERROR BORRAR ELEMENTO</h1>"
        if request.form['submit'] == 'borrarcarrito':
            try:
                url = 'http://router.fission.svc/borrarcarrito'
                data = {'username': sessionU}
                carritoList = json.loads(requests.post(url, json=data).text)
                return render_template('carrito.html', productos=carritoList, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>ERROR BORRAR CARRITO</h1>"
        if request.form['submit'] == 'comprarcarrito':
            try:
                # QUEREMOS ENVIAR UN CORREO ELECTRÓNICO
                # Para ello lo primero que necesitamos es una lista con todos los productos que había en el carrito
                data1 = {'username': sessionU}
                url1 = 'http://router.fission.svc/getcarrito'
                compraList = json.loads(requests.post(url1, json=data1).text)
                # Finalmente llamamos a la función encargada de enviar el correo
                data2 = {'username': sessionU, 'destinatario': sessionE, 'compraList': compraList}
                url2 = 'http://router.fission.svc/sendemail'
                requests.post(url2, json=data2)
                # DESPUÉS VACÍA LA BASE DE DATOS DEL CARRITO Y SUMA LOS VALORES EN EL ATRIBUTO soldUnits DE CADA PRODUCTO
                data3 = {'username': sessionU}
                url3 = 'http://router.fission.svc/comprarcarrito'
                carritoList = json.loads(requests.post(url3, json=data3).text)
                return render_template('carrito.html', productos=carritoList, sessionU=sessionU, sessionR=sessionR, sessionE=sessionE)
            except:
                return "<h1>ERROR COMPRANDO CARRITO</h1>"

    return redirect("http://34.69.19.98/inicio")
