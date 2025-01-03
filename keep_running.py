import sys
import pygame
from sys import exit
from random import randint

# every second the player gets 1 point
def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (255, 255, 255))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

# Function to load and prepare background layers
def load_layer(image_path, scale, rect_side, rect_position):
    surf = pygame.image.load(image_path).convert_alpha()
    surf = pygame.transform.scale(surf, scale)
    rect = surf.get_rect(**{rect_side: rect_position})
    return surf, rect

# Function to update background layers
def update_layer(screen, layer_surf, layer_rect, speed, reset_pos):
    layer_rect.x -= speed
    if layer_rect.right <= 0:
        layer_rect.left = reset_pos
    screen.blit(layer_surf, layer_rect)

def snail_animation():
    global snail_surf, snail_index
    snail_index += 0.1
    if snail_index >= len(snail_walk): snail_index = 0
    snail_surf = snail_walk[int(snail_index)]

# Function to handle Obstacle movement
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rec in obstacle_list:
            obstacle_rec.x -= 5
            screen.blit(snail_surf, obstacle_rec)

        # Behalte Hindernisse, die sich noch im sichtbaren Bereich befinden
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -obstacle.width]
        return obstacle_list
    else:
        return []


def collisions(player, obstacle):
    if obstacle:
        for obstacle_rect in obstacle:
            if player.colliderect(obstacle_rect): return False
    return True



# starts pygame
pygame.init()


# set window
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height)) # as a tuple
pygame.display.set_caption("Keep running buddy!") # window title

