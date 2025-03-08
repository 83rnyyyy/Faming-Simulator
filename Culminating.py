import pygame
pygame.init()
import sys
import random

# window resolution
WIDTH = 800
HEIGHT = 800
# draw window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# colours
WHITE = (255,255,255)
BLACK = (0,0,0)

# load image
start_menu = pygame.image.load("start_menu.png")
start_button = pygame.image.load("start_button.png")
start_button_hover = pygame.image.load("start_button_hover.png")
instructions_button = pygame.image.load("instructions_button.png")
instructions_button_hover = pygame.image.load("instructions_hover.png")
garden= pygame.image.load("garden4.png")
corn_stage1 = pygame.image.load("corn_1.png")
corn_stage2 = pygame.image.load("corn_2.png")
corn_stage3 = pygame.image.load("corn_3.png")
cabbage_stage1 = pygame.image.load("cabbage_1.png")
cabbage_stage2 = pygame.image.load("cabbage_2.png")
cabbage_stage3 = pygame.image.load("cabbage_3.png")
pumpkin_stage1 = pygame.image.load("pumpkin_1.png")
pumpkin_stage2 = pygame.image.load("pumpkin_2.png")
pumpkin_stage3 = pygame.image.load("pumpkin_3.png")
grape_stage1 = pygame.image.load("grape_1.png")
grape_stage2 = pygame.image.load("grape_2.png")
grape_stage3 = pygame.image.load("grape_3.png")
inventory = pygame.image.load("inventory.png")
character_idle_down = pygame.image.load("down_idle.png")
character_idle_up = pygame.image.load("up_idle.png")
character_idle_right = pygame.image.load("right_idle.png")
character_idle_left = pygame.image.load("left_idle.png")
character_moving_down1 = pygame.image.load("moving_down1.png")
character_moving_down2 = pygame.image.load("moving_down2.png")
character_moving_left1 = pygame.image.load("moving_left1.png")
character_moving_left2 = pygame.image.load("moving_left2.png")
character_moving_right1 = pygame.image.load("moving_right1.png")
character_moving_right2 = pygame.image.load("moving_right2.png")
character_moving_up1 = pygame.image.load("moving_up1.png")
character_moving_up2 = pygame.image.load("moving_up2.png")
shop_button = pygame.image.load("shop_button.png")
shop_button_hover = pygame.image.load("shop_button_hover.png")
money_symbol = pygame.image.load("money.png")
hud = pygame.image.load("hud.png")
back = pygame.image.load("x.png")
back_hover = pygame.image.load("x_hover.png")
interact_background = pygame.image.load("interact_background.png")
well = pygame.image.load("well.png")
day_symbol = pygame.image.load("clock.png")
empty_bucket = pygame.image.load("empty_bucket.png")
water_bucket = pygame.image.load("water_bucket.png")
crop_shop_background =  pygame.image.load("crop_shop.png")
corn_shop = pygame.image.load("item_shop_corn.png")
corn_buy_button = pygame.image.load("corn_price.png")
shop_corn_bg = pygame.image.load("shop_corn_bg.png")
crop_type_corn = pygame.image.load("crop_type_corn.png")
corn_buy_button_hover = pygame.image.load("corn_buy_button_hover.png")
corn_inventory = pygame.image.load("corn_inventory.png")
cabbage_shop = pygame.image.load("item_shop_cabbage.png")
cabbage_buy_button = pygame.image.load("cabbage_price.png")
shop_cabbage_bg = pygame.image.load("shop_cabbage_bg.png")
crop_type_cabbage = pygame.image.load("crop_type_cabbage.png")
cabbage_buy_button_hover = pygame.image.load("cabbage_buy_button_hover.png")
cabbage_inventory = pygame.image.load("cabbage_inventory.png")
pumpkin_shop = pygame.image.load("item_shop_pumpkin.png")
pumpkin_buy_button = pygame.image.load("pumpkin_price.png")
shop_pumpkin_bg = pygame.image.load("shop_pumpkin_bg.png")
crop_type_pumpkin = pygame.image.load("crop_type_pumpkin.png")
pumpkin_buy_button_hover = pygame.image.load("pumpkin_buy_button_hover.png")
pumpkin_inventory = pygame.image.load("pumpkin_inventory.png")
grape_shop = pygame.image.load("item_shop_grape.png")
grape_buy_button = pygame.image.load("grape_price.png")
shop_grape_bg = pygame.image.load("shop_grape_bg.png")
crop_type_grape = pygame.image.load("crop_type_grape.png")
grape_buy_button_hover = pygame.image.load("grape_buy_button_hover.png")
grape_inventory = pygame.image.load("grape_inventory.png")
bed_shop = pygame.image.load("item_shop_bed.png")
bed_buy_button = pygame.image.load("bed_price.png")
shop_bed_bg = shop_corn_bg
furniture_type_bed = pygame.image.load("furniture_type_bed.png")
bed_buy_button_hover = corn_buy_button_hover
tv_shop = pygame.image.load("item_shop_tv.png")
tv_buy_button = pygame.image.load("tv_price.png")
shop_tv_bg = shop_cabbage_bg
furniture_type_tv = pygame.image.load("furniture_type_tv.png")
tv_buy_button_hover = cabbage_buy_button_hover
water_up = pygame.image.load("water_up.png")
water_down = pygame.image.load("water_down.png")
water_right = pygame.image.load("water_right.png")
water_left = pygame.image.load("water_left.png")
house = pygame.image.load("house.png")
garden_house = pygame.image.load("garden_house.png")
rabbit_up1 = pygame.image.load("rabbit_up1.png")
inventory1_select = pygame.image.load("inventory1_select.png")
inventory2_select = pygame.image.load("inventory2_select.png")
inventory3_select = pygame.image.load("inventory3_select.png")
inventory4_select = pygame.image.load("inventory4_select.png")
arrow_right_button_hover = pygame.image.load("next.png")
arrow_right = pygame.image.load("next_hover.png")
go_back_hover = pygame.image.load("return.png")
go_back = pygame.image.load("return_hover.png")
furniture_shop = pygame.image.load("furniture_shop.png")
tool_up = pygame.image.load("tool_up.png")
tool_down = pygame.image.load("tool_down.png")
tool_right = pygame.image.load("tool_right.png")
tool_left = pygame.image.load("tool_left.png")
house_tv = pygame.image.load("house_tv.png")
house_bed = pygame.image.load("house_bed.png")
instructions_page1 = pygame.image.load("instructions_page1.png")
instructions_page2 = pygame.image.load("instructions_page2.png")
next_page = pygame.image.load("next_page.png")
next_page_hover = pygame.image.load("next_page_hover.png")
previous_page = pygame.image.load("previous_page.png")
previous_page_hover = pygame.image.load("previous_page_hover.png")

# Track the state of "f" key
f_key_processed = False
q_key_processed = False

# Mouse click processing flags
mouse_left_click_processed = False

# variable for if the user purchased any crops from the shop
inventory_purchase = False

# image of the crop that the user has bought
inventory1_image = corn_inventory
inventory2_image = corn_inventory
inventory3_image = corn_inventory
inventory4_image = corn_inventory

# control the stage that the crop in each plot is in
plot1_crop_stage = 0
plot2_crop_stage = 0
plot3_crop_stage = 0
plot4_crop_stage = 0

# crop coordinates
CROP_FIELD1_X = 125
CROP_FIELD1_Y = 200

CROP_FIELD2_X = 300
CROP_FIELD2_Y = 200

CROP_FIELD3_X = 125
CROP_FIELD3_Y = 300

CROP_FIELD4_X = 300
CROP_FIELD4_Y = 300

# number of different crops the user has
number_of_crops = 0

# variable for the plot soils having seeds planted
plot1_crop = False
plot2_crop = False
plot3_crop = False
plot4_crop = False

# determine which crop is planted in each plot
plot1_crop_type = None
plot2_crop_type = None
plot3_crop_type = None
plot4_crop_type = None

# constant for what type of crop the crop is 
CORN = "corn"
CABBAGE = "cabbage"
PUMPKIN = "pumpkin"
GRAPE = "grape"

# determine which crop the user bought 
inventory_slot1 = None
inventory_slot2 = None
inventory_slot3 = None
inventory_slot4 = None

# inventory slot selected
item_selected = inventory1_image

# control which slot the user selected to use
inventory_key1 = False
inventory_key2 = False
inventory_key3 = False
inventory_key4 = False

# control what crop the user selected to use
selected_slot = None

# control the player's location
player_x = 400
player_y = 400

# control the rabbit's location 
rabbit_x = 0
rabbit_y = 0

# control which crop the rabbit will attack
crop_random = 0

# control which side the rabbit will appear
rabbit_side = 0

# control when the rabbit appears
rabbit_killed = True

# rabbit animation variable from bottom side
rabbot_aniamtion_bottom = rabbit_up1

# control the x and y coords that the rabbit is trying to get to
crop_field_x = 0
crop_field_y = 0

# control the side that the rabbit will come from
rabbot_side = 0

# number of days in the game
day = 1

# variable for time throuhgout a day
time = 0
time_bool = True

# control when the water animation is active
animation_water = False

# control when the tool animation is active
animation_tool = False

