DROP DATABASE IF EXISTS TP1 ;
CREATE DATABASE TP1;
USE TP1;

CREATE TABLE livre(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	nom VARCHAR(255)
);

CREATE TABLE prologue(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	id_livre INTEGER,
	nom VARCHAR(255),
	texte text,
	FOREIGN KEY (id_livre) REFERENCES livre(id)
);

CREATE TABLE chapitre(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	id_livre INTEGER,
	no_chapitre INTEGER,
	texte text,
	FOREIGN KEY (id_livre) REFERENCES livre(id)
);

CREATE TABLE lien_chapitre(
	id_chapitre_origine INTEGER,
	id_chapitre_destination INTEGER,
	PRIMARY KEY(id_chapitre_origine, id_chapitre_destination),
	FOREIGN KEY(id_chapitre_origine) REFERENCES chapitre(id),
	FOREIGN KEY(id_chapitre_destination) REFERENCES chapitre(id)
);


SELECT * FROM prologue;