import pygame
import math

from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# global background_color, background_color_board
background_color = (240, 230, 140)
background_color_board = (255, 0, 255)
screen.fill(background_color)

SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()

img = pygame.image.load('wood.png')
img_width, img_height = img.get_size()

# While loop will continue work until runnning become False
running = True

# number of rectangles on baord
number_rectangles = 9

# Array for empty & vacant positions
space_area = ''
board_array = [1, 2, 3,
               5, space_area, 8,
               6, 7, 4]
board_array1 = [1, 2, 3,
               5, space_area, 8,
               6, 7, 4,9,10,11,12,13,14,15]

temp_array = board_array[:]

'''# Final array has the final arrangement for the numbers in sequnce then to be compared with 
board_array to descide if the user win the game 
'''
final_array = []
for num in range(number_rectangles - 1):
    final_array.append(num + 1)
final_array.append(space_area)
'''# Final array has the final arrangement for the numbers in sequnce then to be compared with 
board_array to descide if the user win the game 
'''
# Font size for numbers on the big board
number_font = pygame.font.Font(None, 150)

# Font size for numbers on the big board
small_number_font = pygame.font.Font(None, 70)

# divide screen width by 4 to use the middle area for the board
img_wid = SCREEN_WIDTH / 4
small_rectangle_dimension = 70

# X, Y for numbers on the game board
number_on_board_x1 = img_wid + 50
number_on_board_x2 = img_wid + 200

number_on_board_y1 = 180
number_on_board_y2 = number_on_board_y1 + 150

i, j = 0, 0
numbers_big_board_xy = []
for num in range(number_rectangles):
    numbers_big_board_xy.append((number_on_board_x1, number_on_board_y1))
    if i < math.sqrt(number_rectangles) - 1:
        i += 1
        j = 0
        number_on_board_x1 = number_on_board_x2
        number_on_board_x2 += 150
    else:
        i, j = 0, 0
        number_on_board_y1 = number_on_board_y2
        number_on_board_y2 = number_on_board_y1 + 150
        number_on_board_x1 = img_wid + 50
        number_on_board_x2 = img_wid + 200
# X, Y for numbers on the game board

# X, Y for small board rectangles, START
x1_small_board = img_wid * 3 + 20
x2_small_board = x1_small_board + small_rectangle_dimension

y1_small_board = 10
y2_small_board = y1_small_board + small_rectangle_dimension

i, j = 0, 0
small_rectangle_xy = []
for num in range(number_rectangles):
    small_rectangle_xy.append((x1_small_board, y1_small_board, small_rectangle_dimension, small_rectangle_dimension))
    if i < round(math.sqrt(number_rectangles)) - 1:
        j = 0
        i += 1
        x1_small_board = x2_small_board
        x2_small_board += small_rectangle_dimension
    else:
        y1_small_board = y2_small_board
        y2_small_board += small_rectangle_dimension
        j, i = 0, 0
        x1_small_board = img_wid * 3 + 20
        x2_small_board = x1_small_board + small_rectangle_dimension
# X, Y for small board rectangles, END

# X, Y for numbers on the small board
number_small_board_x1 = img_wid * 3 + 20
number_small_board_x2 = number_small_board_x1 + small_rectangle_dimension

number_small_board_y1 = 10
number_small_board_y2 = number_small_board_y1 + small_rectangle_dimension

i, j = 0, 0
numbers_small_board_xy = []
for num in range(number_rectangles):
    numbers_small_board_xy.append((number_small_board_x1, number_small_board_y1))
    if i < math.sqrt(number_rectangles) - 1:
        i += 1
        j = 0
        number_small_board_x1 = number_small_board_x2
        number_small_board_x2 += small_rectangle_dimension
    else:
        i, j = 0, 0
        number_small_board_y1 = number_small_board_y2
        number_small_board_y2 = number_small_board_y1 + small_rectangle_dimension
        number_small_board_x1 = img_wid * 3 + 20
        number_small_board_x2 = number_small_board_x1 + small_rectangle_dimension
# X, Y for numbers on the small board


rectangle_color = (0, 0, 0)
# global rectangle_dimension, rectangle_x, rectangle_y, rectangle_thickness
big_rectangle_dimension = 150
rectangle_x = img_wid
rectangle_y = 150
rectangle_thickness = 10
rectangle_thickness_clear = 0

