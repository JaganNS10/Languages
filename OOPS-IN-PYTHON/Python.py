'''Unpack = ["Fruits","Vegetables","Dresses"]
x,*y = Unpack
print(x,y)#return y as list 

#casting 
x = int("3")
y = str(3)
z = float(3)

#String method upper(),lower(),strip(),replace(),split(),filter(),f"",center(),find(),rfind()
Var = "    hello world     Using Strip we can remove   whitespace"
Upper = Var.upper()
Lower = Var.lower()
Title = Var.title()
Strip  = Var.strip()
Replace = Var.replace("  ","")#Var.replace("H","J")//Three spaces
Float = "39.78"
Split = Float.split(".")
Split_Var = Var.split(" ")#Split_Var = Var.split()

List = [" ","Jagan"," ","","N.S"]
Filter = list(filter(str.strip,List))
print(Filter)
#Formatted String
Age = 56
print(f"My Age is {Age}")

name = "My Name is {fname} and My Age is {Age}".format(fname="Jagan",Age=19)

name = "My Name is {0} and My Age is {1}".format("Hemanth",23)
print(name)

Center = str(Age).center(22)
print(Center)

Name = "Jagan"
Find = Name.find("a")#find() return -1 if the value is not found but index()return error
print(Find)
RFind = Name.rfind("a")
print(RFind)'''

'''
insert(),append(),extend(),remove(),pop(),del(),index(),sort(),sort(reverse=True)
Mylist = ["apple","orange","banana","graph","goa"]
#Mylist[1:2]=["vegatable","Fruits"]
Mylist[1:4] = ["vegetable","Fruit"]
print(Mylist)

My = ["1",2,3,4,5,6,"1",2,1,1]
My.remove("1")
My.pop(2)
del My[4]
print(My)
List = [1,2,3,4,5]
New_List = [i if i!=3 else "3" for i in List]
print(New_List)'''

''' tuple()
Tuple = tuple(("apple","mango","orange","banana"))
print(Tuple[2:],Tuple[:2])

#add(we must change into list then only we can add)
List = list(Tuple)
List.append("kiwi")
Tuple = tuple(List)
print(Tuple)

for i in Tuple:
    Index = Tuple.index(i)
    print(Index)'''
'''
set(),add(),remove() or discard(),update() or union(),intersection(),difference(),symmetric_difference()
Set = {"apple","orange",True,1,2,3,4,False,0,5,6}
print(Set)

#add()
Set.add(10)
#update()==extend()
New_Set = {"vegatable","orange"}
Set.update(New_Set)
print(Set)
#remove(),discard() if the value is not in set() remove() method will raise an error.but discard() will not raise an error

New_Set.remove("orange")
#New_Set.remove("apple")raise an error
New_Set.discard("apple")
print(New_Set)

#union() or |,intersection()or &,intersection_update(),difference(),difference_update(),symmetric()

Set1 = {"a","b","c",2}
Set2 = {1,2,3,"a"}

#union() Set1|Set2

Set3 = Set1.intersection(Set2)#create new set()return same elements from both set
print(Set3)

#Set1.intersection_update(Set2) change in existing set()
print(Set1)

Set4 = Set1.difference(Set2)#return difference elements in first set
print(Set4)

#Set1.difference_update(Set2)change in existing set()
print(Set1)

Set5 = Set1.symmetric_difference(Set2)#return difference elements in both set
print(Set5)
#Set1.symmetric_difference_update(Set2)'''


'''
dict(),get(),keys(),values(),items(),update(),pop(),copy()
Dict = dict(name='Jagan',age=19,school='sgrvv')
#get()
Get  = Dict.get('name')
print("GET():",Get)
#keys()
Keys = list(Dict.keys())
print("KEYS():",Keys)
#values()
Values = Dict.values()
print("VALUES():",Values)
#items()
Items = Dict.items()
print("ITEMS():",Items)
#update()
Dict.update({'name':'Hemanth'})
print('UPDATE():',Dict)
#pop()
Dict.pop('name')
print('POP():',Dict)'''

'''
if-else(To check one condition),if-elif-else(To check More than one condition)
a=10
b=20

if a>b:
    print("a is greater")
else:
    print("b is greater")

a,b,c=10,20,5
if a>b:
    print("a is greater than  b")
elif a>c:
    print("a is greater than c")
else:
    print("b is greater")'''


i=1
while i<6:
    #print(i)
    i+=1
else:
    print("The While loop execute in continue not in break")

j=1
while j<6:
    #print(j)
    if j==4:
        break
    j+=1
else:
    print("This else part will not work")

k=0
while k<6:
    k+=1
    if k==4:
        continue
    print(k)
else:
    print("This else part will work")

    


