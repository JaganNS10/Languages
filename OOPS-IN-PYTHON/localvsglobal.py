#local scope
"""def display():
    a=10 #local variable
    print(a)
display()"""

#global scope

"""a=10#global variable
def display():
    a=20#local variable
    print(a)
display()
print(a)"""

a=10#global variable
def display():
    a=20 #local to display method and global to show method
    def show():
        #a=30
        print(a)
    show()
display()
print(a)


