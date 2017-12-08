/* 
	Esta b.d. es un diseño monolítico, con todas las tablas de los subsistemas
	existiendo en el mismo esquema. Como ventaja, es sencilla de unificar y mantener,
	pero requiere de atención por parte de cada subsistema con respecto a sus tablas.
	Propuestas alternativas:
		a) Cada subsistema toma sus tablas y crea su propia b.d. Se integran, copian o fusionan con la b.d. central.
		b) Cada subsistema usa su propia b.d., el portal del sistema no utiliza b.d.
*/

DROP DATABASE IF EXISTS egc-bd;
CREATE DATABASE egc-bd;

USE egc-db;

--Tablas del subsistema de autenticación
CREATE TABLE autenticacion (
	/*
		Información del subsistema de autenticación.
	*/
)

--Tablas del subsistema de administración de votaciones.
CREATE TABLE votacion (
	/*
		Información de votaciones.
	*/
)

CREATE TABLE pregunta (
	/*
		Información de preguntas.
	*/
)

CREATE TABLE respuesta (
	/*
		Información de respuestas.
	*/
)

--Tablas del subsistema de administración de censos.
CREATE TABLE censo (
	/*
		Información de censos.
	*/
)

--Tablas del subsistema de almacenamiento de votos.
CREATE TABLE voto (
	/*
		Información de votos.
	*/
)

--Tablas del subsistema de recuento de votos.
CREATE TABLE recuento (
	/*
		Información del subsistema de recuento de votos.
	*/
)