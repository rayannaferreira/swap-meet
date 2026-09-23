class Vendor:
    def __init__(self,inventory=None):
        if inventory is None:
            self.inventory = []
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

    def get_by_id(self, id):
        for  item in self.inventory:
            if item.id == id:
                return item
        return None   

    def swap_items(self,other_vendor,my_item,their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)

            other_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True 
        return False

    def swap_first_item(self, other_vendor):
        if  self.inventory and  other_vendor.inventory:
                    my_item = self.inventory.pop(0)
                    their_item = other_vendor.inventory.pop(0)

                    self.inventory.insert(0,their_item)
                    other_vendor.inventory.insert(0,my_item)
        
                    return True 
        return False

    # wave 6 
    def get_by_category(self, category):
        matching_items = []
        for item in self.inventory:
            if item.__class__.__name__ == category:
                matching_items.append(item)
        return matching_items
    
    def get_best_by_category(self, category):
        category_items = self.get_by_category(category)
        if not category_items:
            return None

        best_item = category_items[0]
        for item in category_items:
            if item.condition > best_item.condition:
                best_item = item
        return best_item
         
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other_vendor.get_best_by_category(my_priority)
        if my_item is None or their_item is None:
            return False
        return self.swap_items(other_vendor, my_item, their_item)


