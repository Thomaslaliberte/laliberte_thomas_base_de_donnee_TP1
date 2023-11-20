import mysql.connector
def activer_livres():
    cnx = mysql.connector.connect(
    user='patate', 
    password='frite',
    host='localhost',
    database='TP1')
    cursor = cnx.cursor(dictionary=True)
    requete = "SELECT id, nom FROM TP1.livre" 
    cursor.execute(requete)
    donnee = cursor.fetchall()
    cursor.close()
    cnx.close()
    return donnee

def activer_kai1():
    cnx = mysql.connector.connect(
    user='patate', 
    password='frite',
    host='localhost',
    database='TP1')
    cursor = cnx.cursor(dictionary=True)
    requete = "SELECT id, nom FROM TP1.discipline" 
    cursor.execute(requete)
    donnee = cursor.fetchall()
    cursor.close()
    cnx.close()
    return donnee

def activer_kai2():
    cnx = mysql.connector.connect(
    user='patate', 
    password='frite',
    host='localhost',
    database='TP1')
    cursor = cnx.cursor(dictionary=True)
    requete = "SELECT id, nom FROM TP1.discipline" 
    cursor.execute(requete)
    donnee = cursor.fetchall()
    cursor.close()
    cnx.close()
    return donnee

def activer_kai3():
    cnx = mysql.connector.connect(
    user='patate', 
    password='frite',
    host='localhost',
    database='TP1')
    cursor = cnx.cursor(dictionary=True)
    requete = "SELECT id, nom FROM TP1.discipline" 
    cursor.execute(requete)
    donnee = cursor.fetchall()
    cursor.close()
    cnx.close()
    return donnee

def activer_kai4():
    cnx = mysql.connector.connect(
    user='patate', 
    password='frite',
    host='localhost',
    database='TP1')
    cursor = cnx.cursor(dictionary=True)
    requete = "SELECT id, nom FROM TP1.discipline" 
    cursor.execute(requete)
    donnee = cursor.fetchall()
    cursor.close()
    cnx.close()
    return donnee

def activer_kai5():
    cnx = mysql.connector.connect(
    user='patate', 
    password='frite',
    host='localhost',
    database='TP1')
    cursor = cnx.cursor(dictionary=True)
    requete = "SELECT id, nom FROM TP1.discipline" 
    cursor.execute(requete)
    donnee = cursor.fetchall()
    cursor.close()
    cnx.close()
    return donnee

def activer_arme1():
    cnx = mysql.connector.connect(
    user='patate', 
    password='frite',
    host='localhost',
    database='TP1')
    cursor = cnx.cursor(dictionary=True)
    requete = "SELECT id, nom FROM TP1.arme" 
    cursor.execute(requete)
    donnee = cursor.fetchall()
    cursor.close()
    cnx.close()
    return donnee

def activer_arme2():
    cnx = mysql.connector.connect(
    user='patate', 
    password='frite',
    host='localhost',
    database='TP1')
    cursor = cnx.cursor(dictionary=True)
    requete = "SELECT id, nom FROM TP1.arme" 
    cursor.execute(requete)
    donnee = cursor.fetchall()
    cursor.close()
    cnx.close()
    return donnee

def activer_prologue(livre):
    cnx = mysql.connector.connect(
    user='patate', 
    password='frite',
    host='localhost',
    database='TP1')
    cursor = cnx.cursor(dictionary=True)
    requete = "SELECT id, nom, texte FROM TP1.prologue WHERE id_livre = %(livre)s" 
    param = {'livre' : livre} 
    cursor.execute(requete, param)
    donnee = cursor.fetchall()
    cursor.close()
    cnx.close()
    return donnee

def activer_recherche_page1(livre):
    cnx = mysql.connector.connect(
    user='patate', 
    password='frite',
    host='localhost',
    database='TP1')
    cursor = cnx.cursor(dictionary=True)
    requete = "SELECT id, no_chapitre FROM TP1.chapitre WHERE id_livre = %(livre)s AND no_chapitre = 1" 
    param = {'livre' : livre} 
    cursor.execute(requete, param)
    donnee = cursor.fetchall()
    cursor.close()
    cnx.close()
    return donnee

