# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 21:56:08 2020

@author: parfait
"""
#+++++++++++++++++++++++++Importation des modules  
from tkinter import *
import file2
import tkinter.messagebox

#+++++++++++++++++++++++++++++++++++++++++Appel de Fonctions+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++Fonction de selection de lignes
def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])
    
#+++++++++++++++++++++++Appel fonction d'affichage
def view_command():
    list1.delete(0,END)
    for row in file2.view():
        list1.insert(END,row)
        
#+++++++++++++++++++++++Appel fonction de recherche
def search_command():
    list1.delete(0,END)
    for row in file2.search(Fullname_text.get(),Age_text.get(),Address_text.get(),Mobile_text.get()):
        list1.insert(END,row)
        
#+++++++++++++++++++++++Appel fonction d'ajout
def add_command():
    file2.insert(Fullname_text.get(),Age_text.get(),Address_text.get(),Mobile_text.get())
    list1.delete(0,END)
    list1.insert(END,(Fullname_text.get(),Age_text.get(),Address_text.get(),Mobile_text.get()))

#+++++++++++++++++++++++Appel fonction de supression
def delete_command():
    messagebox.showinfo("Success","Delected Seccessfully")
    file2.delete(selected_tuple[0])
    
#+++++++++++++++++++++++Appel fonction de mise à jour        
def update_command():
   file2.update(selected_tuple[0],Fullname_text.get(),Age_text.get(),Address_text.get(),Mobile_text.get())

#Definition fonction de fermeture de l'application Tkinter
def iExit():
    iExit = tkinter.messagebox.askyesno("User administration application","Confirm if you want to exit")
    if iExit > 0:
      fen.destroy()
      return 
  
#+++++++++++++++++++++++++++++++++++++++++++++++++++Label et Entry++++++++++++++++++++++++++++++++++++++++++++++++++

#+++++++++++++++++++++++Definition de la fenetre pricipale
fen=Tk()
fen.title("UserAdministrationApplication")
fen.geometry("1350x750+0+0")
fen.config(bg="cadet blue")

#+++++++++++++++++++++++Defibition des labels
l_0 = Label(fen, text="UserAdministrationApplication",width=23,font=("bold", 30))
l_0.place(x=170,y=40)

l1=Label(fen,text="Fullname",bg="darkblue" , fg = "yellow")
l1.place(x=30 , y = 200 , width = 155)

l2=Label(fen,text="Age",bg="darkblue" , fg = "yellow")
l2.place(x=30 , y=225 ,  width = 155 )

l3=Label(fen,text="Address",bg="darkblue" , fg = "yellow")
l3.place(x=30 , y=250 ,  width = 155 )

l4=Label(fen,text="Mobile",bg="darkblue" , fg = "yellow")
l4.place(x=30 , y=275 ,  width = 155 )

#+++++++++++++++++++++Definition des champs de saisis
Fullname_text=StringVar()
e1 = Entry(fen,textvariable=Fullname_text)
e1.place(x = 182,  y =200 , width=525)

Age_text=StringVar()
e2= Entry(fen,textvariable=Age_text)
e2.place(x = 182,  y =225 , width=525)

Address_text=StringVar()
e3 = Entry(fen,textvariable=Address_text)
e3.place(x = 182,  y =250 , width=525)

Mobile_text=StringVar()
e4= Entry(fen,textvariable=Mobile_text)
e4.place(x = 182,  y =275 , width=525)

#+++++++++++++++++++++++Definition l'espace d'affichage
list1=Listbox(fen)
list1.place(x=710, y=100, width = 525, height = 296)

#+++++++++++++++++++++Definition boutton de defilement
sb1=Scrollbar(fen)
sb1.place(x=1240, y=200, height=100)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
list1.bind('<<ListboxSelect>>',get_selected_row)

#++++++++++++++++++++++Definition des boutons
b1 = Button(fen , text = "Display" , bg="darkblue" , fg = "yellow",command=view_command)
b1.place(x= 160 ,  y = 400 , width = 155)

b2 = Button(fen , text = "Search" , bg="darkblue" , fg = "yellow",command=search_command)
b2.place(x= 290 ,  y = 400 , width = 155)

b3 = Button(fen , text = "Add User" , bg="darkblue" , fg = "yellow",command= add_command)
b3.place(x= 30 ,  y = 400 , width = 155)

b4= Button(fen , text = "update" , bg="darkblue" , fg = "yellow",command=update_command )
b4.place(x= 420 ,  y = 400 , width =155)

b5= Button(fen , text = "Delete" , bg="darkblue" , fg = "yellow",command=delete_command)
b5.place(x= 570 ,  y = 400 , width = 155)

bExit= Button(fen , text = "Close" , bg="darkblue" , fg = "yellow",command=iExit)
bExit.place(x= 700 ,  y = 400 , width =155)

#++++++++++++++++++++++++++++++++++++++++Initialisation+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

fen.mainloop()
