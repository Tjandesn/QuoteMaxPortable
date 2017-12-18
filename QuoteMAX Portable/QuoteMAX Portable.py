#Imports
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
import csv
import datetime
import tkinter as tk


#Variables
app = Tk()
login = 0
username = ''
err = ''
varB = IntVar()
varR = IntVar()
varP = IntVar()
varID = IntVar()
varE = IntVar()
varPL = IntVar()

#Cost Variables
builder = 0
removalist = 0
plumber = 0
electrician = 0
interiordecorator = 0
landscaper = 0

#Definitions



#New quote
def newquote():

    global entrycustomer, entryquotenew, entryquoteID, entrycost, varB, varR, varPL, varE, varID, varP


    
    #Create Window Widget
    winnew = Toplevel()
    
    winnew.title('New Quote')
    winnew.minsize(320,480)
    winnew.maxsize(320,480)
    winnew.geometry('320x480+200+200')
    winnew.iconbitmap("Images\\favicon.ico")
    
    #Labels

    labelquoteheading = Label(winnew, text = 'Generate New Quote', fg = 'Purple', font = ('Courier', 12))
    labelquoteheading.pack()

    labelcustomername = Label(winnew, text = 'Quote Title:', fg = 'Blue', font = ('Courier', 10))
    labelcustomername.place(x = 20, y = 60)

    labelquotename = Label(winnew, text = 'Client Name:', fg = 'Blue', font = ('Courier', 10))
    labelquotename.place(x = 20, y = 90)

    labelquoterefID = Label(winnew, text = 'Contact Number:', fg = 'Blue', font = ('Courier', 10))
    labelquoterefID.place(x = 20, y = 120)

    labeldate = Label(winnew, text = 'Quote Date:', fg = 'Blue', font = ('Courier', 10))
    labeldate.place(x = 20, y = 150)

    labeldate2 = Label(winnew, text = str(datetime.date.today()), fg = 'Red', font = ('Courier', 10))
    labeldate2.place(x = 160, y = 150)
    
    labeltrade = Label(winnew, text = 'Tradesmen required:', fg = 'Blue', font = ('Courier', 10))
    labeltrade.place(x = 80, y = 210)

    labeltotalcost = Label(winnew, text = 'Cost Per Hour:', fg = 'Blue', font = ('Courier', 10))
    labeltotalcost.place(x = 20, y = 180)

    labelinfo = Label(winnew, text = 'Additional $6 per hour to be added', fg = 'Red', font = ('Courier', 10))
    labelinfo.place(x = 20, y = 240)

    labelinfo2 = Label(winnew, text = 'for each additional tradesman.', fg = 'Red', font = ('Courier', 10))
    labelinfo2.place(x = 20, y = 260)

    #Entries
    entrycustomer = Entry(winnew)
    entrycustomer.place(x = 160, y = 60)
    entrycustomer.delete(0, END)
    entrycustomer.insert(0, '')

    entryquotenew = Entry(winnew)
    entryquotenew.place(x = 160, y = 90)
    entryquotenew.delete(0, END)
    entryquotenew.insert(0, '')

    entryquoteID = Entry(winnew)
    entryquoteID.place(x = 160, y = 120)
    entryquoteID.delete(0, END)
    entryquoteID.insert(0, '')

    entrycost = Entry(winnew)
    entrycost.place(x = 160, y = 180)
    entrycost.delete(0, END)
    entrycost.insert(0, '$10')


    #Check Buttons
    varB = StringVar()
    checkbuilder = Checkbutton(winnew, text = 'Builder', onvalue = 'Yes', offvalue = 'No', variable = varB)
    checkbuilder.place(x = 20, y = 290)
    checkbuilder.deselect()
    
    varR = StringVar()
    checkremove = Checkbutton(winnew, text = 'Demolition', onvalue = 'Yes', offvalue = 'No', variable = varR)
    checkremove.place(x = 160, y = 290)
    checkremove.deselect()

    varPL = StringVar()
    checkplumber = Checkbutton(winnew, text = 'Plumber', onvalue = 'Yes', offvalue = 'No', variable = varPL)
    checkplumber.place(x = 20, y = 340)
    checkplumber.deselect()

    varE = StringVar()
    checksparky = Checkbutton(winnew, text = 'Electrician', onvalue = 'Yes', offvalue = 'No', variable = varE)
    checksparky.place(x = 160, y = 340)
    checksparky.deselect()

    varID = StringVar()
    checkdeco = Checkbutton(winnew, text = 'Interior Decorator', onvalue = 'Yes', offvalue = 'No', variable = varID)
    checkdeco.place(x = 20, y = 390)
    checkdeco.deselect()

    varP = StringVar()
    checkpainter = Checkbutton(winnew, text = 'Painter', onvalue = 'Yes', offvalue = 'No', variable = varP)
    checkpainter.place(x = 160, y = 390)
    checkpainter.deselect()






    #Discard
    def discard():
        winnew.destroy()

    #Submit
    def submit():
        winsubmit = Toplevel()

        winsubmit.title('Quote Approval')
        winsubmit.minsize(320,480)
        winsubmit.maxsize(320,480)
        winsubmit.geometry('320x480+200+200')
        winsubmit.iconbitmap("Images\\favicon.ico")



    
        #Save
        def savequote():

        
            clientname = entrycustomer.get()
            quotetype = entryquotenew.get()
            quoteID = entryquoteID.get()
            quotedate = datetime.date.today()
            quotecost = entrycost.get()
            builder = varB.get()
            removalist = varR.get()
            plumber = varPL.get()
            electrician = varE.get()
            decorator = varID.get()
            painter = varP.get()

            
            
            with open("Data\\QuoteData.csv", 'a', newline = '') as fp:
                QuoteData = csv.writer(fp, delimiter = ',')
                data = ([clientname] + [quotetype] + [quoteID] + [quotedate] + [quotecost] + [builder] + [removalist] + [plumber] + [electrician] + [decorator] + [painter])
                QuoteData.writerow(data)
                messagebox.showinfo('Saved Quote', 'Your Quote has successfully been published!')
                fp.close()
                
            winnew.destroy()
            winsubmit.destroy()


       

        labelquoteheading = Label(winsubmit, text = 'Quote Submission Review', fg = 'Purple', font = ('Courier', 12))
        labelquoteheading.pack()

        labelcustomer = Label(winsubmit, text = 'Client Name:', fg = 'Blue', font = ('Courier', 10))
        labelcustomer.place(x = 20, y = 90)

        labelcustomer2 = Label(winsubmit, text = ''+str(entryquotenew.get()))
        labelcustomer2.place(x = 160, y = 90)

        labeltitle = Label(winsubmit, text = 'Quote Title:', fg = 'Blue', font = ('Courier', 10))
        labeltitle.place(x = 20, y = 60)

        labeltitle2 = Label(winsubmit, text = ''+str(entrycustomer.get()))
        labeltitle2.place(x = 160, y = 60)

        labelrefID = Label(winsubmit, text = 'Contact Number:', fg = 'Blue', font = ('Courier', 10))
        labelrefID.place(x = 20, y = 120)

        labelrefID2 = Label(winsubmit, text = ''+str(entryquoteID.get()))
        labelrefID2.place(x = 160, y = 120)

        labeldate1 = Label(winsubmit, text = 'Quote Date:', fg = 'Blue', font = ('Courier', 10))
        labeldate1.place(x = 20, y = 150)

        labeldate2 = Label(winsubmit, text = str(datetime.date.today()), fg = 'Red')
        labeldate2.place(x = 160, y = 150)

        labelcost = Label(winsubmit, text = 'Cost Per Hour:', fg = 'Blue', font = ('Courier', 10))
        labelcost.place(x = 20, y = 180)

        labelcost2 = Label(winsubmit, text = str(entrycost.get()))
        labelcost2.place(x = 160, y = 180)

        labeltrade3 = Label(winsubmit, text = 'Tradesmen required:', fg = 'Purple', font = ('Courier', 10))
        labeltrade3.place(x = 80, y = 210)

        labelbuilder = Label(winsubmit, text = 'Builder:', fg = 'Blue', font = ('Courier', 10))
        labelbuilder.place(x = 20, y = 240)

        labelbuilder2 = Label(winsubmit, text = str(varB.get()))
        labelbuilder2.place(x = 200, y = 240)

        labeldemo = Label(winsubmit, text = 'Demolition:', fg = 'Blue', font = ('Courier', 10))
        labeldemo.place(x = 20, y = 270)

        labeldemo2 = Label(winsubmit, text = str(varR.get()))
        labeldemo2.place(x = 200, y = 270)

        labelplumber = Label(winsubmit, text = 'Plumber:', fg = 'Blue', font = ('Courier', 10))
        labelplumber.place(x = 20, y = 300)

        labelplumber2 = Label(winsubmit, text = str(varPL.get()))
        labelplumber2.place(x = 200, y = 300)

        labelelectrician = Label(winsubmit, text = 'Electrician:', fg = 'Blue', font = ('Courier', 10))
        labelelectrician.place(x = 20, y = 330)

        labelelectrician2 = Label(winsubmit, text = str(varE.get()))
        labelelectrician2.place(x = 200, y = 330)

        labeldeco = Label(winsubmit, text = 'Interior Decorator:', fg = 'Blue', font = ('Courier', 10))
        labeldeco.place(x = 20, y = 360)

        labeldeco2 = Label(winsubmit, text = str(varID.get()))
        labeldeco2.place(x = 200, y = 360)

        labelpainter = Label(winsubmit, text = 'Painter:', fg = 'Blue', font = ('Courier', 10))
        labelpainter.place(x = 20, y = 390)

        labelpainter2 = Label(winsubmit, text = str(varP.get()))
        labelpainter2.place(x = 200, y = 390)

        
        buttonsave = Button(winsubmit, text = 'Save Quote', command = savequote)
        buttonsave.place(x = 245, y = 450)

        buttonsubquit = Button(winsubmit, text = 'Discard', command = winsubmit.destroy)
        buttonsubquit.place(x = 5, y = 450)



        
 
 

    #Buttons
    buttondiscard = Button(winnew, text = 'Discard', height = 1, width = 6, command = discard)
    buttondiscard.place(x = 5, y = 450)

    buttonsubmit = Button(winnew, text = 'Submit', height = 1, width = 6, command = submit)
    buttonsubmit.place(x = 263, y = 450)

