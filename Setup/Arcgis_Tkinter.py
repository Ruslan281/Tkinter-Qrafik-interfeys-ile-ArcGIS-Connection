#  -*- coding: utf-8 -*-

# Created by Ruslan Huseynov

# platform: Windows NT
import os
import sys
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as Mesaj
from tkinter import BOTH, END, LEFT 

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import arcpy
from arcpy import Delete_management
import os

root = tk.Tk()

root.geometry("1363x860+267+69")
root.minsize(116, 1)
root.maxsize(1924, 1062)

root.title("Arcgis")
root.configure(background="#6c4f71")

_bgcolor = '#d9d9d9'  
_fgcolor = '#000000'  
_compcolor = '#d9d9d9'
_ana1color = '#d9d9d9'
_ana2color = '#ececec'


font10 = "-family {Segoe UI} -size 11 -weight bold -underline "  \
            "1"
font11 = "-family {Segoe UI} -size 9 -weight bold"
font12 = "-family {Courier New} -size 11 -weight bold"
font13 = "-family {Segoe UI} -size 9 -weight bold"
font14 = "-family {Courier New} -size 12 -weight bold"
font15 = "-family {Segoe UI} -size 12 -weight bold"
font16 = "-family {Courier New} -size 9 -weight bold"
font17 = "-family {Courier New} -size 8 -weight bold"
font18 = "-family {Courier New} -size 10 -weight bold"
font9 = "-family {Segoe UI} -size 11 -weight bold"


#***********************************BACK END***********************************
#***********************************BACK END***********************************
#***********************************BACK END***********************************

ddd=tk.StringVar()
ttt=tk.StringVar()


def Cixis():
    a=Mesaj.askquestion("Çıxış", "Proqramdan çıxmaq istəyirsinizmi?")
    if a == "yes" or a == "Evet":
        root.destroy()


def Daxil_et():
    a=filedialog.askdirectory(initialdir=r'C:\Users\itmtraining9\Desktop')
    ttt.set(a)


def Feature_Classes():
    if Entry1.get() == "":
        Mesaj.showinfo("Məlumat","Xahiş olunur məlumat əlavə edin")

    else:
        Listbox1.delete(0,END)
        arcpy.env.workspace=(Entry1.get())
        feature_class=arcpy.ListFeatureClasses() # Hazir
        for i in feature_class:
            Listbox1.insert(END,i)

            Mesaj.showinfo("Məlumat","Siyahi yeniləndi")
        
    

def Feature_Class_Sil():
    if (Entry2.get() == ""):
        Mesaj.showinfo("Silinəcəklər","Silinəcək məlumat yoxdur")
    else:
        arcpy.env.overwriteOutput = True
        arcpy.Delete_management(Entry1.get()+"/"+Entry2.get(),   # Hazir
                            'FeatureClass') 
        
        Mesaj.showinfo("Silinmə","Məlumat uğurla silindi")


        

def Fields():
    Listbox2.delete(0,END)
    if Entry3.get() == "":
        Mesaj.showinfo("Məlumat","Xahiş olunur məlumat əlavə edin")

    else:

        aa=arcpy.ListFields(Entry3.get())
        for i in aa:
            Listbox2.insert(END,i.name)
        Mesaj.showinfo("Məlumat","Siyahi yeniləndi")




def Fields_Sil():
    if Entry3.get() == "" and Entry4.get()=="":
        Mesaj.showinfo("Məlumat","Xahiş olunur field əlavə edin")

    else:
        arcpy.env.overwriteOutput = True
        arcpy.DeleteField_management(Entry1.get()+'/'+Entry3.get() ,Entry4.get()) # Hazir
        Mesaj.showinfo("Silinmə","Məlumat uğurla silindi")
    







