import email
from flask import Flask, request
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def main():
    data = request.json
    nombreDestinatario = data['username']
    destinatario = data['destinatario']
    compraList = data['compraList']
    
    msg = MIMEMultipart()
    
    detallesTabla = ""
    for articulo in compraList:
        detallesTabla += f"""
        <tr>
            <td style="vertical-align: middle; border: 1px solid;">{articulo['id']}</td>
            <td style="vertical-align: middle; border: 1px solid;">{articulo['productType']}</td>
            <td style="vertical-align: middle; border: 1px solid;">{articulo['productStyle']}</td>
            <td style="vertical-align: middle; border: 1px solid;">{articulo['gender']}</td>
            <td style="vertical-align: middle; border: 1px solid;">{articulo['currentPrice']}€</td>
            <td style="vertical-align: middle; border: 1px solid;">{articulo['cantidad']}</td>
        </tr>
        """
    
    message = f"""
    <html>
    <body>
        <strong>Hola {nombreDestinatario}, ¡gracias por comprar en nuestra tienda!</strong><br><br>
        <div>
            <p>Estos son los detalles de su compra:</p>
                <table id="miTabla" style="text-align: center; border: 1px solid;">
                    <thead style="background-color: aqua; border: 1px solid;">
                        <th style="vertical-align: middle; border: 1px solid;">Identificador</th>
                        <th style="vertical-align: middle; border: 1px solid;">Tipo de prenda</th>
                        <th style="vertical-align: middle; border: 1px solid;">Estilo de prenda</th>
                        <th style="vertical-align: middle; border: 1px solid;">Género</th>
                        <th style="vertical-align: middle; border: 1px solid;">Precio/Unidad(€)</th>
                        <th style="vertical-align: middle; border: 1px solid;">Unidades</th>
                    </thead>
                    <tbody style="font-size: 95%; font-style: italic; border: 1px solid;">
                        {detallesTabla}
                    </tbody>              
                </table>
            Ante cualquier incidencia no dude en ponerse en contacto con nosotros a través del correo electónico tiendaTFGfaas@gmail.com
        </div>
    </body>
    </html>
    """
 
    # setup the parameters of the message
    password = "JaimeTFG1_"
    msg['From'] = "tiendaTFGfaas@gmail.com"
    msg['To'] = destinatario
    msg['Subject'] = "Recibo de compra "
    
    # add in the message body
    msg.attach(MIMEText(message, 'html'))
    
    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
    
    server.starttls()
    
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    
    
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    
    server.quit()
    