def openquote():


    
    #New Window
    winopen = Toplevel()

    winopen.title('Quote Display Panel')
    winopen.minsize(320,480)
    winopen.maxsize(320,480)
    winopen.geometry('320x480+200+200')
    winopen.iconbitmap("Images\\favicon.ico")

    #Listbox for choosing quotes to load
    selection = listquote.curselection()
    value = listquote.get(selection[0])
    selected = listquote.curselection()
    index = int(listquote.curselection()[0])

    QT = QTitle[index]
    QN = QName[index]
    QNN = QNumber[index]
    QD = QDate[index]
    QC = QCost[index]
    QB = QBuilder[index]
    QDD = QDemo[index]
    QP = QPlumber[index]
    QE = QElectrician[index]
    QDE = QDeco[index]
    QPA = QPaint[index]

    #Labels for displaying quote information
    labelH = Label(winopen, text = 'Quote Display Panel', fg = 'Purple', font = ('Courier', 12))
    labelH.pack()

    labelT = Label(winopen, text = 'Quote Title:', fg = 'Blue', font = ('Courier', 10))
    labelT.place(x = 20, y = 60)

    labelTL = Label(winopen, text = QT, font = ('Courier', 10))
    labelTL.place(x = 160, y = 60)

    labelN = Label(winopen, text = 'Client Name:', fg = 'Blue', font = ('Courier', 10))
    labelN.place(x = 20, y = 90)

    labelNL = Label(winopen, text = QN, font = ('Courier', 10))
    labelNL.place(x = 160, y = 90)

    labelC = Label(winopen, text = 'Contact Number:', fg = 'Blue', font = ('Courier', 10))
    labelC.place(x = 20, y = 120)

    labelCL = Label(winopen, text = QNN, font = ('Courier', 10))
    labelCL.place(x = 160, y = 120)

    labelD = Label(winopen, text = 'Quote Date:', fg = 'Blue', font = ('Courier', 10))
    labelD.place(x = 20, y = 150)

    labelDL = Label(winopen, text = QD, fg = 'Red', font = ('Courier', 10))
    labelDL.place(x = 160, y = 150)

    labelPR = Label(winopen, text = 'Estimated Cost:', fg = 'Blue', font = ('Courier', 10))
    labelPR.place(x = 20, y = 180)

    labelPRL = Label(winopen, text = QC+' per hour', font = ('Courier', 10))
    labelPRL.place(x = 160, y = 180)

    labeltrade2 = Label(winopen, text = 'Tradesmen required:', fg = 'Purple', font = ('Courier', 10))
    labeltrade2.place(x = 80, y = 210)

    labelB = Label(winopen, text = 'Builder:', fg = 'Blue', font = ('Courier', 10))
    labelB.place(x = 20, y = 240)

    labelBL = Label(winopen, text = QB, font = ('Courier', 10))
    labelBL.place(x = 200, y = 240)

    labelDD = Label(winopen, text = 'Demolition:', fg = 'Blue', font = ('Courier', 10))
    labelDD.place(x = 20, y = 270)

    labelDDL = Label(winopen, text = QDD, font = ('Courier', 10))
    labelDDL.place(x = 200, y = 270)    

    labelP = Label(winopen, text = 'Plumber:', fg = 'Blue', font = ('Courier', 10))
    labelP.place(x = 20, y = 300)

    labelPL = Label(winopen, text = QP, font = ('Courier', 10))
    labelPL.place(x = 200, y = 300)

    labelE = Label(winopen, text = 'Electrician:', fg = 'Blue', font = ('Courier', 10))
    labelE.place(x = 20, y = 330)

    labelEL = Label(winopen, text = QE, font = ('Courier', 10))
    labelEL.place(x = 200, y = 330)

    labelDE = Label(winopen, text = 'Interior Decorator:', fg = 'Blue', font = ('Courier', 10))
    labelDE.place(x = 20, y = 360)

    labelDEL = Label(winopen, text = QDE, font = ('Courier', 10))
    labelDEL.place(x = 200, y = 360)

    labelPA = Label(winopen, text = 'Painter:', fg = 'Blue', font = ('Courier', 10))
    labelPA.place(x = 20, y = 390)

    labelPAL = Label(winopen, text = QPA, font = ('Courier', 10))
    labelPAL.place(x = 200, y = 390)

    buttondiscard2 = Button(winopen, text = 'Close', height = 1, width = 6, command = winopen.destroy)
    buttondiscard2.place(x = 5, y = 450)