def Attribute_Delete():
    if Entry3.get() == "":
        Mesaj.showinfo("Məlumat","Xahiş olunur Field_name və Feature_Class sütununa məlumat əlavə edin")

    elif Entry5.get() == "":
        Mesaj.showinfo("Məlumat","Xahiş olunur Field_name və Feature_Class sütununa məlumat əlavə edin")

    elif Entry6.get() == "":

        Mesaj.showinfo("Məlumat","Xahiş olunur Field_name və Feature_Class sütununa məlumat əlavə edin")

    else:
        arcpy.env.overwriteOutput = True

        parsel = Entry3.get()
        parsel__2_ = parsel
        parsel__3_ = parsel__2_
        

        arcpy.MakeFeatureLayer_management(Entry1.get()+'/'+Entry3.get(), "Numune")
        arcpy.SelectLayerByAttribute_management ("Numune", "NEW_SELECTION", " {} = '{}' ".format(Entry5.get(),Entry6.get()))
        arcpy.DeleteFeatures_management(parsel__2_)

        Mesaj.showinfo("Silinmə","Məlumat uğurla silindi")
        
        





def Cedvel_Siyahi():
    if Entry1.get() == "" :
        Mesaj.showinfo("Məlumat","Xahiş olunur məlumat əlavə edin")

    else:
        
        Listbox3.delete(0,END)
        cedvel=arcpy.ListTables()
        for i in cedvel:
            Listbox3.insert(0,i)

            Mesaj.showinfo("Məlumat","Siyahi yeniləndi")



def Cedvel_Sil():
    if Entry7.get() == "":
        Mesaj.showinfo("Məlumat","Xahiş olunur Cədvəl sütununa məlumat əlavə edin")

    else:
        
        arcpy.env.overwriteOutput = True
        arcpy.Delete_management(Entry1.get()+"/"+Entry7.get(),   # Hazir
                            'Table')

        Mesaj.showinfo("Silinmə","Cədvəl uğurla silindi")

    




def add_field():

    if Entry8.get() == "":
        
        Mesaj.showinfo("Məlumat","Xahiş olunur bütün sütunlara məlumat əlavə edin")

    elif Entry9.get() == "":

        Mesaj.showinfo("Məlumat","Xahiş olunur bütün sütunlara məlumat əlavə edin")

    elif Entry10.get() == "":
        
        Mesaj.showinfo("Məlumat","Xahiş olunur bütün sütunlara məlumat əlavə edin")
        

    else:

        arcpy.AddField_management(Entry8.get(), Entry9.get(), Entry10.get(), '#', '#', '#', '#', 'NULLABLE', 'NON_REQUIRED', '#')

        Mesaj.showinfo("Məlumat","Yeni 'Field' uğurla əlavə edildi")

        
        
    
    







#***********************************BACK END***********************************
#***********************************BACK END***********************************
#***********************************BACK END***********************************


Labelframe1 = tk.LabelFrame(root)
Labelframe1.place(relx=0.007, rely=0.012, relheight=0.971
                , relwidth=0.335)
Labelframe1.configure(relief='groove')
Labelframe1.configure(borderwidth="5")
Labelframe1.configure(font=font10)
Labelframe1.configure(foreground="#c0c0c0")
Labelframe1.configure(labelanchor="n")
Labelframe1.configure(text='''FEATURE CLASSES''')
Labelframe1.configure(background="#6c4f71")


Label1 = tk.Label(Labelframe1)
Label1.place(relx=0.022, rely=0.036, height=31, width=74
                , bordermode='ignore')
Label1.configure(background="#408080")
Label1.configure(disabledforeground="#a3a3a3")
Label1.configure(font=font11)
Label1.configure(foreground="#000000")
Label1.configure(text='''GDB File :''')


Entry1 = tk.Entry(Labelframe1)
Entry1.place(relx=0.197, rely=0.036, height=30, relwidth=0.623
                , bordermode='ignore')
Entry1.configure(background="white")
Entry1.configure(borderwidth="4")
Entry1.configure(disabledforeground="#a3a3a3")
Entry1.configure(font=font12)
Entry1.configure(foreground="#000000")
Entry1.configure(insertbackground="black")
Entry1.configure(textvariable=ttt)


Button1 = tk.Button(Labelframe1)
Button1.place(relx=0.833, rely=0.036, height=31, width=67
                , bordermode='ignore')
