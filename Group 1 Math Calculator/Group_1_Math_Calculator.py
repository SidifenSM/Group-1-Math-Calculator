#Group 1: Annabelle, Ismael, Jean, Stephen

import os

#clearing the terminal if need be for just making it look nice
def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

# in case if we choose anything related to math
import math

#list test
#select_list = ["0,1,2,3,4,5"]

selection = ''

degree = True

while selection != "0":
    
    print(
    """    
    Topic Idea
    
    1 - Placeholder
    2 - Placeholder
    0 - Exit

    """
    )

    

    selection = input("You selected: ")

    
    if selection == "0":
        print("\n")
        print("Have a great day! Come again!")

    elif selection == "1":
        print()
       
    elif selection == "2":
        print()
               
    else:
        clear_screen()
        print("Please select the listed options!")
