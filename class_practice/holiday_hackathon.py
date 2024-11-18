import pygame
import random
import time

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
BRICK_COLOR = (178, 34, 34)  # Firebrick color for bricks
MORTAR_COLOR = (192, 192, 192)  # Light Gray for mortar

# Load reindeer images
try:
    reindeer_right = pygame.image.load('reindeer_icon.png')
    reindeer_right = pygame.transform.scale(reindeer_right, (60, 40))  # Adjust size as needed
    reindeer_left = pygame.transform.flip(reindeer_right, True, False)
except pygame.error as e:
    print(f"Couldn't load reindeer image: {e}")
    reindeer_right = pygame.Surface((60, 40))
    reindeer_right.fill((255, 0, 0))  # Red rectangle as fallback
    reindeer_left = reindeer_right.copy()

# Reindeer properties
reindeer_width = 60
reindeer_height = 40

# Platform properties
platform_width = 100
platform_height = 20
platform_speed = 2  # Speed at which platforms will move

# Game variables
reindeer_speed = 5
jump_speed = -15
gravity = 0.8
facing_right = True
score = 0
platforms_moving = False  # Flag to check if platforms should be moving

def create_platform(last_platform):
    max_jump_height = (jump_speed ** 2) / (2 * gravity)  # Maximum jump height
    min_y_distance = 50  # Minimum vertical distance between platforms
    max_y_distance = int(max_jump_height * 0.8)  # Maximum vertical distance (80% of max jump height)

    # Limit horizontal distance
    max_x_distance = 200  # Maximum horizontal distance
    min_x = max(0, last_platform[0] - max_x_distance)
    max_x = min(WIDTH - platform_width, last_platform[0] + max_x_distance)

    x = random.randint(min_x, max_x)
    y = last_platform[1] - random.randint(min_y_distance, max_y_distance)
    direction = random.choice([-1, 1])  # Random direction for platform movement
    return [x, y, direction]

def draw_brick_platform(surface, x, y, width, height):
    brick_height = height // 2
    brick_width = width // 4

    for row in range(2):
        for col in range(4):
            brick_x = x + col * brick_width
            brick_y = y + row * brick_height

            # Draw mortar
            pygame.draw.rect(surface, MORTAR_COLOR, (brick_x, brick_y, brick_width, brick_height))

            # Draw brick with the new brick color
            inner_margin = 2
            pygame.draw.rect(surface, BRICK_COLOR, (brick_x + inner_margin, brick_y + inner_margin,
                                                    brick_width - 2 * inner_margin,
                                                    brick_height - inner_margin * 2))

            # Add some shading to bricks for depth effect (optional)
            pygame.draw.line(surface, (139,69,19), (brick_x + inner_margin, brick_y + inner_margin), 
                             (brick_x + brick_width - inner_margin, brick_y + inner_margin), 1)
            pygame.draw.line(surface, (139,69,19), (brick_x + inner_margin, brick_y + brick_height - inner_margin), 
                             (brick_x + brick_width - inner_margin, brick_y + brick_height - inner_margin), 1)

    # Add vertical mortar lines for a staggered effect in the second row if necessary.
    if width % brick_width != 0:
        pygame.draw.line(surface, MORTAR_COLOR,
                         (x + width - 1, y + brick_height),
                         (x + width - 1, y + height), 
                         2)

def reset_game():
    global reindeer_x, reindeer_y, platforms, score, jump, y_velocity, facing_right, platforms_moving
    platforms = [[WIDTH // 2 - platform_width // 2, HEIGHT - 100, 1]]  # Added direction
    for _ in range(5):
        platforms.append(create_platform(platforms[-1]))
    reindeer_x = platforms[0][0] + platform_width // 2 - reindeer_width // 2
    reindeer_y = platforms[0][1] - reindeer_height
    score = 0
    jump = False
    y_velocity = 0
    facing_right = True
    platforms_moving = False

# Game loop
running = True
clock = pygame.time.Clock()

reset_game()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jump:
                jump = True
                y_velocity = jump_speed

    # Move reindeer left and right based on key presses.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and reindeer_x > 0:
        reindeer_x -= reindeer_speed
        facing_right = False
    if keys[pygame.K_RIGHT] and reindeer_x < WIDTH - reindeer_width:
        reindeer_x += reindeer_speed
        facing_right = True

    # Apply gravity to the reindeer's vertical position.
    reindeer_y += y_velocity
    y_velocity += gravity

    # Check if score has reached 100 and activate platform movement
    if score >= 50 and not platforms_moving:
        platforms_moving = True

    # Check collisions with platforms and move platforms if necessary.
    on_platform = False
    for platform in platforms:
        if platforms_moving:
            platform[0] += platform_speed * platform[2]  # Move platform
            if platform[0] <= 0 or platform[0] + platform_width >= WIDTH:
                platform[2] *= -1  # Reverse direction if hitting screen edge

        if (reindeer_y + reindeer_height >= platform[1] and 
            reindeer_y + reindeer_height <= platform[1] + platform_height and 
            reindeer_x < platform[0] + platform_width and 
            reindeer_x + reindeer_width > platform[0] and
            y_velocity > 0):  # Only collide when moving downwards
            jump = False
            y_velocity = 0 
            reindeer_y = platform[1] - reindeer_height
            on_platform = True
            break

    if not on_platform:
        jump = True

    # Move platforms down and create new ones.
    if reindeer_y < HEIGHT // 2:
        scroll_speed = 5 
        reindeer_y += scroll_speed 
        for platform in platforms:
            platform[1] += scroll_speed

        # Create new platforms more frequently.
        while platforms[-1][1] > 0:
            platforms.append(create_platform(platforms[-1]))
            score += 1

    # Remove off-screen platforms.
    while len(platforms) > 0 and platforms[0][1] > HEIGHT:
        platforms.pop(0)

    # Check if reindeer has fallen off the screen
    if reindeer_y > HEIGHT:
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", True, (255, 0, 0))
        screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
        pygame.display.flip()
        time.sleep(2)  # Display "Game Over" for 2 seconds
        reset_game()

    # Draw everything on the screen.
    if background:
        screen.blit(background, (0, 0))
    else:
        screen.fill(WHITE)

    # Draw the reindeer facing the correct direction
    if facing_right:
        screen.blit(reindeer_right, (reindeer_x, reindeer_y))
    else:
        screen.blit(reindeer_left, (reindeer_x, reindeer_y))

    for platform in platforms:
        draw_brick_platform(screen, platform[0], platform[1], platform_width, platform_height)

    # Display score on the screen.
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
