import pygame
import sys

# Inicializar pygame
pygame.init()

# Configurar pantalla
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("¡Feliz Día del Maestro!")

# Definir colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Fuente del texto
font = pygame.font.Font(None, 50)
text = font.render("¡Feliz Día del Maestro!", True, BLUE)

# Posición inicial
x, y = WIDTH // 2 - text.get_width() // 2, HEIGHT

# Reloj para controlar la velocidad
clock = pygame.time.Clock()

# Bucle de animación
running = True
while running:
    screen.fill(WHITE)

    # Mover el texto hacia arriba
    if y > HEIGHT // 2:
        y -= 2

    screen.blit(text, (x, y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()