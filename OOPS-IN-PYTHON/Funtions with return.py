#Funtion with return 
"""def format(a,b):
    changeofa=a.title()
    changeofb = b.title()
    return f"{changeofa} {changeofb}"
result=format("jagan","HEMANTH")
print(result)"""
  

#Return mulitple values

"""import statistics
def mean_median_mode(list1):
    return statistics.mean(list1),statistics.median(list1),statistics.mode(list1)
a,b,c=mean_median_mode([1,2,3,4,5])
print(a,b,c)"""

#Multiple return statement
"""def add(a,b):
    if a==0 and b==0:
        return "You have Entered 0 for both numbers..."
    else:
        return a+b
a=int(input("Enter Number1:\n"))
b=int(input("Enter Number2:\n"))
result=add(a,b)
print(result)"""
def format_name(name1,name2):
    if not name1 and not name2: #if len(name1)==0 and len(name2)==0 #if name1="" and name2="":
        return "You Have Entered Empty String"
    else:
        changeofname1=name1.title()
        changeofname2=name2.title()
        return f"{changeofname1} {changeofname2}"
name1 = input("Enter Name1:\n")
name2=input("Enter Name2:\n")
final_result=format_name(name1,name2)
print(final_result)