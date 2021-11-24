# Import pygame and time modules
import pygame
import time
# Initialize pygame
pygame.init() 

screen = pygame.display.set_mode((550, 400))
pygame.display.set_caption("City Runner Game")

# Create image loading function here
def image_load(location, length, width):
    img = pygame.image.load(location).convert_alpha()
    img_scaled = pygame.transform.smoothscale(img,(length,width))
    return img_scaled
      
# Create text display function here, name it as "text_display"





# Define coin display function here
def coin_display(x):
    screen.blit(coin,(70*(x+1),210))
        
bgImg = image_load("background.png",800,400)
char = image_load("character.png",40,90)
coin = image_load("coin.png",50,50)

# All variables required to track backround, character, and coin positions are defined here
bgx = 0
charx = 10
chary = 210
x = 0

# Variables required to track money collected and time elapsed are defined here
money = 0
total_time = 60

# Game loop
carryOn = True
# Create first time point here
t1 = time.time()
while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                carryOn = False  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    charx += 5
                    bgx -= 1
                if charx >= 500:
                    charx = 10
                    bgx = 0
                    x = 0
                    coin_display(x)

        # Display the background, character and coins here
        screen.blit(bgImg,(bgx,0))
        coin_display(x)
        screen.blit(char,(charx,chary))
        
        # Get the rectangle images of character and coin to determine collision between them
        char_rect = char.get_rect(topleft=(charx,chary))
        coin_rect = coin.get_rect(topleft=(70*(x+1), 210))
        # Check if coin and character collided  

            # 1. Increment "money" by 1000

            # 2. Increment "x" by 1

            # 3. Call "coin_display()" function and pass "x" as input to it.

        
        # Display "Money Collected: " text along with "money" variable value here 
        # Choose text color rgb as (255,255,255)
        # Display text at location (10, 10)

       
        t2 = time.time()
        time_elapsed = t2 - t1
        time_left = round((total_time - time_elapsed))
        # Display "Time Left: " text along with "time_left" variable value here in seconds
        # Choose text color rgb as (255,255,255)
        # Display text at location (290, 10)

     
        if time_elapsed >= 60:
            pygame.time.wait(2000)
            # Code to close the game here
            # 1. Fill the screen with color having rgb combination (100,100,255)

            font = pygame.font.Font(None, 34)
            # Display "Money collected: " text along with "money" variable value here 
            # Choose text color rgb as (255,255,255)
            # Display text at location (120, 180)

            pygame.display.flip()
            pygame.time.wait(2000)
            break
    
        pygame.display.flip()
pygame.quit()