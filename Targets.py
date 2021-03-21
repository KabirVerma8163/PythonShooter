import pygame


class Target(pygame.sprite.Sprite):
    def __init__(self, x, y, points_worth, shots_to_kill, image_path):
        super().__init__()
        self.x = x
        self.y = y
        self.position = (self.x, self.y)
        self.center = (self.x + self.image.get_width()//2, self.y + self.image.get_height()//2)
        self.points_worth = points_worth
        self.shots_to_kill = shots_to_kill
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = self.center

    @staticmethod
    def target_destroy(target_group, target, player_score, score_multiplier):
        target.shots_to_kill -= 1
        if len(target_group):
            if target.shots_to_kill <= 0:
                player_score += (target.points_worth * score_multiplier)//1
                target_group.remove(target)
                return player_score
        return player_score


class Target1(Target):
    image = pygame.image.load("Files\Target1.png")

    def __init__(self, x, y):
        super().__init__(x, y, 1, 1, "Files\Target1.png")
