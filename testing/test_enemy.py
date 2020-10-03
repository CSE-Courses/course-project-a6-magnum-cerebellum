import unittest
import json

import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from enemies import Enemy
from actions import Action
import config
class TestEnemy(unittest.TestCase):
    def test_enemy_actions(self):
        f = open(os.path.join(parentdir,"data/enemy_data.json"),"r")
        data = json.load(f)
        f.close()
        enemies = data.keys()
        for enemy in enemies: 
            new_enemy = Enemy(enemy)
            actions = new_enemy.actions
            actions_from_data = []
            for i in data[enemy]["actions"]:
                actions_from_data.append(i)
            for entry in actions:
                self.assertIn(entry.action_name, actions_from_data)
    
if __name__ == '__main__':
    unittest.main()