clock = pygame.time.Clock()
test_font = pygame.font.Font('./font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

# Load background layers
sky_right_surf, sky_right_rect = load_layer('./city/1.png', (800, 400), 'bottomright', (800, 400))
sky_left_surf, sky_left_rect = load_layer('./city/1.png', (800, 400), 'bottomleft', (800, 400))

towers_one_left_surf, towers_one_left_rect = load_layer('./city/2.png', (800, 400), 'bottomright', (800, 400))
towers_one_right_surf, towers_one_right_rect = load_layer('./city/2.png', (800, 400), 'bottomleft', (800, 400))

towers_two_left_surf, towers_two_left_rect = load_layer('./city/3.png', (800, 400), 'bottomright', (800, 400))
towers_two_right_surf, towers_two_right_rect = load_layer('./city/3.png', (800, 400), 'bottomleft', (800, 400))

towers_three_left_surf, towers_three_left_rect = load_layer('./city/4.png', (800, 400), 'bottomright', (800, 400))
towers_three_right_surf, towers_three_right_rect = load_layer('./city/4.png', (800, 400), 'bottomleft', (800, 400))

towers_four_left_surf, towers_four_left_rect = load_layer('./city/5.png', (800, 400), 'bottomright', (800, 400))
towers_four_right_surf, towers_four_right_rect = load_layer('./city/5.png', (800, 400), 'bottomleft', (800, 400))

# Ground
ground_left_surf, ground_left_rect = load_layer('./graphics/ground.png', (800, 50), 'bottomright', (0, 400))
ground_right_surf, ground_right_rect = load_layer('./graphics/ground.png', (800, 50), 'bottomleft', (0, 400))

# Intro Text
text_game_name_surf = test_font.render('Keep  runnin  buddy!', False, (255, 255, 255))
text_game_name_rect = text_game_name_surf.get_rect(center = (screen_width / 2, 50))

text_intro_surf = test_font.render('- Press Space on your Keyboard -', False, (255, 255, 255))
text_intro_rect = text_intro_surf.get_rect(center = (screen_width / 2, 100))

# snail
snail_walk_1 = pygame.image.load('./graphics/snail/snail_walk_1.png').convert_alpha()
snail_walk_2 = pygame.image.load('./graphics/snail/snail2_walk_2.png').convert_alpha()
snail_walk = [snail_walk_1, snail_walk_2]
snail_index = 0
snail_surf = snail_walk[snail_index]
snail_rect = snail_surf.get_rect(bottomright = (600,350))

obstacle_rect_list = []

# Player sprite sheet, animation setup and sound
player_run_sprite_sheet = pygame.image.load('./graphics/player/Cyborg_run.png').convert_alpha()
frames_run = []
frame_run_width = 48
frame_run_height = 48
number_frames_run = 6

for i in range(number_frames_run):
    x = i * frame_run_width
    frame_run_surf = player_run_sprite_sheet.subsurface(x, 0, frame_run_width, frame_run_height)
    frame_run_surf = pygame.transform.scale(
        frame_run_surf, (frame_run_width * 3, frame_run_height * 3)
    )
    frames_run.append(frame_run_surf)

# Player variables
player_rect = frames_run[0].get_rect(midbottom=(80, 350))
player_gravity = 0
current_frame = 0.0
animation_speed = 0.2
jump_sound = pygame.mixer.Sound('./audio/jump.wav')
jump_sound.set_volume(0.30)

background_music = pygame.mixer.Sound('./audio/keep_runnin_buddy_song.mp3')
background_music.play(loops=-1)
background_music.set_volume(0.5)

# Timer
obstacle_timer = pygame.USEREVENT + 1 # to avoid a conflict
pygame.time.set_timer(obstacle_timer, 1500)

# Main Loop
# ------------------
while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            print("Quitting Game")

        if game_active:
            # Player jump with space key
            if event.type == pygame.KEYDOWN and player_rect.bottom == 350:
                if event.key == pygame.K_SPACE:
                    player_gravity = -20
                    jump_sound.play()

            if event.type == obstacle_timer:
                obstacle_rect_list.append(snail_surf.get_rect(bottomright=(randint(900, 1100),350)))

        else:
            if not game_active:
                # Start game on space key
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active = True
                    start_time = int(pygame.time.get_ticks() / 1000)

                    # reset all relevant variables
                    obstacle_rect_list = []  # Hindernisliste leeren
                    player_gravity = 0  # Schwerkraft zurücksetzen
                    player_rect.midbottom = (80, 350)  # Spielerposition zurücksetzen
                    snail_rect.left = 800  # Hindernisse zurücksetzen

    # Update animation
    current_frame += animation_speed
    if current_frame >= number_frames_run:
        current_frame = 0
    player_current_img = frames_run[int(current_frame)]


    if game_active:
        # Background layers
        update_layer(screen, sky_right_surf, sky_right_rect, 1, 800)
        update_layer(screen, sky_left_surf, sky_left_rect, 1, 800)

        update_layer(screen, towers_one_left_surf, towers_one_left_rect, 1, 800)
        update_layer(screen, towers_one_right_surf, towers_one_right_rect, 1, 800)

        update_layer(screen, towers_two_left_surf, towers_two_left_rect, 1, 800)
        update_layer(screen, towers_two_right_surf, towers_two_right_rect, 1, 800)

        update_layer(screen, towers_three_left_surf, towers_three_left_rect, 2, 800)
        update_layer(screen, towers_three_right_surf, towers_three_right_rect, 2, 800)

        update_layer(screen, towers_four_left_surf, towers_four_left_rect, 2, 800)
        update_layer(screen, towers_four_right_surf, towers_four_right_rect, 2, 800)

        # Ground
        update_layer(screen, ground_left_surf, ground_left_rect, 8, 800)
        update_layer(screen, ground_right_surf, ground_right_rect, 8, 800)



        # Score
        score = display_score()

        # Snail movement
        screen.blit(snail_surf, snail_rect)
        snail_animation()


        # Player animation and movement
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 350:
            player_rect.bottom = 350
        screen.blit(player_current_img, player_rect)

        # Custom Hitbox for collision
        hit_width = player_rect.width - 100
        hit_height = player_rect.height - 30
        offset_x = 20
        offset_y = 20
        player_hit_rect = pygame.Rect(
            player_rect.x + offset_x,
            player_rect.y + offset_y,
            hit_width,
            hit_height
        )

        # Debugging: Draw hitbox
        # pygame.draw.rect(screen, (255, 0, 0), player_hit_rect, 2)
        # pygame.draw.rect(screen, (0, 0, 0), player_rect, 2)

        # Collision
        game_active = collisions(player_hit_rect, obstacle_rect_list)

        # Obstacle
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

    else:
        # Intro Screen
        screen.fill((38, 45, 117))
        frame_index = int(current_frame)
        player_run_img = frames_run[frame_index]
        run_rect = player_run_img.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(player_run_img, run_rect)

        # Text
        if score == 0:
            screen.blit(text_game_name_surf, text_game_name_rect)
        else:
            score_message = test_font.render(f'Your Score: {score}', False, (255, 255, 255))
            score_message_rect = score_message.get_rect(center=(screen_width / 2, 50))
            screen.blit(score_message, score_message_rect)
        screen.blit(text_intro_surf, text_intro_rect)


    pygame.display.update()
    clock.tick(60)