# movement state variables
moving_up = False
moving_down = False
moving_right = False
moving_left = False
RIGHT = 0
LEFT = 1
UP = 2
DOWN = 3
direction = DOWN

# player dimensions
player_size_x = 65
player_size_y = 120

# variable for how much money the player has
money = 50

# crops have not been watered
soil_water = False

# game window constant
IN_MENU = 0
IN_GAME = 1
IN_SHOP = 2
IN_SHOP2 = 3
IN_HOUSE = 4
IN_INSTRUCTIONS1 = 5
IN_INSTRUCTIONS2 = 6

# game window variable
game_window = IN_MENU

# player movement speed
player_speed = 5

# moving animation counter to change movinganimations
moving_animation = 0

# moving animatino counter to change water animation
water_animation = 0

# moving animatino counter to change tool animation
tool_animation = 0

# rabbit animation count to change animations
rabbit_moving = 0

# used to control the framerate
game_clock = pygame.time.Clock()

# variable for if the user picked up water from the well
water = False

# variable for if the user bought or furniture
bed_purchase = False
tv_purchase = False

# control if the character is selecting an inventory item
inventory_key = False

def back_to_menu():
    global game_window, mouse_left_click_processed
    # draw back button
    WINDOW.blit(back, (720, 30))

    # create a mask for back button
    back_button_mask = pygame.mask.from_surface(back)

    # create collision detection rectangle for back button
    back_rectangle = pygame.Rect(720, 30, back.get_width(), back.get_height())

    if back_rectangle.collidepoint(mouse_x, mouse_y) and (game_window == IN_GAME or game_window == IN_INSTRUCTIONS1 or game_window == IN_INSTRUCTIONS2):
        # calculate distance from mouse to image
        local_x = mouse_x - back_rectangle.x
        local_y = mouse_y - back_rectangle.y
        
        # change image if the mouse is over the back button
        if back_button_mask.get_at((local_x, local_y)):
            # draw back button hover
            WINDOW.blit(back_hover, (715, 25))
            # change game window when clicked
            if mouse_left_click and not mouse_left_click_processed:
                mouse_left_click_processed = True
                game_window = IN_MENU

def back_to_game():
    global game_window, mouse_left_click_processed
        # create a mask for back button
    back_button_mask = pygame.mask.from_surface(back)

    # create collision detection rectangle for back button
    back_rectangle = pygame.Rect(720, 105, back.get_width(), back.get_height())

    # draw back button
    WINDOW.blit(back, (720, 100))

    # check if mouse and back button is colliding
    if back_rectangle.collidepoint(mouse_x, mouse_y) and (game_window == IN_SHOP or game_window == IN_SHOP2):
        # calculate distance from mouse to image
        local_x = mouse_x - back_rectangle.x
        local_y = mouse_y - back_rectangle.y

        # check if the mouse is over a non-transparent part of the image
        if back_button_mask.get_at((local_x, local_y)):
            # draw back button hover
            WINDOW.blit(back_hover, (715, 95))
            # change game window when clicked
            if mouse_left_click and not mouse_left_click_processed:
                mouse_left_click_processed = True
                game_window = IN_GAME 

def button_shop(mouse_x, mouse_y, mouse_left_click):
    global game_window
    
    # draw shop button
    WINDOW.blit(shop_button, (650, 10))

    # Create a mask for the shop button
    shop_button_mask = pygame.mask.from_surface(shop_button)

    # Create collision detection rectangle for shop button
    shop_rectangle = pygame.Rect(650, 10, shop_button.get_width(), shop_button.get_height())

    # Check if the mouse is over the shop button
    if shop_rectangle.collidepoint(mouse_x, mouse_y) and game_window == IN_GAME:
        local_x = mouse_x - shop_rectangle.x
        local_y = mouse_y - shop_rectangle.y

        # change image if the mouse is over the shop button
        if shop_button_mask.get_at((local_x, local_y)):
            # draw shop button hover
            WINDOW.blit(shop_button_hover, (647, 7))
            # change game window when clicked
            if mouse_left_click:
                game_window = IN_SHOP

def shop_money():
    # create font for hud
    HUD_FONT = pygame.font.SysFont("retro-pixel-arcade.ttf", 20)

    # create text for money
    MONEY_TEXT = HUD_FONT.render(str(money), True, WHITE)
    
    # draw hud for money
    WINDOW.blit(hud, (650, 30))

    # draw money symbol
    WINDOW.blit(money_symbol, (670, 35))

    # draw money text
    WINDOW.blit(MONEY_TEXT, (720, 47))

