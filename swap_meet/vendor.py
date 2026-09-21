class Vendor:
    def __init__(self,inventory=None):
        if inventory is None:
            self.inventory=[]
        else:    
            self.inventory = inventory
    def add(self, item):
        self.inventory.append(item)
        return item 

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item

        return False

    
    #     def add_to_list_ok(word, word_list=None):
    # word_list = [] if word_list is None else word_list
    # word_list.append(word)  # if word_list not supplied, defaults to None, resulting in a new
    # return word_list        # list being created with each invocation
