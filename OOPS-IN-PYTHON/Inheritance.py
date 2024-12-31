#Single Inheritance
"""class Class_one:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("This Is Class One")
class Class_Two(Class_one):
    def __init__(self,Name,Age,rollno):
        super().__init__(Name,Age)
        self.rollno=rollno
    def display(self):
        super().display()
        
object = Class_Two("jagan",19,28)
object.display()"""


#Multiple Inheritance
"""class Class_one:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        # print("hello")
    def display(self):
        print("This is class one")
class Class_Two:
    def __init__(self,name,age):
        # super().__init__(name,age)
        self.name=name
        self.age=age
    def display(self):
        super().display()
        print("This is class Two")
class Class_Three(Class_Two,Class_one):
    def __init__(self,Name,Age,rollno):
        super().__init__(Name,Age)#using parent class attribute
        self.rollno=rollno
        # print(self.name,self.age)
    def display(self):
        super().display()#using parent class method 
object = Class_Three("jagan",19,28)
object.display()"""

#Multi-level Inheritance

"""class Class_one:
    def __init__(self,name):
        self.Name=name
    def display_Function_one(self):
        print("THIS IS CLASS_ONE\nPARENTCLASS FOR CLASS_TWO")
class Class_Two(Class_one):
    def __init__(self,age,Name):
        super().__init__(name=Name)
        self.Age=age
    def display_Function_Two(self):
        super().display_Function_one()
        print("THIS IS CLASS_TWO\nPARENTCLASS FOR CLASS_THREE AND CHILDCLASS FOR CLASS_ONE")
class Class_Three(Class_Two):
    def __init__(self,rollno,Age_of_three,Name_of_three):
        super().__init__(Name=Name_of_three,age=Age_of_three)
        self.Rollno=rollno
        print("Name:",self.Name)
        print("Age:",self.Age)
        print("Rollno:",self.Rollno)
    def display_Class_Three(self):
        super().display_Function_Two()
        print("THIS IS CLASS_THREE\nCHILDCLASS FOR CLASS_TWO AND ACCESS THE CLASS_ONE THROUGH CLASS_TWO")
object= Class_Three(rollno=27,Name_of_three="jagan",Age_of_three=19)
object.display_Class_Three()"""

#Hybrid Inheritance

"""class Class_one:
    def __init__(self,Name,Age):
        self.Name=Name
        self.Age=Age
        print("YOUR ARE GETTING ATTRIBUTES(Name&Age)FROM CLASS ONE(Parent class)")
class Class_Two(Class_one):
    def __init__(self,Roll_one,get_name,get_age):
        super().__init__(Name=get_name,Age=get_age)
        self.Roll_one=Roll_one
        print(self.Name)
        print(self.Age)
        print("THIS IS CHILD CLASS ONE")
class Class_Three(Class_one):
    def __init__(self,Roll_Two,get_name,get_age):
        super().__init__(Name=get_name,Age=get_age)
        self.Roll_Two=Roll_Two
        print(self.Name)
        print(self.Age)
        print("THIS IS CHILD CLASS TWO")

Object_one = Class_Two(2213281058007,"Jagan",19)
Object_two = Class_Three(2213281058040,"kamesh",18)"""


"""class Class_one:
    def find_sum(self,list):
        sum=0
        for i in list:
            sum=sum+i
        return sum
class Class_Two(Class_one):
    def display(self,list):
        return f"sum is:{super().find_sum(list)}"
        # print(super().find_sum(list))
a=[1,2,3,4,5,20]
obj = Class_Two()
print(obj.display(list=a))"""

class Item:
    bonus=3000
    all=[]
    def __init__(self,name,age,sal):
        #Run vaildation
        assert isinstance(name,str),f"Your Input {name} is not vaild"
        assert age>=0,f"Your Input {age} is not vaild"
        assert sal>=0,f"Your Input {sal} is not vaild"
        #assign To the self object
        self.name=name
        self.age=age
        self.sal=sal
        Item.all.append(self)
    def calculate_sal(self):
        return self.sal+Item.bonus #self.bonus
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name},{self.age},{self.sal})" 
class Item_Two(Item):
    def __init__(self,name,age,sal,Increment):
        super().__init__(name,age,sal)
        self.Increment=Increment
object_one = Item_Two("jagan",19,2000,3000)
# Item.bonus=5000 #object_one.bonus=5000
# print(object_one.calculate_sal()+object_one.Increment)
print(Item.all)
print(object_one.all)