Button1.configure(activebackground="#00ff00")
Button1.configure(activeforeground="#000000")
Button1.configure(background="#008000")
Button1.configure(borderwidth="4")
Button1.configure(disabledforeground="#a3a3a3")
Button1.configure(font=font11)
Button1.configure(foreground="#000000")
Button1.configure(highlightbackground="#d9d9d9")
Button1.configure(highlightcolor="black")
Button1.configure(pady="0")
Button1.configure(text='''Daxil Et''')
Button1.configure(command=Daxil_et)


Label2 = tk.Label(Labelframe1)
Label2.place(relx=0.022, rely=0.084, height=31, width=74
                , bordermode='ignore')
Label2.configure(background="#408080")
Label2.configure(disabledforeground="#a3a3a3")
Label2.configure(font=font13)
Label2.configure(foreground="#000000")
Label2.configure(text='''Feature Class''')


Entry2 = tk.Entry(Labelframe1)
Entry2.place(relx=0.197, rely=0.084, height=30, relwidth=0.623
                , bordermode='ignore')
Entry2.configure(background="white")
Entry2.configure(borderwidth="4")
Entry2.configure(disabledforeground="#a3a3a3")
Entry2.configure(font=font12)
Entry2.configure(foreground="#000000")
Entry2.configure(insertbackground="black")
Entry2.configure(textvariable=ddd)


Button2 = tk.Button(Labelframe1)
Button2.place(relx=0.833, rely=0.084, height=31, width=67
                , bordermode='ignore')
Button2.configure(activebackground="#ff0000")
Button2.configure(activeforeground="white")
Button2.configure(activeforeground="#000000")
Button2.configure(background="#b90746")
Button2.configure(borderwidth="4")
Button2.configure(disabledforeground="#a3a3a3")
Button2.configure(font=font9)
Button2.configure(foreground="#000000")
Button2.configure(highlightbackground="#d9d9d9")
Button2.configure(highlightcolor="black")
Button2.configure(pady="0")
Button2.configure(text='''Sil''')
Button2.configure(command=Feature_Class_Sil)


Listbox1 = tk.Listbox(Labelframe1)
Listbox1.place(relx=0.022, rely=0.132, relheight=0.805
                , relwidth=0.952, bordermode='ignore')
Listbox1.configure(background="#808040")
Listbox1.configure(borderwidth="5")
Listbox1.configure(disabledforeground="#a3a3a3")
Listbox1.configure(font=font14)
Listbox1.configure(foreground="#000000")


Button3 = tk.Button(Labelframe1)
Button3.place(relx=0.197, rely=0.946, height=34, width=267
                , bordermode='ignore')
Button3.configure(activebackground="#00ff00")
Button3.configure(activeforeground="#000000")
Button3.configure(background="#008040")
Button3.configure(borderwidth="5")
Button3.configure(disabledforeground="#a3a3a3")
Button3.configure(font=font15)
Button3.configure(foreground="#000000")
Button3.configure(highlightbackground="#d9d9d9")
Button3.configure(highlightcolor="black")
Button3.configure(pady="0")
Button3.configure(text='''FEATURE CLASSES''')
Button3.configure(command=Feature_Classes)


Labelframe2 = tk.LabelFrame(root)
Labelframe2.place(relx=0.352, rely=0.012, relheight=0.971
                , relwidth=0.311)
Labelframe2.configure(relief='groove')
Labelframe2.configure(borderwidth="5")
Labelframe2.configure(font=font10)
Labelframe2.configure(foreground="#c0c0c0")
Labelframe2.configure(labelanchor="n")
Labelframe2.configure(text='''FIELDS''')
Labelframe2.configure(background="#6c4f71")



Label3 = tk.Label(Labelframe2)
Label3.place(relx=0.024, rely=0.036, height=31, width=114
                , bordermode='ignore')
Label3.configure(background="#408080")
Label3.configure(disabledforeground="#a3a3a3")
Label3.configure(font=font11)
Label3.configure(foreground="#000000")
Label3.configure(text='''Feature Class :''')


Entry3 = tk.Entry(Labelframe2)
Entry3.place(relx=0.307, rely=0.036, height=30, relwidth=0.67
                , bordermode='ignore')
