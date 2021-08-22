from tkinter import*
from tkinter import messagebox







#create window
window=Tk()
window.title('GUI bancker')  # window title
window.grid()  # make window visible
window.geometry('800*800')  # window size

# create name label and entry

name_label=Label(window,text="Имя",font=("Arial",25))
name_label.grid(column=0,row=0)









window.mainloop()
