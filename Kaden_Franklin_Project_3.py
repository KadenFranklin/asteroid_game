from typing import *
from graphics import *
import random
import math

def title_screen() -> bool:
    title_screen_win = GraphWin("TITLE SCREEN", 400, 400, autoflush = False)
    title_screen_win.setBackground("#191919")
    title_text = Text(Point(200, 50), "Mine Dodger")
    title_text.setSize(36)
    title_text.setTextColor("#CCCCCC")
    title_text.draw(title_screen_win)

    click_text = Text(Point(200, 350), "Click anywhere to continue.")
    click_text.setSize(18)
    click_text.setTextColor("#CCCCCC")
    click_text.draw(title_screen_win)

    click_bool = False
    while click_bool == False:
        click = title_screen_win.getMouse()
        if 0 <= click.y < 400 and 0 < click.x < 400:
            click_bool = True
            title_screen_win.close()
            return True

def main_menu() -> str:
    main_menu_win = GraphWin("MAIN MENU", 400, 400, autoflush = False)
    main_menu_win.setBackground("#191919")
    main_menu_text = Text(Point(200, 25), "Main Menu")
    main_menu_text.setSize(22)
    main_menu_text.setTextColor("#CCCCCC")
    main_menu_text.draw(main_menu_win)

    rect_1 = Rectangle(Point(50, 50), Point(350, 100))
    rect_1.draw(main_menu_win)
    rect_1.setFill("#CCCCCC")
    rect_1_text = Text(Point(200, 75), "New Game")
    rect_1_text.setSize(18)
    rect_1_text.setTextColor("#000000")
    rect_1_text.draw(main_menu_win)

    rect_2 = Rectangle(Point(50, 120), Point(350, 170))
    rect_2.draw(main_menu_win)
    rect_2.setFill("#CCCCCC")
    rect_2_text = Text(Point(200, 145), "Continue")
    rect_2_text.setSize(18)
    rect_2_text.setTextColor("#000000")
    rect_2_text.draw(main_menu_win)

    rect_3 = Rectangle(Point(50, 190), Point(350, 240))
    rect_3.draw(main_menu_win)
    rect_3.setFill("#CCCCCC")
    rect_3_text = Text(Point(200, 215), "Load A Level")
    rect_3_text.setSize(18)
    rect_3_text.setTextColor("#000000")
    rect_3_text.draw(main_menu_win)

    rect_4 = Rectangle(Point(50, 260), Point(350, 310))
    rect_4.draw(main_menu_win)
    rect_4.setFill("#CCCCCC")
    rect_4_text = Text(Point(200, 285), "Character Customization")
    rect_4_text.setSize(18)
    rect_4_text.setTextColor("#000000")
    rect_4_text.draw(main_menu_win)

    rect_5 = Rectangle(Point(50, 330), Point(350, 380))
    rect_5.draw(main_menu_win)
    rect_5.setFill("#CCCCCC")
    rect_5_text = Text(Point(200, 355), "Exit Game")
    rect_5_text.setSize(18)
    rect_5_text.setTextColor("#000000")
    rect_5_text.draw(main_menu_win)

    click_bool = False
    while click_bool == False:
        click = main_menu_win.getMouse()
        if 50 <= click.y < 100 and 50 < click.x < 350:
            click_bool = True
            main_menu_win.close()
            return "start_new_game"
        if 120 <= click.y < 170 and 50 < click.x < 350:
            click_bool = True
            main_menu_win.close()
            return "continue"
        if 190 <= click.y < 240 and 50 < click.x < 350:
            click_bool = True
            main_menu_win.close()
            return "load_game"
        if 260 <= click.y < 310 and 50 < click.x < 350:
            click_bool = True
            main_menu_win.close()
            return "character_customiztion"
        if 330 <= click.y < 380 and 50 < click.x < 350:
            click_bool = True
            main_menu_win.close()
            quit()

