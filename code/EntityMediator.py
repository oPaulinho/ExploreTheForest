from code.Player import Player
from code.Item import Item


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent):
        if isinstance(ent, Item) and ent.rect.right < 0:
            ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        if ent1.rect.colliderect(ent2.rect):

            if isinstance(ent1, Player) and isinstance(ent2, Item):
                ent1.score += ent2.score
                ent2.health = 0

            elif isinstance(ent1, Item) and isinstance(ent2, Player):
                ent2.score += ent1.score
                ent1.health = 0

    @staticmethod
    def verify_collision(entity_list):
        for i in range(len(entity_list)):
            EntityMediator.__verify_collision_window(entity_list[i])
            for j in range(i + 1, len(entity_list)):
                EntityMediator.__verify_collision_entity(
                    entity_list[i], entity_list[j]
                )

    @staticmethod
    def verify_health(entity_list):
        for ent in entity_list[:]:
            if isinstance(ent, (Player, Item)):
                if ent.health <= 0:
                    entity_list.remove(ent)