def loadquote():

    #Global Variables for loading quotes.
    global listquote, QTitle, QName, QNumber, QDate, QCost, QBuilder, QDemo, QPlumber, QElectrician, QDeco, QPaint
    
    #New Window
    winload = Toplevel()

    winload.title('Quote Review Panel')
    winload.minsize(320,240)
    winload.maxsize(320,240)
    winload.geometry('320x240+200+200')
    winload.iconbitmap("Images\\favicon.ico")

    #Label
    labelloadtitle = Label(winload, text = 'Select a quote to review.', fg = 'Purple', font = ('Courier', 10))
    labelloadtitle.place(x = 5, y = 5)

    

    #Buttons
    loadbutton = Button(winload, text = 'Load Quote', command = openquote)
    loadbutton.place(x = 230, y = 210)

    loadclose = Button(winload, text = 'Close', command = winload.destroy)
    loadclose.place(x = 5, y = 210)

    #Listbox
    listquote = Listbox(winload, width = 48)
    listquote.place(x = 5, y = 25)

    yscroll = Scrollbar(winload, command = listquote.yview, borderwidth = 1, orient = tk.VERTICAL)
    yscroll.place(x = 299, y = 80)
    xscroll = Scrollbar(winload, command = listquote.xview, borderwidth = 1, orient = tk.HORIZONTAL)
    xscroll.place(x = 130, y = 190)
    
    listquote.configure(yscrollcommand = yscroll.set)
    listquote.configure(xscrollcommand = xscroll.set)
   

    rows = []
    with open ("Data\\QuoteData.csv", 'r') as fl:
        for line in fl:
            vals = line.strip('\r\n').strip('\n').split(',')
            rows.append(vals)

        QTitle = []
        for row in rows:
            if len(row) > 1:
                QTitle.append(row[0])

        QName = []
        for row in rows:
            if len(row) > 1:
                QName.append(row[1])

        QNumber = []
        for row in rows:
            if len(row) > 1:
                QNumber.append(row[2])

        QDate = []
        for row in rows:
            if len(row) > 1:
                QDate.append(row[3])

        QCost = []
        for row in rows:
            if len(row) > 1:
                QCost.append(row[4])

        QBuilder = []
        for row in rows:
            if len(row) > 1:
                QBuilder.append(row[5])

        QDemo = []
        for row in rows:
            if len(row) > 1:
                QDemo.append(row[6])

        QPlumber = []
        for row in rows:
            if len(row) > 1:
                QPlumber.append(row[7])

        QElectrician = []
        for row in rows:
            if len(row) > 1:
                QElectrician.append(row[8])

        QDeco = []
        for row in rows:
            if len(row) > 1:
                QDeco.append(row[9])

        QPaint = []
        for row in rows:
            if len(row) > 1:
                QPaint.append(row[10])

                listquote.insert(END, row[0:])
        listquote.bind(loadbutton, loadquote)
        fl.close()
    

