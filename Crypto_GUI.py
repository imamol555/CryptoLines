from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from algo  import CryptoLines
from tkinter.filedialog import *
import os

class GuiCrypto:
    #file_path = StringVar()
    #content = ''
    #option_ed = StringVar()
    #e_or_dvar = StringVar()

    def __init__(self,rsa_obj):
        self.root = Tk()
        self.crypto_obj = rsa_obj
        self.file_path = StringVar()
        self.content = ''
        self.option_ed = StringVar()
        #self.e_or_dvar = StringVar()
    def ed_option(self):
        self.option_frame = LabelFrame(self.root,
                                 text="Select Option",
                                 padx=5, pady=5)
        self.option_frame.place(height=100,width=400,
                          relx=0.05,rely=0.25)

        #option_ed = StringVar()
        e_btn = Radiobutton(self.option_frame, text='Encryption',
                               variable=self.option_ed,
                           value='encryption',
                            tristatevalue="x")
        e_btn.pack()
        d_btn = Radiobutton(self.option_frame, text='Decryption',
                               variable=self.option_ed,
                           value='decryption',
                            tristatevalue="x")
        d_btn.pack()


        next_btn = Button(self.option_frame, text="Next",
             command=lambda :self.selectInputType())
        next_btn.pack()

    def selectInputType(self):
        operation = self.option_ed.get()
        self.e_or_d_btn()
        print(operation)
        if(operation == "encryption" or operation == "decryption"):
            self.file_frame = LabelFrame(self.root,
                                     text="Upload file",
                                     padx=5, pady=5)
            self.file_frame.place(height=100,width=400,
                              relx=0.55,rely=0.25)
            self.file_gui()
        else:
            messagebox.showwarning('Warning','Select an Option')

    def file_gui(self):
        noteVar = "Upload a file or enter the plainText directly"
        noteLabel = Label(self.file_frame,text=noteVar)
        noteLabel.pack()

        name = Entry(self.file_frame,
                     textvariable=self.file_path,width=300)

        name.pack()
        browse_btn = Button(self.file_frame, text="Browse",
             command = lambda : self.open_file(name))
        browse_btn.pack()
    def open_file(self,name):
        operation = self.option_ed.get()
        if(operation == "encryption"):
            fmode = "r"
        else:
            fmode = "rb"
        self.filename = askopenfilename()

        infile = open(self.filename,fmode)
        self.content = infile.read()
        self.file_path = os.path.dirname(self.filename)
        name.insert(INSERT,self.filename)
        self.show_content()

    def show_content(self):
        if(len(self.content) > 0):
            self.ftext1.delete("1.0",END)
            self.ftext1.insert("1.0",self.content)

    def create_frames(self):
        self.frame1 = LabelFrame(self.root,text="PlainText",
                    width=200,
                   height=200, bd= 0)
        self.frame1.place(height=300,width=400,
                          relx=0.05,rely=0.45)

        self.frame2 = LabelFrame(self.root,text="CipherText",
                    width=200,
                   height=200, bd= 0)
        self.frame2.place(height=300,width=400,
                          relx=0.55,rely=0.45)
        self.ftext1 = Text(self.frame1)
        self.ftext1.pack()
        self.ftext2 = Text(self.frame2)
        self.ftext2.pack()

    def e_or_d_btn(self):
       operation = self.option_ed.get()
       print("operation is ",operation)
       if(operation == "encryption"):
           #GuiCrypto.e_or_dvar.set("Encrypt")
           self.en_btn = Button(self.root, text="Encrypt",
                                command=lambda :self.encryptMessage(self.crypto_obj))
           self.en_btn.place(relx = 0.48, rely= 0.70)
       elif(operation == "decryption" ):
           #print("decryption selected")
           self.en_btn = Button(self.root, text="Decrypt",
                  command=lambda :self.decryptMessage(self.crypto_obj))
           self.en_btn.place(relx = 0.48, rely= 0.70)

    def encryptMessage(self,crypto_obj):
        #msg = self.ftext1.get('1.0', END)
        msg = self.content
        emsg = crypto_obj.encrypt(msg)
        self.ftext2.delete("1.0",END)
        self.ftext2.insert("1.0", emsg)
        self.save(edmsg=emsg,crypto_str="Cipher_")

    def decryptMessage(self,crypto_obj):
        #msg = self.ftext1.get('1.0', END)
        msg = self.content
        dmsg = crypto_obj.decrypt(msg)
        self.ftext2.delete("1.0",END)
        self.ftext2.insert("1.0", dmsg)
        self.save(edmsg=dmsg,crypto_str="Plain_")

    def save(self,crypto_str,edmsg):
        if messagebox.askyesno('Save','Do you want to save Ciphertext ?'):
            file2 = self.filename.strip(self.file_path)
            name1,name2 = file2.split('.')
            file2 = "{}{}{}".format(crypto_str,name1,".txt")
            newfilepath = "{}{}{}".format(self.file_path,"/",file2)
            fmode = ''
            if(crypto_str == "Cipher_"):
                fmode = "wb"
            elif(crypto_str=="Plain_"):
                fmode = "w"
            with open(newfilepath, fmode) as newfile:
                newfile.write(edmsg)
            messagebox.showinfo('Success',"File Saved Successfully")
    def show_gui(self):
        self.root.update()
        self.root.minsize(1000,600)
        self.root.mainloop()




new_obj = CryptoLines()
my_project = GuiCrypto(new_obj)

my_project.ed_option()
my_project.create_frames()
my_project.e_or_d_btn()
my_project.show_gui()





