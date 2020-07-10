from tkinter import *

bodyfont = ('times', 15)


def err(code, error):
    def stop():
        errortk.destroy()
        return
    errortk = Toplevel()
    errortk.title("Bazaar Flipping v1.0 -Error " + str(code))
    errortk.geometry("1000x200")
    ce = Canvas(errortk, width=1000, height=200)
    ce.pack(side='top', fill='both', expand='yes')
    errortk.resizable(0, 0)

    img = PhotoImage(file="S.gif")

    ce.create_image(40, 75, image=img, anchor='nw')
    ce.create_text(250, 50, text="There is an error with " + error, fill="Black", anchor='nw', font=('times', 20, 'bold'))
    ce.create_image(885, 75, image=img, anchor='nw')
    b1 = Button(errortk, text="Continue", command=stop, width=20, font=bodyfont, borderwidth=0, background="white", cursor="hand2", highlightbackground="blue", relief="sunken")
    ce.create_window(480, 100, window=b1)

    errortk.mainloop()