#Logout
def logout():
    app.destroy()

#Login
def login():
    i = 0
    input = ''
    username = entryusername.get()
    password = entrypassword.get()
    a = username + ',' + password
    for row in csv.reader([a]):
        input = row
    with open ("Data\\UsernamePasswordLog.csv", newline = '') as f:
        login = csv.reader(f, delimiter=',', quoting = csv.QUOTE_ALL)
        for row in login:
            if input == row:
                i = 1
                labellogin = Label(app, text = 'Logged in as '+username, fg = 'Blue')
                labellogin.pack()

                #Destroy Widgets
                labelusername.destroy()
                entryusername.destroy()
                labelpassword.destroy()
                entrypassword.destroy()
                buttonlogin.destroy()

                #Create Widgets
                buttonnew = Button(app, text = 'New Quote', height = 1, width = 8, command = newquote)
                buttonnew.place(x = 128, y = 70)

                buttonload = Button(app, text = 'Load Quote', height = 1, width = 8, command = loadquote)
                buttonload.place(x = 128, y = 110)

                buttonlogout = Button(app, text = 'Logout', height = 1, width = 6, command = logout)
                buttonlogout.place(x = 5, y = 210)
                


    if i == 1:
        login = 1
    else:
        
        #Error Message
        messagebox.showerror('Error', 'Incorrect Username and/or Password!')

    
#Interface settings
app.title("QuoteMAX")
app.minsize(320,240)
app.maxsize(320,240)
app.geometry('320x240+200+200')
app.iconbitmap("Images\\favicon.ico")

#Heading
labelheading = Label(app, text = "QuoteMAX Portable ver. 2.0", fg = 'Purple', font = ('Courier', 12))
labelheading.pack()

#Username Widgets
labelusername = Label(app, text = 'Username', font = ('Courier', 10))
labelusername.pack()

entryusername = Entry(app)
entryusername.pack()
entryusername.delete(0, END)
entryusername.insert(0, '')

#Password Widgets
labelpassword = Label(app, text = 'Password', font = ('Courier', 10))
labelpassword.pack()

entrypassword = Entry(app, show = '*')
entrypassword.pack()
entrypassword.delete(0, END)
entrypassword.insert(0, '')

#Buttons
buttonlogin = Button(app, text = 'Login', height = 1, width = 6, command = login)
buttonlogin.place(x = 133, y = 115)

#Version Number
lablever = Label(app, text = 'Copyright 2013 QuoteMAX Pty Ltd.', fg = 'Red', font = ('Courier', 10))
lablever.place()



    

#Loop
app.mainloop()

