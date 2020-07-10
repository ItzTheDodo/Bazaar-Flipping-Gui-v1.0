from Conn import *
from tkinter import *
import urllib.request
import json
import webbrowser

headerfont = ('times', 40, 'bold', 'underline')
bodyfont = ('times', 15)
smallfont = ('times', 8)


def stop():
    global root
    root.destroy()


def txt():
    global product_info
    name = "Bazzar-API.txt"
    f = open(name, "w")
    f.write(str(product_info) + "\n\n\n")
    webbrowser.open(name)


def reload(productid):
    root.destroy()
    out(productid)


def out(productid):
    global root
    global product_info

    response = urllib.request.urlopen(str(Important_URLS[0]) + productid)
    result = json.loads(response.read())
    response.close()

    product_info = result["product_info"]
    buy_summ = product_info["buy_summary"]
    sell_summ = product_info["sell_summary"]
    q_s = product_info["quick_status"]

    bp = q_s["buyPrice"]
    sp = q_s["sellPrice"]
    sv = q_s["sellVolume"]
    bv = q_s["buyVolume"]
    so = q_s["sellOrders"]
    bo = q_s["buyOrders"]

    root = Tk()
    root.title("Bazzar Flipping v1.0 -Stocks -Output")
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

    cv.create_text(100, 200, text="- Buy-Price: " + str(bp), fill="White", anchor='nw', font=bodyfont)
    cv.create_text(100, 250, text="- Sell-Price: " + str(sp), fill="White", anchor='nw', font=bodyfont)
    cv.create_text(100, 300, text="- Buy-Volume: " + str(bv), fill="White", anchor='nw', font=bodyfont)
    cv.create_text(100, 350, text="- Sell-Volume: " + str(sv), fill="White", anchor='nw', font=bodyfont)
    cv.create_text(100, 400, text="- Buy-Orders: " + str(bo), fill="White", anchor='nw', font=bodyfont)
    cv.create_text(100, 450, text="- Sell-Orders: " + str(so), fill="White", anchor='nw', font=bodyfont)

    cv.create_text(530, 220, text="Latest Buy-Summary: ", fill="White", anchor='nw', font=bodyfont)
    cv.create_text(545, 245, text="- Amount: " + str(buy_summ[1]["amount"]), fill="White", anchor='nw', font=bodyfont)
    cv.create_text(545, 270, text="- pPU: " + str(buy_summ[1]["pricePerUnit"]), fill="White", anchor='nw', font=bodyfont)
    cv.create_text(545, 295, text="- Orders: " + str(buy_summ[1]["orders"]), fill="White", anchor='nw', font=bodyfont)

    cv.create_text(530, 345, text="Latest Sell-Summary: ", fill="White", anchor='nw', font=bodyfont)
    cv.create_text(545, 370, text="- Amount: " + str(sell_summ[1]["amount"]), fill="White", anchor='nw', font=bodyfont)
    cv.create_text(545, 394, text="- pPU: " + str(sell_summ[1]["pricePerUnit"]), fill="White", anchor='nw', font=bodyfont)
    cv.create_text(545, 420, text="- Orders: " + str(sell_summ[1]["orders"]), fill="White", anchor='nw', font=bodyfont)

    b1 = Button(root, text="Quit", command=stop, width=10, font=bodyfont, borderwidth=0, background="white", cursor="hand2", highlightbackground="blue", relief="sunken")
    cv.create_window(820, 470, window=b1)

    b2 = Button(root, text="Send to Txt", command=txt, width=10, font=bodyfont, borderwidth=0, background="white", cursor="hand2", highlightbackground="blue", relief="sunken")
    cv.create_window(820, 415, window=b2)

    b3 = Button(root, text="Reload", command=lambda: reload(productid), width=10, font=bodyfont, borderwidth=0, background="white", cursor="hand2", highlightbackground="blue", relief="sunken")
    cv.create_window(820, 360, window=b3)

    root.mainloop()
