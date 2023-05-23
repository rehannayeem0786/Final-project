from Admin import *
from User import *
import sys
print("** Welcom To Food Ordering App **")
while True:
    role=int(input("Please Enter Your Role for Food Ordering App.. \n1. Admin \n2. User \n3. Exit \n"))
    if role==1:
        res=Admin()
        while True:
            print("*"*100)
            print("Press 1--For Add Food Items")
            print("Press 2--For Edit Food Items")
            print("Press 3--For Remove Food Items")
            print("Press 4--For View Food Items")
            print("Press 0--For Exit")
            Admin_input=int(input("Choose Your Preference ==> "))

            if Admin_input==1:
                res.add_food_item()
            elif Admin_input==2:
                res.edit_food_item()
            elif Admin_input==3:
                res.remove_food_item()
            elif Admin_input==4:
                res.view_food_item()
            elif Admin_input==0:
                sys.exit()
            else:
                print("Please Enter Valid Option")
    if role==2:
        res=User()
        while True:
            print("*"*100)
            print("Press 1-- For User Registration")
            print("Press 2-- For Login")
            print("Press 3-- For Place New Order")
            print("Press 4-- For View List of Selected Items :")
            print("Press 5-- For Order History")
            print("Press 6-- For Update Profile")
            print("Press 0-- For Exit from application")
            User_input=int(input("Chose Your Option ==>  "))

            if User_input==1:
                res.registration()
            elif User_input==2:
                res.login()
            elif User_input==3:
                res.place_order()
            elif User_input==4:
                res.list_item()
            elif User_input==5:
                res.history()
            elif User_input==6:
                res.update_profile()
            elif User_input==0:
                sys.exit()
            else:
                print("Please Enter Valid Option")
    if role==3:
        print("Thank You For Visiting Our Restaurant....")
        sys.exit()