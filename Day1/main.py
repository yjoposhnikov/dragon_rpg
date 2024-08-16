from enemy import Properly_Designed_Enemy, Poorly_Designed_Enemy

Bubub = Properly_Designed_Enemy(enemy_type="Demon", enemy_name="Bubub", hp=100, attack_damage=24)

print(Bubub.enemy_name, Bubub.enemy_type, Bubub.hp, Bubub.attack_damage)

Kukub = Poorly_Designed_Enemy()

print(Kukub.enemy_name)