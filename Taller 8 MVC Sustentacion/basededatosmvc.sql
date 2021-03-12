CREATE database tallermvc1
USE tallermvc1
CREATE TABLE persona(
id integer NOT NULL AUTO_INCREMENT,
nombres varchar(60) NOT NULL,
apellidos varchar(60) NOT NULL,
tipoDocumento varchar(5),
documento integer NOT NULL,
municipio varchar(60),
departamento varchar(60),
fechaNacimiento date NOT NULL,
email varchar(60) NOT NULL,
telefono integer NOT NULL,
usuario varchar(60) NOT NULL,
contrasena varchar(60) NOT NULL,
PRIMARY KEY(id)
);
USE tallermvc1
INSERT	INTO	persona (id, nombres, apellidos, tipodocumento, documento, municipio, departamento, fechaNacimiento, email, telefono,
usuario, contrasena)
VALUES	
(1, 'Daniel', 'Lizcano', 'CC', 1098791718, 'Bucaramanga', 'SANTANDER', '1996-11-13', 'jdaniellizcanoc', 317571, 'Daniiell', 'Proyecto');
SELECT * FROM persona
