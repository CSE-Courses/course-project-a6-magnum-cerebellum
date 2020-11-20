from player import Player
from enemies import Enemy
from items import Item

class Battle():
    def __init__(self, player: Player, enemy: Enemy):
        self.player = player
        self.enemy = enemy
        self.isActive = True

    def player_hp(self) -> int:
        return self.player.hp 

    def enemy_hp(self) -> int:
        return self.enemy.hp
    
    def defend_with_damage(self, damage: int):
        if self.player.hp < 100:
            if self.player.hp + damage >= 100:
                self.player.hp = 100
            else:
                self.player.hp = self.player.hp + damage
        
    def attack_ememy_with_damage(self, damage: int) -> bool:
        if self.enemy.decrease_hp(damage):
            return True
        else:
            self.isActive = False
            return False
    #player attacks enemy, inflict items damage,  return true if attack was successful, false if enemy was destroyed
    def attack_enemy(self,item: Item) -> bool:
        damage = item.amount
        if self.enemy.decrease_hp(damage):
            return True
        else:
            self.isActive = False
            return False
    
    def attack_player_with_damage(self, damage: int) -> bool:
        if self.player.decrease_hp(damage):
            return True
        else:
            self.isActive = False
            return False

    # enemy attacks player, inflicit items damage, return true if attack was successful, false if player was destroyed
    def attack_player(self, item: Item) -> bool:
        damage = item.damage
        if self.player.decrease_hp(damage):
            return True
        else:
            self.isActive = False
            return False