def play_level(level : int):
    level_win = GraphWin(f"LEVEL {level}", 400, 400, autoflush = False)
    level_win.setBackground("#191919")
    char = Character(200, 200)
    char.draw(level_win)
    character_alive_bool = True
    win_bool = False
    counter = 0
    enemies_in_lev = []
    level = int(level)
    if level == 1:
        a = 3
    if level == 2:
        a = 5
    if level == 3:
        a = 6
    if level == 4:
        a = 8
    if level >= 5:
        a = level * 2
    for num in range(a):
        x_val = random.randint(1, 7) * 55
        z_val = random.randint(1, 2)
        if z_val == 1:
            y_val = (random.randint(50, 100))
        if z_val == 2:
            y_val = (random.randint(300, 350))
        enemies_in_lev.append(Enemy(x_val, y_val, level))

    for i in enemies_in_lev:
        i.draw(level_win)
    while character_alive_bool == True:
        counter += 1
        if character_alive_bool == True:
            character_alive_bool = \
                char.char_collision_with_en(enemies_in_lev)
            for n in range(counter):
                for i in enemies_in_lev:
                    i.update()
                    char.update(character_alive_bool, level_win)
                    character_alive_bool = \
                        char.char_collision_with_en(enemies_in_lev)

                if character_alive_bool == True and counter >= 100:
                    character_alive_bool = False
                    win_bool = True
                    level_winner(level)
                    level_win.close()
                update(120)
    if character_alive_bool == False and win_bool == False:
        level_lose()
        level_win.close()

def level_winner(level : int):
    win_screen_win = GraphWin("YOU WIN", 400, 400, autoflush = False)
    win_screen_win.setBackground("#191919")
    win_text = Text(Point(200, 50), "You Win!")
    win_text.setSize(36)
    win_text.setTextColor("#CCCCCC")
    win_text.draw(win_screen_win)

    click_text = Text(Point(200, 350), "Click anywhere to continue.")
    click_text.setSize(18)
    click_text.setTextColor("#CCCCCC")
    click_text.draw(win_screen_win)

    game_data = open('game_data.txt', 'r')
    game_data_list: List[int] = []
    for entry in game_data.readlines():
        game_data_list.append(entry.strip())
    current_color: int = game_data_list[0]
    current_shape: int = game_data_list[1]
    level = int(level) + 1
    game_data = open('game_data.txt', 'w')
    game_data.write(f'{current_color}\n')
    game_data.write(f'{current_shape}\n')
    game_data.write(f'{level}\n')
    game_data.close()

    click_bool = False
    while click_bool == False:
        click = win_screen_win.getMouse()
        if 0 <= click.y < 400 and 0 < click.x < 400:
            click_bool = True
            win_screen_win.close()

def level_lose():
    loss_screen_win = GraphWin("YOU LOSE", 400, 400, autoflush = False)
    loss_screen_win.setBackground("#191919")
    loss_text = Text(Point(200, 50), "You Lose")
    loss_text.setSize(36)
    loss_text.setTextColor("#CCCCCC")
    loss_text.draw(loss_screen_win)

    click_text = Text(Point(200, 350), "Click anywhere to continue.")
    click_text.setSize(18)
    click_text.setTextColor("#CCCCCC")
    click_text.draw(loss_screen_win)

    click_bool = False
    while click_bool == False:
        click = loss_screen_win.getMouse()
        if 0 <= click.y < 400 and 0 < click.x < 400:
            click_bool = True
            loss_screen_win.close()