def crop_item_shop():
    global game_window, money, inventory_purchase, number_of_crops, inventory1_image, inventory2_image,inventory3_image, inventory4_image
    global inventory_slot1, inventory_slot2, inventory_slot3, inventory_slot4, mouse_left_click_processed, money_text
    # draw item shop background
    WINDOW.blit(crop_shop_background, (0,0))

    # draw corn background in shop
    WINDOW.blit(shop_corn_bg, (0,0))

    # Create a mask for the corn background
    corn_bg_mask = pygame.mask.from_surface(shop_corn_bg)

    # create collision detection rectangle for corn background
    corn_bg_rect = pygame.Rect(0, 0 , shop_corn_bg.get_width(), shop_corn_bg.get_height())

    # check if background and mouse is collding
    if corn_bg_rect.collidepoint(mouse_x, mouse_y):
        # calculate distance from mouse to image
        local_x1 = mouse_x - corn_bg_rect.x
        local_y1 = mouse_y - corn_bg_rect.y

        # check if the mouse is over a non-transparent part of the image
        if corn_bg_mask.get_at((local_x1, local_y1)):
            # draw crop type
            WINDOW.blit(crop_type_corn, (0,0))
        else:
            WINDOW.blit(corn_shop, (0,0))

    # create a mask for buy button
    corn_buy_button_mask = pygame.mask.from_surface(corn_buy_button)

    # create collisiion detection rectangle for buy corn buy button
    corn_buy_button_rect = pygame.Rect(0,0, corn_buy_button.get_width(), corn_buy_button.get_height())

    if corn_buy_button_rect.collidepoint(mouse_x, mouse_y):
        # calculate distance from mouse to image
        local_x1 = mouse_x - corn_buy_button_rect.x
        local_y1 = mouse_y - corn_buy_button_rect.y

        # check if the mouse is over a non-transparent part of the image
        if corn_buy_button_mask.get_at((local_x1, local_y1)):
            # draw buy button hover
            WINDOW.blit(corn_buy_button_hover, (0,0))

            # buy corn
            if mouse_left_click and number_of_crops < 4 and money >= 10 and not mouse_left_click_processed:
                money = money - 10
                if number_of_crops == 0:
                    inventory_slot1 = CORN
                    inventory1_image = corn_inventory
                    inventory_purchase = True
                
                elif number_of_crops == 1:
                    inventory_slot2 = CORN
                    inventory2_image = corn_inventory
                    

                elif number_of_crops == 2:
                    inventory_slot3 = CORN
                    inventory3_image = corn_inventory

                elif number_of_crops == 3:
                    inventory_slot4 = CORN
                    inventory4_image = corn_inventory
                
                number_of_crops = number_of_crops + 1
            # when you click mouse button you only input one time 
            mouse_left_click_processed = True
        else:
            # draw buy button
            WINDOW.blit(corn_buy_button, (0,0))

    # draw cabbage background in shop
    WINDOW.blit(shop_cabbage_bg, (0,0))

    # Create a mask for the cabbage background
    cabbage_bg_mask = pygame.mask.from_surface(shop_cabbage_bg)

    # create collision detection rectangle for cabbage background
    cabbage_bg_rect = pygame.Rect(0, 0 , shop_cabbage_bg.get_width(), shop_cabbage_bg.get_height())

    # check if background and mouse is collding
    if cabbage_bg_rect.collidepoint(mouse_x, mouse_y):
        # calculate distance from mouse to image 
        local_x1 = mouse_x - cabbage_bg_rect.x
        local_y1 = mouse_y - cabbage_bg_rect.y

        # check if the mouse is over a non-transparent part of the image
        if cabbage_bg_mask.get_at((local_x1, local_y1)):
            # draw crop type
            WINDOW.blit(crop_type_cabbage, (0,0))
        else:
            # draw cabbage
            WINDOW.blit(cabbage_shop, (0,0))


    # create a mask for buy button
    cabbage_buy_button_mask = pygame.mask.from_surface(cabbage_buy_button)

    # create collisiion detection rectangle for buy cabbage buy button
    cabbage_buy_button_rect = pygame.Rect(0,0, cabbage_buy_button.get_width(), cabbage_buy_button.get_height())

    if cabbage_buy_button_rect.collidepoint(mouse_x, mouse_y):
        # calculate distance from mouse to image
        local_x1 = mouse_x - cabbage_buy_button_rect.x
        local_y1 = mouse_y - cabbage_buy_button_rect.y

        # check if the mouse is over a non-transparent part of the image
        if cabbage_buy_button_mask.get_at((local_x1, local_y1)):
            # draw buy button hover
            WINDOW.blit(cabbage_buy_button_hover, (0,0))

            #buy cabbage
            if mouse_left_click and number_of_crops < 4 and money >= 10 and not mouse_left_click_processed:
                money = money - 10
                
                if number_of_crops == 0:
                    inventory_slot1 = CABBAGE
                    inventory1_image = cabbage_inventory
                    inventory_purchase = True
                
                elif number_of_crops == 1:
                    inventory_slot2 = CABBAGE
                    inventory2_image = cabbage_inventory
                    

                elif number_of_crops == 2:
                    inventory_slot3 = CABBAGE
                    inventory3_image = cabbage_inventory

                elif number_of_crops == 3:
                    inventory_slot4 = CABBAGE
                    inventory4_image = cabbage_inventory

                number_of_crops = number_of_crops + 1
            # when you click mouse button you only input one time 
            mouse_left_click_processed = True
        else:
            # draw buy button
            WINDOW.blit(cabbage_buy_button, (0,0))

    # draw pumpkin background in shop
    WINDOW.blit(shop_pumpkin_bg, (0,0))

    # Create a mask for the pumpkin background
    pumpkin_bg_mask = pygame.mask.from_surface(shop_pumpkin_bg)

    # create collision detection rectangle for corn background
    pumpkin_bg_rect = pygame.Rect(0, 0 , shop_pumpkin_bg.get_width(), shop_pumpkin_bg.get_height())

    # check if background and mouse is collding
    if pumpkin_bg_rect.collidepoint(mouse_x, mouse_y):
        # calculate distance from mouse to image
        local_x1 = mouse_x - pumpkin_bg_rect.x
        local_y1 = mouse_y - pumpkin_bg_rect.y

        # check if the mouse is over a non-transparent part of the image
        if pumpkin_bg_mask.get_at((local_x1, local_y1)):
            # draw crop type
            WINDOW.blit(crop_type_pumpkin, (0,0))
        else:
            WINDOW.blit(pumpkin_shop, (0,0))

    # create a mask for buy button
    pumpkin_buy_button_mask = pygame.mask.from_surface(pumpkin_buy_button)

    # create collisiion detection rectangle for buy pumpkin buy button
    pumpkin_buy_button_rect = pygame.Rect(0,0, pumpkin_buy_button.get_width(), pumpkin_buy_button.get_height())

    if pumpkin_buy_button_rect.collidepoint(mouse_x, mouse_y):
        # calculate distance from mouse to image
        local_x1 = mouse_x - pumpkin_buy_button_rect.x
        local_y1 = mouse_y - pumpkin_buy_button_rect.y

        # check if the mouse is over a non-transparent part of the image
        if pumpkin_buy_button_mask.get_at((local_x1, local_y1)):
            # draw buy button hover
            WINDOW.blit(pumpkin_buy_button_hover, (0,0))

            # buy pumpkin
            if mouse_left_click and number_of_crops < 4 and money >= 10 and not mouse_left_click_processed:
                money = money - 10

                if number_of_crops == 0:
                    inventory_slot1 = PUMPKIN
                    inventory1_image = pumpkin_inventory
                    inventory_purchase = True
                
                elif number_of_crops == 1:
                    inventory_slot2 = PUMPKIN
                    inventory2_image = pumpkin_inventory
                    

                elif number_of_crops == 2:
                    inventory_slot3 = PUMPKIN
                    inventory3_image = pumpkin_inventory

                elif number_of_crops == 3:
                    inventory_slot4 = PUMPKIN
                    inventory4_image = pumpkin_inventory
                
                number_of_crops = number_of_crops + 1
            # when you click mouse button you only input one time 
            mouse_left_click_processed = True
        else:
            # draw buy button
            WINDOW.blit(pumpkin_buy_button, (0,0))
    
    # draw grape background in shop
    WINDOW.blit(shop_grape_bg, (0,0))

    # Create a mask for the grape background
    grape_bg_mask = pygame.mask.from_surface(shop_grape_bg)

    # create collision detection rectangle for corn background
    grape_bg_rect = pygame.Rect(0, 0 , shop_grape_bg.get_width(), shop_grape_bg.get_height())

    # check if background and mouse is collding
    if grape_bg_rect.collidepoint(mouse_x, mouse_y):
        # calculate distance from mouse to image
        local_x1 = mouse_x - grape_bg_rect.x
        local_y1 = mouse_y - grape_bg_rect.y

        # check if the mouse is over a non-transparent part of the image
        if grape_bg_mask.get_at((local_x1, local_y1)):
            # draw crop type
            WINDOW.blit(crop_type_grape, (0,0))
        else:
            WINDOW.blit(grape_shop, (0,0))

    # create a mask for buy button
    grape_buy_button_mask = pygame.mask.from_surface(grape_buy_button)

    # create collisiion detection rectangle for buy grape buy button
    grape_buy_button_rect = pygame.Rect(0,0, grape_buy_button.get_width(), grape_buy_button.get_height())

    if grape_buy_button_rect.collidepoint(mouse_x, mouse_y):
        # calculate distance from mouse to image
        local_x1 = mouse_x - grape_buy_button_rect.x
        local_y1 = mouse_y - grape_buy_button_rect.y

        # check if the mouse is over a non-transparent part of the image
        if grape_buy_button_mask.get_at((local_x1, local_y1)):
            # draw buy button hover
            WINDOW.blit(grape_buy_button_hover, (0,0))

            # buy grape
            if mouse_left_click and number_of_crops < 4 and money >= 10 and not mouse_left_click_processed:
                money = money - 10

                if number_of_crops == 0:
                    inventory_slot1 = GRAPE
                    inventory1_image = grape_inventory
                    inventory_purchase = True
                
                elif number_of_crops == 1:
                    inventory_slot2 = GRAPE
                    inventory2_image = grape_inventory
                    

                elif number_of_crops == 2:
                    inventory_slot3 = GRAPE
                    inventory3_image = corn_inventory

                elif number_of_crops == 3:
                    inventory_slot4 = GRAPE
                    inventory4_image = grape_inventory
                
                number_of_crops = number_of_crops + 1
            # when you click mouse button you only input one time 
            mouse_left_click_processed = True
        else:
            # draw buy button
            WINDOW.blit(grape_buy_button, (0,0))

    # create mask for next button
    arrow_right_mask = pygame.mask.from_surface(arrow_right)

    # create collision detection rectangle for next button
    arrow_right_rect = pygame.Rect(0,0, arrow_right.get_width(), arrow_right.get_height())

    # check if mask and mouse is colliding
    if arrow_right_rect.collidepoint(mouse_x, mouse_y):
        # calculate distance from mouse to image
        local_x = mouse_x - arrow_right_rect.x
        local_y = mouse_y - arrow_right_rect.y

        # check if the mouse is over a non-transparent part of the image
        if arrow_right_mask.get_at((local_x, local_y)):
            # draw next button hover
            WINDOW.blit(arrow_right_button_hover, (0,0))
            # change game window when clicked
            if mouse_left_click:
                game_window = IN_SHOP2
        else:
            # draw next button
            WINDOW.blit(arrow_right, (0,0))   

    back_to_game()
    
    shop_money()

def furniture_item_shop():
    global game_window, money, mouse_left_click_processed, bed_purchase, tv_purchase

    # draw furniture shop
    WINDOW.blit(furniture_shop, (0,0))

    back_to_game()

    # draw bed in shop
    WINDOW.blit(shop_bed_bg, (0,0))

    # Create a mask for the bed background
    bed_bg_mask = pygame.mask.from_surface(shop_bed_bg)

    # create collision detection rectangle for bed background
    bed_bg_rect = shop_bed_bg.get_rect(topleft = (0,0))

    # check if the mouse is over a non-transparent part of the image
    if bed_bg_mask.get_at((mouse_x - bed_bg_rect.x, mouse_y - bed_bg_rect.y)):
        # draw furniture type
        WINDOW.blit(furniture_type_bed, (0,0))
    else:
        # draw bed
        WINDOW.blit(bed_shop, (0,0))

    # create a mask for buy button
    bed_buy_button_mask = pygame.mask.from_surface(bed_buy_button)

    # create collisiion detection rectangle for buy bed buy button
    bed_buy_button_rect = bed_buy_button.get_rect(topleft = (0,0))

    # check if the mouse is over a non-transparent part of the image
    if bed_buy_button_mask.get_at((mouse_x - bed_buy_button_rect.x, mouse_y - bed_buy_button_rect.y)):
        # draw bed buy button hover
        WINDOW.blit(bed_buy_button_hover, (0,0))
        if mouse_left_click and bed_purchase == False and money >= 40:
            bed_purchase = True
            money = money - 40
    else:
        # draw buy button
        WINDOW.blit(bed_buy_button, (0,0))

    # draw background for tv
    WINDOW.blit(shop_tv_bg, (0,0))

    # Create a mask for the tv background
    tv_bg_mask = pygame.mask.from_surface(shop_tv_bg)

    # create collision detection rectangle for tv background
    tv_bg_rect = shop_tv_bg.get_rect(topleft = (0,0))

    # check if the mouse is over a non-transparent part of the image
    if tv_bg_mask.get_at((mouse_x - tv_bg_rect.x, mouse_y - tv_bg_rect.y)):
        # draw furniture type
        WINDOW.blit(furniture_type_tv, (0,0))
    else:
        # draw furniture
        WINDOW.blit(tv_shop, (0,0))

    # create a mask for buy button
    tv_buy_button_mask = pygame.mask.from_surface(tv_buy_button)

    # create collisiion detection rectangle for buy cabbage buy button
    tv_buy_button_rect = tv_buy_button.get_rect(topleft =(0,0))

    # check if the mouse is over a non-transparent part of the image
    if tv_buy_button_mask.get_at((mouse_x - tv_buy_button_rect.x, mouse_y - tv_buy_button_rect.y)):
        # draw buy button
        WINDOW.blit(tv_buy_button_hover, (0,0))
        if mouse_left_click and tv_purchase == False and money >= 50 :
            tv_purchase = True
            money = money - 50
    else:
        # draw buy button hover
        WINDOW.blit(tv_buy_button, (0,0))

    # create mask for furniture go back button
    go_back_mask = pygame.mask.from_surface(go_back)

    # create collision detection rectangle for go back button
    go_back_rect = go_back.get_rect(topleft = (0,0))

    # check if the mouse is over a non-transparent part of the image
    if go_back_mask.get_at((mouse_x - go_back_rect.x, mouse_y - go_back_rect.y)):
        # draw button hover
        WINDOW.blit(go_back_hover, (0,0))
        # change game window
        if mouse_left_click:
            game_window = IN_SHOP
    else:
        # draw button 
        WINDOW.blit(go_back, (0,0))

    shop_money()  

