import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reindeer Platform Jumper")

# Load and scale the background image
try:
    background = pygame.image.load('Christmas_Hackathon.png').convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
except pygame.error as e:
    print(f"Couldn't load background image: {e}")
    background = None

# Load the reindeer icon image
try:
    icon = pygame.image.load('reindeer_icon.png')
    pygame.display.set_icon(icon)
except pygame.error as e:
    print(f"Couldn't load icon image: {e}")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Load reindeer image
try:
    reindeer_img = pygame.image.load('reindeer_icon.png')
    reindeer_img = pygame.transform.scale(reindeer_img, (60, 40))  # Adjust size as needed
except pygame.error as e:
    print(f"Couldn't load reindeer image: {e}")
    reindeer_img = pygame.Surface((60, 40))
    reindeer_img.fill((255, 0, 0))  # Red rectangle as fallback

# Reindeer properties
reindeer_width = 60
reindeer_height = 40
reindeer_x = WIDTH // 2 - reindeer_width // 2
reindeer_y = HEIGHT - reindeer_height - 10
reindeer_speed = 5
jump_speed = -15
gravity = 0.8

# Platform properties
platform_width = 100
platform_height = 20
platforms = [[WIDTH // 2 - platform_width // 2, HEIGHT - 100]]

# Game variables
score = 0
jump = False
y_velocity = 0

def create_platform(last_platform):
    max_jump_height = (jump_speed ** 2) / (2 * gravity)  # Maximum jump height
    min_y_distance = 50  # Minimum vertical distance between platforms
    max_y_distance = int(max_jump_height * 0.8)  # Maximum vertical distance (80% of max jump height)

    x = random.randint(0, WIDTH - platform_width)
    y = last_platform[1] - random.randint(min_y_distance, max_y_distance)
    return [x, y]

# Create initial platforms
for _ in range(5):
    platforms.append(create_platform(platforms[-1]))

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jump:
                jump = True
                y_velocity = jump_speed

    # Move reindeer
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and reindeer_x > 0:
        reindeer_x -= reindeer_speed
    if keys[pygame.K_RIGHT] and reindeer_x < WIDTH - reindeer_width:
        reindeer_x += reindeer_speed

    # Apply gravity
    if jump:
        reindeer_y += y_velocity
        y_velocity += gravity

    # Check platform collisions
    for platform in platforms:
        if (reindeer_y + reindeer_height >= platform[1] and 
            reindeer_y + reindeer_height <= platform[1] + platform_height and
            reindeer_x < platform[0] + platform_width and
            reindeer_x + reindeer_width > platform[0]):
            jump = False
            y_velocity = 0
            reindeer_y = platform[1] - reindeer_height

    # Move platforms down and create new ones
    if reindeer_y < HEIGHT // 2:
        scroll_speed = 5
        reindeer_y += scroll_speed
        for platform in platforms:
            platform[1] += scroll_speed
        
        # Create new platforms more frequently
        while platforms[-1][1] > 0:
            platforms.append(create_platform(platforms[-1]))
            score += 1

    # Remove off-screen platforms
    while len(platforms) > 0 and platforms[0][1] > HEIGHT:
        platforms.pop(0)

    # Draw everything
    if background:
        screen.blit(background, (0, 0))
    else:
        screen.fill(WHITE)
    
    screen.blit(reindeer_img, (reindeer_x, reindeer_y))
    for platform in platforms:
        pygame.draw.rect(screen, BLUE, (platform[0], platform[1], platform_width, platform_height))

    # Display score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
