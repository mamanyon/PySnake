


# Import the pygame library and initialise the game engine
import pygame, random, time, sys
pygame.init()

# Define some colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

# Open a new window
size = (900, 900)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Eitan SHTAK")


# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
x=[]
y=[]
snake_size = 1
Direction = 0
rows = 900/30
cols = 900/30
apple =[]

def init():
    x.clear()
    y.clear()
    x.append(random.randint(1, rows-2))
    y.append(random.randint(1, cols-2))
    Direction = 0
    snake_size=1
    apple.append(random.randint(1, rows-2))
    apple.append(random.randint(1, cols-2))

def GenApple():
    apple[0] = random.randint(1, rows-2)
    apple[1] = random.randint(1, cols-2)

init()

font = pygame.font.Font('freesansbold.ttf', 32)

# create a text surface object,
# on which text is drawn on it.
text = font.render(str(snake_size), True ,(0,0,0))




# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and Direction != 3:
                Direction = 1
            if event.key == pygame.K_LEFT and Direction != 4:
                Direction = 2
            if event.key == pygame.K_DOWN and Direction != 1:
                Direction = 3
            if event.key == pygame.K_RIGHT and Direction != 2:
                Direction = 4
        # --- Game logic should go here

        def move(snakesize):
            if Direction == 2:
                x[0] = x[0] - 1
            elif Direction == 1:
                y[0] = y[0] - 1
            elif Direction == 4:
                x[0] = x[0] + 1
            elif Direction == 3:
                y[0] = y[0] + 1
            if x[0] == apple[0] and y[0] == apple[1]:
                snakesize += 1
                GenApple()
                snake_size = snakesize
                text = font.render(str(snake_size), True, (0, 0, 0))
                screen.blit(text, (0, 0))
            time.sleep(0.1)
            out_of_bounds()
            return snakesize

        def out_of_bounds():
            if x[0] > rows:
                exit(1)
            elif y[0] > cols:
                exit(1)
            elif x[0] == -2:
                exit(1)
            elif y[0] == -2:
                exit(1)

        # --- Drawing code should go here
        # First, clear the screen to white.

    screen.fill(WHITE)
    # The you can draw different shapes and lines or add text to your background stage.

#    screen.blit(text, (0, 0))
    pygame.draw.rect(screen, BLACK, [x[0]*30, y[0]*30, 30, 30])
    pygame.draw.rect(screen, RED, [apple[0]*30, apple[1]*30, 30, 30])
    snake_size = move(snake_size)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()


    # --- Limit to 60 frames per second
    clock.tick(60)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()