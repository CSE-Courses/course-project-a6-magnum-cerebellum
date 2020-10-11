import json
import os 
import pygame

class Item():
    # initiate Item with an item_name corresponding to an item in item_data.json #
    # and a sprite object #
    def __init__(self, item_name, item_type):
        png = item_name + ".png"
        item_image = pygame.image.load(os.path.join("assets/item_sprites", png)).convert()        
        f = open(os.path.join("data/item_data.json"))
        data = json.load(f)
        
        if item_name not in data.keys():
            raise Exception("Sorry, no item availible")
        self.item_data = data[item_name]
        self.item_name = item_name
        self.item_attr = self.item_data["attributes"]
        
        #Added sprite and rec
        self.sprite =  item_image
        self.rect = self.sprite.get_rect()
        #Item type, if it's a consumable, equip, etc
        self.item_type = item_type

    #This resizes the object image, mainly for dragging around items
    def resize(self, size):
        return pygame.transform.scale(self.sprite,(size,size))
