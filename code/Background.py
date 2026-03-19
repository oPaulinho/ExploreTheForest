import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, ENTITY_SPEED


class Background:
    def __init__(self, name: str, position: tuple):
        self.name = name
        
        if 'Bg' in name:
            bg_num = '4' if 'Level1' in name else '1'
            bg_folder = f'game_background_{bg_num}'
            filepath = f'./asset/background/PNG/{bg_folder}/{bg_folder}.png'
        else:
            bg_type = name.split('_')[0]
            bg_folder = 'game_background_' + bg_type.replace('bg', '')
            filename = name.replace(bg_type + '_', '') + '.png'
            filepath = f'./asset/background/PNG/{bg_folder}/layers/{filename}'

        self.surf = pygame.image.load(filepath).convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        
        # Default speed for fixed background is 0
        self.speed = ENTITY_SPEED.get(self.name, 0)

    def move(self, delta_x=0):
        # Move relative to the player speed and this layer's scale
        self.rect.x += delta_x * self.speed
        
        # Wrap logic for dual-image loop (each image is WIN_WIDTH wide)
        if delta_x < 0:  # Moving left (player going right)
            if self.rect.right <= 0:
                self.rect.left += 2 * WIN_WIDTH
        elif delta_x > 0:  # Moving right (player going left)
            if self.rect.left >= WIN_WIDTH:
                self.rect.right -= 2 * WIN_WIDTH