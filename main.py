from tkinter import *
from tkinter import ttk

from front_end.home_page import home_page_display
from front_end.search_platform_page import search_platform_display
from front_end.cheapest_price_page import cheapest_price_display


root = Tk()
root.title('Ecommerce Scouting system')
root.geometry("900x600+300+0")

# Background For Pages
main_page_bg = PhotoImage(file="img/bg/home_page_bg.png")
search_page_bg = PhotoImage(file="img/bg/Search_page_bg.png")
cheapest_page_bg = PhotoImage(file="img/bg/Cheapest_page_bg.png")


# SETTING TAB MENU
menu_bar = ttk.Notebook(root)
menu_bar.pack()

# 1) creating tabs
frame_home_page = home_page_display(menu_bar, main_page_bg)
frame_search_platforms = search_platform_display(menu_bar, search_page_bg)
frame_cheapest_price = cheapest_price_display(menu_bar, cheapest_page_bg)

frame_home_page.pack()
frame_search_platforms.pack()
frame_cheapest_price.pack()


# 2) adding created tabs to menu bar
menu_bar.add(frame_home_page, text='Home Page')
menu_bar.add(frame_search_platforms, text='Multi-Platform Search')
menu_bar.add(frame_cheapest_price, text='Cheapest Price')


# 3) tab selecetion functions
def select_main_page():
    menu_bar.select(0)
def select_search_platform():
    menu_bar.select(1)
def select_cheapest_price():
    menu_bar.select(2)



# SIDE MENU FUNCTIONS
def create_side_bar(frame_name):
    main_menu_button = Button(frame_name, image=home_page_button_img, command=select_main_page, borderwidth=1)
    main_menu_button.place(x=35, y=200)

    search_platforms_button = Button(frame_name, image=search_platforms_button_img, command=select_search_platform,
                                     borderwidth=1)
    search_platforms_button.place(x=35, y=250)

    cheapest_price_button = Button(frame_name, image=cheapest_price_button_img, command=select_cheapest_price,
                                   borderwidth=1)
    cheapest_price_button.place(x=35, y=300)

    

#    Side menu's button images
home_page_button_img = PhotoImage(file="img/buttons/Home button.png")
search_platforms_button_img = PhotoImage(file="img/buttons/Search button.png")
cheapest_price_button_img = PhotoImage(file="img/buttons/Cheapest button.png")



#   sidebar for all pages
create_side_bar(frame_home_page)
create_side_bar(frame_search_platforms)
create_side_bar(frame_cheapest_price)


# select_track_product()
root.mainloop()
