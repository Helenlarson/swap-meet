import uuid

class Item:
    def __init__(self, id=None, condition=0):
        if id is None:
            self.id = uuid.uuid4().int
        else: 
            self.id = id

        self.condition = condition

    def get_category(self):
        return "Item"
    
    def condition_description(self):
        descriptions = {
            0: "Worst condition",
            1: "Heavily used",
            2: "Fair",
            3: "Good",
            4: "Like new",
            5: "Best condition"
        }

        if self.condition in descriptions:
            return descriptions[self.condition]
        else:
            return False

    def __str__(self):
        return f"An object of type Item with id {self.id}."

