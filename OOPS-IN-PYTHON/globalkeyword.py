#Global keyword
def ToprintGlobal():
    a=45
    def Tocallglobal():
        global a 
        a=30 #It is changed The local variable a into global a using global keyword
        b=20
    Tocallglobal()
    print(a)
ToprintGlobal()
print("a:",a)