player_name = "Player Name: "
player_font = pygame.font.Font(None, 50)

quit_game = "Quit"

# X,Y for each big rectangle
x1 = img_wid
x2 = x1 + big_rectangle_dimension

y1 = rectangle_y
y2 = y1 + big_rectangle_dimension

number_sqrt = round(math.sqrt(number_rectangles))
big_rectangle_xy = []
i, j = 0, 0
for num in range(number_rectangles):
    big_rectangle_xy.append((x1, y1, big_rectangle_dimension, big_rectangle_dimension))
    if i < number_sqrt - 1:
        x1 = x2
        x2 += big_rectangle_dimension
        j = 0
        i += 1

    else:
        i = 0
        y1 = y2
        y2 += big_rectangle_dimension
        j += 1
        x1 = img_wid
        x2 = x1 + big_rectangle_dimension
# X,Y for each big rectangle

# Location for old and new number to be used in dict locations
old_new_locations = [(0, 1, 3,0,0), (1, 2, 4, 0,0), (2, 5, 1,0,0),
                     (3, 0, 4, 6,0), (4, 1, 5, 7, 3), (5, 8, 4, 2,0),
                     (6, 3, 7,0,0), (7, 6, 4, 8,0), (8, 7, 5,0,0)]
old_new_locations1 = [(0, 1, 4), (1, 2, 5, 0), (2, 3,6, 1),(3,7,2),
                     (4, 0, 5, 8), (5, 1, 6, 9, 4), (6, 2, 7, 10,5),(7,11,6,3),
                     (8, 4, 9,12), (9, 5, 10, 13,8), (10, 6, 11,14,9),(11,15,10,7),
                     (12,8,13),(13,12,9,14),(14,13,10,15),(15,14,11)]

dict_locations = {k: v for k, v in zip(big_rectangle_xy, old_new_locations)}
# Location for old and new number to be used in dict locations


# move number to empty position based on mouse click by user action
def move_to_rectangle(**move_para):
    global numbers_big_board_xy, background_color, board_array, space_area, rectangle_thickness_clear

    # Swap old number and put space in the old location
    board_array[move_para['board_new_location']] = board_array[move_para['board_old_location']]
    board_array[move_para['board_old_location']] = space_area

    # Draw black rectangle to hide the old number
    draw_rect(rectangle_color=background_color,
              rectangle_xy=move_para['mouse_pos_xy'],
              rectangle_thickness_clear=rectangle_thickness_clear)
# move number to empty position based on mouse click by user action


# function to be called after mouse position matching in big_rectangle_dict
def big_rectangle_func(**rect_para):
    global board_array, background_color, space_area, number_font

    click1 = pygame.mouse.get_pressed()
    if click1[0] == 1:
        if board_array[rect_para['new_location_xy1']] == space_area:
            move_to_rectangle(board_old_location=rect_para['old_location_xy'],
                              board_new_location=rect_para['new_location_xy1'],
                              mouse_pos_xy=rect_para['mouse_pos_xy'])
        elif board_array[rect_para['new_location_xy2']] == space_area:
            move_to_rectangle(board_old_location=rect_para['old_location_xy'],
                              board_new_location=rect_para['new_location_xy2'],
                              mouse_pos_xy=rect_para['mouse_pos_xy'])
        elif board_array[rect_para['new_location_xy3']] == space_area:
            move_to_rectangle(board_old_location=rect_para['old_location_xy'],
                              board_new_location=rect_para['new_location_xy3'],
                              mouse_pos_xy=rect_para['mouse_pos_xy'])
        elif board_array[rect_para['new_location_xy4']] == space_area:
            move_to_rectangle(board_old_location=rect_para['old_location_xy'],
                              board_new_location=rect_para['new_location_xy4'],
                              mouse_pos_xy=rect_para['mouse_pos_xy'])


# function to be called after mouse position matching in big_rectangle_dict


# function to be called after mouse position matching in big_rectangle_dict
func_dict=[]
for num in range(number_rectangles):
    func_dict.append(big_rectangle_func)

