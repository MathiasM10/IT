import tkinter as tk

def Return_Event(event):
    print(event.keysym)
    print("ABC")

mw = tk.Tk()
mw.title('AIIT Cheat Engine')
mw.geometry('500x200+0+0')
mw.resizable(0, 0)
background=tk.Frame(master=mw, bg='lightgray')
background.pack_propagate(0)

#Widgets
Txt1=tk.Entry(master=mw,bg='white').grid(row=2,column=0)
Lab1=tk.Label(master=mw,text="Search:").grid(row=1,column=0)
mw.bind_all('<Return>', Return_Event)
mw.mainloop()