import uuid
class Item:
    def __init__(self,id=None, condition=0): 
        if id is  None :
            id = uuid.uuid4().int   
        self.id = id
        self.condition = condition


    def get_category (self):
        return "Item"
 

    def __str__(self):
        return f"An object of type Item with id {self.id}."


    def condition_description(self):
        if self.condition == 5:
            return "mint"
        elif self.condition == 4:
            return "pristine"
        elif self.condition == 3:
            return "good"
        elif self.condition == 2:
            return "acceptable"
        elif self.condition == 1:
            return "heavily used"
        else:
            return "just throw this garbage away"
    

