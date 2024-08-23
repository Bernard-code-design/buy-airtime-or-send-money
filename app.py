#THIS VERSION HAS NO try AND except
def service():
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
        int(input("Invalid Input.\n"
                  "Enter an option between 1-3\n"
                    "1. Buy Airtime\n"
                    "2. Send Money\n"
                    "3. Exit\n"
                    ": "))
        
def buy_airtime():
    buy = int(input("Enter an option\n"
                    "1. Buy For Sef\n"
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
        elif confirm == 2:
            print("You have canceled your purchase.")
            service()
        else: 
            print("Invalid Option")
            buy_airtime()
    elif buy == 2:
        other = int(input("Enter Phone Number\n" ": "))   
        repeat_other = int(input("Reapeat Phone Number\n" ": "))  
        if other == repeat_other:
             purchase = float(input("Enter Amount\n" ": "))  
             confirmation = int(input("Enter option\n"
                            "1. Buy\n"
                            "2. cancel\n"
                            ": "))  
             if  confirmation == 1:
                 print(f"An amount of {purchase} has been sent to {other}")
             elif confirmation == 2 :
                 print("Purchase Cancelled")
                 service()
        else:
            print("Number mismatch")   
            buy_airtime()    
    elif buy == 3:
        service()         
    else:
        print("Invalid Input")
        send_money()
                
             
def send_money():
    send = int(input("Enter Phone Number\n" ": "))   
    repeat = int(input("Reapeat Phone Number\n" ": "))  
    if send == repeat:
        amount = float(input("Enter Amount\n" ": "))  
        choose = int(input("Enter option\n"
                            "1. Buy\n"
                            "2. cancel\n"
                            ": "))  
        if  choose == 1:
                 print(f"An amount of {amount} has been sent to {repeat}")
        elif choose == 2 :
                 print("Purchase Cancelled")
                 service()
    else:
        print("Invalid Input")
        send_money()
        
def exit_app():
        end = int(input("Are you sure youb want to exit?\n"
                        "1. Yes\n"
                        "2. NO\n"
                        ": "))  
        if end == 1:
            exit
        elif end == 2:
            service()  
        else:
            print("Invalid Input")
            exit_app()
    
        
service()