def player_controls():
    global moving_animation, player_x, player_y, direction, current_animation, keys
    # the current image that the player is shown
    current_animation = character_idle_down

    # get all key presses
    keys = pygame.key.get_pressed()

    # update the player movement state variables so that we know which
    # direction they want to move
    if keys[pygame.K_a]:
        moving_left = True
        direction = LEFT
    else:
        moving_left = False
    if keys[pygame.K_d]:
        moving_right = True
        direction = RIGHT
    else:
        moving_right = False
    if keys[pygame.K_w]:
        moving_up = True
        direction = UP
    else:
        moving_up = False
    if keys[pygame.K_s]:
        moving_down = True
        direction = DOWN
    else:
        moving_down = False

    # move the player based on the movement state variables
    if moving_up == True:
        moving_animation = moving_animation + 1
        player_y = player_y - player_speed

        # change animation
        if moving_animation > 10:
            current_animation = character_moving_up1
        else:
            current_animation = character_moving_up2

    if moving_down == True:
        moving_animation = moving_animation + 1
        player_y = player_y + player_speed

        # change animation
        if moving_animation > 10:
            current_animation = character_moving_down1
        else:
            current_animation = character_moving_down2

    if moving_left == True:
        moving_animation = moving_animation + 1
        player_x = player_x - player_speed

        # change animation
        if moving_animation > 10:
            current_animation = character_moving_left1
        else:
            current_animation = character_moving_left2

    if moving_right == True:
        moving_animation = moving_animation + 1
        player_x = player_x + player_speed

        # change animation

        if moving_animation > 10:
            current_animation = character_moving_right1
        else:
            current_animation = character_moving_right2
    
    # to change moving animation
    if moving_animation >= 20:
        moving_animation = 0

    # change idle animation
    if direction == RIGHT and moving_right == False:
        current_animation = character_idle_right
    
    elif direction == LEFT and moving_left == False:
        current_animation = character_idle_left

    elif direction == UP and moving_up == False:
        current_animation = character_idle_up
    
    elif direction == DOWN and moving_down == False:
        current_animation = character_idle_down

def game_house():
    global game_window, moving_animation
    global character_idle_down, character_idle_right, character_idle_left, character_idle_up, character_moving_up1, character_moving_up2, character_moving_left2, character_moving_left1, character_moving_down1, character_moving_down2, character_moving_right2, character_moving_right1
    global player_x, player_y
    global bed_purchase, tv_purchase
    # draw black background
    WINDOW.fill(BLACK)

    # draw house
    WINDOW.blit(house, (50,200))

    player_controls()

    # create collision detection rectangle for character
    character_rectangle = pygame.Rect(player_x, player_y, player_size_x, player_size_y)

    # create door rectangle collision detection
    door_rect = pygame.Rect(380, 520, 80, 40)

    # leave house if player is colliding with the door
    if character_rectangle.colliderect(door_rect):
        game_window = IN_GAME
    
    # create house boundaries
    if player_x < 50:
        player_x = player_x + 5

    if player_x > 650:
        player_x = player_x - 5

    if player_y < 200:
        player_y = player_y + 5

    if player_y > 450:
        player_y = player_y -5

    if bed_purchase:
        WINDOW.blit(house_bed, (650, 305))
    
    if tv_purchase:
        WINDOW.blit(house_tv, (330, 260))

    # draw character
    WINDOW.blit(current_animation, (player_x, player_y))

def inventory_slot_select():
    global item_selected, inventory_key, inventory_key1, inventory_key2, inventory_key3, inventory_key4
    # change image on which inventory slot is selected
    if keys[pygame.K_1]:
        item_selected = inventory1_select
        inventory_key = True
        inventory_key1 = True
        inventory_key2 = False
        inventory_key3 = False
        inventory_key4 = False

    elif keys[pygame.K_2]:
        item_selected = inventory2_select
        inventory_key = True
        inventory_key2 = True
        inventory_key1 = False
        inventory_key3 = False
        inventory_key4 = False

    elif keys[pygame.K_3]:
        item_selected = inventory3_select
        inventory_key = True
        inventory_key3 = True
        inventory_key1 = False
        inventory_key2 = False
        inventory_key4 = False

    elif keys[pygame.K_4]:
        item_selected = inventory4_select
        inventory_key = True
        inventory_key4 = True
        inventory_key3 = False
        inventory_key2 = False
        inventory_key1 = False

def map_boundaries():
    global player_x, player_y
    # create map boundaries
    if player_x >= WIDTH - player_size_x:
        player_x = WIDTH - player_size_x

    if player_x < 0:
        player_x = 0

    if player_y >= HEIGHT - player_size_y:
        player_y = HEIGHT - player_size_y

    if player_y < 100:
        player_y = 100
    
    # draw inventory
    inventory_x, inventory_y = 565, 735
    WINDOW.blit(inventory, (inventory_x, inventory_y))

    # create inventory mask
    inventory_mask = pygame.mask.from_surface(inventory) # create inventory mask

    # calculate offset for inventory collision detection
    inventory_offset = (player_x - inventory_x, player_y - inventory_y)

    # create collision detection for ineventory and character
    if inventory_mask.overlap(character_mask, inventory_offset):
        # boundaries for inventory
        if (player_size_x + player_x - inventory_x)/ (player_size_x + player_x) > (player_y + player_size_y - player_size_y)/(player_y+player_size_y) and direction == DOWN:

            player_y = inventory_y - player_size_y
        elif (player_size_x + player_x - inventory_x)/ (player_size_x + player_x) > (player_y + player_size_y - player_size_y)/(player_y+player_size_y) and direction == RIGHT:
            player_x = inventory_x - player_size_x

        elif (player_size_x + player_x - inventory_x)/ (player_size_x + player_x) < (player_y + player_size_y - player_size_y)/(player_y+player_size_y) and direction == RIGHT:
             player_x = inventory_x - player_size_x

        else:
            player_y = inventory_y - player_size_y

def house_boundaries():
    global game_window
    # create mask for house
    house_mask = pygame.mask.from_surface(garden_house)

    # house coordinates
    house_x = 580
    house_y = 165
    WINDOW.blit(garden_house, (house_x, house_y))

    # calculate offset for house collision detection
    house_offset = (house_x - player_x, house_y - player_y)

    # check if character is overlapping with house
    if character_mask.overlap(house_mask, (house_offset)):
        # change game window
        game_window = IN_HOUSE

def inventory_images():
    # draw inventory selected frame
    if inventory_key == True:
        WINDOW.blit(item_selected, (565, 735))

    # draw crops in inventory
    if inventory_purchase == True:
        if number_of_crops >=1:
            WINDOW.blit(inventory1_image, (568, 740))

        if number_of_crops >= 2:
            WINDOW.blit(inventory2_image, (628, 740))

        if number_of_crops >= 3:
            WINDOW.blit(inventory3_image, (688, 740))

        if number_of_crops >= 4:
            WINDOW.blit(inventory4_image, (745, 740))
            
def inventory_rearragement():
    global inventory_slot1, inventory_slot2, inventory_slot3, inventory_slot4, inventory4_image, inventory2_image, inventory3_image, inventory1_image

    # Rearrange inventory slots
    if inventory_slot1 is None:
        inventory_slot1 = inventory_slot2
        inventory_slot2 = inventory_slot3
        inventory_slot3 = inventory_slot4
        inventory_slot4 = None

    elif inventory_slot2 is None:
        inventory_slot2 = inventory_slot3
        inventory_slot3 = inventory_slot4
        inventory_slot4 = None

    elif inventory_slot3 is None:
        inventory_slot3 = inventory_slot4
        inventory_slot4 = None

     # Update images based on new slot arrangements
    inventory1_image = get_image_for_slot(inventory_slot1)
    inventory2_image = get_image_for_slot(inventory_slot2)
    inventory3_image = get_image_for_slot(inventory_slot3)
    inventory4_image = get_image_for_slot(inventory_slot4)

    # Redraw inventory
    inventory_images()  

