"""class Creating_First_class():
    def Calculating_quantity(self,x,y):  #if we use def keyword inside the class we can call that as method
        return x*y                      # if we use def keyword outside the class we can call that as Function
        
object = Creating_First_class() #Creating Instance of the class that means Creating object to the class

object.name='Phone'
object.price=20000
object.quantity=3

print(object.Calculating_quantity(object.price,object.quantity))"""

# class Using_Constructor():

#     def __init__(self,Name,Price,Quantity):
#         self.name=Name   #self.name here name is a variable and Name is Paramater passing value to self.name
#         self.price=Price
#         self.quantity=Quantity
#         print("values are placed To the right position...")
#     def Display(self):
#         print(self.name)
#         print(self.price)
#         print(self.quantity)
# Name='phone'
# Price=10000
# Quantity=3
# object=Using_Constructor(Name,Price,Quantity)
# object.Display()

import csv

class using_constructor():
    pay_rate=0.8 #class or instance attribute we can access this using class name 
    all_instance=[]
    def __init__(self,name:str,price:float,quantity=0):
        #Run vaildation To the received arguments
        assert price>=0,f"price {price} is not greater than 0"
        assert quantity>=0, f"quantity {quantity} is not greater than 0"

        #Assign To The self object
        self.Name=name
        self.Price=price
        self.Quantity=quantity
        #storing instance in list    
        using_constructor.all_instance.append(self) # using_constructor.all_instance.append(self) self=object1 means all_instance.append(using_constructor('phone',100,2)) like this it will go on  
        #self.all_instance.append(self)
    def calculate_quantity(self):
        return self.Price*self.Quantity
    def apply_discount(self):
        self.Price=self.Price*self.pay_rate  #using_constructor.pay_rate 
        return self.Price
    def __repr__(self):
        return f"using_constructor({self.Name},{self.Price},{self.Quantity})"
    #why using __repr__ because to return a string representation of object
    # (<__main__.using_constructor object at 0x000001CF2975FCD0>) change this into (using_constructor('phone',100,2)  
    @classmethod
    def instantiate_from_csv(cls):
        with open('D:/python2/Study/Main.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for i in items:
            using_constructor(
                name=i.get('name'),price=float(i.get('price')),quantity=int(i.get('quantity'))
            )
    @staticmethod
    def check_integer(num):
        if isinstance(num,float):
            return num.is_integer()#To check the floating Number is an integer
        elif isinstance(num,int):
            return "Truee"
        else:
            return False
print(using_constructor.check_integer(8.0))    
    
# using_constructor.instantiate_from_csv()
# print(using_constructor.all_instance)


# object1=using_constructor('phone',100,2)    
# object2=using_constructor('laptop',1000,3)
# object3=using_constructor('cabel',10,5)
# object4=using_constructor('mouse',15,5)
# object5=using_constructor('keyboard',75,5)
# print(using_constructor.all_instance)

#using for loop 
# for instance in using_constructor.all_instance:
#     print(instance)


# object_one=using_constructor('phone',100,2)
# print(object_one.apply_discount())

# object_Two=using_constructor("laptop",1000,3)
# object_Two.pay_rate=0.7  #using_constructor.pay=0.7 (changing class attribute value) 
# print(object_Two.apply_discount())



# print(using_constructor.pay_rate) #Accessing class attribute using clsname
# print("using object:",object_one.pay_rate)# Accessing class attribute using object name 
# print("using object:",object_Two.pay_rate) 

#__dict__ Magic Attribute 
# print(using_constructor.__dict__) get all attributes for class level
# print(object_one.__dict__) get  all attributes for instance level

