
import tkinter as tk
from tkinter import* 
from tkinter import ttk
from tkinter import font
import mysql.connector
import time
import datetime
import random

#creating class
class hospital:
    def __init__(self,window) :
        self.window = window
        self.window.title("HOSPITAL MANAGEMENT SYSTEM")
        self.window.geometry("1500x800+0+0")

        system_title = Label(self.window, borderwidth=5, relief=GROOVE,text="Hospital Supervision System",fg="#00adef",bg="white",font=("algerian",40,"bold"))
        system_title.pack(side=TOP, fill=X)

        df = Frame(self.window, bd = 20, relief=RIDGE)
        df.place(x = 0,y = 70,  width= 1520,height = 400 )

        dflab1 = LabelFrame(df,bd=10,relief=GROOVE,padx= 10,text="Patient Info",font=("times new roman",12,"bold" ))
        dflab1.place(x = 0,y = 5,  width= 980,height = 350 )

        dflab2 = LabelFrame(df,bd=10,relief=GROOVE,padx = 10, font=("times new roman", 16,"bold"),text="Presription")
        dflab2.place(x = 990,y = 5,  width= 460,height = 350 )

        pressf = Frame(self.window, bd = 20, pady=3,relief=GROOVE)
        pressf.place(x = 0,y = 400,  width= 1500,height = 100)

        detail = Frame(self.window, bd = 20, relief=GROOVE)
        detail.place(x = 0,y = 490,  width= 1500,height = 200)

        # ********************************************************************************************
        tab_name = Label(dflab1,text="Names of medicine", font=("times new roman",12, "bold"),padx=2, pady=6)
        tab_name.grid(row = 0, column = 0)

        tab_box = ttk.Combobox( dflab1, font=("times new roman",12 , "bold"),width= 33)
        tab_box["values"]=("Paracetamol","Mahacef200", "Adrenaline", "remedesivir", "Acethromycin")
        tab_box.grid(row = 0, column = 1)

        tab_ref = Label(dflab1,font=("times new roman",12,"bold"),text ="Reference no:",padx=2)
        tab_ref.grid(row= 1, column = 0, sticky=W)
        txtref = Entry(dflab1,font=("times new roman",13,"bold"),width=35)
        txtref.grid(row=1,column=1)

        dose = Label(dflab1,font=("times new roman",12,"bold"),text="Dose: ",padx=2,pady=4)
        dose.grid(row=2,column=0,sticky=W)
        txtdose = Entry(dflab1,font=("times new roman",13,"bold"),width=35)
        txtdose.grid(row=2,column=1)

        tabno =Label(dflab1,font=("times new roman",12,"bold"),text ="No of Tablets: ",padx=2,pady=6)
        tabno.grid(row=3,column=0,sticky=W)
        txttab = Entry(dflab1,font=("times new roman",13,"bold"),width=35)
        txttab.grid(row=3,column=1)

        lbllot = Label(dflab1,font=("times new roman",12,"bold"),text="Lot:",padx=2,pady=6)
        lbllot.grid(row=4,column=0,sticky=W)
        txtlot = Entry(dflab1,font=("times new roman",13,"bold"),width=35)
        txtlot.grid(row=4,column=1)

        lblissue =Label(dflab1,font=("times new roman",12,"bold"),text="Issue date:",padx=2,pady=6)
        lblissue.grid(row=5,column=0,sticky=W)
        issuedate = Entry(dflab1,font=("times new roman",13,"bold"),width=35)
        issuedate.grid(row=5,column=1)

        expdate = Label(dflab1,font=("times new roman",12,"bold"),text="Exp Date:",padx=2,pady=6)
        expdate.grid(row=6,column=0,sticky=W)
        txtexpdate = Entry(dflab1,font=("times new roman",13,"bold"),width=35)
        txtexpdate.grid(row=6,column=1)

        dailydose = Label(dflab1,font=("times new roman",12,"bold"),text="Daily dose:",padx=2,pady=4)
        dailydose.grid(row=7,column=0,sticky=W)
        dailydosetxt =Entry(dflab1,font=("times new roman",13,"bold"),width=35)
        dailydosetxt.grid(row = 7, column=1)

        lblEffect = Label(dflab1,font=("times new roman",12,"bold"),text="Side effect:",padx=2,pady=6)
        lblEffect.grid(row=8,column=0,sticky=W)
        effect =Entry(dflab1,font=("times new roman",13,"bold"),width=35)
        effect.grid(row = 7, column=1)

        moreinfo = Label(dflab1,font=("times new roman",12,"bold"),text="More info:",padx=2)
        moreinfo.grid(row=0,column=2,sticky=W)
        txtmoreinfo =Entry(dflab1,font=("times new roman",13,"bold"),width=35)
        txtmoreinfo.grid(row = 0, column=3)

        bloodpressure = Label(dflab1,font=("times new roman",12,"bold"),text="Blood Pressure:",padx=2,pady=6)
        bloodpressure.grid(row=1,column=2,sticky=W)
        bp =Entry(dflab1,font=("times new roman",13,"bold"),width=35)
        bp.grid(row = 1, column=3)

        storage = Label(dflab1,font=("times new roman",12,"bold"),text="Storage Advice:",padx=2,pady=6)
        storage.grid(row=2,column=2,sticky=W)
        storagetxt=Entry(dflab1,font=("times new roman",13,"bold"),width=35)
        storagetxt.grid(row = 2, column=3)

        medicine = Label(dflab1,font=("times new roman",12,"bold"),text="Medication:",padx=2,pady=6)
        medicine.grid(row=3,column=2,sticky=W)
        txtmedicine=Entry(dflab1,font=("times new roman",13,"bold"),width=35)
        txtmedicine.grid(row = 3, column=3)

        patientid = Label(dflab1,font=("times new roman",12,"bold"),text="Medication:",padx=2,pady=6)
        patientid.grid(row=4,column=2,sticky=W)
        txtmedcine=Entry(dflab1,font=("times new roman",13,"bold"),width=35)
        txtmedcine.grid(row = 4, column=3)

        Nhsnum=Label(dflab1,font=("times new roman",12,"bold"),text="NHS Number:",padx=2,pady=6)
        Nhsnum.grid(row=5,column=2,sticky=W)
        nhsnumtxt=Entry(dflab1,font=("times new roman",13,"bold"),width=35)
        nhsnumtxt.grid(row = 5, column=3)

        Patientname=Label(dflab1,font=("times new roman",12,"bold"),text="patient name:",padx=2,pady=6)
        Patientname.grid(row=6,column=2,sticky=W)
        patienttxt=Entry(dflab1,font=("times new roman",13,"bold"),width=35)
        patienttxt.grid(row = 6, column=3)

        Dob=Label(dflab1,font=("times new roman",12,"bold"),text="Date of birth:",padx=2,pady=6)
        Dob.grid(row=7,column=2,sticky=W)
        Dobtxt=Entry(dflab1,font=("times new roman",13,"bold"),width=35)
        Dobtxt.grid(row = 7, column=3)

        patientaddress=Label(dflab1,font=("times new roman",12,"bold"),text="patient address:",padx=2,pady=6)
        patientaddress.grid(row=8,column=2,sticky=W)
        addresstxt=Entry(dflab1,font=("times new roman",13,"bold"),width=35)
        addresstxt.grid(row = 8, column=3)

