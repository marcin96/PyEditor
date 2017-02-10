#Script in Python 3.3.2
#Version 0.0.1
import os
import sys
import tkinter
import subprocess
import py_compile
from tkinter import*
from tkinter import ttk
import tkinter.filedialog
import keyword
import webbrowser
import datetime
import time
from subprocess import *
#*********************
files=[]
keywords=keyword.kwlist
now = datetime.datetime.now()
#*********************
class find:
    def __init__(self,TEXT):
        self.point=0
        self.TEXT=TEXT
        self.GESUCHT=""
        self.root=Tk()
        self.gedruck=False
        self.root.title("find")
        self.root.geometry("200x100")
        self.text1=Text(self.root)
        self.text1.pack(fill="both",expand=True)
        self.text1.bind('<Return>',self.enter)
        self.CORR=None
        self.t=False
        
    def enter(self,event):
        self.GESUCHT=self.text1.get("1.0",END)
        self.find()
        
    def find(self):
        print("Suche gestartet....")
        zähler=0
        corr=[]
        txt=self.TEXT.split(' ')
        for i in txt:
            if i.find(self.GESUCHT)!=-1:
                print(zähler)
                corr.append(zähler)
            zähler+=1
        self.t=True
        self.CORR=corr
        self.root.quit()
class Pyedit:
    def __init__(self,Gui,methods):
        self.gui=Gui
        self.met=methods
        self.file=None
        self.syntax=None
        self.workdir=os.path
        self.used=False
    def get_Lines(self):
        None
    def Keys_Save(self,event):
        print("Speichernd....")
        self.save_file()
        print("Wurde erfolgreich gespeichert\a")
    def Keys_find(self,event):
        self.find()
    def Keys_open(self,event):
        self.open_file()
    def Keys_new(self,event):
        self.new_file()
    def mark_key_words(self):
        text_full=self.gui.txt.get("0.0",END)
        index=[0,0]
        text_gesplitet=text_full.split(' ')
        for textw in text_gesplitet:
            index[1]+=len(textw)+1
            index[2]=0
            for i in keywords:
                if i==textw:
                    print("Keyword")
        
    def Active_Searcher(self,event):
        text_full=self.gui.txt.get("0.0",END)
        text_gesplitet=text_full.split(' ')
        textw=str(text_gesplitet[len(text_gesplitet)-1])
        wort=text_gesplitet[len(text_gesplitet)-1]
        wort_länge=len(wort)
        index1=int(len(text_full)-len(text_gesplitet[len(text_gesplitet)-1]))
        curr=self.gui.txt.index(CURRENT)
        x_corr=curr.split('.')
        #print(index1,index2)
        for i in keywords:
            if textw.strip()==i:
                print("KeyWord")
                self.gui.txt.tag_add(i,x_corr[0]+"."+str(int(x_corr[1])-len(i)-1),str(x_corr[0])+"."+str(x_corr[1]))
                print(x_corr)
                self.gui.txt.tag_config(i,foreground="orange")
            else:
                None
        self.gui.txt.tag_remove(textw,END)
        del x_corr
    def Debug(self):
        None
        
                
    def start_gui(self):
        self.gui.start()
        self.gui.txt.config(state="disabled",bg="grey")
        self.gui.filemenu.add_command(label="New", command=self.new_file)
        self.gui.filemenu.add_command(label="Open...", command=self.open_file)
        self.gui.filemenu.add_command(label="Save",command=self.save_file)
        self.gui.filemenu.add_command(label="Save as",command=self.save_as_file)
        self.gui.filemenu.add_separator()
        self.gui.filemenu.add_command(label="exit", command=self.met.destroy)
        self.gui.editmenu.add_command(label="Undo",command=self.Undo)
        self.gui.editmenu.add_command(label="Redo",command=self.Redo)
        self.gui.editmenu.add_command(label="Cut",command=self.Cut)
        self.gui.editmenu.add_command(label="Copy",command=self.Copy)
        self.gui.editmenu.add_command(label="Paste",command=self.Paste)
        self.gui.editmenu.add_command(label="select all",command=self.select_all)
        self.gui.editmenu.add_command(label="find",command=self.find)
        self.gui.viewmenu.add_command(label="Maximize",command=None)
        self.gui.viewmenu.add_command(label="Normalize",command=None)
        self.gui.viewmenu.add_command(label="Minimize",command=None)
        self.gui.viewmenu.add_command(label="Zoom in",command=None)
        self.gui.viewmenu.add_command(label="Zoom out",command=None)
        self.gui.syntaxmenu.add_command(label="Get Syntax()",command=None)
        self.gui.syntaxmenu.add_command(label="Html",command=None)
        self.gui.syntaxmenu.add_command(label="Pythone",command=None)
        self.gui.formatmenu.add_command(label="Font",command=None)
        self.gui.formatmenu.add_command(label="Forecolor",command=None)
        self.gui.formatmenu.add_command(label="Backcolor",command=None)
        self.gui.projectmenu.add_command(label="Debug",command=self.Debug)
        self.gui.projectmenu.add_command(label="Execute to Pyc",command=None)
        self.gui.projectmenu.add_command(label="Execute to exe",command=None)
        self.gui.toolmenu.add_command(label="Get Language",command=None)
        self.gui.toolmenu.add_command(label="Definition",command=None)
        self.gui.toolmenu.add_command(label="Search",command=None)
        self.gui.toolmenu.add_command(label="Cipher",command=None)
        self.gui.helpmenu.add_command(label="Help",command=self.Help)
        #Key Bindings for the root form
        self.gui.root.bind('<Control-Key-1>',exit)
        self.gui.root.bind('<Control-Key-s>',self.Keys_Save)
        self.gui.root.bind('<Control-Key-q>',exit)
        self.gui.root.bind('<Control-Key-o>',self.Keys_open)
        self.gui.root.bind('<Control-Key-n>',self.Keys_new)
        self.gui.root.bind('<Control-Key-a>',self.select_all)
        self.gui.root.bind('Control-Key-x>',self.delete_some)
        self.gui.root.bind('Control-Key-c>',self.Copy)
        self.gui.root.bind('<Control-Key-v>',self.Paste)
        self.gui.txt.bind('Control-Key-w>',self.Keys_find)
        self.gui.txt.bind('<Control-Key-z>',self.Undo)
        self.gui.txt.bind('<Control-Key-r>',self.Redo)
        self.gui.txt.bind('<Button-1>',self.Cklicked)
        self.gui.root.bind('<F5>',self.Debug)
        self.gui.txt.bind('<space>',self.Active_Searcher)
        self.gui.root.mainloop()
        
    def Cklicked(self,event):
        index=self.gui.txt.index(CURRENT)
        index2=index.split('.')
        self.gui.statusbar.set_text("["+index2[0]+" . "+index2[1]+"]")
        self.start_Console()
    def start_Console(self):
        None#Here we start the python process and make Stdin and stdout
    def new_file(self):
        self.gui.txt.delete('0.0',END)
        self.used=True
        self.file=None
        self.gui.root.title("New File")
        self.gui.txt.config(state="normal",bg="white")
    def Debug(self,*event):
        self.met.Debug(self.file)
    def Execute_to_exe(self,*event):
        self.met.execute_exe(self.file)
    def Execute_to_pyc(self,*event):
        self.met.execute_pyc(self.file)
    def save_file(self):
        if self.file is None:
            filename = tkinter.filedialog.asksaveasfilename()
            f=open(filename,mode='a')
            f.close()
            d=open(filename,mode='w')
            d.write(str(self.gui.txt.get("0.0",END)))
            self.file=filename
            self.gui.root.title(self.file)
        else:
            filename=self.file
            f=open(filename,mode='a')
            f.close()
            d=open(filename,mode='w')
            d.write(str(self.gui.txt.get("0.0",END)))
            self.file=filename
            self.gui.root.title(self.file)
            
    def save_as_file(self):
            filename = tkinter.filedialog.asksaveasfilename()
            f=open(filename,mode='a')
            f.close()
            d=open(filename,mode='w')
            d.write(str(self.gui.txt.get("0.0",END)))
            self.file=filename
            self.gui.root.title(self.file)
        
    def open_file(self):
        try:
            self.gui.txt.delete('0.0',END)
            filename=tkinter.filedialog.askopenfilename()
            if filename is not None:
                f=open(filename,mode='r')
                text=f.read()
                f.close()
                self.file=filename
                self.gui.root.title(filename)
                self.gui.txt.config(state="normal",bg="white")
                self.gui.txt.insert(END,str(text))
                self.mark_key_words()
            else:
                None
        except:
            print("Falls eine Datei ausgewählt wurde, konnte diese nicht geöfnet werden")

    def select_all(self,event):
        self.gui.txt.tag_add(SEL, "1.0", END)
        self.gui.txt.mark_set(INSERT,"1.0")
        self.gui.txt.see(INSERT)
    def delete_some(self,event):
        self.gui.txt.delete("sel.first","sel.last")

    def Copy(self,*event):
        self.gui.txt.event_generate('<<Copy>>')

    def Cut(self,*event):
        self.gui.txt.event_generate('<<Cut>>')

    def Paste(self,*event):
        self.gui.txt.event_generate('<<Paste>>')

    def Undo(self,*event):
        self.gui.txt.event_generate('<<Undo>>')

    def Redo(self,*event):
        self.gui.txt.event_generate('<<Redo>>')

    def Help(self):
        try:
            tkinter.messagebox.showinfo("Abaut","Programmed by Marcin Chere")
        except:
            None
    def find(self):
        text=str(self.gui.txt.get("0.0",END))
        point=0
        finder=find(text)
        finder.root.mainloop()
        Korr=finder.CORR
        worte=self.gui.txt.get("0.0",END)
        worte_gesplitet=worte.split(' ')
        for z in Korr:
            self.gui.txt.tag_add(SEL,str(float(z)),str(float(len(worte_gesplitet[z])+z)))
            self.gui.txt.mark_set(INSERT, str(float(z)))
            self.gui.txt.see(INSERT)

