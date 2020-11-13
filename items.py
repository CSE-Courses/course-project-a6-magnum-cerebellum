import json
import os 
import pygame


class Item():
    # initiate Item with an item_name corresponding to an item in item_data.json #
    # and a sprite object #
    def __init__(self, item_name):
        png = item_name + ".png"
        item_image = pygame.image.load(os.path.join("assets/item_sprites", png)).convert()        
        f = open(os.path.join("data/item_data.json"))
        data = json.load(f)
       
        if item_name not in data.keys():
            raise Exception("Sorry, no item availible")
        self.item_name = item_name
        self.item_data = data[item_name]
        self.item_attr = self.item_data["attributes"]
        self.item_desc = self.item_data["description"]
        self.item_type = self.item_data["type"]

        #Amount is the item effect number. 
        #EX. Armor w/ 20 defense means amount = 20. 
        #EX. Consumable gives 20 hp, amount = 20. 
        #EX. If it takes away 20 hp, amount = -20.
        self.amount = self.item_data["amount"]

        #Sprite image and it's rect
        self.sprite =  item_image
        self.rect = self.sprite.get_rect()

        #Below will get initialized in setupItemData, based on the type of item

        #If it's an EQUIP it will be either Weapon or Armor
        self.equip_type = None

        #If it's an CONSUMABLE the effect is either Health or Mana
        self.effect = None

        self.setupItemData()

    #This resizes the object image, mainly for dragging around items
    def resize(self, size):
        return pygame.transform.scale(self.sprite,(size,size))

    def __str__(self):
        return self.item_name

    def setupItemData(self):
        if (self.item_type == "Equip"):
            self.equip_type = self.item_data["equipType"]
        elif (self.item_type == "Consumable"):
            self.effect = self.item_data["effect"]
        