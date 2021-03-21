import pygame
from Colours import Colors


class Button():
    def __init__(self, x, y, width, height, start_color, text, border_width, text_color, hover_colour):
        self.start_color = start_color
        self.color = self.start_color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border_width = border_width
        self.text = text
        self.text_color = text_color
        self.visible = True
        self.hover_colour = hover_colour
        self.text_size = 20

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if self.visible:
            if outline:
                pygame.draw.rect(win, outline, (self.x-self.border_width, self.y-self.border_width,
                                                self.width+2*self.border_width, self.height+2*self.border_width), 0)

            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

            if self.text != '':
                font = pygame.font.SysFont('comicsans', self.text_size)
                text = font.render(self.text, True, self.text_color)
                win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y +
                                (self.height/2 - text.get_height()/2)))

    def is_over(self, pos):
        if self.visible:
            if self.x < pos[0] < self.x + self.width:
                if self.y < pos[1] < self.y + self.height:
                    self.color = self.hover_colour
                    return True
        self.color = self.start_color
        return False

    def clicked(self):
        self.visible = False


class StartButton(Button):
    def __init__(self, x, y, width, height, color=(0, 0, 0), text="START!", border_width=2, text_color=(255, 255, 255)):
        Button.__init__(self, x, y, width, height, color, text, border_width, text_color, Colors["green"])


class PlayerOptionsButton(Button):
    def __init__(self, x, y, text):
        button_width, button_height = 250, 100
        start_colour, hover_colour = Colors["lightNavyBlue"], Colors["paleTurquoise"]
        border_width = 3
        text_colour = Colors["lightGreen"]
        Button.__init__(self, x, y, button_width, button_height, start_colour, text, border_width, text_colour,
                        hover_colour)
        self.text_size = 40


class BackButton(Button):
    def __init__(self, x, y, text):
        button_width, button_height = 150, 60
        start_colour, hover_colour = Colors["lightNavyBlue"], Colors["paleTurquoise"]
        border_width = 3
        text_colour = Colors["lightRed"]
        Button.__init__(self, x, y, button_width, button_height, start_colour, text, border_width, text_colour,
                        hover_colour)
        self.text_size = 45
