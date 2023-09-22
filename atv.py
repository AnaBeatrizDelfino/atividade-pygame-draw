import pygame
import random

pygame.init()

width, height = 800, 600
tela = pygame.display.set_mode((width, height))
pygame.display.set_caption("Desenho de Formas")

WHITE = (255, 255, 255)

desenho = False
shape_type = "quadrado"
shapes = [] 

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

cores = random_color()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            desenho = True
            x, y = event.pos
            cores = random_color() 
            if shape_type == "retangulo":
                width = random.randint(20, 100)
                height = random.randint(20, 100)
                rect = pygame.Rect(x, y, width, height)
                shapes.append(("retangulo", rect, cores))
            elif shape_type == "quadrado":
                side = random.randint(20, 100)
                rect = pygame.Rect(x, y, side, side)
                shapes.append(("quadrado", rect, cores))
            elif shape_type == "circulo":
                radius = random.randint(10, 50)
                circle = (x, y, radius)
                shapes.append(("circulo", circle, cores))
        elif event.type == pygame.MOUSEBUTTONUP:
            desenho = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                shape_type = "retangulo"
                cores = random_color() 
            elif event.key == pygame.K_q:
                shape_type = "quadrado"
                cores = random_color()
            elif event.key == pygame.K_c:
                shape_type = "circulo"
                cores = random_color()

    tela.fill(WHITE)

    for shape, item, shape_cores in shapes:
        if shape == "retangulo" or shape == "quadrado":
            pygame.draw.rect(tela, shape_cores, item)
        elif shape == "circulo":
            pygame.draw.circle(tela, shape_cores, item[0:2], item[2])

    if desenho:
        if shape_type == "retangulo":
            pygame.draw.rect(tela, cores, (x, y, width, height), 2)
        elif shape_type == "quadrado":
            pygame.draw.rect(tela, cores, (x, y, side, side), 2)
        elif shape_type == "circulo":
            pygame.draw.circle(tela, cores, (x, y), radius, 2)

    pygame.display.flip()

pygame.quit()
