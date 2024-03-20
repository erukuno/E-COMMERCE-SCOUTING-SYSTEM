from tkinter import *
from tkinter import messagebox
import webbrowser

from back_end.cheapest_price import best_price_sorted_list

def cheapest_price_display(menu, background):

    def erase_all_fields():
        best_price_entry.delete(0, END)
        from_website_entry.delete(0, END)
        product_name_entry.delete(0, END)
        product_link_entry.delete(0, END)
        jumia_entry.delete(0, END)
        jumia_name.delete(0, END)
        flipkart_entry.delete(0, END)
        flipkart_name.delete(0, END)
        alibaba_entry.delete(0, END)
        alibaba_name.delete(0, END)
        amazon_entry.delete(0, END)
        amazon_name.delete(0, END)

    def fill_best_product(liste: list):
        best_price_entry.insert(0, f"{liste[0]['Price']} $")
        from_website_entry.insert(0, liste[0]['Website'])
        product_name_entry.insert(0, liste[0]['Name'])
        product_link_entry.insert(0, liste[0]['Link'])

    def fill_price_name_fields(liste: list):
        sort_alphabetic = sorted(liste, key=lambda x: x['Website'])
        jumia_entry.insert(0, f"{sort_alphabetic[0]['Price']} $")
        jumia_name.insert(0, sort_alphabetic[0]['Name'])
        flipkart_entry.insert(0, f"{sort_alphabetic[1]['Price']} $")
        flipkart_name.insert(0, sort_alphabetic[1]['Name'])
        alibaba_entry.insert(0, f"{sort_alphabetic[2]['Price']} $")
        alibaba_name.insert(0, sort_alphabetic[2]['Name'])
        amazon_entry.insert(0, f"{sort_alphabetic[3]['Price']} $")
        amazon_name.insert(0, sort_alphabetic[3]['Name'])

    def bind_entries(liste: list):
        sort_alphabetic = sorted(liste, key=lambda x: x['Website'])
        jumia_name.bind("<Button-1>", lambda e: callback(sort_alphabetic[0]['Link']))
        flipkart_name.bind("<Button-1>", lambda e: callback(sort_alphabetic[1]['Link']))
        alibaba_name.bind("<Button-1>", lambda e: callback(sort_alphabetic[2]['Link']))
        amazon_name.bind("<Button-1>", lambda e: callback(sort_alphabetic[3]['Link']))

    def callback(url):
        webbrowser.open_new_tab(url)

    def button_clicked(event=0):
        searched_model = search_entry.get().replace(' ', '%20')
        if searched_model == "":
            messagebox.showerror("Error", message="Enter A Mobile Model To Search For")
            erase_all_fields()
        else:
            erase_all_fields()
            sorted_list = best_price_sorted_list(searched_model)
            if sorted_list:
                messagebox.showinfo("Info", message=f"Best price is {sorted_list[0]['Price']} US "
                                                    f"from {sorted_list[0]['Website']}!")
                fill_best_product(sorted_list)
                fill_price_name_fields(sorted_list)
                bind_entries(sorted_list)
                product_link_entry.bind("<Button-1>", lambda e: callback(product_link_entry.get()))
            else:
                messagebox.showerror("Error", message="No data available")

    frame_cheapest_price = Frame(menu, width=850, height=550)
    main_bg_label = Label(frame_cheapest_price, image=background)
    main_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    entry_list = []

    search_label = Label(frame_cheapest_price, text="Mobile Model:", font=("Helvetica bold", 14), bg='#fff')
    search_entry = Entry(frame_cheapest_price, width=32)
    search_button = Button(frame_cheapest_price, text='Compare', command=button_clicked, pady=2, bg="#F96D00")

    entry_list.extend([search_entry, search_button])

    search_entry.bind('<Return>', button_clicked)
    search_label.place(x=320, y=151)
    search_entry.place(x=435, y=150)
    search_button.place(x=740, y=149)

    best_price_label = Label(frame_cheapest_price, text="Best Price:", font=("Helvetica bold", 14), bg="#fff")
    best_price_label.place(x=320, y=226)
    best_price_entry = Entry(frame_cheapest_price, width=10, fg="#0a5ef2", font=("Helvetica bold", 14), justify=CENTER)
    best_price_entry.place(x=435, y=224)

    from_website_label = Label(frame_cheapest_price, text="From Where:", font=("Helvetica bold", 14), bg="#fff")
    from_website_label.place(x=320, y=256)
    from_website_entry = Entry(frame_cheapest_price, width=11, fg="#0a5ef2", font=("Helvetica bold", 14),
                               justify=CENTER)
    from_website_entry.place(x=435, y=254)

    product_name_entry = Entry(frame_cheapest_price, width=32)
    product_name_entry.place(x=540, y=254)

    product_link_label = Label(frame_cheapest_price, text="Product Link:", font=("Helvetica bold", 14), bg="#fff")
    product_link_label.place(x=320, y=286)
    product_link_entry = Entry(frame_cheapest_price, width=43, fg="#0a5ef2")
    product_link_entry.place(x=435, y=284)

    entry_list.extend([best_price_entry, from_website_entry, product_name_entry, product_link_entry])

    jumia_label = Label(frame_cheapest_price, text="Jumia:", font=("Helvetica bold", 14), bg="#fff")
    jumia_label.place(x=320, y=350)
    jumia_entry = Entry(frame_cheapest_price, width=10, justify=CENTER)
    jumia_entry.place(x=435, y=350)
    jumia_name = Entry(frame_cheapest_price, width=31)
    jumia_name.place(x=540, y=350)

    flipkart_label = Label(frame_cheapest_price, text="flipkart:", font=("Helvetica bold", 14), bg="#fff")
    flipkart_label.place(x=320, y=380)
    flipkart_entry = Entry(frame_cheapest_price, width=10, justify=CENTER)
    flipkart_entry.place(x=435, y=380)
    flipkart_name = Entry(frame_cheapest_price, width=31)
    flipkart_name.place(x=540, y=380)

    alibaba_label = Label(frame_cheapest_price, text="Alibaba:", font=("Helvetica bold", 14), bg="#fff")
    alibaba_label.place(x=320, y=410)
    alibaba_entry = Entry(frame_cheapest_price, width=10, justify=CENTER)
    alibaba_entry.place(x=435, y=410)
    alibaba_name = Entry(frame_cheapest_price, width=31)
    alibaba_name.place(x=540, y=410)

    amazon_label = Label(frame_cheapest_price, text="Amazon:", font=("Helvetica bold", 14), bg="#fff")
    amazon_label.place(x=320, y=440)
    amazon_entry = Entry(frame_cheapest_price, width=10, justify=CENTER)
    amazon_entry.place(x=435, y=440)
    amazon_name = Entry(frame_cheapest_price, width=31)
    amazon_name.place(x=540, y=440)

    entry_list.extend([jumia_entry, jumia_name, flipkart_entry, flipkart_name,
                       alibaba_entry, alibaba_name, amazon_entry, amazon_name])

    return frame_cheapest_price
