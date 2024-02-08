from tkinter import *

ventana = Tk()
ventana.title("Zonas-A00573792")
ventana.geometry("500x500")


def fnsur():
  km = float(entkm.get())
  sub = 7 * km
  if sub >= 70:
    adi = km * .04
    total = sub + adi
    lblt2.config(text=total, bg="red", fg="white")
  else:
    total = sub
    adi = 0
    lblt2.config(text=total, bg="green", fg="black")
  lbls2.config(text=sub)
  lbla2.config(text=adi)


def fncentro():
  km = float(entkm.get())
  sub = 5 * km
  if sub >= 60:
    adi = km * .06
    total = sub + adi
    lblt2.config(text=total, bg="red", fg="white")
  else:
    total = sub
    adi = 0
    lblt2.config(text=total, bg="green", fg="black")
  lbls2.config(text=sub)
  lbla2.config(text=adi)


def fnnorte():
  km = float(entkm.get())
  sub = 12 * km
  if sub >= 180:
    adi = km * .10
    total = sub + adi
    lblt2.config(text=total, bg="red", fg="white")
  else:
    total = sub
    adi = 0
    lblt2.config(text=total, bg="green", fg="black")
  lbls2.config(text=sub)
  lbla2.config(text=adi)


lblkm = Label(text="Km recorridos")
lblkm.place(x=100, y=50)

lbls = Label(text="Subtotal")
lbls.place(x=100, y=100)

lbla = Label(text="Adicional")
lbla.place(x=100, y=150)

lblt = Label(text="TOTAL")
lblt.place(x=100, y=200)

entkm = Entry()
entkm.place(x=200, y=50)

lbls2 = Label(text="---", )
lbls2.place(x=200, y=100)

lbla2 = Label(text="---")
lbla2.place(x=200, y=150)

lblt2 = Label(text="---")
lblt2.place(x=200, y=200)

btns = Button(text="Sur", command=fnsur)
btns.place(x=100, y=450)

btnc = Button(text="Centro", command=fncentro)
btnc.place(x=200, y=450)

btnn = Button(text="Norte", command=fnnorte)
btnn.place(x=300, y=450)

mainloop()