# get image for inventory slots
def get_image_for_slot(slot):
    if slot == CORN:
        return corn_inventory 
    elif slot == CABBAGE:
        return cabbage_inventory  
    elif slot == PUMPKIN:
        return pumpkin_inventory
    elif slot == GRAPE:
        return grape_inventory
    else: 
        return None

def plant_crop():
    global plot1_soil,  plot2_soil, plot3_soil, plot4_soil, plot1_crop, plot2_crop, plot3_crop, plot4_crop, plot1_crop_stage
    global plot2_crop_stage, plot3_crop_stage, plot4_crop_stage, plot1_crop_type, plot2_crop_type, plot3_crop_type, plot4_crop_type
    global number_of_crops, f_key_processed
    global inventory_slot1, inventory_slot2, inventory_slot3, inventory_slot4
    if plot1_soil.colliderect(character_rectangle) and soil_water == True and plot1_crop == False and number_of_crops >= 1:
        # draw interact background
        WINDOW.blit(interact_background, (40,223))
        # draw interact text
        WINDOW.blit(INTERACT_TEXT2, (47, 243))
        # check if the user is selecting anything in the inventory
        if inventory_key == True:
             # use the seed to plant
            if keys[pygame.K_f] and not f_key_processed:
                # check if user has anything in their slots 
                if inventory_key1 == True and inventory_slot1 != None:
                    # check what crop they have and remove their crop
                    selected_slot = inventory_slot1
                    plot1_crop = True
                    plot1_crop_type = selected_slot
                    inventory_slot1 = None
                    # begin crop growth
                    plot1_crop_stage = 1
                    # remove a seed
                    number_of_crops = number_of_crops - 1

                # check if user has anything in their slots 
                elif inventory_key2 == True and inventory_slot2 != None:
                    # check what crop they have and remove their crop
                    selected_slot = inventory_slot2
                    plot1_crop = True
                    plot1_crop_type = selected_slot
                    inventory_slot2 = None
                    # begin crop growth
                    plot1_crop_stage = 1
                    # remove a seed
                    number_of_crops = number_of_crops - 1
            
                # check if user has anything in their slots 
                elif inventory_key3 == True and inventory_slot3 != None:
                    # check what crop they have and remove their crop
                    selected_slot = inventory_slot3
                    plot1_crop = True
                    plot1_crop_type = selected_slot
                    inventory_slot3 = None
                    # begin crop growth
                    plot1_crop_stage = 1
                    # remove a seed
                    number_of_crops = number_of_crops - 1

                # check if user has anything in their slots 
                elif inventory_key4 == True and inventory_slot4 != None:
                    # check what crop they have and remove their crop
                    selected_slot = inventory_slot4
                    plot1_crop = True
                    plot1_crop_type = selected_slot
                    inventory_slot4 = None
                    # begin crop growth
                    plot1_crop_stage = 1
                    # remove a seed
                    number_of_crops = number_of_crops - 1

                # make sure crop can be planted once per click
                f_key_processed = True  
                
    elif plot2_soil.colliderect(character_rectangle) and soil_water == True and plot2_crop == False and number_of_crops >= 1:
        # draw interact background
        WINDOW.blit(interact_background, (362,223))
        # draw interact text
        WINDOW.blit(INTERACT_TEXT2, (369, 243))
        # check if the user is selecting anything in the inventory
        if inventory_key == True:
            # use the seed to plant
            if keys[pygame.K_f] and not f_key_processed:
                # check if user has anything in their slots 
                if inventory_key1 == True and inventory_slot1 != None:
                    # check what crop they have and remove their crop
                    selected_slot = inventory_slot1
                    plot2_crop = True
                    plot2_crop_type = selected_slot
                    inventory_slot1 = None
                    # begin crop growth
                    plot2_crop_stage = 1
                    # remove a seed
                    number_of_crops = number_of_crops - 1

                # check if user has anything in their slots 
                elif inventory_key2 == True and inventory_slot2 != None:
                    # check what crop they have and remove their crop
                    selected_slot = inventory_slot2
                    plot2_crop = True
                    plot2_crop_type = selected_slot
                    inventory_slot2 = None
                    # begin crop growth
                    plot2_crop_stage = 1
                    # remove a seed
                    number_of_crops = number_of_crops - 1
                
                # check if user has anything in their slots 
                elif inventory_key3 == True and inventory_slot3 != None:
                    # check what crop they have and remove their crop
                    selected_slot = inventory_slot3
                    plot2_crop = True
                    plot2_crop_type = selected_slot
                    inventory_slot3 = None
                    # begin crop growth
                    plot2_crop_stage = 1
                    # remove a seed
                    number_of_crops = number_of_crops - 1

                # check if user has anything in their slots 
                elif inventory_key4 == True and inventory_slot4 != None:
                    # check what crop they have and remove their crop
                    selected_slot = inventory_slot4
                    plot2_crop = True
                    plot2_crop_type = selected_slot
                    inventory_slot4 = None
                    # begin crop growth
                    plot2_crop_stage = 1
                    # remove a seed
                    number_of_crops = number_of_crops - 1

                # make sure crop can be planted once per click
                f_key_processed = True

    elif plot3_soil.colliderect(character_rectangle) and soil_water == True and plot3_crop == False and number_of_crops >= 1:
        # draw interact background
        WINDOW.blit(interact_background, (40,300))
        # draw interact text
        WINDOW.blit(INTERACT_TEXT2, (47, 320))
        # check if the user is selecting anything in the inventory
        if inventory_key == True:
            # use the seed to plant
            if keys[pygame.K_f] and not f_key_processed:
                # check if user has anything in their slots 
                if inventory_key1 == True and inventory_slot1 != None:
                    # check what crop they have and remove their crop
                    selected_slot = inventory_slot1
                    plot3_crop = True
                    plot3_crop_type = selected_slot
                    inventory_slot1= None
                    # begin crop growth
                    plot3_crop_stage = 1
                    # remove a seed
                    number_of_crops = number_of_crops - 1

                # check if user has anything in their slots 
                elif inventory_key2 == True and inventory_slot2 != None:
                    # check what crop they have and remove their crop
                    selected_slot = inventory_slot2
                    plot3_crop = True
                    plot3_crop_type = selected_slot
                    inventory_slot2 = None
                    # begin crop growth
                    plot3_crop_stage = 1
                    # remove a seed
                    number_of_crops = number_of_crops - 1

                # check if user has anything in their slots 
                elif inventory_key3 == True and inventory_slot3 != None:
                    # check what crop they have and remove their crop
                    selected_slot = inventory_slot3
                    plot3_crop = True
                    plot3_crop_type = selected_slot
                    inventory_slot3 = None
                    # begin crop growth
                    plot3_crop_stage = 1
                    # remove a seed
                    number_of_crops = number_of_crops - 1

                # check if user has anything in their slots 
                elif inventory_key4 == True and inventory_slot4 != None:
                    # check what crop they have and remove their crop
                    selected_slot = inventory_slot4
                    plot3_crop = True
                    plot3_crop_type = selected_slot
                    inventory_slot4 = None
                    # begin crop growth
                    plot3_crop_stage = 1
                    # remove a seed
                    number_of_crops = number_of_crops - 1

                # make sure crop can be planted once per click
                f_key_processed = True

    elif plot4_soil.colliderect(character_rectangle) and soil_water == True and plot4_crop == False and number_of_crops >= 1:
        # draw interact background
        WINDOW.blit(interact_background, (362,300))
        # draw interact text
        WINDOW.blit(INTERACT_TEXT2, (369, 320))
        # check if the user is selecting anything in the inventory
        if inventory_key == True:
            # use the seed to plant
            if keys[pygame.K_f] and not f_key_processed:
                # check if user has anything in their slots 
                if inventory_key1 == True and inventory_slot1 != None:
                    # check what crop they have and remove their crop
                    selected_slot = inventory_slot1
                    plot4_crop = True
                    plot4_crop_type = selected_slot
                    selected_slot = None
                    inventory_slot1 = None
                    # begin crop growth
                    plot4_crop_stage = 1
                    # remove a seed
                    number_of_crops = number_of_crops - 1
                    # make sure that the key is released to press again
                    f_key_processed = True

                # check if user has anything in their slots 
                elif inventory_key2 == True and inventory_slot2 != None:
                    # check what crop they have and remove their crop
                    selected_slot = inventory_slot2
                    plot4_crop = True
                    plot4_crop_type = selected_slot
                    selected_slot = None
                    inventory_slot2 = None
                    # begin crop growth
                    plot4_crop_stage = 1
                    # remove a seed
                    number_of_crops = number_of_crops - 1
                    # make sure that the key is released to press again
                    f_key_processed = True

                # check if user has anything in their slots 
                elif inventory_key3 == True and inventory_slot3 != None:
                    # check what crop they have and remove their crop
                    selected_slot = inventory_slot3
                    plot4_crop = True
                    plot4_crop_type = selected_slot
                    selected_slot = None
                    inventory_slot3 = None
                    # begin crop growth
                    plot4_crop_stage = 1
                    # remove a seed
                    number_of_crops = number_of_crops - 1
                    # make sure that the key is released to press again
                    f_key_processed = True

                # check if user has anything in their slots 
                elif inventory_key4 == True and inventory_slot4 != None:
                    # check what crop they have and remove their crop
                    selected_slot = inventory_slot4
                    plot4_crop = True
                    plot4_crop_type = selected_slot
                    selected_slot = None
                    inventory_slot4 = None
                    # begin crop growth
                    plot4_crop_stage = 1
                    # remove a seed
                    number_of_crops = number_of_crops - 1
            
                # make sure that the key is released to press again
                f_key_processed = True

