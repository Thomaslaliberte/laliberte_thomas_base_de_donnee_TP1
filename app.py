import sys
import mysql.connector
from datetime import date
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from affichage import Ui_MainWindow
from fonctions import *

default = 0
livre = 1
chapitre = 0 
id_sauvegarde = 0
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # On va créer la fenêtre avec cette commande
        global default
        self.setupUi(self)
        self.afficher_livre(default)
        self.afficher_sauvegarde()
        self.nouv_game.clicked.connect(self.fonction_nouv_game)
        self.changer_chapitre.clicked.connect(self.prochain_chapitre)
        self.supprimer.clicked.connect(self.activer_supprimer)
        self.sauvegarde.clicked.connect(self.enregistrer)
        self.charger.clicked.connect(self.charger_bd)
        

    def charger_bd(self):
        global id_sauvegarde
        global livre
        global chapitre
        id = self.choix_sauvegarde.currentData()
        donnee = activer_charger(id)
        for (ligne) in donnee:
            id_sauvegarde = ligne['id']
            self.nom_joueur.setText(ligne['nom_joueur'])
            donnee2 = activer_prochain_chapitre(ligne['id_livre'], ligne['id_chapitre'])
            for ligne2 in donnee2:
                self.histoire.setText(ligne2['texte']) 
                self.valeur_chapitre.setText("chapitre " + str(ligne2['no_chapitre']))
            self.compteur_or.setValue(ligne['po'])
            self.compteur_endurence.setValue(ligne['endurence'])
            self.compteur_habileter.setValue(ligne['habilete'])
            self.compteur_repas.setValue(ligne['repas'])
            self.objet.setText(ligne['objet'])
            self.objet_s.setText(ligne['objet_speciaux'])
            chapitre = ligne['id_chapitre']
            livre = ligne['id_livre']
            donnee2 = activer_recherche(livre, chapitre)
            self.choix.clear()
            for (ligne2) in donnee2:
                self.choix.addItem('chap.' + str(ligne2['no_chapitre']), ligne2['id_chapitre_destination']) 
            self.afficher_kai1(selectionner_kai(id_sauvegarde, 1))
            self.afficher_kai2(selectionner_kai(id_sauvegarde, 2))
            self.afficher_kai3(selectionner_kai(id_sauvegarde, 3))
            self.afficher_kai4(selectionner_kai(id_sauvegarde, 4))
            self.afficher_kai5(selectionner_kai(id_sauvegarde, 5))
            self.afficher_arme1(selectionner_arme(id_sauvegarde, 1))
            self.afficher_arme2(selectionner_arme(id_sauvegarde, 2)) 

    def enregistrer(self):
        global id_sauvegarde
        if self.arme1.currentData():
            global chapitre
            global livre
            supprimer_kai(id_sauvegarde)
            supprimer_armes(id_sauvegarde)
            supprimer_bd(id_sauvegarde)
            nom = self.nom_joueur.toPlainText()
            po = self.compteur_or.value()
            habileter = self.compteur_habileter.value()
            endurence = self.compteur_endurence.value()
            repas = self.compteur_repas.value()
            objet = self.objet.toPlainText()
            objet_special = self.objet_s.toPlainText()
            activer_enregistrer(id_sauvegarde, nom, chapitre, livre,po, habileter, endurence, repas, objet, objet_special)
            arme1 = self.arme1.currentData()
            activer_enregistrer_arme(1,arme1, id_sauvegarde)
            arme2 = self.arme2.currentData()
            activer_enregistrer_arme(2,arme2, id_sauvegarde)
            k1 = self.k1.currentData()
            activer_enregistrer_kai(1,k1, id_sauvegarde)
            k2 = self.k2.currentData()
            activer_enregistrer_kai(2,k2, id_sauvegarde)
            k3 = self.k3.currentData()
            activer_enregistrer_kai(3,k3, id_sauvegarde)
            k4 = self.k4.currentData()
            activer_enregistrer_kai(4,k4, id_sauvegarde)
            k5 = self.k5.currentData()
            activer_enregistrer_kai(5,k5, id_sauvegarde)
            self.message.setText("enregistrer avec succes")
            self.choix_sauvegarde.clear()
            self.afficher_sauvegarde()
        else:
            QMessageBox.warning(self,'Warning','veuillez démarer une partie pour enregister')

    def activer_supprimer(self):
        if self.choix_sauvegarde.currentData():
            id = int(self.choix_sauvegarde.currentData())
            supprimer_kai(id)
            supprimer_armes(id)
            supprimer_bd(id)
            self.choix_sauvegarde.clear()
            self.afficher_sauvegarde()
        else:
            QMessageBox.warning(self,'Warning','il n\'y a pas d\'enregistrement dans le systeme')


    def prochain_chapitre(self):
        self.message.clear()
        global livre
        global chapitre
        chapitre = int(self.choix.currentData())
        donnee = activer_prochain_chapitre(livre, chapitre)
        for ligne in donnee:
            self.histoire.setText(ligne['texte']) 
            self.valeur_chapitre.setText("chapitre " + str(ligne['no_chapitre']))
        donnee = activer_recherche(livre, chapitre)
        self.choix.clear()
        for (ligne) in donnee:
            self.choix.addItem('chap.' + str(ligne['no_chapitre']), ligne['id_chapitre_destination']) 

    def fonction_nouv_game(self):
        global id_sauvegarde
        global chapitre
        chapitre = 0
        try:
            id_sauvegarde = chercher_prochain_id()
        except:
            id_sauvegarde = 1
        self.choix.clear()
        self.afficher_kai1(default)
        self.afficher_kai2(default)
        self.afficher_kai3(default)
        self.afficher_kai4(default)
        self.afficher_kai5(default)
        self.afficher_arme1(default)
        self.afficher_arme2(default) 
        global livre
        livre = int(self.livre.currentData())
        self.afficher_prologue()

    def afficher_prologue(self):
        global livre
        donnee = activer_prologue(livre)
        for ligne in donnee:
            self.histoire.setText(ligne['texte']) 
            self.valeur_chapitre.setText(ligne['nom'])
        donnee = activer_recherche_page1(livre)
        for (ligne) in donnee:
            self.choix.addItem('chap.' + str(ligne['no_chapitre']), ligne['id'])  
         
    def afficher_sauvegarde(self):
        donnee = activer_sauvegarde()
        for (ligne) in donnee:
            self.choix_sauvegarde.addItem(ligne['nom_joueur'], ligne['id'])  

    def afficher_livre(self, default):
        donnee  = activer_livres()
        for (ligne) in donnee:
            self.livre.addItem(ligne['nom'], ligne['id'])   
        self.livre.setCurrentIndex(default)

    def afficher_kai1(self, default):
        donnee = activer_kai1()
        for (ligne) in donnee:
            self.k1.addItem(ligne['nom'], ligne['id'])  
        self.k1.setCurrentIndex(default)

    def afficher_kai2(self, default):
        donnee = activer_kai2()
        for (ligne) in donnee:
            self.k2.addItem(ligne['nom'], ligne['id'])  
        self.k2.setCurrentIndex(default)

    def afficher_kai3(self, default):
        donnee = activer_kai3()
        for (ligne) in donnee:
            self.k3.addItem(ligne['nom'], ligne['id'])  
        self.k3.setCurrentIndex(default)

    def afficher_kai4(self, default):
        donnee = activer_kai4()
        for (ligne) in donnee:
            self.k4.addItem(ligne['nom'], ligne['id'])  
        self.k4.setCurrentIndex(default)

    def afficher_kai5(self, default):
        donnee = activer_kai5()
        for (ligne) in donnee:
            self.k5.addItem(ligne['nom'], ligne['id'])  
        self.k5.setCurrentIndex(default)

    def afficher_arme1(self, default):
        donnee = activer_arme1()
        for (ligne) in donnee:
            self.arme1.addItem(ligne['nom'], ligne['id'])  
        self.arme1.setCurrentIndex(default)

    def afficher_arme2(self, default):
        donnee = activer_arme2()
        for (ligne) in donnee:
           self.arme2.addItem(ligne['nom'], ligne['id'])  
        self.arme2.setCurrentIndex(default)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()