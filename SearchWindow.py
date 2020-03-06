from tkinter import *

def Return_Event(event):
    SearchWindow.destroy()


SearchWindow = Tk()
Txt1=Entry(master=SearchWindow, bg='lightgray')
#TODO Set Window pos to Top Left
# SearchWindow.geometry('0+0')
Txt1.pack()
SearchWindow.bind_all('<Return>', Return_Event)
Txt1.focus_set()
SearchWindow.mainloop()
