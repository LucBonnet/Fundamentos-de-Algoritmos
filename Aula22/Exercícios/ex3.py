# Faça uma calculadora com as 4 operações básicas, 
# potência, sen, cos, tan, log e raiz quadrada.

from tkinter import *
import math

window = Tk()
window.geometry('370x300')
window.title('Calculadora')

txt_display = Entry(window, font=("Arial Black", 14), width=27)
txt_display.place(x=10, y=20)

def btn_num(num):
  v = txt_display.get()
  v += num
  txt_display.delete(0, END)
  txt_display.insert(0, v)

def btn_op(op):
  v = txt_display.get()
  if not len(v) == 0 or op == '-':
    if op == '-':
      v += op
    elif v[len(v)-1].isnumeric():
      v += op
  txt_display.delete(0, END)
  txt_display.insert(0, v)

def sen():
  btn_igual()
  v = txt_display.get()
  if v == '':
    return
  txt_display.delete(0, END)
  txt_display.insert(0, math.sin(float(v)))

def cos():
  btn_igual()
  v = txt_display.get()
  if v == '':
    return
  txt_display.delete(0, END)
  txt_display.insert(0, math.cos(float(v)))

def tan():
  btn_igual()
  v = txt_display.get()
  if v == '':
    return
  txt_display.delete(0, END)
  txt_display.insert(0, math.tan(float(v)))
 
def log():
  btn_igual()
  v = txt_display.get()
  if v == '':
    return
  txt_display.delete(0, END)
  txt_display.insert(0, math.log(float(v)))
  
def raiz():
  btn_igual()
  v = txt_display.get()
  if v == '':
    return
  txt_display.delete(0, END)
  txt_display.insert(0, math.sqrt(float(v)))

def clear():
  txt_display.delete(0, END)

def btn_igual():
  exp = txt_display.get()
  if exp == '':
    return 
  resul = eval(exp)
  clear()
  txt_display.insert(0, resul)

btn7 = Button(window, text='7', width=3, height=0, font=('Arial Black', 14), command=lambda: btn_num('7'))
btn8 = Button(window, text='8', width=3, height=0, font=('Arial Black', 14), command=lambda: btn_num('8'))
btn9 = Button(window, text='9', width=3, height=0, font=('Arial Black', 14), command=lambda: btn_num('9'))
btn4 = Button(window, text='4', width=3, height=0, font=('Arial Black', 14), command=lambda: btn_num('4'))
btn5 = Button(window, text='5', width=3, height=0, font=('Arial Black', 14), command=lambda: btn_num('5'))
btn6 = Button(window, text='6', width=3, height=0, font=('Arial Black', 14), command=lambda: btn_num('6'))
btn1 = Button(window, text='1', width=3, height=0, font=('Arial Black', 14), command=lambda: btn_num('1'))
btn2 = Button(window, text='2', width=3, height=0, font=('Arial Black', 14), command=lambda: btn_num('2'))
btn3 = Button(window, text='3', width=3, height=0, font=('Arial Black', 14), command=lambda: btn_num('3'))
btn0 = Button(window, text='0', width=3, height=0, font=('Arial Black', 14), command=lambda: btn_num('0'))
btnPonto = Button(window, text='.', width=3, height=0, font=('Arial Black', 14), command=lambda: btn_op('.'))

btnSoma =  Button(window, text='+', width=3, height=0, font=('Arial Black', 14), command=lambda: btn_op('+'))
btnSub  =  Button(window, text='-', width=3, height=0, font=('Arial Black', 14), command=lambda: btn_op('-'))
btnMult =  Button(window, text='x', width=3, height=0, font=('Arial Black', 14), command=lambda: btn_op('*'))
btnDiv  =  Button(window, text='/', width=3, height=0, font=('Arial Black', 14), command=lambda: btn_op('/'))
btnSen  =  Button(window, text='sen', width=3, height=0, font=('Arial Black', 14), command=sen)
btnCos  =  Button(window, text='cos', width=3, height=0, font=('Arial Black', 14), command=cos)
btnTan  =  Button(window, text='tan', width=3, height=0, font=('Arial Black', 14), command=tan)
btnLog  =  Button(window, text='log', width=3, height=0, font=('Arial Black', 14), command=log)
btnPot  =  Button(window, text='^', width=3, height=0, font=('Arial Black', 14), command=lambda: btn_op('**'))
btnRaiz =  Button(window, text='√', width=3, height=0, font=('Arial Black', 14), command=raiz)

btnIgual = Button(window, text='=', width=3, height=0, font=('Arial Black', 14), command=btn_igual)
btnC     = Button(window, text='C', width=8, height=0, font=('Arial Black', 14), command=clear)

btn7.place(x=10 + 60 * 0, y=60 + 60 * 0)
btn8.place(x=10 + 60 * 1, y=60 + 60 * 0)
btn9.place(x=10 + 60 * 2, y=60 + 60 * 0)
btnSoma.place(x=10 + 60 * 3, y= 60 + 60 * 0)
btnC.place(x=10 + 60 * 4, y=60)
btn4.place(x=10 + 60 * 0, y=60 + 60 * 1)
btn5.place(x=10 + 60 * 1, y=60 + 60 * 1)
btn6.place(x=10 + 60 * 2, y=60 + 60 * 1)
btnSub.place(x=10 + 60 * 3, y= 60 + 60 * 1)
btnSen.place(x=10 + 60 * 4, y= 60 + 60 * 1)
btnCos.place(x=10 + 60 * 5, y= 60 + 60 * 1)
btn1.place(x=10 + 60 * 0, y=60 + 60 * 2)
btn2.place(x=10 + 60 * 1, y=60 + 60 * 2)
btn3.place(x=10 + 60 * 2, y=60 + 60 * 2)
btnMult.place(x=10 + 60 * 3, y= 60 + 60 * 2)
btnTan.place(x=10 + 60 * 4, y= 60 + 60 * 2)
btnLog.place(x=10 + 60 * 5, y= 60 + 60 * 2)
btnIgual.place(   x = 10, y=60 + 60 * 3)
btn0.place(x=10 + 60 * 1, y=60 + 60 * 3)
btnPonto.place(x=10 + 60 * 2, y=60 + 60 * 3)
btnDiv.place(x=10 + 60 * 3, y= 60 + 60 * 3)
btnPot.place(x=10 + 60 * 4, y= 60 + 60 * 3)
btnRaiz.place(x=10 + 60 * 5, y= 60 + 60 * 3)

window.mainloop()