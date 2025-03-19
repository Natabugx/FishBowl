import pygame


pygame.init()
screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Sandys House")
clock = pygame.time.Clock() #handles FPS
BLUE = (3, 165, 252)

#SandyChar Class


#Sandy House Class
self.HouseImage = pygame.image.load("New Piskel.png").convert_alpha()
pygame.Surface.set_colorkey (self.HouseImage, [255,0,255])
def collision(bx, by, px, py): #bx, by is mouse, px, py is house position
    print(bx, by, px, py)
    
    if bx > px and bx<px+30 and by>py and by<py+30: #simple bounding box collision
        return True
    else: 
        return False

def draw(self, screen):
    screen.blit(self.HouseImage, (self.xpos, self.ypos))
running = True
while running: #game loop##########################################################
    
    #input/event section----------------------------------------
    for event in pygame.event.get():

        if event.type == pygame.QUIT: #quit game if x is pressed
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN: #check if mouse clicked
            mouse_x, mouse_y = event.pos #grab position
    
    #render section--------------------------------------------------
    screen.fill(BLUE)  # Clear the screen
    
    pygame.display.flip()
    

pygame.quit()

