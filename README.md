# tienda-TFG
Versión inicial de la tienda acabada. Abierta a posibles nuevas funcionalidades.

Despliegue:

**1. Abrir clúster de GKE**

      gcloud container clusters create demo --num-nodes=5 --zone=us-central1-a

**2. Instalar Fission con el comando:**

      export FISSION_NAMESPACE="fission" && kubectl create namespace $FISSION_NAMESPACE && kubectl create -k "github.com/fission/fission/crds/v1?ref=v1.15.1" && helm repo add fission-charts https://fission.github.io/fission-charts/ && helm repo update && helm install --version v1.15.1 --namespace $FISSION_NAMESPACE fission fission-charts/fission-all && curl -Lo fission https://github.com/fission/fission/releases/download/v1.15.1/fission-v1.15.1-linux-amd64 && chmod +x fission && sudo mv fission /usr/local/bin/

**3. Desplegar base de datos:**

      kubectl apply -f db_conf/secrets.yaml;
      kubectl apply -f db_conf/mysql-pv.yaml;
      kubectl apply -f db_conf/mysql-deployment.yaml;

**4. Ingresar en la base de datos con:**

      kubectl run -it --rm --image=mysql --restart=Never mysql-client --namespace=fission -- mysql --host mysql --password=jaime

**6. Rellenar BBDD con el contenido de data.sql**

**7. Comprobar endpoint de la base de datos y modificar la ip en todos los archivos .py distintos de app.py:**

      kubectl describe service mysql -n fission
      
**9. Instalar el environment para las funciones, hacer un zip para el frontend y crear las funciones y rutas del frontend y backend:**

      fission environment create --name python --image jaimegc00/python-env --builder fission/python-builder:latest;
      
      zip -r main.zip app.py templates;
      fission package create --name frontend-pkg --sourcearchive main.zip --env python;
      fission fn create --name inicio --pkg frontend-pkg --entrypoint "app.inicio";
      fission fn create --name brand --pkg frontend-pkg --entrypoint "app.brand";
      fission fn create --name product --pkg frontend-pkg --entrypoint "app.product"; 
      fission fn create --name lookbook --pkg frontend-pkg --entrypoint "app.lookbook"; 
      fission fn create --name carrito --pkg frontend-pkg --entrypoint "app.carrito"; 
      fission fn create --name login --pkg frontend-pkg --entrypoint "app.login"; 

      fission fn create --name iniciarsesion --env python --code iniciarsesion.py;
      fission fn create --name getproducts --env python --code getproducts.py;
      fission fn create --name getdetails --env python --code getdetails.py;
      fission fn create --name registrar --env python --code registrar.py;
      fission fn create --name getcarrito --env python --code carrito_getcarrito.py;
      fission fn create --name borrarelemento --env python --code carrito_borrarelemento.py;
      fission fn create --name borrarcarrito --env python --code carrito_borrarcarrito.py;
      fission fn create --name agregarencarrito --env python --code carrito_agregarencarrito.py;
      fission fn create --name comprarcarrito --env python --code carrito_comprarcarrito.py;
      fission fn create --name sendemail --env python --code sendemail.py;

      fission route create --name inicio --method POST --method GET --url /inicio --function inicio;
      fission route create --name brand --method POST --method GET --url /brand --function brand;
      fission route create --name product --method POST --method GET --url /product --function product;
      fission route create --name lookbook --method POST --method GET --url /lookbook --function lookbook;
      fission route create --name carrito --method POST --method GET --url /carrito --function carrito;
      fission route create --name login --method POST --method GET --url /login --function login;
      fission route create --name iniciarsesion --method POST --url /iniciarsesion --function iniciarsesion;
      fission route create --name getproducts --method POST --url /getproducts --function getproducts;
      fission route create --name getdetails --method POST --url /getdetails --function getdetails;
      fission route create --name registrar --method POST --url /registrar --function registrar;
      fission route create --name getcarrito --method POST --url /getcarrito --function getcarrito;
      fission route create --name borrarelemento --method POST --url /borrarelemento --function borrarelemento;
      fission route create --name borrarcarrito --method POST --url /borrarcarrito --function borrarcarrito;
      fission route create --name agregarencarrito --method POST --url /agregarencarrito --function agregarencarrito;
      fission route create --name comprarcarrito --method POST --url /comprarcarrito --function comprarcarrito;
      fission route create --name sendemail --method POST --url /sendemail --function sendemail;

**10. Por último obtener la dirección IP externa con:**
      
      kubectl get svc -n fission
      
**11. Las rutas disponibles del frontend se encuentran en app.py y son:**
      
      /inicio
      /brand
      /lookbook
      /login
      (una vez iniciada sesión también estarán disponibles)
      /product
      /carrito