def load_game():
    game_data = open('game_data.txt', 'r')
    game_data_list: List[int] = []
    for entry in game_data.readlines():
        game_data_list.append(entry.strip())
    current_color: int = game_data_list[0]
    current_shape: int = game_data_list[1]
    current_level: int = game_data_list[2]
    game_data.close()
    click_bool = False
    while click_bool == False:
        load_game_win = GraphWin("LOAD A LEVEL", 400, 400, autoflush = False)
        load_game_win.setBackground("#191919")
        load_game_text = Text(Point(200, 25), "Load A Level")
        load_game_text.setSize(22)
        load_game_text.setTextColor("#CCCCCC")
        load_game_text.draw(load_game_win)

        back_rect = Rectangle(Point(10, 10), Point(85, 50))
        back_rect.draw(load_game_win)
        back_rect.setFill("#CCCCCC")
        back_arrow = Polygon([Point(12, 30), Point(29, 45), Point(29, 15)])
        back_arrow.draw(load_game_win)
        back_arrow.setFill("#000000")
        back_rect_text = Text(Point(57, 32), "Back")
        back_rect_text.setSize(18)
        back_rect_text.setTextColor("#000000")
        back_rect_text.draw(load_game_win)

        level_rect_1 = Rectangle(Point(50, 55), Point(350, 105))
        level_rect_1.draw(load_game_win)
        level_rect_1.setFill("#CCCCCC")
        level_rect_1_text = Text(Point(200, 80), "Level 1")
        level_rect_1_text.setSize(18)
        level_rect_1_text.setTextColor("#000000")
        level_rect_1_text.draw(load_game_win)

        level_rect_2 = Rectangle(Point(50, 125), Point(350, 175))
        level_rect_2.draw(load_game_win)
        level_rect_2.setFill("#CCCCCC")
        level_rect_2_text = Text(Point(200, 150), "Level 2")
        level_rect_2_text.setSize(18)
        level_rect_2_text.setTextColor("#000000")
        level_rect_2_text.draw(load_game_win)
        if int(current_level) < 2:
            locked_circ_2 = Circle(Point(65, 150), 10)
            locked_circ_2.draw(load_game_win)
            locked_circ_2.setFill("#CCCCCC")
            locked_circ_2.setOutline("#000000")
            locked_rect_2 = Rectangle(Point(55, 150), Point(75, 170))
            locked_rect_2.draw(load_game_win)
            locked_rect_2.setFill("#000000")

        level_rect_3 = Rectangle(Point(50, 195), Point(350, 245))
        level_rect_3.draw(load_game_win)
        level_rect_3.setFill("#CCCCCC")
        level_rect_3_text = Text(Point(200, 220), "Level 3")
        level_rect_3_text.setSize(18)
        level_rect_3_text.setTextColor("#000000")
        level_rect_3_text.draw(load_game_win)
        if int(current_level) < 3:
            locked_circ_3 = Circle(Point(65, 220), 10)
            locked_circ_3.draw(load_game_win)
            locked_circ_3.setFill("#CCCCCC")
            locked_circ_3.setOutline("#000000")
            locked_rect_3 = Rectangle(Point(55, 220), Point(75, 240))
            locked_rect_3.draw(load_game_win)
            locked_rect_3.setFill("#000000")

        level_rect_4 = Rectangle(Point(50, 265), Point(350, 315))
        level_rect_4.draw(load_game_win)
        level_rect_4.setFill("#CCCCCC")
        level_rect_4_text = Text(Point(200, 290), "Level 4")
        level_rect_4_text.setSize(18)
        level_rect_4_text.setTextColor("#000000")
        level_rect_4_text.draw(load_game_win)
        if int(current_level) < 4:
            locked_circ_4 = Circle(Point(65, 290), 10)
            locked_circ_4.draw(load_game_win)
            locked_circ_4.setFill("#CCCCCC")
            locked_circ_4.setOutline("#000000")
            locked_rect_4 = Rectangle(Point(55, 290), Point(75, 310))
            locked_rect_4.draw(load_game_win)
            locked_rect_4.setFill("#000000")

        level_rect_5 = Rectangle(Point(50, 335), Point(350, 385))
        level_rect_5.draw(load_game_win)
        level_rect_5.setFill("#CCCCCC")
        level_rect_5_text = Text(Point(200, 360), "Level 5")
        level_rect_5_text.setSize(18)
        level_rect_5_text.setTextColor("#000000")
        level_rect_5_text.draw(load_game_win)
        if int(current_level) < 5:
            locked_circ_5 = Circle(Point(65, 360), 10)
            locked_circ_5.draw(load_game_win)
            locked_circ_5.setFill("#CCCCCC")
            locked_circ_5.setOutline("#000000")
            locked_rect_5 = Rectangle(Point(55, 360), Point(75, 380))
            locked_rect_5.draw(load_game_win)
            locked_rect_5.setFill("#000000")

        click = load_game_win.getMouse()
        if 10 <= click.y < 50 and 10 < click.x < 85:
            click_bool = True
            load_game_win.close()

        if (55 <= click.y < 105 and 50 < click.x < 350) :
            click_bool = True
            load_game_win.close()
            play_level(1)

        if (125 <= click.y < 175 and 50 < click.x < 350)\
                and int(current_level) >= 2:
            click_bool = True
            load_game_win.close()
            play_level(2)

        if (195 <= click.y < 245 and 50 < click.x < 350)\
                and int(current_level) >= 3:
            click_bool = True
            load_game_win.close()
            play_level(3)

        if (265 <= click.y < 315 and 50 < click.x < 350)\
                and int(current_level) >= 4:
            click_bool = True
            load_game_win.close()
            play_level(4)

        if (335 <= click.y < 385 and 50 < click.x < 350)\
                and int(current_level) >= 5:
            click_bool = True
            load_game_win.close()
            play_level(5)
        else:
            load_game_win.close()