def time_events():
    global time, time_bool, plot1_crop , plot2_crop , plot3_crop, plot4_crop, day, soil_water, plot1_crop, plot2_crop
    global plot3_crop, plot4_crop, plot1_crop_stage, plot2_crop_stage, plot3_crop_stage, plot4_crop_stage, rabbit_killed
    global rabbit_side, crop_random, crop_field_x, crop_field_y, CROP_FIELD1_X, CROP_FIELD1_Y, CROP_FIELD2_X, CROP_FIELD2_Y
    global CROP_FIELD3_X, CROP_FIELD3_Y, CROP_FIELD4_X, CROP_FIELD4_Y, rabbit_x, rabbit_y
    # make time increase
    if time_bool == True:
        time = time + 5

    

    # increase day count after 1500
    if time % 1500 == 0:
        day = day + 1
        # reset water
        soil_water = False
        # reset time 
        time = 0

        #change stage that the crops are in
        if plot1_crop and plot1_crop_stage <= 2:
            plot1_crop_stage = plot1_crop_stage + 1
        if plot2_crop and plot2_crop_stage <= 2:
            plot2_crop_stage = plot2_crop_stage + 1
        if plot3_crop and plot3_crop_stage <= 2:
            plot3_crop_stage = plot3_crop_stage + 1
        if plot4_crop and plot4_crop_stage <= 2:
            plot4_crop_stage = plot4_crop_stage + 1

        # spawn rabbit
        if rabbit_killed == True and (plot1_crop_stage >= 2 or plot2_crop_stage >= 2 or plot3_crop_stage >= 2 or plot4_crop_stage >= 2) and (plot1_crop == True or plot2_crop == True or plot3_crop == True or plot3_crop): 
            # pick side that the rabbit will spawn from
            rabbit_side = random.randint(1, 2)
            if plot1_crop_stage >= 2 and plot1_crop == True:
                crop_random = 1
            elif plot2_crop_stage >= 2 and plot2_crop == True:
                crop_random = 2
            elif plot3_crop_stage >= 2 and plot3_crop == True:
                crop_random = 3
            elif plot4_crop_stage >= 2 and plot4_crop == True:
                crop_random = 4
            
            # determine which crop field coordinates the rabbit will go to
            if crop_random == 1:
                crop_field_x = CROP_FIELD1_X
                crop_field_y = CROP_FIELD1_Y
                    
            elif crop_random ==2:
                crop_field_x = CROP_FIELD2_X
                crop_field_y = CROP_FIELD2_Y
            
            elif crop_random ==3:
                crop_field_x = CROP_FIELD3_X
                crop_field_y = CROP_FIELD3_Y
            
            elif crop_random ==4:
                crop_field_x = CROP_FIELD4_X
                crop_field_y = CROP_FIELD4_Y
            
            # determine start coordinates for rabbit
            if rabbit_side == 1:
                rabbit_x = random.randint(0, 800)
                rabbit_y = 800

            elif rabbit_side == 2:
                rabbit_x = 0
                rabbit_y = random.randint(400,800)

            rabbit_killed = False      

    # remove crops if not watered throughout the day
    if time == 1499 and soil_water == False:
        plot1_crop = False
        plot2_crop = False
        plot3_crop = False
        plot4_crop = False
        

def change_water_animation():
    global current_animation, animation_water, water_animation
    # Change animation when picking up water
    if animation_water:
        water_animation = water_animation + 1
        if direction == UP:
            current_animation = water_up
        elif direction == DOWN:
            current_animation = water_down
        elif direction == LEFT:
            current_animation = water_left
        elif direction == RIGHT:
            current_animation = water_right

        if water_animation > 10:
            water_animation = 0
            animation_water = False
            # Reset to idle animation
            if direction == RIGHT:
                current_animation = character_idle_right
            elif direction == LEFT:
                current_animation = character_idle_left
            elif direction == UP:
                current_animation = character_idle_up
            elif direction == DOWN:
                current_animation = character_idle_down

def change_tool_animation():
    global current_animation, animation_tool, tool_animation
    # Change animation when picking up tool
    if animation_tool:
        tool_animation = tool_animation + 1
        if direction == UP:
            current_animation = tool_up
        elif direction == DOWN:
            current_animation = tool_down
        elif direction == LEFT:
            current_animation = tool_left
        elif direction == RIGHT:
            current_animation = tool_right

        if tool_animation > 10:
            tool_animation = 0
            animation_tool = False
            # Reset to idle animation
            if direction == RIGHT:
                current_animation = character_idle_right
            elif direction == LEFT:
                current_animation = character_idle_left
            elif direction == UP:
                current_animation = character_idle_up
            elif direction == DOWN:
                current_animation = character_idle_down


