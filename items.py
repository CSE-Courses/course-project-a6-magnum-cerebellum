import json
import os 

class Item():
    # initiate Item with an item_name corresponding to an item in item_data.json #
    # and a sprite object #
    def __init__(self, item_name):
        
        f = open(os.path.join("data/item_data.json"))
        data = json.load(f)
        if item_name not in data.keys():
            raise Exception("Sorry, no item availible")
        self.item_data = data[item_name]
        self.item_name = item_name
        self.item_attr = self.item_data["attributes"]