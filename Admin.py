import json
class Admin:
    def __init__(self):
        self.food={}
        self.food_id= len(self.food)+1

    def add_food_item(self):
        self.name=input("Enter Name of Food Item :")
        self.quantity=int(input("Enter Food Quantity :"))
        self.price=int(input("Enter Food Price : "))
        self.discount=int(input("Enter Food Discount :"))
        self.stock=int(input("Enter the stock of that Food :"))
        self.items={"Name":self.name,"Quantity":self.quantity,"Price":self.price,"Discount":self.discount,"Stock":self.stock}
        print(self.items)
        self.food_id=len(self.food)+1
        self.food[self.food_id]=self.items
        print(self.food)
        
        #store data in json
        with open("food_item.json","w")as f:
            json.dump(self.food,f,indent=4)
        print("Item Added sucessfully")

     #delete food item from dict
    def remove_food_item(self):
        for k,v in self.food.items():
            print("Food id",k,"Food items",v)
        del self.food[int(input("Enter Food Id which you want to delete :"))]
        with open("food_item.json","w")as f:
            json.dump(self.food,f,indent=4)
        print("Item Removed Successfully")

    #view all item
    def view_food_item(self):
        for k,v in self.food.items():
            print("Food Id",k,"\nFood Item",v)

    #edit food item using food id
    def edit_food_item(self):
        f_id=int(input("Enter food id which you want to update :"))
        for i in self.food[f_id]:
            self.food[f_id][i]=input(f"Enter the {i} you want to update :")
        with open("food_item.json","w")as f:
            json.dump(self.food,f,indent=4)
        print("Food details have be updated Successfully")
