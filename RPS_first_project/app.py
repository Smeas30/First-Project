from folder.menu import show_homepage
from folder.endless_rps import rockpaperscissors
from folder.duel_rps import battlerps

show_homepage()

while True:
    menu_select = input("Please select menu option: ")
    if menu_select == "1":
        rockpaperscissors()

    elif menu_select == "2":
        battlerps()

    elif menu_select == "3":
        print('goodbye')
        break

# if __name__ == "__main__":

#     # if show_homepage.menu_select == "2":

#     # if menu_select == "3":
#     #     print('goodbye')