def chercher_sauvegarde():
    cnx = mysql.connector.connect(
    user='patate', 
    password='frite',
    host='localhost',
    database='TP1')
    cursor = cnx.cursor(dictionary=True)
    requete = "SELECT id, nom_joueur, id_chapitre, id_livre, po, habilete, endurence, repas, objet, objet_speciaux FROM TP1.sauvegarde WHERE id = %(id)s" 
    cursor.execute(requete)
    donnee = cursor.fetchall()
    cursor.close()
    cnx.close()
    return donnee

def activer_sauvegarde():
    cnx = mysql.connector.connect(
    user='patate', 
    password='frite',
    host='localhost',
    database='TP1')
    cursor = cnx.cursor(dictionary=True)
    requete = "SELECT id, nom_joueur FROM TP1.sauvegarde" 
    cursor.execute(requete)
    donnee = cursor.fetchall()
    cursor.close()
    cnx.close()
    return donnee

def activer_prochain_chapitre(livre, chapitre):
    cnx = mysql.connector.connect(
    user='patate', 
    password='frite',
    host='localhost',
    database='TP1')
    cursor = cnx.cursor(dictionary=True)
    requete = "SELECT no_chapitre, texte, id FROM TP1.chapitre WHERE id_livre = %(livre)s AND id = %(chapitre)s" 
    parametre = {'livre' : livre, 'chapitre' : chapitre } 
    cursor.execute(requete,parametre)
    donnee = cursor.fetchall()
    cursor.close()
    cnx.close()
    return donnee

def activer_recherche(livre, id):
    cnx = mysql.connector.connect(
    user='patate', 
    password='frite',
    host='localhost',
    database='TP1')
    cursor = cnx.cursor(dictionary=True)
    requete = "SELECT id_chapitre_destination, no_chapitre FROM TP1.lien_chapitre INNER JOIN chapitre ON id_chapitre_destination = id WHERE id_chapitre_origine = %(id)s AND TP1.lien_chapitre.id_livre = %(livre)s;" 
    param = {'livre' : livre, 'id' : id} 
    cursor.execute(requete, param)
    donnee = cursor.fetchall()
    cursor.close()
    cnx.close()
    return donnee

def supprimer_bd(id):
    cnx = mysql.connector.connect(
    user='patate', 
    password='frite',
    host='localhost',
    database='TP1')
    cursor = cnx.cursor(dictionary=True)
    requete = "DELETE FROM sauvegarde WHERE id = %(id)s;" 
    param = {'id' : id} 
    cursor.execute(requete, param)
    donnee = cursor.fetchall()
    cnx.commit()
    cursor.close()
    cnx.close()

def activer_enregistrer(id, nom, chapitre, livre, po, habileter, endurence, repas, objet, objet_special):
    cnx = mysql.connector.connect(
    user='patate', 
    password='frite',
    host='localhost',
    database='TP1')
    cursor = cnx.cursor(dictionary=True)
    requete = "INSERT INTO sauvegarde VALUES (%(id)s, %(nom)s, %(chapitre)s, %(livre)s, %(po)s, %(habileter)s, %(endurence)s, %(repas)s, %(objet)s, %(objet_special)s)" 
    param = {'id' : id, 'nom' : nom, 'chapitre' : chapitre, 'livre' : livre, 'po' : po, 'habileter' : habileter, 'endurence' : endurence, 'repas' : repas, 'objet' : objet, 'objet_special' : objet_special} 
    cursor.execute(requete, param)
    donnee = cursor.fetchall()
    cnx.commit()
    cursor.close()
    cnx.close()
    return donnee

def chercher_prochain_id():
    cnx = mysql.connector.connect(
    user='patate', 
    password='frite',
    host='localhost',
    database='TP1')
    cursor = cnx.cursor(dictionary=True)
    requete = "SELECT id FROM sauvegarde ORDER BY id DESC LIMIT 1 ;" 
    cursor.execute(requete)
    donnee = cursor.fetchall()
    cursor.close()
    cnx.close()
    return (donnee[0]['id'])+1

