port pygame

def main():
    pygame.init()
    screen_width, screen_height = 500, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('color changing sprite')

    # Mapping of color names to RGB values
    colors = {
        'red': pygame.Color('red'),
        'green': pygame.Color('green'),
        'blue': pygame.Color('blue'),
        'yellow': pygame.Color('yellow'),
        'white': pygame.Color('white')
    }
    current_color = colors['white']

    x, y = 30, 30
    sprite_width, sprite_height = 60, 60

    clock = pygame.time.Clock()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.k_LEFT]: x -= 3
        if pressed[pygame.k_RIGHT]: x += 3
        if pressed[pygame.k_UP]: x -= 3
        if pressed[pygame.k_DOWN]: y += 3

        x = min(max(0,x), screen_width - sprite_width)
        y = min(max(0,y), screen_height - sprite_height)


        if x == current_color = colours['blue']
        elif x == screen_width - sprite_width: current_color = colours['yellow']
        elif y == 0: current_color = colours['red']
        
