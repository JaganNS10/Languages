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