Entry3.configure(background="white")
Entry3.configure(borderwidth="4")
Entry3.configure(disabledforeground="#a3a3a3")
Entry3.configure(font=font12)
Entry3.configure(foreground="#000000")
Entry3.configure(insertbackground="black")


Label4 = tk.Label(Labelframe2)
Label4.place(relx=0.024, rely=0.084, height=31, width=114
                , bordermode='ignore')
Label4.configure(background="#408080")
Label4.configure(disabledforeground="#a3a3a3")
Label4.configure(font=font11)
Label4.configure(foreground="#000000")
Label4.configure(text='''Field Name :''')



Entry4 = tk.Entry(Labelframe2)
Entry4.place(relx=0.307, rely=0.084, height=30, relwidth=0.528
                , bordermode='ignore')
Entry4.configure(background="white")
Entry4.configure(borderwidth="4")
Entry4.configure(disabledforeground="#a3a3a3")
Entry4.configure(font=font16)
Entry4.configure(foreground="#000000")
Entry4.configure(insertbackground="black")



Button4 = tk.Button(Labelframe2)
Button4.place(relx=0.849, rely=0.084, height=31, width=57
                , bordermode='ignore')
Button4.configure(activebackground="#ff0000")
Button4.configure(activeforeground="white")
Button4.configure(activeforeground="#000000")
Button4.configure(background="#c3063c")
Button4.configure(borderwidth="4")
Button4.configure(disabledforeground="#a3a3a3")
Button4.configure(font=font9)
Button4.configure(foreground="#000000")
Button4.configure(highlightbackground="#d9d9d9")
Button4.configure(highlightcolor="black")
Button4.configure(pady="0")
Button4.configure(text='''Sil''')
Button4.configure(command=Fields_Sil)


Label5 = tk.Label(Labelframe2)
Label5.place(relx=0.024, rely=0.132, height=31, width=74
                , bordermode='ignore')
Label5.configure(background="#408080")
Label5.configure(disabledforeground="#a3a3a3")
Label5.configure(font=font11)
Label5.configure(foreground="#000000")
Label5.configure(text='''Field Name''')



Entry5 = tk.Entry(Labelframe2)
Entry5.place(relx=0.212, rely=0.132, height=30, relwidth=0.292
                , bordermode='ignore')
Entry5.configure(background="white")
Entry5.configure(borderwidth="3")
Entry5.configure(disabledforeground="#a3a3a3")
Entry5.configure(font=font17)
Entry5.configure(foreground="#000000")
Entry5.configure(insertbackground="black")


Label6 = tk.Label(Labelframe2)
Label6.place(relx=0.519, rely=0.132, height=31, width=14
                , bordermode='ignore')
Label6.configure(background="#6c4f71")
Label6.configure(disabledforeground="#a3a3a3")
Label6.configure(font=font15)
Label6.configure(foreground="#000000")
Label6.configure(text='''=''')


Entry6 = tk.Entry(Labelframe2)
Entry6.place(relx=0.566, rely=0.132, height=30, relwidth=0.269
                , bordermode='ignore')
Entry6.configure(background="white")
Entry6.configure(borderwidth="3")
Entry6.configure(disabledforeground="#a3a3a3")
Entry6.configure(font=font17)
Entry6.configure(foreground="#000000")
Entry6.configure(insertbackground="black")


Button5 = tk.Button(Labelframe2)
Button5.place(relx=0.849, rely=0.132, height=34, width=57
                , bordermode='ignore')
Button5.configure(activebackground="#ff0000")
Button5.configure(activeforeground="white")
Button5.configure(activeforeground="#000000")
Button5.configure(background="#b90746")
Button5.configure(borderwidth="4")
Button5.configure(disabledforeground="#a3a3a3")
Button5.configure(font=font9)
Button5.configure(foreground="#000000")
Button5.configure(highlightbackground="#d9d9d9")
Button5.configure(highlightcolor="black")
Button5.configure(pady="0")
Button5.configure(text='''Sil''')
Button5.configure(command=Attribute_Delete)



Listbox2 = tk.Listbox(Labelframe2)
Listbox2.place(relx=0.024, rely=0.18, relheight=0.757
                , relwidth=0.953, bordermode='ignore')