def activer_charger(id):
    cnx = mysql.connector.connect(
    user='patate', 
    password='frite',
    host='localhost',
    database='TP1')
    cursor = cnx.cursor(dictionary=True)
    requete = "SELECT id, nom_joueur, id_chapitre, id_livre, po, habilete, endurence, repas, objet, objet_speciaux FROM sauvegarde WHERE id = %(id)s;" 
    param = {'id' : id} 
    cursor.execute(requete, param)
    donnee = cursor.fetchall()
    cursor.close()
    cnx.close()
    return donnee

def activer_enregistrer_arme(position, arme, sauvegarde):
    cnx = mysql.connector.connect(
    user='patate', 
    password='frite',
    host='localhost',
    database='TP1')
    cursor = cnx.cursor(dictionary=True)
    requete = "INSERT INTO sauvegarde_arme VALUES (%(id_arme)s, %(id_sauvegarde)s, %(position)s);" 
    param = {'position' : position, 'id_arme' : arme, 'id_sauvegarde' : sauvegarde} 
    cursor.execute(requete, param)
    donnee = cursor.fetchall()
    cnx.commit()
    cursor.close()
    cnx.close()
    return donnee

def supprimer_armes(id):
    cnx = mysql.connector.connect(
    user='patate', 
    password='frite',
    host='localhost',
    database='TP1')
    cursor = cnx.cursor(dictionary=True)
    requete = "DELETE FROM sauvegarde_arme WHERE id_sauvegarde = %(id)s;" 
    param = {'id' : id} 
    cursor.execute(requete, param)
    donnee = cursor.fetchall()
    cnx.commit()
    cursor.close()
    cnx.close()

def supprimer_kai(id):
    cnx = mysql.connector.connect(
    user='patate', 
    password='frite',
    host='localhost',
    database='TP1')
    cursor = cnx.cursor(dictionary=True)
    requete = "DELETE FROM sauvegarde_discipline WHERE id_sauvegarde = %(id)s;" 
    param = {'id' : id} 
    cursor.execute(requete, param)
    donnee = cursor.fetchall()
    cnx.commit()
    cursor.close()
    cnx.close()

def activer_enregistrer_kai(position, kai, sauvegarde):
    cnx = mysql.connector.connect(
    user='patate', 
    password='frite',
    host='localhost',
    database='TP1')
    cursor = cnx.cursor(dictionary=True)
    requete = "INSERT INTO sauvegarde_discipline VALUES (%(id_discipline)s, %(id_sauvegarde)s, %(position)s);" 
    param = {'position' : position, 'id_discipline' : kai, 'id_sauvegarde' : sauvegarde} 
    cursor.execute(requete, param)
    donnee = cursor.fetchall()
    cnx.commit()
    cursor.close()
    cnx.close()
    return donnee

def selectionner_arme(id_sauvegarde, position):
    cnx = mysql.connector.connect(
    user='patate', 
    password='frite',
    host='localhost',
    database='TP1')
    cursor = cnx.cursor(dictionary=True)
    requete = "SELECT id_arme FROM sauvegarde_arme WHERE id_sauvegarde = %(id)s AND id_position = %(position)s;" 
    param = {'id' : id_sauvegarde, 'position' : position} 
    cursor.execute(requete, param)
    donnee = cursor.fetchall()
    cursor.close()
    cnx.close()
    return donnee[0]['id_arme']-1

def selectionner_kai(id_sauvegarde, position):
    cnx = mysql.connector.connect(
    user='patate', 
    password='frite',
    host='localhost',
    database='TP1')
    cursor = cnx.cursor(dictionary=True)
    requete = "SELECT id_discipline FROM sauvegarde_discipline WHERE id_sauvegarde = %(id)s AND id_position = %(position)s;" 
    param = {'id' : id_sauvegarde, 'position' : position} 
    cursor.execute(requete, param)
    donnee = cursor.fetchall()
    cursor.close()
    cnx.close()
    return donnee[0]['id_discipline']-1