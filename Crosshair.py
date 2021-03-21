import pygame
from Targets import *


class Crosshair(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Files/Crosshair.png")
        self.sound = pygame.mixer.Sound("Files/Gunshot.wav")
        self.rect = pygame.Rect(self.image.get_rect().center[0] - 5, self.image.get_rect().center[1] - 5, 20, 20)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def shoot(self, target_group, player_score, start_button_visible, score_multiplier):
        if not start_button_visible:
            self.sound.play()
            for target in target_group:
                if self.rect.colliderect(target):
                    return Target1.target_destroy(target_group, target, player_score, score_multiplier)
        return player_score

    def draw(self, screen):
        self.update()
        image_pos = (self.rect.x - self.image.get_width()//2 + self.rect.width//2, self.rect.y -
                     self.image.get_height()//2 + self.rect.height//2)
        screen.blit(self.image, image_pos)
        # pygame.draw.rect(screen, (255, 0, 0), self.rect)