Listbox2.configure(background="#808040")
Listbox2.configure(borderwidth="5")
Listbox2.configure(disabledforeground="#a3a3a3")
Listbox2.configure(font=font12)
Listbox2.configure(foreground="#000000")



Button6 = tk.Button(Labelframe2)
Button6.place(relx=0.189, rely=0.946, height=34, width=267
                , bordermode='ignore')
Button6.configure(activebackground="#00ff00")
Button6.configure(activeforeground="#000000")
Button6.configure(background="#008040")
Button6.configure(borderwidth="5")
Button6.configure(disabledforeground="#a3a3a3")
Button6.configure(font=font15)
Button6.configure(foreground="#000000")
Button6.configure(highlightbackground="#d9d9d9")
Button6.configure(highlightcolor="black")
Button6.configure(pady="0")
Button6.configure(text='''FİELD SİYAHI''')
Button6.configure(command=Fields)



Labelframe3 = tk.LabelFrame(root)
Labelframe3.place(relx=0.675, rely=0.012, relheight=0.971
                , relwidth=0.318)
Labelframe3.configure(relief='groove')
Labelframe3.configure(borderwidth="5")
Labelframe3.configure(font=font10)
Labelframe3.configure(foreground="#c0c0c0")
Labelframe3.configure(labelanchor="n")
Labelframe3.configure(text='''TABLES''')
Labelframe3.configure(background="#6c4f71")



Label7 = tk.Label(Labelframe3)
Label7.place(relx=0.023, rely=0.036, height=31, width=104
                , bordermode='ignore')
Label7.configure(background="#408080")
Label7.configure(disabledforeground="#a3a3a3")
Label7.configure(font=font11)
Label7.configure(foreground="#000000")
Label7.configure(text='''Table Name :''')



Entry7 = tk.Entry(Labelframe3)
Entry7.place(relx=0.277, rely=0.036, height=30, relwidth=0.564
                , bordermode='ignore')
Entry7.configure(background="white")
Entry7.configure(borderwidth="4")
Entry7.configure(disabledforeground="#a3a3a3")
Entry7.configure(font=font18)
Entry7.configure(foreground="#000000")
Entry7.configure(insertbackground="black")




Button7 = tk.Button(Labelframe3)
Button7.place(relx=0.855, rely=0.036, height=31, width=57
                , bordermode='ignore')
Button7.configure(activebackground="#ff0000")
Button7.configure(activeforeground="white")
Button7.configure(activeforeground="#000000")
Button7.configure(background="#b90746")
Button7.configure(borderwidth="4")
Button7.configure(disabledforeground="#a3a3a3")
Button7.configure(font=font9)
Button7.configure(foreground="#000000")
Button7.configure(highlightbackground="#d9d9d9")
Button7.configure(highlightcolor="black")
Button7.configure(pady="0")
Button7.configure(text='''Sil''')
Button7.configure(command=Cedvel_Sil)


TSeparator1 = ttk.Separator(Labelframe3)
TSeparator1.place(relx=0.072, rely=0.151, relwidth=0.866
                , bordermode='ignore')



Label8 = tk.Label(Labelframe3)
Label8.place(relx=0.323, rely=0.108, height=21, width=154
                , bordermode='ignore')
Label8.configure(background="#6c4f71")
Label8.configure(disabledforeground="#a3a3a3")
Label8.configure(font=font9)
Label8.configure(foreground="#000000")
Label8.configure(text='''Add Field''')




Label9 = tk.Label(Labelframe3)
Label9.place(relx=0.069, rely=0.168, height=21, width=94
                , bordermode='ignore')
Label9.configure(background="#408080")
Label9.configure(disabledforeground="#a3a3a3")
Label9.configure(font=font11)
Label9.configure(foreground="#000000")
Label9.configure(text='''Feature/Table :''')



Entry8 = tk.Entry(Labelframe3)
Entry8.place(relx=0.3, rely=0.168, height=20, relwidth=0.637
                , bordermode='ignore')
Entry8.configure(background="white")
Entry8.configure(borderwidth="3")
Entry8.configure(disabledforeground="#a3a3a3")
Entry8.configure(font=font18)
Entry8.configure(foreground="#000000")
Entry8.configure(insertbackground="black")


