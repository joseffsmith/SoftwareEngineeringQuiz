from tkinter import *
from Question import Question
import shelve
from Question import *
import tkinter.messagebox as tkm


class ViewEditQuestions(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.createViewEditQuestions()
        self.availableQuestions()
        self.bindListBox()
       
    def createViewEditQuestions(self):
        
        ## Add C U Logo
        photo = PhotoImage(file="Images/logo.gif")
        labelLogo = Label(self,image = photo)
        labelLogo.image=photo
        labelLogo.grid(row=0, column=0, rowspan =2 )

        ## create AdminOptions button

        butAdminOptions = Button(self, text = "Admin Options", font=("MS", 8, "bold"), height=1, width = 15)
        ##butAdminOptions["command"]=AdminOptions.AdminOptions() ## look
        butAdminOptions.grid(row=0, column=8, columnspan=2, sticky = NW, padx=10, pady=5)

        ##sets Category title
        lblCategory = Label(self, text = "Category  ", font=("MS", 12, "bold"))    ### Needs coding
        lblCategory.grid(row = 0, column = 1, columnspan = 6, sticky = SW, padx=10, pady=5)

        ##sets title
        lblViewEditQuestions = Label(self, text = "View / Edit Questions  ", font=("MS", 14, "bold"))
        lblViewEditQuestions.grid(row = 1, column = 1, columnspan = 6, sticky = NW, padx=10, pady=5)

        # sets currently available label
        lblCurrentlyAvailable = Label(self, text = "(Select From Currently Available Questions)  ", font=("MS", 8, "bold"))
        lblCurrentlyAvailable.grid(row = 3, column = 0, columnspan = 3, sticky = W, padx=10, pady=5)

        #sets up questions listbox
        self.listQ = Listbox(self,height=6, selectmode = SINGLE)
        scroll = Scrollbar(self, command= self.listQ.yview)
        self.listQ.configure(yscrollcommand=scroll.set, exportselection=False)

        #Placed list box next to label and scroll bar after.  Listbox and scrollbar aligned
        #to be next to one another
        self.listQ.grid(row=4, column=0, columnspan=9, sticky=EW, padx=(10,0), pady=5)
        scroll.grid(row=4,column=9,sticky="nsw", rowspan=6)


        #create a labelframe to group q and a

        lblFQandA = LabelFrame(self, bg = "light slate gray")
        lblFQandA.grid(row=10, column = 0, columnspan = 10, sticky = W, padx=10, pady=5)
        #create label for question text box

        lblViewEditQuestion = Label(lblFQandA, text = "Question  ", font=("MS", 8, "bold"), bg="light slate gray", fg = "white")
        lblViewEditQuestion.grid(row = 10, column = 0, columnspan = 10, sticky = W, padx=10, pady=1)

        ##inserts a text box for question

        self.txtViewEditQuestion = Entry(lblFQandA,  width = 70)
        self.txtViewEditQuestion.grid(row =  11, column = 0, columnspan = 10, sticky = W, padx=10, pady=1)

        #create label for answer text box

        lblViewEditAnswer = Label(lblFQandA, text = "Answer  ", font=("MS", 8, "bold"), bg="light slate gray", fg = "white")
        lblViewEditAnswer.grid(row = 12, column = 0, columnspan = 10, sticky = W, padx=10, pady=1)

        ##inserts a text box for editing question

        self.txtViewEditAnswer = Entry(lblFQandA,  width = 70)
        self.txtViewEditAnswer.grid(row =  13, column = 0, columnspan = 10, sticky = W, padx=10, pady=(1,15))
        
        #create a labelframe to group choices

        lblFChoices = LabelFrame(self, bg = "light slate gray")
        lblFChoices.grid(row=14, column = 0, columnspan = 10, sticky = W, padx=10, pady=15)
        #create label for Choices text boxes

        lblViewEditChoices = Label(lblFChoices, text = "Choices  ", font=("MS", 8, "bold"), bg="light slate gray", fg = "white")
        lblViewEditChoices.grid(row = 14, column = 0, columnspan = 9, sticky = W, padx=10, pady=10)

        ##inserts a text box for adding a choice1

        self.txtViewEditChoice1 = Entry(lblFChoices,  width = 70)
        self.txtViewEditChoice1.grid(row =  15, column = 0, columnspan = 10, sticky = W, padx=10, pady=5)

       ##inserts a text box for adding a choice2

        self.txtViewEditChoice2 = Entry(lblFChoices,  width = 70)
        self.txtViewEditChoice2.grid(row =  16, column = 0, columnspan = 10, sticky = W, padx=10, pady=5)

	##inserts a text box for adding a choice3

        self.txtViewEditChoice3 = Entry(lblFChoices,  width = 70)
        self.txtViewEditChoice3.grid(row =  17, column = 0, columnspan = 10, sticky = W, padx=10, pady=(5,15))

        ## create Clear Add button

        butClearEdit = Button(self, text = "Undo Edits", font=("MS", 8, "bold"), height=1, width = 15)
        butClearEdit["command"] = self.clearEdit
        butClearEdit.grid(row=18, column=0, columnspan=2, sticky = W, padx=10, pady=5)

        ## create AddAndUpdate button

        butSaveAndUpdate = Button(self, text = "Save and Update", font=("MS", 8, "bold"), height=1, width = 15, fg = "white", bg = "blue")
        butSaveAndUpdate["command"]=self.saveAndUpdate  
        butSaveAndUpdate.grid(row=18, column=8, columnspan=2, sticky = E, padx=10, pady=5)

    def bindListBox(self):
        self.listQ.bind('<<ListboxSelect>>', self.fillTextBox)

        
        ##insert available questions

    def availableQuestions(self):
        #this should pull questions from shelve file
        self.listQ.delete(0,END)
        with shelve.open('questiondb') as avail:
            klist = list(avail.keys())
            for questionID in klist:
                questionText = avail[questionID].entQuestion
                self.listQ.insert(END,questionText)
                
        
    def clearEdit(self):
        #clears all text boxes
        self.txtViewEditChoice1.delete(0,END)
        self.txtViewEditChoice2.delete(0,END)
        self.txtViewEditChoice3.delete(0,END)
        self.txtViewEditQuestion.delete(0,END)
        self.txtViewEditAnswer.delete(0,END)
           
        
    def fillTextBox(self,listQ):
        #clears first
        self.clearEdit()
        #adds to question box
        #adds to other boxes if matched
        with shelve.open('questiondb') as avail:
            for questionID in avail.keys():
                if  avail[questionID].entQuestion ==  self.getAnchor():
                    question = avail[questionID].entQuestion
                    answer = avail[questionID].entAnswer
                    choice1 = avail[questionID].entA1
                    choice2 = avail[questionID].entA2
                    choice3 = avail[questionID].entA3
                    self.txtViewEditQuestion.insert(END,question)
                    self.txtViewEditAnswer.insert(END,answer)
                    self.txtViewEditChoice1.insert(END,choice1)
                    self.txtViewEditChoice2.insert(END,choice2)
                    self.txtViewEditChoice3.insert(END,choice3)
            
    def getAnchor(self):
        test = self.listQ.get("anchor")
        return test
                        
                            
    def saveAndUpdate(self):
        #checks which question has been edited and saves new version (changed or otherwise)
        Q = self.txtViewEditQuestion
        A = self.txtViewEditAnswer
        A1 = self.txtViewEditChoice1
        A2 = self.txtViewEditChoice2
        A3 = self.txtViewEditChoice3

        avail = shelve.open('questiondb', writeback=True)
        strMsg = "All boxes must be completed"

        if Q.get() != "" and A.get()!="" and A1.get() != "" and A2.get() !="" and A3.get() !="":    
            for questionID in avail.keys():
                if  avail[questionID].entQuestion ==  self.getAnchor():
                    avail[questionID].entQuestion = Q.get() 
                    avail[questionID].entAnswer =  A.get()
                    avail[questionID].entA1 = A1.get()
                    avail[questionID].entA2 = A2.get()
                    avail[questionID].entA3 = A3.get()
                    avail.sync
                    avail.close
                    self.clearEdit()
                    self.availableQuestions()
        else:
            tkm.showwarning("Error",strMsg)

   


#main
root = Tk()  # call the Tk method
root.title("View/Edit Questions") # set the title
app= ViewEditQuestions(root)    # creates a new instance of the ViewEditQuestions class
root.mainloop()  # starts window with mainloop method
