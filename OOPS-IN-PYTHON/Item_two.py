from Item import Item
class Item_Two(Item):
    def __init__(self,name,age,sal,Increment):
        super().__init__(name,age,sal)
        self.Increment=Increment