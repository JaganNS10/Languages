def Function(Name):
    print("My Name is:",Name)
'''Function("Jagan")
Function("Hemanth")'''


def Postional_argument(Age,Name):
    print(f"My Name is:{Name}")
    print(f"My Age is:{Age}")
'''Postional_argument("Jagan",19)'''

def keyword_argument(Name2,Name1):
    print(f"My Father's Name is:{Name1}")
    print(f"My Mother's Name is:{Name2}")
'''keyword_argument(Name1='Senthil',Name2='Jothi')'''

def default_argument(Name,School='srgvv'):
    print("My name is:",Name)
    print("Iam studying in:",School)

'''default_argument("Jagan")
default_argument("Heman")'''

def arbitary_positional_argument(*argu):
    print(argu)
'''arbitary_positional_argument(1,2,3,4,5)'''

def arbitary_keyword_argument(**argu):
    print(argu,argu["one"])
#arbitary_keyword_argument(one=1,two=2)



'''#local variable

def Local_variable():
    a=10
    return a
Return = Local_variable()
print(Return)

#Global variable
a=20
def Global_variable(a):
    a=30
    return a
Return1 = Global_variable(a)
print(Return1)
print(a)

#a=40
def Both():
    a=30
    def show(a):
        #a=20
        print(a)
    show(a)
#Both()'''

'''def ToprintGlobal():
    a=50
    def Tocallglobal():
        global a
        a=30 #It is the changed The local variable a into global a using global keyword
        b=20
    Tocallglobal()
    print(a)
ToprintGlobal()
print("a:",a)'''

class Myclass:
    def __init__(self,Name,age):
        self.Name = Name
        self.Age = age
    def __str__(self):
        return f"{self.Name} {self.Age}"
Object = Myclass("Jagan",19)
#print(Object)


'''a="Hemanth"
def Global():
    print(a)
    global b
    b=20#Local variable by using global keyword we can use it as global variable
Global()
print(b)'''

#Creating class &constructor
class Create_Class:
    def __init__(self,name,age):
        self.Name = name
        self.Age=age
    def Return(self):
        return f"{self.Name} {self.Age}" 
Object = Create_Class("Jagan",19)
#print(Object.Return())

#Storing Instances or objects
class Storing_Instance:
    Instance=[]
    def __init__(self,name,age):
        self.Name=name
        self.Age=age
        Storing_Instance.Instance.append(self)
    def __repr__(self):
        return f"Storing_Instance({self.Name},{self.Age})"
obj1=Storing_Instance("Jagan",19)
obj2=Storing_Instance(age=19,name="hemanth")
#print(Storing_Instance.Instance)

#Run Validation

class Validation:
    pay=0.5
    def __init__(self,name:str,age:int,Rollno:int):
        assert str(name)==name,f"name {name} is not string"
        assert age>=0,f"age {age} is not greater than 0"
        self.Name=name
        self.Age=age
        self.Number=Rollno
    def Add(self):
        self.Number = self.Number*Validation.pay
        return self.Number
Obj1=Validation("Jagan",19,7)
Obj2=Validation("Hemanth",23,8)
#print(Obj1.Add())
Validation.pay=0.7
#print(Obj2.Add())


#@classmethod without creating Object
'''
A class method is a method that is bound to the class not to the instance of the class(Object)

'''
import csv
class ClassMethod:
    def __init__(self,name,age):
        self.Name=name
        self.Age=age
        print("Hello")
    @classmethod
    def instaniate_from_csv(cls):
        with open('D:/Language/Pratice/Main.csv','r') as f:
            reader = csv.DictReader(f)
            List = list(reader)
            for i in List:
                #print(i['name'],i.get('age'))
                ClassMethod(name=i['name'],age=int(i.get('age')))
ClassMethod.instaniate_from_csv()

#@staticemthod 
class StaticMethod:
    @staticmethod
    def add(x,y):
        return x+y
result = StaticMethod.add(10,20)
print(result)

#Encapsulation

class Encapsulation:
    def __init__(self,public,protected,private):
        self.Public = public
        self._Protected = protected
        self.__Private = private
    def Disp(self):
        return f"{self.Public},{self._Protected} {self.__Private}"
Object1=Encapsulation("Jagan",19,7)

Object1.Public = "Hemanth"
Object1.__Private = 8

print(Object1.Disp())
print(Object1.Public)
print(Object1._Protected)
#print(Object1.__Private)

class Inheritance:
    All=[]
    def __init__(self,name):
        self.Name=name
        Inheritance.All.append(self)
    def __repr__(self):
        #return f"Inheritance({self.Name})"
        return f"{self.__class__.__name__}({self.Name})"
class second(Inheritance):
    def __init__(self,name):
        super().__init__(name)
        print(self.Name)
B = second("Hemanth")
print(Inheritance.All)























    