def game_garden():
    global player_x, player_y, moving_animation, direction, game_window, time, time_bool, day, water, inventory_purchase, inventory1_image, soil_water
    global plot1_crop, plot2_crop, plot3_crop, plot4_crop
    global character_rectangle, moving_animation, current_animation
    global rabbit_x, rabbit_y, rabbit_killed, crop_field_x, crop_field_y, rabbit_side
    global item_selected, character_mask, current_corn_plot3
    global plot1_crop_stage, plot2_crop_stage, plot3_crop_stage, plot4_crop_stage
    global inventory_key, mouse_left_click_processed, animation_water, water_animation
    global selected_slot, INTERACT_TEXT2, tool_animation, animation_tool
    global inventory_key1, inventory_key2, inventory_key3, inventory_key4, plot1_soil, plot2_soil, plot3_soil, plot4_soil
    global f_key_processed, number_of_crops, plot1_crop_type, plot2_crop_type, plot3_crop_type, plot4_crop_type
    global current_corn_plot1, current_corn_plot2, current_cabbage_plot1, current_cabbage_plot2, current_corn_plot4
    global inventory_slot1, inventory_slot2,inventory_slot3, inventory_slot4, crop_random, money, q_key_processed, rabbit_moving, MONEY_TEXT
    # show image items
    if number_of_crops == 0:
        inventory_purchase == False

    time_events()

    # draw garden
    WINDOW.blit(garden, (-600,0))

    # draw well
    WINDOW.blit(well, (-600, 0))

    player_controls()

    # create collision detection rectangle for character
    character_rectangle = pygame.Rect(player_x, player_y, player_size_x, player_size_y)

    back_to_menu()

    # create a mask for well
    well_mask = pygame.mask.from_surface(well)

    # create mask for character
    character_mask = pygame.mask.from_surface(current_animation)

    # create font and text for interact buttons
    INTERACT_FONT = pygame.font.SysFont("LeagueSpartan-Medium.ttf", 20)
    INTERACT_TEXT = INTERACT_FONT.render("E", True, WHITE)
    INTERACT_TEXT2 = INTERACT_FONT.render("F", True, WHITE)
    INTERACT_TEXT3 = INTERACT_FONT.render("Q", True, WHITE)
    INTERACT_TEXT4 = INTERACT_FONT.render("R", True, WHITE)

    # adjust offset to match well position
    offset = (player_x + 600, player_y)  
    # check collision between well and character
    if well_mask.overlap(character_mask, offset) and water == False:
        # draw interact background
        WINDOW.blit(interact_background, (480,290))
        # draw interact text
        WINDOW.blit(INTERACT_TEXT, (488, 310))
        if keys[pygame.K_e]:
            water_animation = 0
            animation_water = True
            water = True
    
    
    # draw hud for money
    WINDOW.blit(hud, (650, 100))

    # draw hud for day count
    WINDOW.blit(hud, (0, 30))

    # draw money symbol
    WINDOW.blit(money_symbol, (670, 105))

    # draw day symbol
    WINDOW.blit(day_symbol, (15, 30))

    # create font for hud
    HUD_FONT = pygame.font.SysFont("retro-pixel-arcade.ttf", 20)

    # create text for money
    MONEY_TEXT = HUD_FONT.render(str(money), True, WHITE)

    # create text for day count
    DAY_TEXT = HUD_FONT.render("Day " + str(day), True, WHITE)

    # draw day text
    WINDOW.blit(DAY_TEXT, (60, 47))
    
    # draw money text
    WINDOW.blit(MONEY_TEXT, (720, 117))

    map_boundaries()

    # draw shop button
    button_shop(mouse_x, mouse_y, mouse_left_click)

    # draw water bucket
    if water == False:
        WINDOW.blit(empty_bucket, (725, 400))
    else:
        WINDOW.blit(water_bucket, (725, 400))

    # create collision detection rectangle for soil
    soil_rect = pygame.Rect(81, 202, 276, 172)

    plot1_soil = pygame.Rect(81, 202, 138, 86)

    plot2_soil = pygame.Rect(219, 202, 138, 86)

    plot3_soil = pygame.Rect(81, 228, 138, 86)

    plot4_soil = pygame.Rect(219, 288, 138, 86) 

    inventory_slot_select()

    inventory_images()

    # move rabbit until it reaches the crop
    if plot1_crop == True or plot2_crop == True or plot3_crop == True or plot3_crop:
        if rabbit_x < crop_field_x and rabbit_killed == False:
            rabbit_x = rabbit_x + 1
        
        if rabbit_x > crop_field_x and rabbit_killed == False:
            rabbit_x = rabbit_x -1


        if rabbit_y > crop_field_y and rabbit_killed == False:
            rabbit_y = rabbit_y - 1

        if rabbit_y < crop_field_y and rabbit_killed == False:
            rabbit_y = rabbit_y + 1
    
    


    if rabbit_y == crop_field_y and rabbit_x == crop_field_x:
        if crop_random == 1 and plot1_crop:
            plot1_crop = False
            plot1_crop_stage = 0
        elif crop_random == 2 and plot2_crop:
            plot2_crop = False
            plot2_crop_stage = 0
        elif crop_random == 3 and plot3_crop:
            plot3_crop = False
            plot3_crop_stage = 0
        elif crop_random == 4 and plot4_crop:
            plot4_crop = False
            plot4_crop_stage = 0
        
        rabbit_y = -800
        rabbit_x = -800
        rabbit_killed = True

    # collision detection for the entire soil
    if soil_rect.colliderect(character_rectangle) and water == True and soil_water == False:
        # draw interact background
        WINDOW.blit(interact_background, (360, 200))
        # draw interact text
        WINDOW.blit(INTERACT_TEXT, (369, 223))
        if keys[pygame.K_e]:
            soil_water = True
            water = False
            water_animation = 0
            animation_water = True
    
    change_water_animation()


    # collision detection for quarter rectangle of soil
    plant_crop()

    # rearrange inventory
    inventory_rearragement()


    # draw rabbit
    if rabbit_killed == False and (plot1_crop_stage >= 2 or plot2_crop_stage >= 2 or plot3_crop_stage >= 2 or plot4_crop_stage >= 2) and (plot1_crop == True or plot2_crop == True or plot3_crop == True or plot3_crop):
        WINDOW.blit(rabbit_up1, (rabbit_x, rabbit_y))

    # create collision detection rectangle for rabbit
    rabbit_rect = pygame.Rect(rabbit_x, rabbit_y, 70, 70)

    # collision detection between rabbit and character to kill the rabbit
    if rabbit_rect.colliderect(character_rectangle):
        # draw interact background
        WINDOW.blit(interact_background, (rabbit_x - 19, rabbit_y - 19))
        # draw interact text
        WINDOW.blit(INTERACT_TEXT4, (rabbit_x - 10, rabbit_y))
        if keys[pygame.K_r]:
            rabbit_killed = True
            tool_animation = 0
            animation_tool = True
            rabbit_x = -800
            rabbit_y = -800
    
    # change crop stages for plot 1
    if plot1_crop:
        # change image corn stage image when plot 1 crop is corn
        if plot1_crop_type == CORN:
            if plot1_crop_stage == 1:
                current_corn_plot1 = corn_stage1
            elif plot1_crop_stage == 2:
                current_corn_plot1 = corn_stage2
            elif plot1_crop_stage == 3:
                current_corn_plot1 = corn_stage3
            # draw the current corn
            WINDOW.blit(current_corn_plot1, (CROP_FIELD1_X, CROP_FIELD1_Y))

        # change image cabbage stage image when plot 1 crop is cabbage
        elif plot1_crop_type == CABBAGE:
            if plot1_crop_stage == 1:
                current_cabbage_plot1 = cabbage_stage1
            elif plot1_crop_stage == 2:
                current_cabbage_plot1 = cabbage_stage2
            elif plot1_crop_stage == 3:
                current_cabbage_plot1 = cabbage_stage3
            # draw current cabbage
            WINDOW.blit(current_cabbage_plot1, (CROP_FIELD1_X, CROP_FIELD1_Y))
        
        # change image pumpkin stage image when plot 1 crop is pumpkin
        elif plot1_crop_type == PUMPKIN:
            if plot1_crop_stage == 1:
                current_pumpkin_plot1 = pumpkin_stage1
            elif plot1_crop_stage == 2:
                current_pumpkin_plot1 = pumpkin_stage2
            elif plot1_crop_stage == 3:
                current_pumpkin_plot1 = pumpkin_stage3
            # draw the current corn
            WINDOW.blit(current_pumpkin_plot1, (CROP_FIELD1_X, CROP_FIELD1_Y))
        
        # change image pumpkin stage image when plot 1 crop is grape
        elif plot1_crop_type == GRAPE:
            if plot1_crop_stage == 1:
                current_grape_plot1 = grape_stage1
            elif plot1_crop_stage == 2:
                current_grape_plot1 = grape_stage2
            elif plot1_crop_stage == 3:
                current_grape_plot1 = grape_stage3
            # draw the current corn
            WINDOW.blit(current_grape_plot1, (CROP_FIELD1_X, CROP_FIELD1_Y))
        
    # change crop stages for plot 2
    if plot2_crop:
        # change image corn stage image when plot 2 crop is corn
        if plot2_crop_type == CORN:
            if plot2_crop_stage == 1:
                current_corn_plot2 = corn_stage1
            elif plot2_crop_stage == 2:
                current_corn_plot2 = corn_stage2
            elif plot2_crop_stage == 3:
                current_corn_plot2 = corn_stage3
            # draw the current corn
            WINDOW.blit(current_corn_plot2, (CROP_FIELD2_X, CROP_FIELD2_Y))
        # change image cabbage stage image when plot 2 crop is cabbage
        elif plot2_crop_type == CABBAGE:
            if plot2_crop_stage == 1:
                current_cabbage_plot2 = cabbage_stage1
            elif plot2_crop_stage == 2:
                current_cabbage_plot2 = cabbage_stage2
            elif plot2_crop_stage == 3:
                current_cabbage_plot2 = cabbage_stage3
            # draw current cabbage
            WINDOW.blit(current_cabbage_plot2, (CROP_FIELD2_X, CROP_FIELD2_Y))
        
        # change image pumpkin stage image when plot 2 crop is pumpkin
        elif plot2_crop_type == PUMPKIN:
            if plot2_crop_stage == 1:
                current_pumpkin_plot2 = pumpkin_stage1
            elif plot2_crop_stage == 2:
                current_pumpkin_plot2 = pumpkin_stage2
            elif plot2_crop_stage == 3:
                current_pumpkin_plot2 = pumpkin_stage3
            # draw the current pumpkin
            WINDOW.blit(current_pumpkin_plot2, (CROP_FIELD2_X, CROP_FIELD2_Y))
        
        # change image pumpkin stage image when plot 2 crop is grape
        elif plot2_crop_type == GRAPE:
            if plot2_crop_stage == 1:
                current_grape_plot2 = grape_stage1
            elif plot2_crop_stage == 2:
                current_grape_plot2 = grape_stage2
            elif plot2_crop_stage == 3:
                current_grape_plot2 = grape_stage3
            # draw the current corn
            WINDOW.blit(current_grape_plot2, (CROP_FIELD2_X, CROP_FIELD2_Y))
        
    # change crop stages for plot 3
    if plot3_crop:
        # change image corn stage image when plot 3 crop is corn
        if plot3_crop_type == CORN:
            if plot3_crop_stage == 1:
                current_corn_plot3 = corn_stage1
            elif plot3_crop_stage == 2:
                current_corn_plot3 = corn_stage2
            elif plot3_crop_stage == 3:
                current_corn_plot3 = corn_stage3
            # draw the current corn
            WINDOW.blit(current_corn_plot3, (CROP_FIELD3_X, CROP_FIELD3_Y))
        # change image cabbage stage image when plot 3 crop is cabbage
        elif plot3_crop_type == CABBAGE:
            if plot3_crop_stage == 1:
                current_cabbage_plot3 = cabbage_stage1
            elif plot3_crop_stage == 2:
                current_cabbage_plot3 = cabbage_stage2
            elif plot3_crop_stage == 3:
                current_cabbage_plot3 = cabbage_stage3
            # draw current cabbage
            WINDOW.blit(current_cabbage_plot3, (CROP_FIELD3_X, CROP_FIELD3_Y))
        
        # change image pumpkin stage image when plot 2 crop is pumpkin
        elif plot3_crop_type == PUMPKIN:
            if plot3_crop_stage == 1:
                current_pumpkin_plot3 = pumpkin_stage1
            elif plot3_crop_stage == 2:
                current_pumpkin_plot3 = pumpkin_stage2
            elif plot3_crop_stage == 3:
                current_pumpkin_plot3 = pumpkin_stage3
            # draw the current pumpkin
            WINDOW.blit(current_pumpkin_plot3, (CROP_FIELD3_X, CROP_FIELD3_Y))
        
        # change image pumpkin stage image when plot 3 crop is grape
        elif plot3_crop_type == GRAPE:
            if plot3_crop_stage == 1:
                current_grape_plot3 = grape_stage1
            elif plot3_crop_stage == 2:
                current_grape_plot3 = grape_stage2
            elif plot3_crop_stage == 3:
                current_grape_plot3 = grape_stage3
            # draw the current corn
            WINDOW.blit(current_grape_plot3, (CROP_FIELD3_X, CROP_FIELD3_Y))
    
    # change crop stages for plot 4
    if plot4_crop:
        # change image corn stage image when plot 4 crop is corn
        if plot4_crop_type == CORN:
            if plot4_crop_stage == 1:
                current_corn_plot4 = corn_stage1
            elif plot4_crop_stage == 2:
                current_corn_plot4 = corn_stage2
            elif plot4_crop_stage == 3:
                current_corn_plot4 = corn_stage3
            # draw the current corn
            WINDOW.blit(current_corn_plot4, (CROP_FIELD4_X, CROP_FIELD4_Y))
        # change image cabbage stage image when plot 4 crop is cabbage
        elif plot4_crop_type == CABBAGE:
            if plot4_crop_stage == 1:
                current_cabbage_plot4 = cabbage_stage1
            elif plot4_crop_stage == 2:
                current_cabbage_plot4 = cabbage_stage2
            elif plot4_crop_stage == 3:
                current_cabbage_plot4 = cabbage_stage3
            # draw current cabbage
            WINDOW.blit(current_cabbage_plot4, (CROP_FIELD4_X, CROP_FIELD4_Y))
        
        # change image pumpkin stage image when plot 4 crop is pumpkin
        elif plot4_crop_type == PUMPKIN:
            if plot4_crop_stage == 1:
                current_pumpkin_plot4 = pumpkin_stage1
            elif plot4_crop_stage == 2:
                current_pumpkin_plot4 = pumpkin_stage2
            elif plot4_crop_stage == 3:
                current_pumpkin_plot4 = pumpkin_stage3
            # draw the current pumpkin
            WINDOW.blit(current_pumpkin_plot4, (CROP_FIELD4_X, CROP_FIELD4_Y))
        
        # change image pumpkin stage image when plot 1 crop is grape
        elif plot4_crop_type == GRAPE:
            if plot4_crop_stage == 1:
                current_grape_plot4 = grape_stage1
            elif plot4_crop_stage == 2:
                current_grape_plot4 = grape_stage2
            elif plot4_crop_stage == 3:
                current_grape_plot4 = grape_stage3
            # draw the current corn
            WINDOW.blit(current_grape_plot4, (CROP_FIELD4_X, CROP_FIELD4_Y))


    # harvest crops when it reaches stage 3
    if plot1_soil.colliderect(character_rectangle) and plot1_crop_stage == 3 and plot1_crop == True:
        # draw interact background
        WINDOW.blit(interact_background, (40,223))
        # draw interact text
        WINDOW.blit(INTERACT_TEXT3, (47, 243))
        if keys[pygame.K_q] and not q_key_processed:
            plot1_crop = False
            money = money + 25
            q_key_processed = True
            tool_animation = 0
            animation_tool = True

    elif plot2_soil.colliderect(character_rectangle) and plot2_crop_stage == 3 and plot2_crop == True:
        # draw interact background
        WINDOW.blit(interact_background, (362,223))
        # draw interact text
        WINDOW.blit(INTERACT_TEXT3, (369, 243))
        if keys[pygame.K_q] and not q_key_processed:
            plot2_crop = False
            money = money + 25
            q_key_processed = True
            tool_animation = 0
            animation_tool = True

    elif plot3_soil.colliderect(character_rectangle) and plot3_crop_stage == 3 and plot3_crop == True:
        # draw interact background
        WINDOW.blit(interact_background, (40,300))
        # draw interact text
        WINDOW.blit(INTERACT_TEXT3, (47, 320))
        if keys[pygame.K_q] and not q_key_processed:
            plot3_crop = False
            money = money + 25
            q_key_processed = True
            tool_animation = 0
            animation_tool = True
    
    elif plot4_soil.colliderect(character_rectangle) and plot4_crop_stage == 3 and plot4_crop == True:
        # draw interact background
        WINDOW.blit(interact_background, (362,300))
        # draw interact text
        WINDOW.blit(INTERACT_TEXT3, (369, 320))
        if keys[pygame.K_q] and not q_key_processed:
            plot4_crop = False
            money = money + 25
            q_key_processed = True
            tool_animation = 0
            animation_tool = True
    
    change_tool_animation()

    house_boundaries()

    # draw character
    WINDOW.blit(current_animation, (player_x, player_y))

