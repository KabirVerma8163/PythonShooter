from Crosshair import Crosshair
from Buttons import *
import methods
import sys
import pygame
from Colours import Colors

# General Setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
winDimensions = (1280, 800)
winCenter = (640, 400)
backgroundDimensions = (1280, 720)
win = pygame.display.set_mode(winDimensions)
pygame.display.set_caption("Shots-a-rama")
background = pygame.image.load("Files\BG.jpg")

# crosshair
crosshair = Crosshair()

# targets
targetGroup = pygame.sprite.Group()
targetArray = []
methods.make_targets(targetArray, backgroundDimensions, 20, 0, 0)
methods.add_targets(targetGroup, targetArray)

bottomBar = pygame.Rect(0, backgroundDimensions[1], winDimensions[0], winDimensions[1] - backgroundDimensions[1])
score, highScore = 0, 0
startButton = StartButton(1000, 735, 150, 50)

timerRun = False
timerStart, timerCurrent, timerEnd = 0, 0, 0
scoreMultiplier = 0
timerNum = 3
gotName = False
name = ""

newPlayerButton, continueButton, backButton = methods.set_other_buttons(win)
buttonsArray = [newPlayerButton, continueButton, backButton]

while True:
    if gotName:
        timerCurrent = pygame.time.get_ticks()
        if timerStart > 100:
            if ((50000 - timerCurrent + timerStart) // 100) > 0:
                scoreMultiplier = (50000 - timerCurrent + timerStart) // 100
            else:
                scoreMultiplier = 1

        keysPressed = pygame.key.get_pressed()
        if keysPressed[pygame.K_w]:
            pygame.quit()
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if startButton.is_over(pygame.mouse.get_pos()):
                    startButton.clicked()
                    pygame.mouse.set_visible(False)
                if not startButton.visible:
                    score = crosshair.shoot(targetGroup, score, startButton.visible, scoreMultiplier)

        startButton.is_over(pygame.mouse.get_pos())

    gotName, name = methods.redraw_window(win, winDimensions, background, bottomBar, targetGroup, crosshair, score, highScore, name,
                                          startButton, gotName, buttonsArray)

    if not timerRun and not startButton.visible:
        timerRun, timerStart = methods.timer_run(win, winDimensions, background, bottomBar, targetGroup, crosshair,
                                                 score, highScore, name, startButton, timerNum, gotName, buttonsArray)

    if len(targetGroup) == 0:
        timerStart, timerCurrent, timerRun, score, highScore = methods.reset_window(highScore, score, startButton,
                                                                                    targetArray, targetGroup,
                                                                                    backgroundDimensions, 20, 0, 0)

    clock.tick(60)
