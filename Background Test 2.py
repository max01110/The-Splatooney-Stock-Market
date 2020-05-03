import pygame            
pygame.init()       

size = (1500, 900)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

done = False

clock = pygame.time.Clock()



background_image = pygame.image.load("StockBackground.jpg").convert()
             

while not done:

   for event in pygame.event.get():
     if event.type == pygame.QUIT:
        done = True
   
  
   screen.blit(background_image, [0, 0])
   
   
   pygame.display.flip()
   

   clock.tick(60)
   

pygame.quit()