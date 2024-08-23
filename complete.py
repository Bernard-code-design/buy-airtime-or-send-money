#THIS VERSION IS COMPLETE AND HAS try AND except

def service():
    while True:
        try:
            user_input = int(input("Enter one of these options\n"
                                    "1. Buy Airtime\n"
                                    "2. Send Money\n"
                                    "3. Exit\n"
                                    ": "))

            if user_input == 1:
                buy_airtime()
            elif user_input == 2:
                send_money()
            elif user_input == 3:
                exit_app()
            else:
                print("Invalid Input. Enter an option between 1-3")
        except ValueError:
            print("Invalid Input. Please enter a number.")

def buy_airtime():
    while True:
        try:
            buy = int(input("Enter an option\n"
                            "1. Buy For Self\n"
                            "2. Buy For Others\n"
                            "3. Back to main Menu\n"
                            ": "))

            if buy == 1:
                yourself = float(input("Enter amount: "))
                confirm = int(input("Enter option\n"
                                    "1. Buy\n"
                                    "2. cancel\n"
                                    ": "))
                if confirm == 1:
                    print(f"You have purchased an airtime of {yourself}")
                    break
                elif confirm == 2:
                    print("You have canceled your purchase.")
                    break
                else:
                    print("Invalid Option")
            elif buy == 2:
                other = int(input("Enter Phone Number: "))
                repeat_other = int(input("Repeat Phone Number: "))
                if other == repeat_other:
                    purchase = float(input("Enter Amount: "))
                    confirmation = int(input("Enter option\n"
                                            "1. Buy\n"
                                            "2. cancel\n"
                                            ": "))
                    if confirmation == 1:
                        print(f"An amount of {purchase} has been sent to {other}")
                        break
                    elif confirmation == 2:
                        print("Purchase Cancelled")
                        break
                    else:
                        print("Invalid Option")
                else:
                    print("Number mismatch")
            elif buy == 3:
                break
            else:
                print("Invalid Input")
        except ValueError:
            print("Invalid Input. Please enter a number.")

def send_money():
    while True:
        try:
            send = int(input("Enter Phone Number: "))
            repeat = int(input("Repeat Phone Number: "))
            if send == repeat:
                amount = float(input("Enter Amount: "))
                choose = int(input("Enter option\n"
                                    "1. Send\n"
                                    "2. cancel\n"
                                    ": "))
                if choose == 1:
                    print(f"An amount of {amount} has been sent to {repeat}")
                    break
                elif choose == 2:
                    print("Purchase Cancelled")
                    break
                else:
                    print("Invalid Option")
            else:
                print("Invalid Input")
        except ValueError:
            print("Invalid Input. Please enter a number.")

def exit_app():
    while True:
        try:
            end = int(input("Are you sure you want to exit?\n"
                            "1. Yes\n"
                            "2. NO\n"
                            ": "))

            if end == 1:
                exit()
            elif end == 2:
                break
            else:
                print("Invalid Input")
        except ValueError:
            print("Invalid Input. Please enter a number.")


# Calling the app Interface
service()
