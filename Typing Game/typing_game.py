import pygame
import random
import time

pygame.init()

WHITE = (254, 254, 254)
BLACK = (1, 1, 1)

windowWidth = 850
windowHeight = 650
screen = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Typing Game by Amir")

font = pygame.font.SysFont(None, 50)

clock = pygame.time.Clock()

score = 0
mistakes = 0
word_speed = 3

words = ['cat', 'dog', 'house', 'computer', 'game', 'python',
         'word', 'but', 'again', 'later', 'school', 'girl', 'boy',
         'day', 'night', 'good', 'right', 'bool', 'false', 'true',
         'london', 'east', 'real', 'fake', 'snake', 'table', 'paper']

word = ''
word_x = 0
word_y = 0

def new_word():
    """Generate a new word and reset its position and speed"""
    global word, word_x, word_y, word_speed
    word = random.choice(words)
    word_x = random.randint(0, windowWidth - font.size(word)[0])
    word_y = 0
    word_speed += 0.1  # Increase speed by 0.1 after every correct word

def draw_text(text, color, x, y):
    """Render and display text on the screen"""
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def game_over():
    """Display game over screen with final score and provide restart or quit options"""
    global score, mistakes
    screen.fill(WHITE)
    draw_text(f"Game over! Final score: {score}  Mistakes: {mistakes}", BLACK, windowWidth//2 - font.size(
        f"Game over! Final score: {score}  Mistakes: {mistakes}")[0]//2, windowHeight//2 - font.size("Game over! ")[1])
    draw_text("Press 'R' to restart or 'Q' to quit", BLACK, windowWidth//2 - font.size("Press 'R' to restart or 'Q' to quit")
              [0]//2, windowHeight//2 + font.size("Press 'R' to restart or 'Q' to quit")[1])
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    score = 0
                    mistakes = 0
                    new_word()
                    return
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

new_word()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.unicode == word[0]:
                word = word[1:]
                if not word:
                    score += 1
                    new_word()
            else:
                score -= 1
                mistakes += 1
                if mistakes >= 5:
                    game_over()
                else:
                    new_word()
                    time.sleep(0.2)  # Delay for 0.5 seconds after mistake

    word_y += word_speed
    if word_y > windowHeight:
        score -= 1
        mistakes += 1
        if mistakes >= 5:
            game_over()
        else:
            new_word()
            time.sleep(0.5)  # Delay for 0.5 seconds after reaching bottom

    screen.fill(WHITE)
    draw_text(word, BLACK, word_x, word_y)
    draw_text(f"Score: {score}  Mistakes: {mistakes}", BLACK, 10, 10)

    pygame.display.update()
    clock.tick(60)
