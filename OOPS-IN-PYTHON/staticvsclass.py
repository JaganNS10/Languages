#when to use class method and when to use static method ?

class Students:

    @staticmethod
    def static():
        #This should do something that has a relationship with the class,
        #but not something that must be unique per instance
        print("This is Staticmethod")
        #In static method it don't use the class reference in the background
        #That means object.Students(object) in other methods but in static its not like that 
    @classmethod
    def Class(cls):
        #This should do something that has a relationship with the class,
        #but usually,those are used to manipulate different structures od data to instantiate
        #objects like we have done with csv
        print("This is Classmethod")

#This methods can be called from instance also that is object
object = Students()
object.static()
object.Class()
