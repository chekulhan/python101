import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame prueba")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Frame rate
clock = pygame.time.Clock()
FPS = 60

# Vehicle class
class Vehicle:
    def __init__(self, name, image_path, x, y):
        self.name = name
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (100, 100))  # Resize the image
        self.x = x
        self.y = y

    def drive(self, dx, dy):
        """Mover el coche """
        self.x += dx
        self.y += dy

    def draw(self, surface):
        """Dibujar el coche """
        surface.blit(self.image, (self.x, self.y))


CAR_IMAGE_PATH = "car.png"  

# Create a vehicle object
car = Vehicle("Coche 1", CAR_IMAGE_PATH, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Main game loop
def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle keys for car movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            car.drive(0, -5)  # Move up
        if keys[pygame.K_DOWN]:
            car.drive(0, 5)  # Move down
        if keys[pygame.K_LEFT]:
            car.drive(-5, 0)  # Move left
        if keys[pygame.K_RIGHT]:
            car.drive(5, 0)  # Move right

        # Borrar el screen
        screen.fill(WHITE)

        # Dibujar el coche
        car.draw(screen)

        # Actualizar todo que has sido dibujado
        pygame.display.flip()

        # Mantener el FPS
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
