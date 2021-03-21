import random
from Targets import *
from Colours import Colors
from Buttons import *
import pygame
import sys
import pymongo
import urllib.parse as parse

# password = parse.quote("MongoDB@01212004")
# cluster = pymongo.MongoClient(f"mongodb+srv://Mongo_Anyone:{password}@cluster0.rvtwf.mongodb.net/<dbname>?retryWrites=true&w=majority")
# db = cluster["PracticePrograms"]
# col = db["ShootingGame"]

# post = col.find_one({"name": name})
# if post is not None:
#     score = post["score"]
# else:
#     col.insert_one({
#         "name": name,
#         "score": 0
#     })
#     print("name inserted")


def make_targets(target_array, bg_dimensions, target1_num, target2_num, target3_num):
    # target array contains 3/multiple arrays for each kind of targets
    target1_array = []
    for target_num in range(target1_num):
        target_x = random.randrange(0, bg_dimensions[0] - Target1.image.get_width())
        target_y = random.randrange(0, bg_dimensions[1] - Target1.image.get_height())
        target1_array.append(Target1(target_x, target_y))
    target_array.append(target1_array)


def add_targets(target_group, target_array):
    for target_list in target_array:
        for target in target_list:
            target_group.add(target)


def set_other_buttons(window):
    window_width, window_height = window.get_width(), window.get_height()
    new_player_button = PlayerOptionsButton(window_width//2 + 60, window_height//2 - 50, "New Player")
    continue_button = PlayerOptionsButton(window_width//2 - 310, window_height//2 - 50, "Continue Game")
    back_button = BackButton(window_width - 170, window_height - 170, "BACK")
    return new_player_button, continue_button, back_button


def draw_other_buttons(window, buttons_array):
    for button in buttons_array:
        button.draw(window)


def reset_window(player_highscore, player_score, start_button, target_array, target_group, bg_dimensions, target1_num, target2_num,
                 target3_num):
    if player_score > player_highscore:
        player_highscore = player_score

    start_button.visible = True

    target_array = []
    make_targets(target_array, bg_dimensions, target1_num, target2_num, target3_num)
    add_targets(target_group, target_array)

    pygame.mouse.set_visible(True)

    return 0, 0, False, 0, player_highscore


def set_bottom_bar(score, highscore, player_name):
    game_font = pygame.font.Font("freesansbold.ttf", 30)
    score_text = game_font.render(f"Score: {score}", False, Colors["lightPurple"])
    highscore_text = game_font.render(f"HighScore: {highscore}", False, Colors["lightPurple"])
    player_name_text = game_font.render(f"Name: {player_name}", False, Colors["lightPurple"])
    return score_text, highscore_text, player_name_text


def draw_bottom_bar(window, bottom_bar, score, highscore, player_name):
    score_text, highscore_text, player_name_text = set_bottom_bar(score, highscore, player_name)
    window.blit(score_text, (bottom_bar.x + (bottom_bar.width//8) - 100, bottom_bar.y + bottom_bar.height//4))
    window.blit(highscore_text, (bottom_bar.x + (3*bottom_bar.width//8) - 150, bottom_bar.y + bottom_bar.height//4))
    window.blit(player_name_text, (bottom_bar.x + (5*bottom_bar.width//8) - 150, bottom_bar.y + bottom_bar.height//4))


# def enter_name(name, got_name):
#     post = col.find_one({"name": name})
#     if post is not None:
#         score = post["score"]
#     else:
#         col.insert_one({
#             "name": name,
#             "score": 0
#         })
#         score = 0
#         print("name inserted")
#     return got_name, score
#
#
# def new_player():
#
#     pass


def get_name(window, player_name):
    keys_pressed = pygame.key.get_pressed()
    got_name = False
    score = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys_pressed[pygame.K_w]:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if len(player_name) > 0 and event.key == 13:
                # got_name, score = enter_name(player_name, got_name)
                got_name = True
                break
            if event.key == pygame.K_BACKSPACE:
                player_name = player_name[:-1]
            else:
                player_name += event.unicode
                player_name = player_name.strip(" ")
                player_name = player_name.strip("\n")
                player_name = player_name.strip("\r")
            if len(player_name) > 0:
                player_name = player_name[0].upper() + player_name[1:]

    return got_name, player_name


def redraw_window(window, window_dimensions, background_img, bottom_bar, target_group, cross_hair, score, highscore,
                  player_name, start_button, got_name, button_array):
    pygame.draw.rect(window, Colors["navyBlue"], bottom_bar)
    window.blit(background_img, (0, 0))
    if got_name:
        target_group.draw(window)
        target_group.update()
        draw_bottom_bar(window, bottom_bar, score, highscore, player_name)
        start_button.draw(window)
    else:
        draw_other_buttons(window, button_array)

        game_font = pygame.font.Font("freesansbold.ttf", 30)
        question_text = game_font.render(f"Please Enter Your Name Below", False, Colors["lightPurple"])
        window.blit(question_text, ((window_dimensions[0] - question_text.get_width())//2,
                                    (window_dimensions[1] - question_text.get_height())//2))
        got_name, player_name = get_name(window, player_name)
        player_name_text = game_font.render(f"Name: {player_name}", False, Colors["lightPurple"])
        window.blit(player_name_text, ((window_dimensions[0] - player_name_text.get_width())//2,
                                       (window_dimensions[1] - player_name_text.get_height())//2 + 100))
    if not start_button.visible:
        cross_hair.draw(window)
    else:
        pygame.mouse.set_visible(True)
    pygame.display.flip()
    return got_name, player_name


def timer_run(window, window_dimensions, background_img, bottom_bar, target_group, cross_hair, score, highscore,
              player_name, start_button, timer_num, got_name, button_array):
    timer_font = pygame.font.Font("freesansbold.ttf", 100)
    while timer_num > 0:
        pygame.time.delay(150)
        timer_text = timer_font.render(str(timer_num), False, Colors["black"])
        window.blit(timer_text, (600, 350))
        pygame.display.flip()
        pygame.time.delay(1000)
        redraw_window(window, window_dimensions, background_img, bottom_bar, target_group, cross_hair, score, highscore,
                      player_name, start_button, got_name, button_array)
        timer_num -= 1
    return True, pygame.time.get_ticks()
