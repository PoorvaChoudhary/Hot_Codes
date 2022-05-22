AdminUsername = []
AdminPassword = []
UserUsername = []
UserPassword = []
veg_pizza_stock = [5, 5, 5, 5]
nonveg_pizza_stock = [5, 5, 5, 5]
budget_pizza_stock = [5, 5, 5, 5]
holi_pizza_stock = [5, 5, 5, 5]

while (True):
    print("\nWELCOME TO PIZZA APPLICAION\n_____________________________")
    print("\nPress 1 : ADMIN LOGIN \nPress 2 : USER LOGIN ")

    login = int(input("\nPlease Choose The Given Option : "))

    # For selection 1...............................................................

    if (login == 1):  # Admin login
        while (True):
            print("\n___"
                  "Admin LOGIN PAGE "
                  "___")
            print("\nPress 1: For Sign Up"
                  "\nPress 2: For Login Up"
                  "\nPress 3: For Back")

            selection = int(input("\nChoose the given Option : "))

            if (selection == 1):
                while (True):
                    Flag = False
                    print("__ "
                          "SIGN UP PAGE"
                          " __")
                    a = (input("\nCreate Your Username : "))
                    b = (input("Create Your Password : "))

                    # list = [a,b]
                    for i in range(len(AdminUsername)):
                        if (a == AdminUsername[i]):
                            print("\nUsername already exist please select other Username")
                            Flag = True
                            break
                    if (Flag == False):
                        AdminUsername.append(a)
                        AdminPassword.append(b)
                        print("\nUser Created Sucessfully")
                        break

            if (selection == 2):
                while (True):
                    Flag1 = False
                    print("\nPress 1: To Login"
                          "\nPress 2: To Exit")
                    key = int(input("Choose The Correct Option : "))

                    if (key == 1):
                        a = (input("username : "))
                        b = (input("Password : "))
                        for i in range(len(AdminUsername)):
                            if (a == AdminUsername[i]):
                                if (b == AdminPassword[i]):
                                    Flag1 = True
                    else:
                        break
                    if (Flag1 == False):
                        print("\nUsername or Password Incorrect , please try again")
                    else:
                        print("\nlogged in Sucessfully\n")
                        print("\nWELCOME STOCK MANAGEMENT SYSTEM")
                        while(True):
                            print("\nPress 0: Creamy Tomato Pizza Quantity = ", veg_pizza_stock[0],
                                  "\nPress 1: Cheese Magherita Quantity = ", veg_pizza_stock[1],
                                  "\nPress 2: Double Cheese Bust Quantity = ", veg_pizza_stock[2],
                                  "\nPress 3: Veg Loaded Quantity =", veg_pizza_stock[3],
                                  "\nPress 4: Chicken Tomato Pizza Quantity =", nonveg_pizza_stock[0],
                                  "\nPress 5: Shai Kabab Pizza Quantity = ", nonveg_pizza_stock[1],
                                  "\nPress 6: Grilled Corn And Chicken Pizza Quantity = ", nonveg_pizza_stock[2],
                                  "\nPress 7: Spicy Chicken Pizza Quantity = ", nonveg_pizza_stock[3],
                                  "\nPress 8: Papperoni Pizza + Papsi Quantity = ", budget_pizza_stock[0],
                                  "\nPress 9: Sahi panner Pizza + Burgur Pizza + Coke Quantity = ", budget_pizza_stock[1],
                                  "\nPress 10: Corn pizza + Cheese Pizza Quantity = ", budget_pizza_stock[2],
                                  "\nPress 11: Spicy Burgur + Papsi + French Fries Quantity = ", budget_pizza_stock[3],
                                  "\nPress 12: 2 Veg Pizza + 1 Non-Veg Combo Offer Quantity = ", holi_pizza_stock[0],
                                  "\nPress 13: Capsicum Pizza + 1 Burgur Pizza + Coke Quantity = ", holi_pizza_stock[1],
                                  "\nPress 14: 1 Corn Pizza + 1 Onion Pizza + 1 Papsi Quantity = ", holi_pizza_stock[2],
                                  "\nPress 15: Party Combo(1 Tomato Pizza + 1 Cheese Pizza + 2 Coke ) Quantity = ",
                                  holi_pizza_stock[3],
                                  "\nPress Any To Exit")

                            stock_selection_input = int(input("Enter the choice"))
                            qty = int(input("Enter the quantity to update for the selected pizza"))
                            if(stock_selection_input<4):
                                veg_pizza_stock[stock_selection_input]=veg_pizza_stock[stock_selection_input]+qty
                                print("Quantity updated")
                            elif(stock_selection_input>=4 and stock_selection_input<=7):
                                nonveg_pizza_stock[stock_selection_input-4]= nonveg_pizza_stock[stock_selection_input-4]+qty
                                print("Quantity Updated")
                            elif(stock_selection_input>7 and stock_selection_input<=11):
                                budget_pizza_stock[stock_selection_input-8]= budget_pizza_stock[stock_selection_input-8]+qty
                                print("Quantity Updated")
                            elif(stock_selection_input>11 and stock_selection_input<=15):
                                holi_pizza_stock[stock_selection_input-12]=holi_pizza_stock[stock_selection_input-12]+qty
                                print("Quantity Updated")
                            else:
                                break

            if(selection == 3):
                break

    # For selection 2................................................................

    if (login == 2):  # USER LOGIN
        while (True):
            print("\n*** USER PAGE ***\n"
                  "\nPress 1: Sign Up : "
                  "\nPress 2: Login Up : "
                  "\nPress 3: Back\n")
            selection = int(input("Choose The Correct Option : "))
            if (selection == 1):
                while (True):
                    Flag2 = False
                    print("\n__ "
                          "SIGN UP PAGE"
                          " __")
                    a1 = (input("\nCreate Your Username : "))
                    b2 = (input("Create Your Password : "))
                    for i in range(len(UserUsername)):
                        if (a1 == UserUsername[i]):
                            print("\nUsername already exist please select other Username")
                            Flag2 = True
                            break
                    if (Flag2 == False):
                        UserUsername.append(a1)
                        UserPassword.append(b2)
                        print("\n***** User Created Sucessfully ******\n")
                        break
            if (selection == 2):
                while (True):
                    Flag3 = False
                    print("Press 1: To Login"
                          "\nPress 2: To Back")
                    key = int(input("Choose The Option : "))
                    if (key == 1):
                        a = (input("username : "))
                        b = (input("Password : "))
                        for i in range(len(UserUsername)):
                            if (a == UserUsername[i]):
                                if (b == UserPassword[i]):
                                    Flag3 = True
                    else:
                        break
                    if (Flag3 == False):
                        print("\nUsername or Password Incorrect , please try again")
                    else:
                        print("\nlogged in Sucessfully")
                        total = 0
                        while (True):
                            print("\n")
                            print("* WELCOME TO PIZZA WORLD *\n"
                                  "\n- FULLY HYGIENE KITCHEN \n"
                                  "- 30 MINUTES DELIVERY AT YOUR DOOR STEP\n"
                                  "- CASH ON DELIVERY AVAILABLE\n"
                                  "- SPECIAL HOLI OFFER IS STARTED\n")

                            print("* SELECT THE PIZZA FROM THE GIVEN MANU : \n"
                                  "\nPRESS 1 : FOR VEG PIZZA "
                                  "\nPRESS 2 : FOR NON-VEG PIZZA "
                                  "\nPRESS 3 : FOR BUDGET VALUE PIZZA "
                                  "\nPRESS 4 : FOR SPECIAL HOLI PIZZA "
                                  "\nPRESS 5 : FOR GRAND TOTAL BILL"
                                  "\nPRESS 6 : FOR BACK")

                            Pizza = int(input("\nEnter The Selection : "))

                            # VEG Pizza

                            if (Pizza == 1):
                                while (True):
                                    #veg_pizza_stock = [500, 500, 500, 500]
                                    price_list = [350, 240, 450, 450]
                                    print("\nPress 0: Creamy Tomato Pizza = ", price_list[0], "Rs"
                                          "\nPress 1: Cheese Magherita = ",price_list[1], "Rs"
                                          "\nPress 2: Double Cheese Bust = ", price_list[2], "Rs"
                                          "\nPress 3: Veg Loaded =",price_list[3], "Rs"
                                          "\nPress other digit to exit")
                                    selection = int(input("\nEnter The Selection : "))
                                    if (selection < 4):
                                        if(veg_pizza_stock[selection]==0):
                                            print("pizza is out of stock")
                                        else:
                                            veg_pizza_stock[selection] = veg_pizza_stock[selection]-1
                                            total += price_list[selection]
                                    else:
                                        break
                                    print("Total Bill = ", total)


                            # NON VEG PIZZA

                            if (Pizza == 2):
                                while (True):
                                    nonveg_price = [550, 440, 650, 400]
                                    print("\nPress 0: Chicken Tomato Pizza = ", nonveg_price[0],
                                          "\nPress 1: Shai Kabab Pizza = ", nonveg_price[1],
                                          "\nPress 2: Grilled Corn And Chicken Pizza = ", nonveg_price[2],
                                          "\nPress 3: Spicy Chicken Pizza = ", nonveg_price[3],
                                          "\nPress other digit to exit")
                                    selection = int(input("\nEnter The Selection : "))
                                    if (selection < 4):
                                        if(nonveg_pizza_stock[selection]==0):
                                            print("Pizza is out of stock")
                                        else:
                                            nonveg_pizza_stock[selection]=nonveg_pizza_stock[selection]-1
                                            total += nonveg_price[selection]
                                    else:
                                        break
                                    print("Total Bill = ", total)

                            # BUDGET VALUE PIZZA

                            if (Pizza == 3):
                                while (True):
                                    budgetpizza_price = [429, 499, 399, 149]
                                    print("\nPress 0: Papperoni Pizza + Papsi = ", budgetpizza_price[0], "Rs"
                                          "\nPress 1: Sahi panner Pizza + Burgur Pizza + Coke = ",budgetpizza_price[1], "Rs"
                                          "\nPress 2: Corn pizza + Cheese Pizza = ",budgetpizza_price[2], "Rs"
                                          "\nPress 3: Spicy Burgur + Papsi + French Fries = ",budgetpizza_price[3], "Rs"
                                          "\nPress 4: To Exit The Menu")
                                    selection = int(input("\nEnter The Selection : "))
                                    if (selection < 4):
                                        if(budget_pizza_stock[selection]==0):
                                            print("Pizza is out of stock")
                                        else:
                                            budget_pizza_stock[selection]=budget_pizza_stock[selection]-1
                                        total += budgetpizza_price[selection]
                                    else:
                                        break
                                    print("Total Bill = ", total)

                            # HOLI OFFER

                            if (Pizza == 4):
                                while (True):
                                    HoliPizza_price = [100, 299, 399, 249]
                                    print("\nPress 0: 2 Veg Pizza + 1 Non-Veg Combo Offer   = ", HoliPizza_price[0], "Rs + 5% OFF"
                                          "\nPress 1: Capsicum Pizza + 1 Burgur Pizza + Coke = ",HoliPizza_price[1], "Rs + 3% OFF"
                                          "\nPress 2: 1 Corn Pizza + 1 Onion Pizza + 1 Papsi = ", list[2],"Rs + 6% OFF"
                                          "\nPress 3: Party Combo(1 Tomato Pizza + 1 Cheese Pizza + 2 Coke ) = ", list[3],"Rs + 10% OFF"
                                          "\nPress 4: To Exit The Menu")
                                    selection = int(input("\nEnter The Selection : "))
                                    if (selection < 4):
                                        if(holi_pizza_stock[selection]==0):
                                            print("Pizza is out of stock")
                                        else:
                                            holi_pizza_stock[selection]=holi_pizza_stock[selection]-1
                                        total += list[selection]
                                    else:
                                        break
                                    print("Total Bill = ", total)

                            if (Pizza == 5):
                                print("Your Grand total Is Rs = ", total, "/-")
                                print("Order Timming : 30 min")
                                print("* THANK YOU AND VIST AGAIN *")
                                break

                            if (Pizza == 6):
                                break
            if(selection==3):
                break
