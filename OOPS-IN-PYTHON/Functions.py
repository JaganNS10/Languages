#function with parameter
"""def greet(Name):Name is formal parameter
    print("Hi",Name)
    print("Are you cs department...")

greet("jagan")"jagan" is actual parameter
greet("Hemanth")"""

#types of arguments

#positional and keyword arguments
"""def student(age,name):
    print(f"I am {name}:") 
    print(f"My Age is {age}:") 

# student("jagan",19) disadvantage of positional argument
#student(19,"jagan") #positional arguements
student(age=19,name="jagan") #keyword arguements"""

#default and non default arguments
"""def studentdetails(name,age,school="gbhss"):#default agrument # non-default argu always comes before default agru
    print(f"NAME:{name}")
    print(f"AGE:{age}")
    print(f"SCHOOL:{school}")
studentdetails("jagan",18) 
# studentdetails("jagan",19,"sgrvv")"""

#arbitary positional arguments
"""def add(*args): 
    sum=0
    for i in args:
        sum=sum+i
    print(f"sum is:{sum}")
add(1,2)
add(1,2,3,4,5)
add(6,7,8,9,11,22)"""
#positional and arbitary postional arguements
"""def add(a,*args):
    print(a)
    print(args)

add(1,2,3)"""

"""def add(*args,name): #def add(*args,name="jagan") add(1,2,3)
    print(args)
    print(name)

add(1,2,3,"jagan")"""

#arbitary keyword arguments

# def information(**kwargs):
#     print(kwargs)
#     print(kwargs["name"])

# information(name="jagan",age=19,city="ponneri")

#arbitary positional and keyword arguments
def information(*args,**kwargs):
    print(args)
    print(kwargs)

information(1,2,3,name="hemanth",age=23,city="ponneri")

#positional argument
#keyword argument (during funtion calling)
#default argument (during funtion definition)
#arbitary arguements -> arbitary positional argument and arbitary keyword argument