def continue_func():
    game_data = open('game_data.txt', 'r')
    game_data_list : List[int] = []
    for entry in game_data.readlines():
        game_data_list.append(entry.strip())
    game_data.close()
    x = game_data_list[2]
    play_level(x)

def character_customization():
    game_data = open('game_data.txt', 'r')
    game_data_list: List[int] = []
    for entry in game_data.readlines():
        game_data_list.append(entry.strip())
    game_data.close()
    current_color: int = game_data_list[0]
    current_shape: int = game_data_list[1]
    current_level: int = game_data_list[2]

    click_bool = False
    while click_bool == False:
        character_customization_win = GraphWin\
            ("CHARACTER CUSTOMIZATION", 400, 400, autoflush = False)
        character_customization_win.setBackground("#191919")
        character_customization_text = \
            Text(Point(242, 25), "Character Customization")
        character_customization_text.setSize(20)
        character_customization_text.setTextColor("#CCCCCC")
        character_customization_text.draw(character_customization_win)

        char = Character(200, 200)
        char.draw(character_customization_win)

        back_rect = Rectangle(Point(10, 10), Point(85, 50))
        back_rect.draw(character_customization_win)
        back_rect.setFill("#CCCCCC")
        back_arrow = Polygon([Point(12, 30), Point(29, 45), Point(29, 15)])
        back_arrow.draw(character_customization_win)
        back_arrow.setFill("#000000")
        back_rect_text = Text(Point(57, 32), "Back")
        back_rect_text.setSize(18)
        back_rect_text.setTextColor("#000000")
        back_rect_text.draw(character_customization_win)

        color_dict: Dict[str, List[str]] = \
            {'color_1' :["Aquamarine", "#72e5be"]\
            , 'color_2':["Blue", "#0000b2"]\
            , 'color_3':["Bright Green", "#00cd00"]\
            , 'color_4':["Brown", "#4c3100"]\
            , 'color_5':["Dark Green", "#005900"]\
            , 'color_6':["Gold", "#ffd700"]\
            , 'color_7':["Gray", "#4c4c4c"]\
            , 'color_8':["Orange", "#ffa500"]\
            , 'color_9':["Pink", "#ff6666"]\
            , 'color_10':["Purple", "#660066"]\
            , 'color_11':["Red", "#b20000"]\
            , 'color_12':["Tan", "#d2b48c"]\
            , 'color_13':["White", "#ffffff"]\
            , 'color_14':["Yellow", "#ffff00"]}
        next_color = Rectangle(Point(315, 300), Point(390, 340))
        next_color.draw(character_customization_win)
        next_color.setFill("#CCCCCC")
        next_color_text = Text(Point(362, 322), "Next")
        next_color_text.setSize(16)
        next_color_text.setTextColor("#000000")
        next_color_text.draw(character_customization_win)
        prev_color = Rectangle(Point(10, 300), Point(100, 340))
        prev_color.draw(character_customization_win)
        prev_color.setFill("#CCCCCC")
        prev_color_text = Text(Point(55, 322), "Previous")
        prev_color_text.setSize(16)
        prev_color_text.setTextColor("#000000")
        prev_color_text.draw(character_customization_win)
        color_text = Text(Point(200, 322), \
                          (color_dict[f"color_{current_color}"])[0:1])
        color_text.setSize(16)
        color_text.setTextColor("#ffffff")
        color_text.draw(character_customization_win)

        next_shape = Rectangle(Point(315, 350), Point(390, 390))
        next_shape.draw(character_customization_win)
        next_shape.setFill("#CCCCCC")
        next_shape_text = Text(Point(362, 372), "Next")
        next_shape_text.setSize(16)
        next_shape_text.setTextColor("#000000")
        next_shape_text.draw(character_customization_win)
        prev_shape = Rectangle(Point(10, 350), Point(100, 390))
        prev_shape.draw(character_customization_win)
        prev_shape.setFill("#CCCCCC")
        prev_shape_text = Text(Point(55, 372), "Previous")
        prev_shape_text.setSize(16)
        prev_shape_text.setTextColor("#000000")
        prev_shape_text.draw(character_customization_win)
        shape_text = Text(Point(200, 372), f"Shape #{current_shape}")
        shape_text.setSize(16)
        shape_text.setTextColor("#ffffff")
        shape_text.draw(character_customization_win)

        click = character_customization_win.getMouse()
        if 10 <= click.y < 50 and 10 < click.x < 85:
            click_bool = True
            game_data = open('game_data.txt', 'w')
            game_data.write(f'{current_color}\n')
            game_data.write(f'{current_shape}\n')
            game_data.write(f'{current_level}\n')
            game_data.close()
            character_customization_win.close()

        if 300 <= click.y < 340 and 315 < click.x < 390:
            current_color = int(current_color) + 1
            if current_color == 15 :
                current_color = 1
                game_data = open('game_data.txt', 'w')
                game_data.write(f'{current_color}\n')
                game_data.write(f'{current_shape}\n')
                game_data.write(f'{current_level}\n')
                game_data.close()
                color_text.undraw()
                color_text.draw(character_customization_win)
                character_customization_win.close()
            else:
                game_data = open('game_data.txt', 'w')
                game_data.write(f'{current_color}\n')
                game_data.write(f'{current_shape}\n')
                game_data.write(f'{current_level}\n')
                game_data.close()
                color_text.undraw()
                color_text.draw(character_customization_win)
                character_customization_win.close()

        if 350 <= click.y < 390 and 315 < click.x < 390:
            current_shape = int(current_shape) + 1
            if current_shape == 6:
                current_shape = 1
                game_data = open('game_data.txt', 'w')
                game_data.write(f'{current_color}\n')
                game_data.write(f'{current_shape}\n')
                game_data.write(f'{current_level}\n')
                game_data.close()
                shape_text.undraw()
                shape_text.draw(character_customization_win)
                character_customization_win.close()
            else:
                game_data = open('game_data.txt', 'w')
                game_data.write(f'{current_color}\n')
                game_data.write(f'{current_shape}\n')
                game_data.write(f'{current_level}\n')
                game_data.close()
                shape_text.undraw()
                shape_text.draw(character_customization_win)
                character_customization_win.close()

        if 300 <= click.y < 340 and 10 < click.x < 100:
            current_color = int(current_color) - 1
            if current_color == 0:
                current_color = 14
                game_data = open('game_data.txt', 'w')
                game_data.write(f'{current_color}\n')
                game_data.write(f'{current_shape}\n')
                game_data.write(f'{current_level}\n')
                game_data.close()
                color_text.undraw()
                color_text.draw(character_customization_win)
                character_customization_win.close()
            else:
                game_data = open('game_data.txt', 'w')
                game_data.write(f'{current_color}\n')
                game_data.write(f'{current_shape}\n')
                game_data.write(f'{current_level}\n')
                game_data.close()
                color_text.undraw()
                color_text.draw(character_customization_win)
                character_customization_win.close()

        if 350 <= click.y < 390 and 10 < click.x < 100:
            current_shape = int(current_shape) - 1
            if current_shape == 0:
                current_shape = 5
                game_data = open('game_data.txt', 'w')
                game_data.write(f'{current_color}\n')
                game_data.write(f'{current_shape}\n')
                game_data.write(f'{current_level}\n')
                game_data.close()
                shape_text.undraw()
                shape_text.draw(character_customization_win)
                character_customization_win.close()
            else:
                game_data = open('game_data.txt', 'w')
                game_data.write(f'{current_color}\n')
                game_data.write(f'{current_shape}\n')
                game_data.write(f'{current_level}\n')
                game_data.close()
                shape_text.undraw()
                shape_text.draw(character_customization_win)
                character_customization_win.close()

        else:
            character_customization_win.close()

