import pygame
import random

# Initialize Pygame
pygame.init()

# Game constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PLAYER_SPEED = 5
ENEMY_SPEED = 3
BULLET_SPEED = 10

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Old School Blaster')

# Player
player = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 60, 50, 50)

# Enemies
enemies = [pygame.Rect(random.randint(0, SCREEN_WIDTH-50), random.randint(0, 100), 50, 50) for _ in range(5)]

# Bullets
bullets = []

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player.x < SCREEN_WIDTH - player.width:
        player.x += PLAYER_SPEED
    if keys[pygame.K_SPACE]:
        bullets.append(pygame.Rect(player.x + player.width // 2, player.y, 5, 10))

    # Bullet movement
    for bullet in bullets[:]:
        bullet.y -= BULLET_SPEED
        if bullet.y < 0:
            bullets.remove(bullet)

    # Enemy movement
    for enemy in enemies:
        enemy.y += ENEMY_SPEED
        if enemy.y > SCREEN_HEIGHT:
            enemies.remove(enemy)
            enemies.append(pygame.Rect(random.randint(0, SCREEN_WIDTH-50), -50, 50, 50))

    # Collision detection
    for enemy in enemies[:]:
        for bullet in bullets[:]:
            if enemy.colliderect(bullet):
                enemies.remove(enemy)
                bullets.remove(bullet)
                enemies.append(pygame.Rect(random.randint(0, SCREEN_WIDTH-50), -50, 50, 50))
                break

    # Drawing
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 128, 255), player)
    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), enemy)
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 255, 255), bullet)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