big_rectangle_dict = {k: v for k, v in zip(big_rectangle_xy, func_dict)}
# function to be called after mouse position matching in big_rectangle_dict


# Function to display exit msg when the user click quit or press ESC
def close_program(**close_para):
    while True:
        pygame.draw.rect(screen, (255, 0, 0),
                         (close_para['rect_x_pos'], close_para['rect_y_pos'], close_para['rect_width'],
                          close_para['rect_height']), close_para['rect_thickness'])
        close_font = pygame.font.Font(None, 50)
        closing = close_font.render(close_para['text'], True, close_para['font_color'])
        screen.blit(closing, (close_para['screen_x'], close_para['screen_y']))
        pygame.display.flip()
        for event_key in pygame.event.get():
            if event_key.type == KEYDOWN:
                if event_key.key in (K_ESCAPE, K_y):
                    return False
                elif event_key.key in (K_SPACE, K_n):
                    return True


# Function to display exit msg when the user click quit or press ESC

# Function to get player name from the user
def get_player_name():
    name = ''
    running1 = True
    global background_color
    close = "Please enter your name"
    close_font = pygame.font.Font(None, 50)
    closing = close_font.render(close, True, (255, 0, 0))
    screen.blit(closing, (150, 250))
    pygame.display.flip()

    while running1:
        for event_key in pygame.event.get():
            if event_key.type == KEYDOWN:
                if event_key.key == K_ESCAPE:
                    running1 = False
                elif event_key.unicode.isalpha() or event_key.unicode.isdigit() or event_key.key == K_SPACE:
                    name += event_key.unicode
                elif event_key.key == K_BACKSPACE:
                    name = name[:-1]
                    screen.fill(background_color)
                elif event_key.key in (K_KP_ENTER, K_RETURN):
                    return name
        closing1 = close_font.render(name, True, (255, 0, 0))
        screen.blit(closing, (150, 250))
        screen.blit(closing1, (150, 300))
        pygame.display.flip()
# Function to get player name from the user


player1_name = get_player_name()
screen.fill(background_color)


# Function to display Quit button
def button(**button_para):
    cursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    global background_color, quit_game, SCREEN_WIDTH, SCREEN_HEIGHT

    running1 = True
    if button_para['rect_width'] + button_para['rect_x'] > cursor[0] > button_para['rect_x'] and \
            button_para['rect_height'] + button_para['rect_y'] > cursor[1] > button_para['rect_y']:
        quit_render = button_para['object_font'].render(quit_game, True, background_color)
        screen.blit(quit_render, (button_para['blit_x'], button_para['blit_y']))
        if click[0] == 1:
            while running1:
                background_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
                if close_program(text="Do you want to exit? (Yes, No)", rect_x_pos=140, rect_y_pos=240,
                                 rect_width=510,
                                 rect_height=50,
                                 font_color=(0, 0, 0),
                                 screen_x=150,
                                 screen_y=250,
                                 rect_thickness=0):
                    # retrieve old display after removing dialog
                    screen.blit(background_surface, (0, 0))
                    screen.fill(background_color)
                    running1 = False
                else:
                    pygame.quit()
# Function to display Quit button


# Check which number clicked and call Move_to_rectangle to move it based on mouse click
def move_number(**move_param):
    # cursor to save mouse cursor coordinates and Click to show which mouse button pressed
    cursor = pygame.mouse.get_pos()

    global number_font, big_rectangle_dimension, background_color_board, background_color, numbers_big_board_xy
    global board_array, space_area, big_rectangle_dict, dict_locations

    rect_x1, rect_y1, rect_x2, rect_y2 = move_param['mouse_pos']

    old_location_xy, new_location_xy1, \
    new_location_xy2, new_location_xy3, new_location_xy4 = dict_locations[move_param['mouse_pos']]

    if rect_x2 + rect_x1 > cursor[0] > rect_x1 and rect_y2 + rect_y1 > cursor[1] > rect_y1:
        player_render1 = number_font.render(str(move_param['board_number']), True, background_color_board)
        screen.blit(player_render1, move_param['blit_xy'])

        # Call dictionary, mouse pos as key, moving numbers as a value
        big_rectangle_dict[move_param['mouse_pos']](old_location_xy=old_location_xy,
                                                    new_location_xy1=new_location_xy1,
                                                    new_location_xy2=new_location_xy2,
                                                    new_location_xy3=new_location_xy3,
                                                    new_location_xy4=new_location_xy4,
                                                    mouse_pos_xy=move_param['mouse_pos'])
        # pygame.display.flip()
        # screen.fill(background_color)