class Character :
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        color_dict: Dict[str, List[str]] =\
             {'color_1': ["Aquamarine", "#72e5be"] \
            , 'color_2': ["Blue", "#0000b2"] \
            , 'color_3': ["Bright Green", "#00cd00"] \
            , 'color_4': ["Brown", "#4c3100"] \
            , 'color_5': ["Dark Green", "#005900"] \
            , 'color_6': ["Gold", "#ffd700"] \
            , 'color_7': ["Gray", "#4c4c4c"] \
            , 'color_8': ["Orange", "#ffa500"] \
            , 'color_9': ["Pink", "#ff6666"] \
            , 'color_10': ["Purple", "#660066"] \
            , 'color_11': ["Red", "#b20000"] \
            , 'color_12': ["Tan", "#d2b48c"] \
            , 'color_13': ["White", "#ffffff"] \
            , 'color_14': ["Yellow", "#ffff00"]}
        shape_dict: Dict[str, Polygon] = {'shape_1': \
        Polygon([Point(self.x - 25, self.y)\
        , Point(self.x + 25, self.y + 20)\
        , Point(self.x + 25, self.y - 20)]), 'shape_2': \
        Polygon([Point(self.x, self.y - 25)\
        , Point(self.x - 25, self.y)\
        , Point(self.x, self.y + 25)\
        , Point(self.x + 25, self.y)]), 'shape_3': \
        Polygon([Point(self.x, self.y - 25)\
        , Point(self.x - 25, self.y - 15)\
        , Point(self.x - 15, self.y + 20)\
        , Point(self.x + 15, self.y + 20)\
        , Point(self.x + 25, self.y - 15)]), 'shape_4': \
        Polygon([Point(self.x + 10, self.y - 25)\
        , Point(self.x - 10, self.y - 25)\
        , Point(self.x - 20, self.y)\
        , Point(self.x - 10, self.y + 25)\
        , Point(self.x + 10, self.y + 25)\
        , Point(self.x + 20, self.y)]), 'shape_5': \
        Polygon([Point(self.x + 9, self.y - 25)\
        , Point(self.x - 9, self.y - 25)\
        , Point(self.x - 25, self.y - 9)\
        , Point(self.x - 25, self.y + 9)\
        , Point(self.x - 9, self.y + 25)\
        , Point(self.x + 9, self.y + 25)\
        , Point(self.x + 25, self.y + 9)\
        , Point(self.x + 25, self.y - 9)])}
        self.color_dict = color_dict
        self.shape_dict = shape_dict
        game_data = open('game_data.txt', 'r')
        game_data_list: List[int] = []
        for entry in game_data.readlines():
            game_data_list.append(entry.strip())
        current_color: int = game_data_list[0]
        current_shape: int = game_data_list[1]
        self.shape = shape_dict[f"shape_{current_shape}"]
        self.color = color_dict[f"color_{current_color}"][1:2]
        self.polygon_1 = self.shape

    def draw(self, win: GraphWin):
        self.polygon_1.draw(win)
        self.polygon_1.setFill(self.color)

    def update(self, bool_1, win: GraphWin):
        self.x += self.vx
        self.y += self.vy
        if bool_1 == False:
            key_press = 0
        if bool_1 == True:
            key_press = win.checkKey()
        if key_press == "w" and (self.y != -400 and self.y != 800):
            self.vy -= 5
            self.y += self.vy
        if key_press == "a" and (self.x != -400 and self.x != 800):
            self.vx -= 5
            self.x += self.vx
        if key_press == "s" and (self.y != -400 and self.y != 800):
            self.vy += 5
            self.y += self.vy
        if key_press == "d" and (self.x != -400 and self.x != 800):
            self.vx += 5
            self.x += self.vx
        self.polygon_1.move(self.vx, self.vy)
        self.vx = 0
        self.vy = 0

    def char_collision_with_en(self, enemies_lst: list):
        for f in enemies_lst:
            if int(math.sqrt((int(f.x) - int(self.x)) ** 2\
                             + (int(f.y) - int(self.y)) ** 2)) <= 43:
                return False
            if int(math.sqrt((int(self.x) - int(f.x)) ** 2\
                             + (int(self.y) - int(f.y)) ** 2)) <= 43:
                return False
            else:
                return True

