import pygame
import random

# Constants for easier adjustments
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 72

# Initialize Pygame
pygame.init()

background_image = pygame.transform.scale(pygame.image.load("bg.jpg"),(SCREEN_WIDTH,SCREEN_HEIGHT))

font = pygame.fontSysFont("times new roman",FONT_SIZE)


class Sprite(pygame,sprite,Sprite):

    def __init__(self,colour,height,width):
        super().__init__()
        self.imgae = pygame.Surface([width,height])
        self.image.fil(
            pygame.Colour('dogerblue'))
        pyagme.draw.rect(self.image,colour,pygame.Rect(0,0,width,height))
        self.rect = self.image.get_rect()

    def move(self, x_change, y_change):
        self.rect.x = max(
            min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width),0)
        
        self.rect.y = max(
            min(self.rect.y + y_change, SCREEN_WIDTH - self.rect.width),0)
        

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("sprite collision")
all_sprites = pygame.sprite.Group()

sprite1 = Sprite(pygame.Clour('black'),20,30)
sprite1.rect.x, sprite1.rect.y = random.randint(
    0, SCREEN_WIDTH - sprite1.rect.width), random.randint(
        0, SCREEN_HEIGHT - sprite1.rect.height)
all_sprites.add(sprite1)

        
