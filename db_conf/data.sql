# kubectl run -it --rm --image=mysql --restart=Never mysql-client --namespace=fission -- mysql --host mysql --password=jaime
CREATE DATABASE TFGJaime;
USE TFGJaime;
CREATE TABLE Users(
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(200) UNIQUE NOT NULL,
    password VARCHAR(200) NOT NULL,
    rol VARCHAR(200) NOT NULL,
    PRIMARY KEY(username)
);
-- la contraseña siempre es el nombre de usuario seguido de 1 (Ej: jaime1)
INSERT INTO Users VALUE ("jaime", "jguerreroc2000@gmail.com", "pbkdf2:sha256:260000$gh8a72EpOF9ZaWh7$58d504de38f49f77b1e9c6e9a6a695b0d6ac5836b92b0687a814f2df1b9527a8", "admin");
INSERT INTO Users VALUE ("admin", "admin@gmail.com", "pbkdf2:sha256:260000$PfGVo05hzuHjKPov$26ee71848fe0eb986e3b2d2a5e5e5ef9fb07ccfc6e13f5923ca563ae207d5220", "admin");
INSERT INTO Users VALUE ("juanma", "juanma@gmail.com", "pbkdf2:sha256:260000$wAeUGpARbHSVQudo$9f219594a46e1e90ae9354e421be087b66fa8e43e28e294d25ee24ea1e7cc69a", "cliente");
INSERT INTO Users VALUE ("usuarioupm", "jaime.guerreroc@alumnos.upm.es", "pbkdf2:sha256:260000$gh8a72EpOF9ZaWh7$58d504de38f49f77b1e9c6e9a6a695b0d6ac5836b92b0687a814f2df1b9527a8", "cliente");

CREATE TABLE Products(
    id int NOT NULL AUTO_INCREMENT,
    productStyle VARCHAR(200) NOT NULL,    
    productType VARCHAR(200) NOT NULL,
    soldUnits int NOT NULL,
    oldPrice int NOT NULL,
    currentPrice int NOT NULL,
    offer int NOT NULL,
    gender VARCHAR(200) NOT NULL,
    photo VARCHAR(200) NOT NULL,
    PRIMARY KEY(id) 
);
INSERT INTO Products VALUE (1,"casual", "camiseta", 12, 39, 29, 1 ,"hombre", "camiseta_casual_hombre.jpg");
INSERT INTO Products VALUE (2,"casual", "chaqueta", 11, 49, 45, 1 ,"hombre", "chaqueta_casual_hombre.jpg");
INSERT INTO Products VALUE (3,"casual", "pantalon", 10, 25, 18, 1 ,"hombre", "pantalon_casual_hombre.jpg");
INSERT INTO Products VALUE (4,"formal", "camiseta", 9, 35, 32, 0 ,"hombre", "camiseta_formal_hombre.jpg");
INSERT INTO Products VALUE (5,"formal", "chaqueta", 8, 45, 40, 0 ,"hombre", "chaqueta_formal_hombre.jpg");
INSERT INTO Products VALUE (6,"formal", "pantalon", 7, 18, 16, 0 ,"hombre", "pantalon_formal_hombre.jpg");
INSERT INTO Products VALUE (7,"casual", "camiseta", 6, 30, 26, 0 ,"mujer", "camiseta_casual_mujer.jpg");
INSERT INTO Products VALUE (8,"casual", "chaqueta", 5, 38, 36, 0 ,"mujer", "chaqueta_casual_mujer.jpg");
INSERT INTO Products VALUE (9,"casual", "pantalon", 4, 20, 10, 0 ,"mujer", "pantalon_casual_mujer.jpg");
INSERT INTO Products VALUE (10,"formal", "camiseta", 3, 30, 25, 1 ,"mujer", "camiseta_formal_mujer.jpg");
INSERT INTO Products VALUE (11,"formal", "chaqueta", 2, 50, 48, 1 ,"mujer", "chaqueta_formal_mujer.jpg");
INSERT INTO Products VALUE (12,"formal", "pantalon", 1, 19, 17, 1 ,"mujer", "pantalon_formal_mujer.jpg");


CREATE TABLE Carritos(
    id_usuario VARCHAR(50) NOT NULL,
    id_product int NOT NULL,
    cantidad int NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES Users(username),
    FOREIGN KEY (id_product) REFERENCES Products(id)
);
INSERT INTO Carritos VALUE ("jaime", 1, 2);
INSERT INTO Carritos VALUE ("jaime", 2, 3);
INSERT INTO Carritos VALUE ("jaime", 3, 5);
INSERT INTO Carritos VALUE ("jaime", 4, 1);
INSERT INTO Carritos VALUE ("juanma", 6, 1);
INSERT INTO Carritos VALUE ("juanma", 7, 7);
INSERT INTO Carritos VALUE ("juanma", 8, 38);