class Enemy:
    def __init__(self, x: int, y: int, color: int):
        self.x = x
        self.y = y
        vel_y = random.randint(-100 * color, 100 * color) / 100
        self.vy = vel_y
        self.vx = 0
        self.enemy_polygon = Polygon([Point(self.x, self.y - 25)\
        , Point(self.x - 13, self.y - 20), Point(self.x - 25, self.y - 7)\
        , Point(self.x - 25, self.y + 7), Point(self.x - 13, self.y + 20)\
        , Point(self.x, self.y + 25), Point(self.x + 13, self.y + 20)\
        , Point(self.x + 25, self.y + 7), Point(self.x + 25, self.y - 7)\
        , Point(self.x + 13, self.y - 20)])
        self.line_1 = Line(Point(self.x + 18, self.y + 18)\
                           , Point(self.x - 20, self.y - 18))
        self.line_2 = Line(Point(self.x + 18, self.y - 18)\
                           , Point(self.x - 20, self.y + 18))
        if color == 1:
            self.color = "#ABCDEF"
        if color == 2:
            self.color = "#800080"
        if color == 3:
            self.color = "#BB0044"
        if color == 4:
            self.color = "#FB2E01"
        if color >= 5:
            self.color = "#FF0000"

    def draw(self, win: GraphWin):
        self.enemy_polygon.draw(win)
        self.line_1.draw(win)
        self.line_2.draw(win)
        self.enemy_polygon.setFill(f"{self.color}")

    def update(self):
        self.x += self.vx
        self.y += self.vy
        # print(f"X-val{self.x}")
        # print(f"Y-val{self.y}")
        en_point_lst = self.enemy_polygon.getPoints()
        for en_point in en_point_lst:
            if int(en_point.getY()) <= 0 or (en_point.getY()) >= 400:
                self.vy = self.vy * -1
        self.enemy_polygon.move(self.vx, self.vy)
        self.line_1.move(self.vx, self.vy)
        self.line_2.move(self.vx, self.vy)

def main():
    title_screen_bool = title_screen()
    while title_screen_bool == True :
        x = main_menu()
        if x == "start_new_game":
            title_screen_bool = False
            play_level(1)
            title_screen_bool = True

        if x == "continue":
            title_screen_bool = False
            continue_func()
            title_screen_bool = True

        if x == "load_game":
            title_screen_bool = False
            load_game()
            title_screen_bool = True

        if x == "character_customiztion":
            title_screen_bool = False
            character_customization()
            title_screen_bool = True

main()
