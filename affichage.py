# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'affichage.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 609)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.choix = QtWidgets.QComboBox(self.centralwidget)
        self.choix.setGeometry(QtCore.QRect(20, 520, 521, 22))
        self.choix.setObjectName("choix")
        self.compteur_or = QtWidgets.QSpinBox(self.centralwidget)
        self.compteur_or.setGeometry(QtCore.QRect(601, 310, 181, 22))
        self.compteur_or.setObjectName("compteur_or")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(530, 310, 81, 16))
        self.label_2.setObjectName("label_2")
        self.nom_joueur = QtWidgets.QTextEdit(self.centralwidget)
        self.nom_joueur.setGeometry(QtCore.QRect(380, 130, 141, 31))
        self.nom_joueur.setObjectName("nom_joueur")
        self.choix_sauvegarde = QtWidgets.QComboBox(self.centralwidget)
        self.choix_sauvegarde.setGeometry(QtCore.QRect(30, 180, 131, 22))
        self.choix_sauvegarde.setObjectName("choix_sauvegarde")
        self.charger = QtWidgets.QPushButton(self.centralwidget)
        self.charger.setGeometry(QtCore.QRect(180, 180, 93, 28))
        self.charger.setObjectName("charger")
        self.supprimer = QtWidgets.QPushButton(self.centralwidget)
        self.supprimer.setGeometry(QtCore.QRect(280, 180, 93, 28))
        self.supprimer.setObjectName("supprimer")
        self.valeur_chapitre = QtWidgets.QLabel(self.centralwidget)
        self.valeur_chapitre.setGeometry(QtCore.QRect(130, 20, 321, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.valeur_chapitre.sizePolicy().hasHeightForWidth())
        self.valeur_chapitre.setSizePolicy(sizePolicy)
        self.valeur_chapitre.setStyleSheet("font: 26pt \"Vladimir Script\";")
        self.valeur_chapitre.setText("")
        self.valeur_chapitre.setObjectName("valeur_chapitre")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(530, 350, 55, 16))
        self.label.setObjectName("label")
        self.label20 = QtWidgets.QLabel(self.centralwidget)
        self.label20.setGeometry(QtCore.QRect(530, 380, 61, 20))
        self.label20.setObjectName("label20")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(530, 460, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(530, 420, 55, 16))
        self.label_4.setObjectName("label_4")
        self.objet = QtWidgets.QTextEdit(self.centralwidget)
        self.objet.setGeometry(QtCore.QRect(600, 460, 181, 51))
        self.objet.setObjectName("objet")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(550, 510, 101, 31))
        self.label_5.setObjectName("label_5")
        self.objet_s = QtWidgets.QTextEdit(self.centralwidget)
        self.objet_s.setGeometry(QtCore.QRect(650, 520, 131, 71))
        self.objet_s.setObjectName("objet_s")
        self.k1 = QtWidgets.QComboBox(self.centralwidget)
        self.k1.setGeometry(QtCore.QRect(590, 100, 201, 22))
        self.k1.setObjectName("k1")
        self.k2 = QtWidgets.QComboBox(self.centralwidget)
        self.k2.setGeometry(QtCore.QRect(590, 140, 201, 22))
        self.k2.setObjectName("k2")
        self.k5 = QtWidgets.QComboBox(self.centralwidget)
        self.k5.setGeometry(QtCore.QRect(590, 260, 201, 22))
        self.k5.setObjectName("k5")
        self.k4 = QtWidgets.QComboBox(self.centralwidget)
        self.k4.setGeometry(QtCore.QRect(590, 220, 201, 22))
        self.k4.setObjectName("k4")
        self.k3 = QtWidgets.QComboBox(self.centralwidget)
        self.k3.setGeometry(QtCore.QRect(590, 180, 201, 22))
        self.k3.setObjectName("k3")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(550, 290, 241, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(530, 110, 55, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(530, 140, 55, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(530, 180, 55, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(530, 220, 55, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(530, 260, 55, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(530, 10, 55, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(530, 50, 55, 16))
        self.label_12.setObjectName("label_12")
        self.arme1 = QtWidgets.QComboBox(self.centralwidget)
        self.arme1.setGeometry(QtCore.QRect(590, 10, 201, 22))
        self.arme1.setObjectName("arme1")
        self.arme2 = QtWidgets.QComboBox(self.centralwidget)
        self.arme2.setGeometry(QtCore.QRect(590, 50, 201, 22))
        self.arme2.setObjectName("arme2")
        self.nouv_game = QtWidgets.QPushButton(self.centralwidget)
        self.nouv_game.setGeometry(QtCore.QRect(250, 130, 111, 31))
        self.nouv_game.setObjectName("nouv_game")
        self.livre = QtWidgets.QComboBox(self.centralwidget)
        self.livre.setGeometry(QtCore.QRect(30, 140, 211, 22))
        self.livre.setObjectName("livre")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(430, 110, 55, 16))
        self.label_13.setObjectName("label_13")
        self.histoire = QtWidgets.QTextEdit(self.centralwidget)
        self.histoire.setGeometry(QtCore.QRect(30, 220, 491, 281))
        self.histoire.setObjectName("histoire")
        self.compteur_habileter = QtWidgets.QSpinBox(self.centralwidget)
        self.compteur_habileter.setGeometry(QtCore.QRect(600, 340, 181, 22))
        self.compteur_habileter.setObjectName("compteur_habileter")
        self.compteur_endurence = QtWidgets.QSpinBox(self.centralwidget)
        self.compteur_endurence.setGeometry(QtCore.QRect(600, 370, 181, 22))
        self.compteur_endurence.setObjectName("compteur_endurence")
        self.compteur_repas = QtWidgets.QSpinBox(self.centralwidget)
        self.compteur_repas.setGeometry(QtCore.QRect(600, 420, 181, 22))
        self.compteur_repas.setObjectName("compteur_repas")
        self.sauvegarde = QtWidgets.QPushButton(self.centralwidget)
        self.sauvegarde.setGeometry(QtCore.QRect(400, 180, 93, 28))
        self.sauvegarde.setObjectName("sauvegarde")
        self.changer_chapitre = QtWidgets.QPushButton(self.centralwidget)
        self.changer_chapitre.setGeometry(QtCore.QRect(22, 560, 521, 28))
        self.changer_chapitre.setObjectName("changer_chapitre")
        self.message = QtWidgets.QLabel(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(130, 90, 291, 16))
        self.message.setText("")
        self.message.setObjectName("message")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "pieces d\'or"))
        self.charger.setText(_translate("MainWindow", "charger"))
        self.supprimer.setText(_translate("MainWindow", "supprimer"))
        self.label.setText(_translate("MainWindow", "Habileter"))
        self.label20.setText(_translate("MainWindow", "Endurence"))
        self.label_3.setText(_translate("MainWindow", "Objet"))
        self.label_4.setText(_translate("MainWindow", "Repas"))
        self.objet.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Objets speciaux"))
        self.label_6.setText(_translate("MainWindow", "kai 1"))
        self.label_7.setText(_translate("MainWindow", "kai 2"))
        self.label_8.setText(_translate("MainWindow", "kai 3"))
        self.label_9.setText(_translate("MainWindow", "kai 4"))
        self.label_10.setText(_translate("MainWindow", "kai 5"))
        self.label_11.setText(_translate("MainWindow", "arme 1"))
        self.label_12.setText(_translate("MainWindow", "arme 2"))
        self.nouv_game.setText(_translate("MainWindow", "nouvelle partie"))
        self.label_13.setText(_translate("MainWindow", "nom"))
        self.sauvegarde.setText(_translate("MainWindow", "sauvegarder"))
        self.changer_chapitre.setText(_translate("MainWindow", "allez au chapitre selectionnée"))
