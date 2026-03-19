import random
from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Player import Player
from code.Item import Item


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:

            case 'Level1Bg':
                return [Background('Level1Bg', (0, 0))]

            case 'Level2Bg':
                return [Background('Level2Bg', (0, 0))]

            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))

            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))

            case 'Item':
                return Item(
                    'Item',
                    (random.randint(40, WIN_WIDTH - 40), random.randint(int(WIN_HEIGHT * 0.25), int(WIN_HEIGHT * 0.82)))
                )