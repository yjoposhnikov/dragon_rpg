# Definition of an enemy
class Poorly_Designed_Enemy:
    # eto ATTRIBUTES
    enemy_type: str
    enemy_name: str
    hp: int = 10
    attack_damage: int = 1


class Properly_Designed_Enemy:
    def __init__(self, enemy_type, enemy_name, hp, attack_damage):
        self.enemy_type = enemy_type
        self.enemy_name = enemy_name
        self.hp = hp
        self.attack_damage = attack_damage
