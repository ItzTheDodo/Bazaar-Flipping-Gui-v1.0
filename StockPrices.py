from tkinter import *
from Conn import *
from err import err
from Output import out
import urllib.request
import json

if __name__ == "__main__":
    exit(-1)

response = urllib.request.urlopen(str(Important_URLS[1]))
result = json.loads(response.read())
response.close()

backup = result

option = None
headerfont = ('times', 40, 'bold', 'underline')
bodyfont = ('times', 15)
smallfont = ('times', 8)
products = []
enchanted = []
non = []
root = ""
use = False


def search():
    global root
    root.destroy()

    def go():
        global products
        global enchanted
        global non
        global use

        li = []
        i = False
        query = text.get().upper()
        for e in backup["productIds"]:
            if str(e).__contains__(query):
                li.append(str(e))
                i = True

        if i is False:
            err(-1, "your search")
            return

        products = li
        enchanted.clear()
        non.clear()

        for i in products:
            if str(i).__contains__("ENCHANTED"):
                enchanted.append(i)
            else:
                non.append(i)

        s.destroy()
        use = True
        start()

    s = Tk()
    s.title("Bazzar Flipping v1.0 -Stocks -Search")
    s.geometry("%dx%d+50+30" % (720, 350))
    c = Canvas(s, width=720, height=350)
    c.pack(side='top', fill='both', expand='yes')
    s.configure(bg="white")
    s.resizable(0, 0)

    c.create_text(295, 30, text="Search", fill="Black", anchor='nw', font=headerfont)
    text = Entry(s, bg="white")
    c.create_window(370, 175, window=text, width=300)
    c.create_text(290, 190, text="E.G: ENCHANTED_BLAZE_ROD", fill="Black", anchor='nw', font=smallfont)

    b1 = Button(s, text="Go", command=go, width=20, font=bodyfont, borderwidth=0, background="white", cursor="hand2", highlightbackground="blue", relief="sunken")
    c.create_window(360, 300, window=b1)

    c.create_window()

    s.mainloop()


def get():
    global option
    return option.get()


def prep():
    global root

    if get() == "None":
        return
    root.destroy()
    out(get())


def start():
    global option
    global products
    global enchanted
    global non
    global root
    global use

    root = Tk()
    root.title("Bazzar Flipping v1.0 -Stocks")
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

    if use is False:
        resp = urllib.request.urlopen(str(Important_URLS[1]))
        res = json.loads(resp.read())
        resp.close()

        products = res["productIds"]
        enchanted = []
        non = []
        option = StringVar(root)
        option.set("None")

        for i in products:
            if str(i).__contains__("ENCHANTED"):
                enchanted.append(i)
            else:
                non.append(i)

        use = True

    if not enchanted == []:
        cv.create_text(290, 270, text="Enchanted", fill="White", anchor='nw', font=bodyfont)
        drop1 = OptionMenu(root, option, *enchanted)
        drop1.place(x=300, y=300)

    if not non == []:
        cv.create_text(535, 270, text="Normal", fill="White", anchor='nw', font=bodyfont)
        drop2 = OptionMenu(root, option, *non)
        drop2.place(x=535, y=300)

    b1 = Button(root, text="Next", command=prep, width=20, font=bodyfont, borderwidth=0, background="white", cursor="hand2", highlightbackground="blue", relief="sunken")
    cv.create_window(450, 450, window=b1)

    b2 = Button(root, text="Search", command=search, width=10, font=bodyfont, borderwidth=0, background="white", cursor="hand2", highlightbackground="blue", relief="sunken")
    cv.create_window(75, 475, window=b2)

    root.mainloop()
