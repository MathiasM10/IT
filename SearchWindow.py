from tkinter import *

def Return_Event(event):
    SearchWord=Txt1.get()
    print(SearchWord)

def Search_Engine():
    pass

SearchWindow = Tk()
Txt1=Entry(master=SearchWindow, bg='white')
SearchWindow.geometry('0x0+0+0')
Txt1.pack()
SearchWindow.bind_all('<Return>', Return_Event)
Txt1.focus_set()
SearchWindow.mainloop()
