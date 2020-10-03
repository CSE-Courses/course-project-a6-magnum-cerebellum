import unittest
import json

import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from actions import Action
import config

class TestAction(unittest.TestCase):
    def test_actions_damage(self):
        f = open(os.path.join(parentdir,"data/action_data.json"),"r")
        data = json.load(f)
        f.close()
        actions = data.keys()
        for action in actions: 
            new_action = Action(action)
            damage_level = new_action.damage_level
            self.assertEqual(data[action]["damage_level"], damage_level)

if __name__ == '__main__':
    unittest.main()