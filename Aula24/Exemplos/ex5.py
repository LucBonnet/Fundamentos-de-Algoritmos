from tkinter import *
from tkinter import Menu

window = Tk()
window.title('Algoritmos')
# cria o objeto menu na janela window
menu = Menu(window)

def click():
  new_window = Tk()
  new_window.title("Nova janela")
  new_window.geometry('150x150')
  label = Label(new_window, text="Janela Nova")
  label.grid(column=0, row=0)
  new_window.mainloop()

# cria menu com nome new_item
new_item = Menu(menu)

# cria um item do menu
menu.add_cascade(label='File', menu=new_item)

# cria subitems do item
new_item.add_command(label="New", command=click)
new_item.add_separator()
new_item.add_command(label="Edit")

window.configure(menu=menu)
window.mainloop()