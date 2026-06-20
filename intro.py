import pygame

pygame.init()

screen = pygame.display.set_mode((500,400))
background_image = pygame.transform.scale(
    pygame.image.load("pexels-valentin-ivantsov-2154772556-36545253.jpg")
)
pygame.display.set_caption("WINDOW")
done = False
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.update()