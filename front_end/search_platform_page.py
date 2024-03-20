from tkinter import *
from tkinter import messagebox
import webbrowser

from back_end.quick_search import get_links

def search_platform_display(menu, background):

    # URL Functions
    def erase_urls():
        amazon_entry.delete(0, END)
        jumia_entry.delete(0, END)
        hepsiburada_entry.delete(0, END)
        alibaba_entry.delete(0, END)
        flipkart_entry.delete(0, END)

    def fill_urls(links: dict):
        amazon_entry.insert(0, links['amazon'])
        jumia_entry.insert(0, links['jumia'])
        hepsiburada_entry.insert(0, links['hepsiburada'])
        alibaba_entry.insert(0, links['alibaba'])
        flipkart_entry.insert(0, links['flipkart'])

    def bind_entries(links: dict):
        amazon_entry.bind("<Button-1>", lambda e: callback(links['amazon']))
        jumia_entry.bind("<Button-1>", lambda e: callback(links['jumia']))
        hepsiburada_entry.bind("<Button-1>", lambda e: callback(links['hepsiburada']))
        alibaba_entry.bind("<Button-1>", lambda e: callback(links['alibaba']))
        flipkart_entry.bind("<Button-1>", lambda e: callback(links['flipkart']))

    def callback(url):
        webbrowser.open_new_tab(url)

    def open_all_links():
        webbrowser.open_new_tab(amazon_entry.get())
        webbrowser.open_new_tab(jumia_entry.get())
        webbrowser.open_new_tab(hepsiburada_entry.get())
        webbrowser.open_new_tab(alibaba_entry.get())
        webbrowser.open_new_tab(flipkart_entry.get())


    def button_clicked(event=0):
        searched_model = search_entry.get()
        if searched_model == "":
            messagebox.showerror("Error", message="Enter A Mobile Name and Model To Search For")
            erase_urls()
        else:
            erase_urls()
            messagebox.showinfo("Info", message="Proceed by pressing okay")
            website_links = get_links(search_entry.get())
            fill_urls(website_links)
            bind_entries(website_links)

# Background for page
    frame_search_platforms = Frame(menu, width=850, height=550)
    main_bg_label = Label(frame_search_platforms, image=background)
    main_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Search bar
    search_label = Label(frame_search_platforms, text="Product Name:", font=("Helvetica bold", 14), bg='#fff')
    search_entry = Entry(frame_search_platforms, width=32)
    search_entry.bind('<Return>', button_clicked)
    search_button = Button(frame_search_platforms, text='Search', command=button_clicked, pady=2, bg='#f96d00')

    search_label.place(x=320, y=151)
    search_entry.place(x=445, y=150)
    search_button.place(x=750, y=149)

# Websites
    amazon_label = Label(frame_search_platforms, text="Amazon Link:", bg="#fff")
    amazon_label.place(x=320, y=225)
    amazon_entry = Entry(frame_search_platforms, width=40, fg="#0a5ef2")
    amazon_entry.place(x=445, y=224)

    jumia_label = Label(frame_search_platforms, text="Jumia Link:", bg="#fff")
    jumia_label.place(x=320, y=265)
    jumia_entry = Entry(frame_search_platforms, width=40, fg="#0a5ef2")
    jumia_entry.place(x=445, y=264)

    hepsiburada_label = Label(frame_search_platforms, text="Hepsiburada Link:", bg="#fff")
    hepsiburada_label.place(x=320, y=305)
    hepsiburada_entry = Entry(frame_search_platforms, width=40, fg="#0a5ef2")
    hepsiburada_entry.place(x=445, y=304)

    alibaba_label = Label(frame_search_platforms, text="Alibaba Link:", bg="#fff")
    alibaba_label.place(x=320, y=345)
    alibaba_entry = Entry(frame_search_platforms, width=40, fg="#0a5ef2")
    alibaba_entry.place(x=445, y=344)

    flipkart_label = Label(frame_search_platforms, text="Flipkart Link:", bg="#fff")
    flipkart_label.place(x=320, y=385)
    flipkart_entry= Entry(frame_search_platforms, width=40, fg="#0a5ef2")
    flipkart_entry.place(x=445, y=384)

    open_all_button = Button(frame_search_platforms, text="OPEN ALL LINKS AT ONCE", command=open_all_links, width= 52, pady=2,bg="#f96d00")
    open_all_button.place(x=400, y=430)

    return frame_search_platforms
