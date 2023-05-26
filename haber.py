import feedparser
from tkinter import *
import webview
from datetime import datetime



def default_color_button():
    btn_sondakika.configure(bg="lightblue")
    btn_dünya.configure(bg="lightblue")
    btn_ekonomi.configure(bg="lightblue")
    btn_sağlık.configure(bg="lightblue")


def clear_frame():
    for widget in fr_haberler.winfo_children():
        widget.destroy()


def open_url(event):
    webview.create_window(event.widget.cget("text"), event.widget.cget("text"))
    webview.start()
def add_haberler(haberler):  
    haber_count = 0       
    for haber in haberler.entries:
        haber_count = haber_count + 1
        if haber_count > 3:
            break
        Label(fr_haberler, text=haber.title, anchor="w", font=("Helveticabold, 14")).pack(side=TOP, fill="x")
        lbl_link = Label(fr_haberler, text=haber.link, anchor="w", font=("Helveticabold, 14"),fg="blue", cursor="hand2")
        lbl_link.pack(side=TOP, fill="x")
        lbl_link.bind("<Button-1>", open_url)
        Label(fr_haberler, text="-", anchor="c",bg="brown").pack(side=TOP, fill="x")


def son_dakika_command():
    clear_frame()
    default_color_button()
    btn_sondakika.configure(bg="blue")
    for url in son_dakika_url:
        haberler = feedparser.parse(url)
        add_haberler(haberler)

def dünya_command():
    clear_frame() 
    default_color_button()
    btn_dünya.configure(bg="blue")
    for url in dünya_url:
        haberler = feedparser.parse(url)
        add_haberler(haberler)
    
def ekonomi_command():
     clear_frame()
     default_color_button()
     btn_ekonomi.configure(bg="blue")
     for url in ekonomi_url:
        haberler = feedparser.parse(url)
        add_haberler(haberler)

def sağlık_command():
    clear_frame()
    default_color_button()
    btn_sağlık.configure(bg="blue")
    for url in sağlık_url:
        haberler = feedparser.parse(url)
        add_haberler(haberler)

son_dakika_url = ["https://www.milliyet.com.tr/rss/rssNew/SonDakikaRss.xml"
                 ,"https://www.ensonhaber.com/rss/ensonhaber.xml"
                 ,"https://www.cnnturk.com/feed/rss/all/news"
                 ,"https://www.sozcu.com.tr/rss/son-dakika.xml"]

dünya_url = ["https://www.milliyet.com.tr/rss/rssNew/dunyaRss.xml"
            ,"https://www.ensonhaber.com/rss/dunya.xml"
            ,"https://www.cnnturk.com/feed/rss/dunya/news"            
            ,"https://www.sozcu.com.tr/rss/dunya.xml"]

ekonomi_url = ["https://www.milliyet.com.tr/rss/rssNew/ekonomiRss.xml"
              ,"https://www.ensonhaber.com/rss/ekonomi.xml"
              ,"https://www.cnnturk.com/feed/rss/ekonomi/news"
              ,"https://www.sozcu.com.tr/rss/ekonomi.xml"]

sağlık_url = ["https://www.milliyet.com.tr/rss/rssNew/sagIikRss.xml"
             ,"https://www.ensonhaber.com/rss/saglik.xml"
             ,"https://www.cnnturk.com/feed/rss/saglik/news"
             ,"https://www.sozcu.com.tr/rss/saglik.xmI"]


window = Tk()
window.title("Haber Bot Programı")
window.geometry("1680x1050")

fr_haberler = Frame(window, height=1050)
fr_buttons = Button(window, relief=RAISED, bg="pink", bd=8)

btn_sondakika = Button(fr_buttons, text="Son Dakika", font=("Helvetica", 14), bg="lightblue", command=son_dakika_command)
btn_dünya = Button(fr_buttons, text="Dünya", font=("Helvetica", 14),bg="lightblue", command=dünya_command)
btn_ekonomi = Button(fr_buttons, text="Ekonomi", font=("Helvetica", 14),bg="lightblue", command=ekonomi_command)
btn_sağlık = Button(fr_buttons, text="Sağlık", font=("Helvetica", 14),bg="lightblue", command=sağlık_command)

btn_sondakika.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_dünya.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_ekonomi.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_sağlık.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
fr_haberler.grid(row=0, column=1, sticky="nsew")


window.mainloop()
