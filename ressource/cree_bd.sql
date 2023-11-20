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
	id_livre INTEGER,
	id_chapitre_origine INTEGER,
	id_chapitre_destination INTEGER,
	PRIMARY KEY(id_livre, id_chapitre_origine, id_chapitre_destination),
	FOREIGN KEY(id_livre) REFERENCES livre(id),
	FOREIGN KEY(id_chapitre_origine) REFERENCES chapitre(id),
	FOREIGN KEY(id_chapitre_destination) REFERENCES chapitre(id)
);


CREATE TABLE discipline(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	nom VARCHAR(255)
);

CREATE TABLE arme(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	nom VARCHAR(255)
);

CREATE TABLE sauvegarde(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	nom_joueur VARCHAR(255),
	id_chapitre INTEGER,
	id_livre INTEGER,
	po INTEGER,
	habilete INTEGER,
	endurence INTEGER,
	repas INTEGER,
	objet TEXT,
	objet_speciaux TEXT,
	FOREIGN KEY (id_chapitre) REFERENCES chapitre(id),
	FOREIGN KEY (id_livre) REFERENCES livre(id)
);

CREATE TABLE sauvegarde_arme(
	id_arme INTEGER,
	id_sauvegarde INTEGER,
	id_position INTEGER,
	FOREIGN KEY (id_arme) REFERENCES arme(id),
	FOREIGN KEY (id_sauvegarde) REFERENCES sauvegarde(id),
	PRIMARY KEY (id_position, id_arme, id_sauvegarde)
);

CREATE TABLE sauvegarde_discipline(
	id_discipline INTEGER,
	id_sauvegarde INTEGER,
	id_position INTEGER,
	FOREIGN KEY (id_discipline) REFERENCES discipline(id),
	FOREIGN KEY (id_sauvegarde) REFERENCES sauvegarde(id),
	PRIMARY KEY (id_discipline, id_sauvegarde, id_position)
);

##insertion de donnees

INSERT INTO discipline(nom) VALUES ('camouflage');
INSERT INTO discipline(nom) VALUES ('chasse');
INSERT INTO discipline(nom) VALUES ('sixième sens');
INSERT INTO discipline(nom) VALUES ('orientation');
INSERT INTO discipline(nom) VALUES ('guérison');
INSERT INTO discipline(nom) VALUES ('maîtrise des armes (poignard)');
INSERT INTO discipline(nom) VALUES ('maîtrise des armes (lance)');
INSERT INTO discipline(nom) VALUES ('maîtrise des armes (masse d\'arme)');
INSERT INTO discipline(nom) VALUES ('maîtrise des armes (sabre)');
INSERT INTO discipline(nom) VALUES ('maîtrise des armes (marteau de guerre)');
INSERT INTO discipline(nom) VALUES ('maîtrise des armes (épée)');
INSERT INTO discipline(nom) VALUES ('maîtrise des armes (hache)');
INSERT INTO discipline(nom) VALUES ('maîtrise des armes (baton)');
INSERT INTO discipline(nom) VALUES ('maîtrise des armes (glaive)');
INSERT INTO discipline(nom) VALUES ('bouclier psychique');
INSERT INTO discipline(nom) VALUES ('puissance psychique');
INSERT INTO discipline(nom) VALUES ('communication animale');
INSERT INTO discipline(nom) VALUES ('maîtrise psychique de la matière');


INSERT INTO arme(nom) VALUES ('poignard');
INSERT INTO arme(nom) VALUES ('lance');
INSERT INTO arme(nom) VALUES ('masse d\'arme');
INSERT INTO arme(nom) VALUES ('sabre');
INSERT INTO arme(nom) VALUES ('marteau de guerre');
INSERT INTO arme(nom) VALUES ('épée'); 
INSERT INTO arme(nom) VALUES ('hache');
INSERT INTO arme(nom) VALUES ('baton');
INSERT INTO arme(nom) VALUES ('glaive');

##trigger

DELIMITER %%
CREATE TRIGGER sauvegarde_prologue BEFORE INSERT ON sauvegarde FOR EACH ROW
BEGIN 
	IF NEW.id_chapitre <= 0 THEN 
		SET NEW.id_chapitre = 1;
	END IF;
END%%
DELIMITER ; 

DELIMITER ¦¦
CREATE TRIGGER max_po BEFORE INSERT ON sauvegarde FOR EACH ROW 
BEGIN 
	IF NEW.po > 50 THEN 
		SET NEW.po = 50;
	END IF;
END¦¦
DELIMITER ;

##user

CREATE USER IF NOT EXISTS 'patate' IDENTIFIED BY 'frite';

GRANT SELECT, INSERT, DELETE
ON TP1.sauvegarde_arme 
TO patate;

GRANT SELECT, INSERT, DELETE
ON TP1.sauvegarde_discipline 
TO patate;

GRANT SELECT, INSERT, DELETE
ON TP1.sauvegarde 
TO patate;

GRANT SELECT
ON TP1.arme
TO patate;

GRANT SELECT
ON TP1.discipline
TO patate;

GRANT SELECT
ON TP1.livre
TO patate;

GRANT SELECT
ON TP1.prologue
TO patate;

GRANT SELECT
ON TP1.chapitre
TO patate;

GRANT SELECT
ON TP1.lien_chapitre
TO patate;