class methods:
    def __init__(self):
        None
    def execute_pyc(self,file):
        try:
            py_compile.compile(file)
        except:
            print("Fail")
    def execute_exe(self,filename):
        None
    def Debug(self,file):
        subprocess.call("py "+file)
    def destroy(self):
        exit()

def main():
    methoden=methods()
    Oberfläche=Gui()
    editor=Pyedit(Oberfläche,methoden)
    editor.start_gui()
class StatusBar(tkinter.Frame):   
    def __init__(self, master):
        tkinter.Frame.__init__(self, master)
        self.variable=tkinter.StringVar()  
        self.label=tkinter.Label(self, bd=1, anchor=tkinter.W,
                           textvariable=self.variable)
        self.label.grid(row=0,column=0,columnspan=2,sticky=tkinter.EW)
        self.variable.set("it's "+str(now.strftime("%A"))+" the "+str(now.month)+" of "+str(now.strftime("%B"))+ "  ["+str(now.year)+"]        "+str(now.hour)+":"+str(now.minute))
        self.label.pack(fill=tkinter.X)
        self.pack()
    def set_text(self,text):
        self.variable.set(text)
class Gui:
    def __init__(self):
        self.met=methods
        self.root=None
        self.menu = None
        self.filemenu = None
        self.editmenu = None
        self.viewmenu = None
        self.syntaxmenu= None
        self.formatmenu= None
        self.projectmenu=None
        self.helpmenu=None
        self.txt=None
        self.scrollbar=None
        self.toolmenu=None
        self.toolbar=None
        self.statusbar=None
        self.Tabs={}
        self.tabs_Buttons=None
        self.tabs_len=0
        self.current_tab=0
        self.console=None
    def start(self):
        self.new_image_data="""
        """
        self.met=methods
        self.root=Tk()
        self.root.title("PyEdit++")
        self.root.geometry("1000x800")
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)
        self.toolbar= Frame(self.root, bd=1, relief=RAISED,height=50)
        self.toolbar.grid(row=1,column=0)
        self.toolbar.pack(side=TOP, fill=X)
        self.filemenu = Menu(self.menu)
        self.editmenu = Menu(self.menu)
        self.viewmenu = Menu(self.menu)
        self.syntaxmenu= Menu(self.menu)
        self.formatmenu= Menu(self.menu)
        self.projectmenu=Menu(self.menu)
        self.toolmenu=Menu(self.menu)
        self.helpmenu=Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.filemenu)
        self.menu.add_cascade(label="edit",menu=self.editmenu)
        self.menu.add_cascade(label="view",menu=self.viewmenu)
        self.menu.add_cascade(label="Syntax",menu=self.syntaxmenu)
        self.menu.add_cascade(label="Format",menu=self.formatmenu)
        self.menu.add_cascade(label="Project",menu=self.projectmenu)
        self.menu.add_cascade(label="Tool",menu=self.toolmenu)
        self.menu.add_cascade(label="help",menu=self.helpmenu)
        self.txt=Text(self.root)
        self.scrollbar=Scrollbar(self.root)
        self.scrollbar.pack(side=RIGHT,fill='y')
        self.txt.config(yscrollcommand=self.scrollbar.set,font=("Purisa",12))
        self.scrollbar.config(command=self.txt.yview)
        self.console=Text(self.root,height=10)
        self.console.pack(side=BOTTOM,fill=tkinter.X)
        self.console.config(fg="blue",bg="white",font=("Purisa",13))
        self.txt.pack(fill="both",expand=True)
        self.statusbar=StatusBar(self.root)
    def Loop(self):
        self.root.mainloop()
        
    def destroy(self):
        exit()

#start of the Programm
#try:
if len(sys.argv)<2:
    main()
else:
    print(sys.argv[1])
#except:
    tkinter.messagebox.showinfo("Fehler","Das durfte nicht passieren, es tut uns leid")
#*********************
