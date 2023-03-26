import pygame
import random

pygame.init()

red = (125, 0, 0)
green = (0, 179, 166)
white = (255, 255, 255)
grey = (196, 201, 183)
food = (236, 153, 42)

width = 600
lenght = 400
block = 10


font_style = pygame.font.SysFont("freesans", 25)
lost_image = font_style.render("You Lost! Press P-Play Again or Q-Quit", True, red)

dis = pygame.display.set_mode((width, lenght),)
pygame.display.set_caption("Snake Game by Martina")
pygame.display.update()
dis.fill(grey)

clock = pygame.time.Clock()
game_close = False
game_over = False

def m_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,green,(x[0], x[1], snake_block, snake_block))
        
def the_score(score):
    value = font_style.render("Your Score: " + str(score), True, food)
    dis.blit(value, [0, 0])

def game_loop():
    game_over = False
    game_close = False   

    x = width / 2
    y = lenght / 2
    x_change = 0
    y_change = 0
    food_x = block*random.randint(0, (width/block)-1)
    food_y = block*random.randint(0,(lenght/block)-1)
    
    snake_list = []
    snake_lenght = 1
    
    while(game_over == False): 
        while(game_close == True):
            dis.fill(white)
            dis.blit(lost_image,[100, 100])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        game_loop()                   
                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -block               
                elif event.key==pygame.K_DOWN:
                    x_change = 0
                    y_change = block              
                elif event.key==pygame.K_RIGHT:
                    x_change = block
                    y_change = 0              
                elif event.key==pygame.K_LEFT:
                    x_change = -block
                    y_change = 0
                    
                
        if x >= width or x < 0 or y >= lenght or y < 0:
            game_close = True
                
        x = x + x_change
        y = y + y_change
        dis.fill(grey)                       
            
        #pygame.draw.rect(dis, red,(x, y, 10, 10))   
        pygame.draw.rect(dis, food,(food_x, food_y, block, block))
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_lenght:
            del snake_list[0]
        for i in snake_list[:-1]:
            if i == snake_head:
                game_close = True
        m_snake(10,snake_list)
        if x == food_x and y == food_y:
            snake_lenght += 1
            food_x = block*random.randint(0, (width/block)-1)
            food_y = block*random.randint(0, (lenght/block)-1)  
        the_score(snake_lenght -1)    
        pygame.display.update()
        clock.tick(10)
    
    pygame.quit()
    
game_loop()
