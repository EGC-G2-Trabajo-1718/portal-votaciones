DROP DATABASE IF EXISTS egc-bd;
CREATE DATABASE egc-bd;

USE egc-db;

--Definir acceso por roles a b.d. si los hubiera.

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