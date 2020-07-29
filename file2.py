# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 21:57:07 2020

@author: parfait
"""
#+++++++++++++++Importer le module sqlite3 
import sqlite3

#+++++++++++++++Fonction création de la base de donées et la table utilusateurs.
def connect():
    #création d'un objet Connection à la base de données(users.db)
    conn=sqlite3.connect("Users.db")
    #Création d'un objet cursor qui permet d'exécuter les instructions sqlite3 
    cur=conn.cursor()
    #création de la table user dans la base de données users.db
    cur.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, Fullname text, Age text, Address text, Mobile text)")
    #Valider les changements 
    conn.commit()
    #Fermer la connection
    conn.close()
    
#+++++++++++++++Fonction d'insertion de données dans la table user.
def insert(Fullname,Age,Address,Mobile):
    conn=sqlite3.connect("Users.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO user VALUES (NULL,?,?,?,?)",(Fullname,Age,Address,Mobile))
    conn.commit()
    conn.close()

#+++++++++++++++Fonction d'affichage de données de la table user.
def view():
    conn=sqlite3.connect("Users.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM user")
    rows=cur.fetchall()
    conn.close()
    return rows

#+++++++++++++++Fonction de recherche de données en fonction des paramettres saisis. 
def search(Fullname="",Age="",Address="",Mobile=""):
    conn=sqlite3.connect("Users.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM user WHERE Fullname=? OR Age=? OR Address=? OR Mobile=?", (Fullname,Age,Address,Mobile))
    rows=cur.fetchall()
    conn.close()
    return rows

#+++++++++++++++Fonction de supression de données selectionnées.
def delete(id):
    conn=sqlite3.connect("Users.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM user WHERE id=?",(id,))
    conn.commit()
    conn.close()

#+++++++++++++++Fonction de mise à jour.
def update(id,Fullname,Age,Address,Mobile):
    conn=sqlite3.connect("Users.db")
    cur=conn.cursor()
    cur.execute("UPDATE user SET Fullname=?, Age=?, Address=?, Mobile=? WHERE id=?",(Fullname,Age,Address,Mobile,id))
    conn.commit()
    conn.close()