def page1_instructions():
    global game_window

    # draw instructions page 1
    WINDOW.blit(instructions_page1, (0,0))

    # draw back button
    back_to_menu()

    # create a mask for next page button
    next_page_mask = pygame.mask.from_surface(next_page)

    # create collision detection rectangle for next button
    next_page_rect = next_page.get_rect(topleft=(0,0))

    # change next page button if hovered
    if next_page_mask.get_at((mouse_x - next_page_rect.x, mouse_y - next_page_rect.y)):
        WINDOW.blit(next_page_hover, (0,0))
        # change game window
        if mouse_left_click:
            game_window = IN_INSTRUCTIONS2
    else:
        # draw next page button
        WINDOW.blit(next_page, (0,0))

def page2_instructions():
    global game_window

    # draw instructions page 2
    WINDOW.blit(instructions_page2, (0,0))

    # draw back button
    back_to_menu()

    # create a mask for previous page button
    previous_page_mask = pygame.mask.from_surface(previous_page)

    # create collision detection rectangle for previous button
    previous_page_rect = previous_page.get_rect(topleft=(0,0))

    # change next page button if hovered
    if previous_page_mask.get_at((mouse_x - previous_page_rect.x, mouse_y - previous_page_rect.y)):
        WINDOW.blit(previous_page_hover, (0,0))
        # change game window
        if mouse_left_click:
            game_window = IN_INSTRUCTIONS1
    else:
        # draw next page button
        WINDOW.blit(previous_page, (0,0))

# set up the game loop variable to control the game loop
draw_window = True

# the game loop to draw the graphics

while draw_window == True:

    # get mouse buttons
    mouse = pygame.mouse.get_pressed()    

    # get mouse cursor positions
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # make left mouse click
    mouse_left_click = mouse[0]

    # set the frame rate target
    game_clock.tick(60)

    # get program "events" so it doesn't freeze
    events = pygame.event.get()

    # check for a program closed event
    for an_event in events:
        if an_event.type == pygame.QUIT:
            # this will close the game
            draw_window = False
        
        # check if key is released
        if an_event.type == pygame.KEYUP:
            if an_event.key == pygame.K_e:
                e_key_processed = False  # Reset when the key is released
            if an_event.key == pygame.K_f:
                f_key_processed = False  # Reset when the key is released
            if an_event.key == pygame.K_q:
                q_key_processed = False # Reset when the key is released

        # check if mouse button is released    
        if an_event.type == pygame.MOUSEBUTTONUP:
            if an_event.button == mouse_left_click:
                mouse_left_click_processed = False
    # draw start menu
    WINDOW.blit(start_menu, (0,0))

    # draw window caption
    pygame.display.set_caption("Sun Dew Valley")
    
    # create collision detection
    instructions_button_rect = instructions_button.get_rect(topleft=(0,0))

    # create mask for instructions button
    instructions_button_mask = pygame.mask.from_surface(instructions_button) 

    # create collision detection rectangle for start button
    start_button_rect = start_button.get_rect(topleft=(0, 0))

    # create mask for start button
    start_button_mask = pygame.mask.from_surface(start_button)

    # change start button image if hovered
    if start_button_mask.get_at((mouse_x - start_button_rect.x, mouse_y - start_button_rect.y)) and game_window == IN_MENU:
        WINDOW.blit(start_button_hover, (0, 0))
        # enter game
        if mouse_left_click:
            game_window = IN_GAME
    else:
         # draw start button
         WINDOW.blit(start_button, (0,0))

    # change instructions button image if hovered
    if instructions_button_mask.get_at((mouse_x - instructions_button_rect.x, mouse_y - instructions_button_rect.y)) and game_window == IN_MENU:
        WINDOW.blit(instructions_button_hover, (0,0))
        # enter instructions menu
        if mouse_left_click:
            game_window = IN_INSTRUCTIONS1
    else:
        # draw instructions button
        WINDOW.blit(instructions_button, (0,0))

    
    # call different game windows
    if game_window == IN_GAME:
        game_garden()

    elif game_window == IN_SHOP:
        crop_item_shop()
    
    elif game_window == IN_HOUSE:
        game_house()

    elif game_window == IN_SHOP2:
        furniture_item_shop()

    elif game_window == IN_INSTRUCTIONS1:
        page1_instructions()

    elif game_window == IN_INSTRUCTIONS2:
        page2_instructions()

    # update display
    pygame.display.flip()

pygame.quit()
sys.exit()