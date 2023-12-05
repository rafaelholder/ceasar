from tkinter import *
from tkinter import messagebox

#Create window
window = Tk()
window.title("Ceasar - Painel de acesso")
window.geometry('600x300')
window.resizable(width=False, height=False)
window.configure(background='green')

#IMG
ImgFile = 'functions\Login\\assets\logo.png'
logo = PhotoImage(ImgFile, height=50, width=50)

#WIDGETS
LeftFrame = Frame(window, width=200, height=300, bg='blue', relief='raise')
LeftFrame.pack(side='left')

RightFrame = Frame(window, width=395, height=300, bg='green', relief='raise')

LogoLabel = Label(LeftFrame, image=logo, bg='white')
LogoLabel.place(x=50, y=100)

#Mantendo a janela
window.mainloop()