# *************************************************************************************************************
        self.txtPres =Text(dflab2,font =("times new roman",12,"bold"),width=45,height=12,padx=2,pady=6)
        self.txtPres.grid(row=0,column=0)

        presbtn = Button(pressf,text="prescription",bg="deep sky blue",fg="black",font=("times new roman",12,"bold"),width=23,height=14,padx=2,pady=4)
        presbtn.grid(row=0,column=1)

        presbtn1 = Button(pressf,text="prescription",bg="deep sky blue",fg="black",font=("times new roman",12,"bold"),width=23,height=14,padx=2,pady=4)
        presbtn1.grid(row=0,column=2)

        presbtn2 = Button(pressf,text="prescription",bg="deep sky blue",fg="black",font=("times new roman",12,"bold"),width=23,height=14,padx=2,pady=4)
        presbtn2.grid(row=0,column=3)

        presbtn3 = Button(pressf,text="prescription",bg="deep sky blue",fg="black",font=("times new roman",12,"bold"),width=23,height=14,padx=2,pady=4)
        presbtn3.grid(row=0,column=4)

        presbtn4 = Button(pressf,text="prescription",bg="deep sky blue",fg="black",font=("times new roman",12,"bold"),width=23,height=14,padx=2,pady=4)
        presbtn4.grid(row=0,column=5)

        presbtn6 = Button(pressf,text="prescription",bg="deep sky blue",fg="black",font=("times new roman",12,"bold"),width=23,height=14,padx=2,pady=4)
        presbtn6.grid(row=0,column=6)


# **************************for changes*********************************************************************************************************************
        scroll_x =ttk.Scrollbar(detail,orient=HORIZONTAL)
        scroll_y =ttk.Scrollbar(detail,orient=VERTICAL)
        self.host_table=ttk.Treeview(detail,columns=("Name of tablets","ref","dose","no of tablets","lot","issuedate","expdate","dailydose","storage","nhs Number","patient","dob","address"),
        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x = ttk.Scrollbar(command = self.host_table.xview)
        scroll_y = ttk.Scrollbar(command = self.host_table.yview)
        self.host_table.heading("Name of tablets",text="name of tablets")
        self.host_table.heading("ref",text="ref")
        self.host_table.heading("dose",text= "dose")
        self.host_table.heading("no of tablets",text="no of tablets")
        self.host_table.heading("lot",text ="lot")
        self.host_table.heading("issuedate",text="issuedate")
        self.host_table.heading("expdate",text="expdate")
        self.host_table.heading("dailydose",text="dailydose")
        self.host_table.heading("storage",text="storage")
        self.host_table.heading("nhs Number",text="NHS number")
        self.host_table.heading("patient",text="patient name")
        self.host_table.heading("dob", text="dob")
        self.host_table.heading("address",text="Address")
        
        self.host_table["show"]= "headings"
        self.host_table.pack(fill=BOTH,expand=1)



        




if __name__ == "__main__":
    window = Tk()
    app_window = hospital(window)
    window.mainloop()
        
