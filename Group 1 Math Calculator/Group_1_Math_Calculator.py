#Group 1: Annabelle, Ismael, Jean, Stephen

import os

#clearing the terminal if need be for just making it look nice
def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

#In case if we choose anything related to math
import math

selection = ''

#gas calculator variables
user = 0
user1 = 0
time_list = []
list = []
new_list = []

#window variable -- paint calculator portion
window = 0
action = 0
window_size = 0

#door variable
doorarea = 0

# window function 
def window_maker(apple):
    apple = apple*(24 * 36)
    return apple

# While the user does not select 0 to exit the program
while selection != "0":

    #If the user select 1 it will display the Fuel Calculator, when they select 2 it will be the paint calculator and 0 will exit the menu option

    print(
    """    
    Math Calculator Program

    1 - Fuel Cost Calculator
    2 - Paint Calculator
    0 - Exit
    """
    )

    

    selection = input("You selected: ")

    # When the user selects 0 it will display a message to the user 
    if selection == "0":
        print("\n")
        print("Have a great day! Come again!")
        print("\n")
        
    # When the user selects it will clear the screen and will display a welcome message prompt the user to input numbers to calculate

    elif selection == "1":
        #clear screen function to make it look nicer
        clear_screen()
        print('\n')
        print("Welcome to the Fuel Cost Calculator!")
        #Average MPG can be from 20-30, chose 27 as a random number between the range
        print("The average car gets 27 miles per gallon.")
        #Based on the current fuel cost of florida, averaged from $3.00 to $4.00, chose a middle-ground
        print("The current average cost of fuel is $3.50")
        print('\n')
        print("If you want to use the calculator to know the fuel cost and gallons of x miles.") 
        print("Please enter the mileage when prompted.")
        print('\n')

        # try clause, to execute if an exception is encountered if user enters a string or negative number
        # or any invalid input

        while True:
            print("\n")
            while True:
                try:
                   user = float(input("Please enter the mileage: "))

                except ValueError:
                    print("Please enter a valid number!")
                    continue
                # Will display a message if the user enters a 0 or a negative number
                if user <= 0:
                    print("No negative numbers or zero please!")
                    continue

                else:
                    break

            #user input divided by miles per gallon        
            user = user / 27
            print('\n')
            print("Gallons:     "'{:.2f}'.format(user))

            #appending each entry
            time_list.append(user)
            user *= 3.5

            #dollar sign format for column format
            dsign = "${:.2f}".format(user)
            print("Fuel cost: ", dsign)
            print('\n')
            #appending each entry
            list.append(dsign)
                    

            #format to show .2 decimal for gallons
            formater = ["%.2f" % gall for gall in time_list]

            print('\n')
            print("-The results of the calculator-")
            print('\n')

            print("Gallons","\tFuel Cost")
            print("-------", "\t--------")

            #column format
            for a, b in zip(formater, list):
                print("%-15s %s" % (a, b))
            
            print('\n')
            #if user wants to continue or exit the program when prompted
            question = input("Do you want to continue? Press enter to continue or type 'n' to leave: ").lower()
            if question == "n":
                break

        print('\n')
        print("Thanks, come again for the gas calculator!")


    elif selection == "2":

        #clear screen function to make it look nicer
        clear_screen()

        print("Welcome to the Paint Calculator!")
        print("Be wary that you'll be asked to enter a lot of information!")
        print("We want to make sure we have the most accurate-to-detail calculation for you!")
        print("'Disclaimer: We are not at fault for the lack of paint!'")
        print("\n")

        #How Much Paint Is Needed for Walls?     
        # A gallon of paint is 400sq ft    
        paint_gallon = 400

        #Can of paint is  5 gallons
        can_of_paint = 5

        #Price of paint is 148 dollars
        price_of_paint = 148

        #Labor cost will be a fixed price 
        labor_cost = 2000

        # Perimeter is the area of the walls that needs painting
        # The perimeter will give us the total square footage that needs to be painted

        
        # Will make sure a person inputs only positive numbers
        while True:
            try:
                print("~The average size of a house is 2500 square feet~")
                print("\n")
                perimeter = int(input( "What is your Perimeter? "))
                print("\n")

                print("Perimeter total:", perimeter )
            # Displays a message to user to input valid numbers
            except ValueError:
                print("\n")
                print("Please enter a valid number!")
                print("\n")
                continue
            # If a user enters a negative number a message will inform a user to only enter positive numbers
            if perimeter < 0:
                print("\n")
                print("We found an negative number in the calculations, please enter the perimeter again!")
                print("\n")
                continue
            # If a user enters 0, displays a message to enter a number higher than 0
            if perimeter == 0:
                print("\n")
                print("Please input something higher than zero!")
                print("\n")
                continue
            else:
                break
 
        user_input = ''

        while True:

            user_input = input('Do you want your door to be painted? yes or no: ')

            if user_input.lower() == "yes":
                print("Perfect!")
                #try except clause
                try:
                    #asking for height input
                    print("\n")
                    print("~The Standard door size is 36 inches wide by 80 inches Tall~")
                    print("\n")
                    height = int(input('Please Enter the Length of the door: '))
                    #asking for width input
                    width = int(input('Please Enter the Width of the door: '))
                    doorarea = height * width

                except ValueError:
                 # Displays a message if the user does not enter a valid number
                    print("Please enter a valid number!")
                    continue

                if height > 0 and width > 0:
                    print("The Area of the Door using", height, "and", width, " = ", doorarea)
                    print("\n")

                if height < 0 or width < 0:
                    print("Please input the length and width again without negative numbers please!")
                    continue

                if height == 0 or width == 0:
                    print("Please input the length and width again without a zero please!")
                    continue

                else:
                    break

            elif user_input.lower() == "no":
                print("No doors will be painted!")
                print("\n")
                break

            else:
                print("\n")
                print("Please type either 'yes' or 'no' please")
                print("\n")
        

        while True:
            # Ask the users if they want the windows to be painted
            prompt = input('Would you like your windows to be painted? "yes" or "no": ')

            if prompt.lower() == "yes":
                print("We'll get straight to it!")
                #try except clause
                try:
                    print("\n")
                    window = int(input("Please enter the number of windows: "))
                        
               # Displays to the user to input a valid number
                except ValueError:
                    print("Please enter a valid number!")
                    print("\n")
                    continue
                # If the user inputs a negative number, it will display a message to not input negative negatives
                if window < 0:
                    print("No negative numbers please!")
                    print("\n")
                    continue

                if window > 0:
                    action = window
                    window_size = window_maker(action)
                    print("\n")
                    print("~Windows are set by the standard size of 24 wide and 36 tall~ ")
                    print("\n")
                    print("The amount of", window, "window(s) has the total area of", window_size)
                    print("\n")

                if window == 0:
                    print("Please input something else than zero!")
                    print("\n")
                    continue

                else:
                    break
                #break statement
            elif prompt.lower() == "no":
                print("No windows will be painted!")
                print("\n")
                break

            else:
                print("Please type either 'yes' or 'no' please!")

        #variables for adding counters to prevent the program from being in a infinite loop
        mainSA = 0
        counter = 1
        count = 1
        numbWalls = 0
        counterman = 1

        #while loop that will be used for the nested for loop
        while True:
            #try except clause
            try:
                numbRooms = int(input("How many rooms does your house have? "))
                height = int(input("How tall is your house walls? In feet: "))
             
            #Displays a message to the user to input a valid number
            except ValueError:
                print("\n")
                print("Please enter a valid number!")
                print("\n")
                continue
                
             # Displays a message if a user inputs a negative or deci
            if numbRooms < 0 or height < 0:
                print("\n")
                print("No negative number or decimal number inputs please!")
                print("\n")
                continue

            if numbRooms == 0 or height == 0:
                print("\n")
                print("Input something else than zero please!")
                print("\n")
                continue

            else:
                break


        while True:
            #try except clause
            try: 
                count += 1
                #iterating through the input of numbRooms within the numbWalls
                for x in range(numbRooms):

                    while True:
                        counter += 1
                        #prompt the user of how many walls
                        try:
                            print("\n")
                            numbWalls = int(input("How many walls does room " + str(x+1) + " have? ")) 
                            print("\n")
                        except ValueError:
                            print("\n")
                            print("Please enter a valid number!")
                            continue

                        if numbWalls < 0:
                            print("No negative numbers please!")
                            continue

                        if numbWalls == 0:
                            print("No walls?")
                            continue

                        else:
                            break
                        #counter break if statement
                        if counter <= 2 or counter == 2:
                            break

                    #numbWalls iterating through number of rooms
                    for y in range(numbWalls):

                        while True:
                            #try except clause
                            try:
                                surfaceA = int(input("What is the base of wall  " + str(y+1) + " of room " + str(x+1) +  " in feet: ")) * height
                                counterman += 1

                                if surfaceA < 0:
                                     print("No negative numbers please")
                                     continue

                                else:
                                     mainSA = mainSA + surfaceA
                                     print("The surface area is: ", mainSA)
 
                            #Diplays a message to the user if they do not input a valid number 
                            except ValueError:
                                print("\n")
                                print("Please enter a valid number!")
                                continue
                            
                        #Displays a messsage if a user enters a negative number
                            if surfaceA < 0:
                                print("\n")
                                print("No negative numbers please!")
                                print("\n")
                                continue
                                
                             # Displays message if a user enters 0
                            if surfaceA == 0:
                                print("\n")
                                print("0 feet? Not much of a wall! Please enter a valid number!")
                                print("\n")
                                continue

                            else:
                                break
                            #counter break if statement
                            if counterman <= 2 or counterman == 2:
                                break
            except:
                pass
            #counter break if statement
            if count == 2:
                break
            else:
                pass

        
        #Grabbing all the calculations for the total cost
        surface_area = perimeter
        new_area = doorarea + window_size + mainSA
        surface_area = surface_area + new_area
        clear_screen()
        print('\n')
        print("Total Paint Cost")
        print("-" * 16)

        #Calculates the gallons of paint needed
        paint__gallon_needed =  surface_area / paint_gallon
        display_paint = "{:.2f}".format(paint__gallon_needed)
        print("Gallons of Paint needed:", display_paint)

        #Convert the gallon of paint to a can of paint
        paint_can_needed = paint__gallon_needed / can_of_paint

        #Cost of paint
        cost_of_paint = math.ceil(paint_can_needed) * price_of_paint 
        print("The cost of a can of paint(s):", cost_of_paint)

        #Displays the amount of cans needed and rounding up
        print(f"You need {math.ceil(paint_can_needed)} cans of paint.")

        #Total price
        total_price = cost_of_paint + labor_cost
        d_sign = "${:.2f}".format(total_price)
        d_sign2 = "${:.2f}".format(cost_of_paint)

        #Print Total cost
        print(f"With {math.ceil(paint_can_needed)} cans of paint, the price is {d_sign2}, and including the labor cost")
        print(f"The total will be: {d_sign}")
        print("\n")
        print("Thanks for coming! Please come again!")
    else:
        clear_screen()
        print("Please select the listed options!")