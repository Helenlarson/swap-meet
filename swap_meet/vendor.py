class Vendor:
    def __init__(self, inventory=None):
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
    
    def get_by_id(self, item_id: int):
        for item in self.inventory:
            if item.id == item_id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
    
        self.remove(my_item)
        other_vendor.add(my_item)

        other_vendor.remove(their_item)
        self.add(their_item)

        return True

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        
        my_first = self.inventory[0] 
        their_first = other_vendor.inventory[0] 

        return self.swap_items(other_vendor, my_first, their_first)
    
    # wave 6 starts here
    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.get_category() == category:
                items.append(item)

        return items
    
    def get_best_by_category(self, category):
        items_from_category = self.get_by_category(category)
        if not items_from_category:
            return None
        best_item = items_from_category[0]

        for item in items_from_category:
            if item.condition > best_item.condition:
                best_item = item
        
        return best_item
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)

        if not my_best_item or not their_best_item:
            return False

        # if my_best_item and their_best_item:
        return self.swap_items(other_vendor, my_best_item, their_best_item)
        
        # return False