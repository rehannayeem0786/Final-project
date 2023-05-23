import json
import sys
import array
class User:
    def __init__(self):
        self.userdetails={}
        self.user_id= len(self.userdetails)+1
        self.orderdetails={}

        
    def registration(self):
        self.fullname=input("Enter Your Full Name : ")
        self.phone_no=int(input("Enter Your Mobile Number : "))
        self.emailid=input("Enter Your Email Id : ")
        self.address=input("Enter Your Address : ")
        self.password=input("Enter your Password : ")

        self.info={"Name":self.fullname,"Phone No":self.phone_no,"Email Id":self.emailid,"Address":self.address,"Password":self.password}
        print(self.info)
        self.user_id=len(self.userdetails)+1
        self.userdetails[self.user_id]=self.info
        print(self.userdetails)

        #store data in json
        with open("user.json","w")as f:
            json.dump(self.userdetails,f,indent=4)
        print("Data Added sucessfully..")

    def login(self):
        self.e=input("Enter Your Email Id :")
        self.p=input("Enter Your Password :")
        if self.emailid==self.e and self.password==self.p:
            print("..... Login Successfully !!!....")
        else:
            print("Please Enter Valid Credentials...")


    def place_order(self):
        self.list_food={"1":{"Name":"Tandoori Chicken","Quantity":"4 Pieces","Price":"INR 240"},
                        "2":{"Name":"Vegan Burger","Quantity":"1 Pieces","Price":"INR 320"},
                        "3":{"Name":"Truffle Cake","Quantity":"500 gm","Price":"INR 900"}}
        print(self.list_food)
        

        for i in self.list_food:
            order_id=int(input("Select Your Order From Above Option.. :"))
            if order_id==1:
                print(i,"=",self.list_food["1"])
            elif order_id==2:
                print(i,"=",self.list_food["2"])
            elif order_id==3:
                print(i,"=",self.list_food["3"])
            else:
                print("Enter valid input")
            self.orderdetails[order_id]=self.list_food[i]
        print(self.orderdetails)


         #store data in json
        with open("orderdetails.json","w")as f:
            json.dump(self.orderdetails,f,indent=4)
        print("Order Added sucessfully...")

        
    def list_item(self):
        print(self.orderdetails)

    def history(self):
        print(self.orderdetails)

    def update_profile(self):
        u_id=int(input("Enter id which you want to update :"))
        for i in self.userdetails[u_id]:
            self.userdetails[u_id][i]=input(f"Enter the {i} you want to update :")
        with open("user.json","w")as f:
            json.dump(self.userdetails,f,indent=4)
        print("User Profile updated Successfully..")