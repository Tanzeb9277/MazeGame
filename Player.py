import pygame

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class Player(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        
        super().__init__()
 
        self.image = pygame.Surface([25, 25])
        self.image.fill(GREEN)
 
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
        self.change_x = 0
        self.change_y = 0
        self.walls = None
 
    def changespeed(self, x, y):

        self.change_x += x
        self.change_y += y
 
    def update(self):

        self.rect.x += self.change_x
 
        
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
         
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                
                self.rect.left = block.rect.right
 
        self.rect.y += self.change_y
 
        
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:

            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom