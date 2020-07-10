from tkinter import *
from StockPrices import start
from Conn import *
import webbrowser

headerfont = ('times', 40, 'bold', 'underline')
bodyfont = ('times', 15)
smallfont = ('times', 8)


def website():
    webbrowser.open(Important_URLS[2])


def info():
    webbrowser.open(Important_URLS[3])


def startStocks():
    root.destroy()
    start()


root = Tk()
root.title("Bazzar Flipping v1.0 -Main")
fname = "bgimg.gif"
background_image = PhotoImage(file=fname)
w = background_image.width()
h = background_image.height()
root.geometry("%dx%d+50+30" % (w, h))
cv = Canvas(root, width=w, height=h)
cv.pack(side='top', fill='both', expand='yes')
cv.create_image(0, 0, image=background_image, anchor='nw')
cv.create_image(0, 0, image=background_image, anchor='nw')
root.resizable(0, 0)

img = PhotoImage(file="banner.gif")
cv.create_image(190, 30, image=img, anchor='nw')

b1 = Button(root, text="Get Stocks", command=startStocks, width=20, height=3,  font=bodyfont, borderwidth=0, background="white", cursor="hand2", highlightbackground="blue", relief="sunken")
cv.create_window(450, 325, window=b1)

b2 = Button(root, text="Website", command=website, width=10,  font=bodyfont, borderwidth=0, background="white", cursor="hand2", highlightbackground="blue", relief="sunken")
cv.create_window(70, 475, window=b2)

b3 = Button(root, text="Info", command=info, width=10,  font=bodyfont, borderwidth=0, background="white", cursor="hand2", highlightbackground="blue", relief="sunken")
cv.create_window(70, 425, window=b3)

root.mainloop()
