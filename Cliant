import pygame

pygame.init()

#Clock
clock = pygame.time.Clock()
start_time = 0

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
Money_count = 0

#bools
walls_visible = True
can_move = False


class Door(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        
        super().__init__()
 
        self.image = pygame.image.load('Door.png')
 
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.player = None

    def update(self):
        is_reached = pygame.sprite.collide_rect(self, self.player)

        if is_reached:
            global wall_list
            wall_list.empty()

            global all_sprite_list
            all_sprite_list.empty()





class Item(pygame.sprite.Sprite):
     
    def __init__(self, x, y):
        
        super().__init__()
 
        self.image = pygame.image.load('Money.png')
 
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.player = None

    #when money is picked up by the player, the money disappears from the screen
    def update(self):
        is_picked_up = pygame.sprite.collide_rect(self, self.player)

        if is_picked_up:
            global Money_count
            Money_count += 1

            global all_sprite_list
            all_sprite_list.remove(self)
  
class Player(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        
        super().__init__()
 
        self.image = pygame.Surface([25, 25])
        self.image = pygame.image.load('Abe.png')
 
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

class Wall(pygame.sprite.Sprite):
    
    def __init__(self, x, y, width, height):
       
        super().__init__()
 

        self.image = pygame.image.load('Wall.png')
        #self.image.fill(RED)
 
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

#fonts
font_cambria = pygame.font.SysFont("Cambria", 30, True)  

#screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('Test')

#sprite lists
all_sprite_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()

#level 1 array (1D array but the following nested for loops read it as a 2D array)
level_1= [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
          1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 
          1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 
          1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 
          1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 
          1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 2, 
          0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 
          1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 
          1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 
          1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 

# create player
player = Player(0, 300)
player.walls = wall_list
all_sprite_list.add(player)

# create money item
item = Item(510, 165)
item.player = player
all_sprite_list.add(item)

i = 0
block_side = 50
for row in range(0, int(SCREEN_HEIGHT/block_side)):
    for col in range(0, int(SCREEN_WIDTH/block_side)):
        if level_1[i] == 1: 
            wall_list.add(Wall(col*block_side, row*block_side, block_side, block_side))
            #all_sprite_list.add(Wall(col*block_side, row*block_side, block_side, block_side))
        elif level_1[i] == 2:
            door = Door(col*block_side, row*block_side)
            door.player = player
            all_sprite_list.add(door)
        i+=1

# Wall to prevent player from going of the screen at the beginning of the level            
wall_list.add(Wall(-50, 300, 50, 50))

# main game loop
game_over = False

while not game_over:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if can_move:
            
            if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_h:
                #     if Money_count >= 1:    
                #         Money_count -= 1
                #         can_move = False
                #         walls_visible = True
                if event.key == pygame.K_LEFT :
                    player.changespeed(-3, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(3, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, -3)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, 3)
     
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(3, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(-3, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, 3)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, -3)
    
    # black out the walls after ~5 seconds from start of game
    # its not exactly 5 seconds but it works
    # once this time is up, the player will be able to move and the walls will become invisible
    if pygame.time.get_ticks() - start_time > 6500:
        walls_visible = False
        can_move = True
    
    all_sprite_list.update()
 
    screen.fill(BLACK)
 
    all_sprite_list.draw(screen)

    #drawing walls separately here so that they can become invisible once the initial time is up
    if walls_visible:
        for wall in wall_list:
            wall.draw()

    if walls_visible and wall_list:
        text = font_cambria.render("Score: $" + str(Money_count), 1, BLACK)
        screen.blit(text, (SCREEN_WIDTH/2 - 75, SCREEN_HEIGHT-50))
    elif not walls_visible and wall_list:
        text = font_cambria.render("Score: $" + str(Money_count), 1, WHITE)
        screen.blit(text, (SCREEN_WIDTH/2 - 75, SCREEN_HEIGHT-50))
    
    if not wall_list:
        text = font_cambria.render("You Win!", 1, WHITE)
        screen.blit(text, (SCREEN_WIDTH/2 - 50, SCREEN_HEIGHT/2 - 25))
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
