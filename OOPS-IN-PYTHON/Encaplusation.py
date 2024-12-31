#public,protected,private

class Class:
    def __init__(self,Name,Age,Phoneno):
        self.Name=Name#public 
        self._Age=Age #protected
        self.__PhoneNo = Phoneno#private
    
    #To change the value of private attribute
    def To_Access_Private(self,value):
        self.__PhoneNo=value
        print(self.__PhoneNo)

Object = Class('Jagan',19,7904136090)

Object.Name="SenthilKumar"

Object._Age=56

print(Object.Name)

print(Object._Age)

# print(Object.__PhoneNo)#Private:We Cannot Access Outside the class(Class' object has no attribute '__PhoneNo')

Object.To_Access_Private(9381458823)





#Public:We Access Inside The class as well as Outside the class and We can change the value also

#Protected:same as public but we use single underscore before the varible name 

#private:Access Only Inside the class Not Outside The Class and subclasses Also and We can change the value only inside the class 