Label10 = tk.Label(Labelframe3)
Label10.place(relx=0.069, rely=0.204, height=21, width=94
                , bordermode='ignore')
Label10.configure(background="#408080")
Label10.configure(disabledforeground="#a3a3a3")
Label10.configure(font=font11)
Label10.configure(foreground="#000000")
Label10.configure(text='''Field Name :''')



Entry9 = tk.Entry(Labelframe3)
Entry9.place(relx=0.3, rely=0.204, height=20, relwidth=0.637
                , bordermode='ignore')
Entry9.configure(background="white")
Entry9.configure(borderwidth="3")
Entry9.configure(disabledforeground="#a3a3a3")
Entry9.configure(font=font18)
Entry9.configure(foreground="#000000")
Entry9.configure(insertbackground="black")


Label11 = tk.Label(Labelframe3)
Label11.place(relx=0.069, rely=0.24, height=21, width=94
                , bordermode='ignore')
Label11.configure(background="#408080")
Label11.configure(disabledforeground="#a3a3a3")
Label11.configure(font=font11)
Label11.configure(foreground="#000000")
Label11.configure(text='''Field Type :''')



Entry10 = tk.Entry(Labelframe3)
Entry10.place(relx=0.3, rely=0.24, height=20, relwidth=0.637
                , bordermode='ignore')
Entry10.configure(background="white")
Entry10.configure(borderwidth="3")
Entry10.configure(disabledforeground="#a3a3a3")
Entry10.configure(font=font18)
Entry10.configure(foreground="#000000")
Entry10.configure(insertbackground="black")


Listbox3 = tk.Listbox(Labelframe3)
Listbox3.place(relx=0.023, rely=0.323, relheight=0.613
                , relwidth=0.956, bordermode='ignore')
Listbox3.configure(background="#808040")
Listbox3.configure(borderwidth="5")
Listbox3.configure(disabledforeground="#a3a3a3")
Listbox3.configure(font=font18)
Listbox3.configure(foreground="#000000")



Button8 = tk.Button(Labelframe3)
Button8.place(relx=0.069, rely=0.946, height=34, width=167
                , bordermode='ignore')
Button8.configure(activebackground="#00ff00")
Button8.configure(activeforeground="#000000")
Button8.configure(background="#008040")
Button8.configure(borderwidth="5")
Button8.configure(disabledforeground="#a3a3a3")
Button8.configure(font=font9)
Button8.configure(foreground="#000000")
Button8.configure(highlightbackground="#d9d9d9")
Button8.configure(highlightcolor="black")
Button8.configure(pady="0")
Button8.configure(text='''TABLES''')
Button8.configure(command=Cedvel_Siyahi)



Button9 = tk.Button(Labelframe3)
Button9.place(relx=0.531, rely=0.946, height=34, width=177
                , bordermode='ignore')
Button9.configure(activebackground="#ececec")
Button9.configure(activeforeground="#000000")
Button9.configure(background="#8080ff")
Button9.configure(borderwidth="5")
Button9.configure(disabledforeground="#a3a3a3")
Button9.configure(font=font15)
Button9.configure(foreground="#000000")
Button9.configure(highlightbackground="#d9d9d9")
Button9.configure(highlightcolor="black")
Button9.configure(pady="0")
Button9.configure(text='''ÇIXIŞ''')
Button9.configure(command=Cixis)


Button10 = tk.Button(Labelframe3)
Button10.place(relx=0.069, rely=0.275, height=34, width=377
                , bordermode='ignore')
Button10.configure(activebackground="#fb5200")
Button10.configure(activeforeground="white")
Button10.configure(activeforeground="#000000")
Button10.configure(background="#ff8000")
Button10.configure(borderwidth="6")
Button10.configure(disabledforeground="#a3a3a3")
Button10.configure(font=font15)
Button10.configure(foreground="#000000")
Button10.configure(highlightbackground="#d9d9d9")
Button10.configure(highlightcolor="black")
Button10.configure(pady="0")
Button10.configure(text='''ƏLAVƏ ET''')
Button10.configure(command=add_field)


root.mainloop()
















    