# Check which number clicked and call Move_to_rectangle to move it based on mouse click


# Function to Draw rectangles as per the given parameters
def draw_rect(**rect):
    global screen, rectangle_color, rectangle_thickness
    rect_x1, rect_y1, rect_x2, rect_y2 = rect['rectangle_xy']

    pygame.draw.rect(screen,
                     rect['rectangle_color'],
                     (rect_x1, rect_y1,
                      rect_x2,
                      rect_y2),
                     rect['rectangle_thickness_clear'])


# Function to Draw rectangles as per the given parameters


# Count how many numbers not arranged in the correct position
def count_numbers():
    global temp_array, board_array
    count = 0
    j = 1

    for row in temp_array:
        if row != j:
            count += 1
        j += 1

    return count
# Count how many numbers not arranged in the correct position


# List for goal board numbers
goal_board_numbers = []

# main program loop start here
while running:
    # List for game board numbers
    game_board_numbers = []

    #global rectangle_thickness

    #pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                # Copy current display to background before called close dialog
                background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
                if close_program(text="Do you want to exit? (Yes, No)", rect_x_pos=140, rect_y_pos=240, rect_width=510,
                                 rect_height=50, font_color=(0, 0, 0), screen_x=150, screen_y=250, rect_thickness=0):
                    running = True
                    # retrieve old display after removing dialog
                    screen.blit(background, (0, 0))
                    screen.fill(background_color)
                else:
                    running = False

    # Wood sign board for player name
    screen.blit(img, (img_wid, 0))
    player_render = player_font.render(player_name, True, (0, 0, 0))
    player_name_render = player_font.render(player1_name, True, (0, 0, 0))
    screen.blit(player_render, (img_wid + 10, 80))
    screen.blit(player_name_render, (img_wid + 240, 80))

    # Wood sign board for Quit
    screen.blit(img, ((img_wid * 2.5), 0))

    # Dislay Quit on the wood board
    player_render = player_font.render(quit_game, True, (0, 0, 0))
    screen.blit(player_render, (img_wid * 2.6, 80))

    # Display rectangles on the goal board
    for num in range(number_rectangles):
        draw_rect(rectangle_color=rectangle_color ,rectangle_xy=small_rectangle_xy[num], rectangle_thickness_clear=rectangle_thickness)

    # Numbers on the goal board
    for final in final_array:
        goal_board_numbers.append(small_number_font.render(str(final), True, (0, 0, 0)))

    # blit number as per array_number position
    for i, num in enumerate(numbers_small_board_xy):
        screen.blit(goal_board_numbers[i], num)

    # Display big rectangles for the numbers grid
    for num in range(number_rectangles):
        draw_rect(rectangle_color=rectangle_color,rectangle_xy=big_rectangle_xy[num], rectangle_thickness_clear=rectangle_thickness)

    # Numbers on the big board
    for i, final in enumerate(board_array):
        # print('final',board_array)
        game_board_numbers.append(number_font.render(str(final), True, (0, 0, 0)))

    # blit numbers on the big board
    for num, final in enumerate(numbers_big_board_xy):
        screen.blit(game_board_numbers[num], final)

    # Function for Quit button only
    button(blit_x=img_wid * 2.6, blit_y=80, rect_x=img_wid * 2.5, rect_y=0, rect_width=img_width,
           rect_height=img_height, object_font=player_font)

    # Function move_number to move number to empty location (USER ACTION)
    for i in range(number_rectangles):
        move_number(dict_locations=dict_locations,
                    mouse_pos=big_rectangle_xy[i],
                    blit_xy=numbers_big_board_xy[i],
                    board_number=board_array[i]
                    )

    # Check if the user arranged the puzzle as per the original arrangement
    if board_array == final_array:
        final_msg = player_font.render("You won", True, (0, 0, 0))
        screen.blit(final_msg, (200, 200))

    pygame.display.flip()
# main program loop end here
