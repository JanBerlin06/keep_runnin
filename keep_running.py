import pygame
from sys import exit

# starts pygame
pygame.init()


# set window
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height)) # as a tuple
pygame.display.set_caption("Keep running buddy!") # window title

clock = pygame.time.Clock()
test_font = pygame.font.Font('./font/Pixeltype.ttf', 50)

"""surfaces are objects - displayed on the the window, like a character, background etc"""
# background & transform to the right size
# city_surface = pygame.image.load('./graphics/city.png').convert()
sky_right_surf = pygame.image.load('./city/1.png').convert()
sky_right_surf = pygame.transform.scale(sky_right_surf, (800, 400))
sky_right_rect = sky_right_surf.get_rect(bottomright = (800, 400))
sky_left_surf = pygame.image.load('./city/1.png').convert()
sky_left_surf = pygame.transform.scale(sky_left_surf, (800, 400))
sky_left_rect = sky_right_surf.get_rect(bottomleft = (800, 400))

towers_one_left_surf = pygame.image.load('./city/2.png').convert_alpha()
towers_one_left_surf = pygame.transform.scale(towers_one_left_surf, (800, 400))
towers_one_left_rect = towers_one_left_surf.get_rect(bottomright = (800, 400))
towers_one_right_surf = pygame.image.load('./city/2.png').convert_alpha()
towers_one_right_surf = pygame.transform.scale(towers_one_right_surf, (800, 400))
towers_one_right_rect = towers_one_left_surf.get_rect(bottomleft = (800, 400))

towers_two_left_surf = pygame.image.load('./city/3.png').convert_alpha()
towers_two_left_surf = pygame.transform.scale(towers_two_left_surf, (800, 400))
towers_two_left_rect = towers_two_left_surf.get_rect(bottomright = (800, 400))
towers_two_right_surf = pygame.image.load('./city/3.png').convert_alpha()
towers_two_right_surf = pygame.transform.scale(towers_two_right_surf, (800, 400))
towers_two_right_rect = towers_two_left_surf.get_rect(bottomleft = (800, 400))

towers_three_left_surf = pygame.image.load('./city/4.png').convert_alpha()
towers_three_left_surf = pygame.transform.scale(towers_three_left_surf, (800, 400))
towers_three_left_rect = towers_three_left_surf.get_rect(bottomright = (800, 400))
towers_three_right_surf = pygame.image.load('./city/4.png').convert_alpha()
towers_three_right_surf = pygame.transform.scale(towers_three_right_surf, (800, 400))
towers_three_right_rect = towers_three_right_surf.get_rect(bottomleft = (800, 400))

towers_four_left_surf = pygame.image.load('./city/5.png').convert_alpha()
towers_four_left_surf = pygame.transform.scale(towers_four_left_surf, (800, 400))
towers_four_left_rect = towers_four_left_surf.get_rect(bottomright = (800, 400))
towers_four_right_surf = pygame.image.load('./city/5.png').convert_alpha()
towers_four_right_surf = pygame.transform.scale(towers_four_right_surf, (800, 400))
towers_four_right_rect = towers_four_right_surf.get_rect(bottomleft = (800, 400))

# ground
ground_surface = pygame.image.load('./graphics/ground.png').convert()

# score
score_surf = test_font.render('Keep  runnin  buddy!', False, (64, 64, 64))
score_rect = score_surf.get_rect(center = (screen_width / 2, 50))

# snail
snail_surf = pygame.image.load('./graphics/snail/snail1.png').convert_alpha() # convert_alpha otherwise we have no transparant background
snail_rect = snail_surf.get_rect(bottomright = (600,350))

# player
player_surf = pygame.image.load('./graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,350))


# main loop
while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            print("Quitting Game")
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print('collision')

    # placing surfaces on the window
    # screen.blit(city_surface, (0, -100))

    # background
    screen.blit(sky_right_surf, sky_right_rect)
    sky_right_rect.x -= 1
    if sky_right_rect.right <= 0: sky_right_rect.left = 800

    screen.blit(sky_left_surf, sky_left_rect)
    sky_left_rect.x -= 1
    if sky_left_rect.right <= 0: sky_left_rect.left = 800

    screen.blit(towers_one_left_surf, towers_one_left_rect)
    towers_one_left_rect.x -= 1
    if towers_one_left_rect.right <= 0: towers_one_left_rect.left = 800

    screen.blit(towers_one_right_surf, towers_one_right_rect)
    towers_one_right_rect.x -= 1
    if towers_one_right_rect.right <= 0: towers_one_right_rect.left = 800

    screen.blit(towers_two_left_surf, towers_two_left_rect)
    towers_two_left_rect.x -= 1
    if towers_two_left_rect.right <= 0: towers_two_left_rect.left = 800

    screen.blit(towers_two_right_surf, towers_two_right_rect)
    towers_two_right_rect.x -= 1
    if towers_two_right_rect.right <= 0: towers_two_right_rect.left = 800

    screen.blit(towers_three_left_surf, towers_three_left_rect)
    towers_three_left_rect.x -= 2
    if towers_three_left_rect.right <= 0: towers_three_left_rect.left = 800

    screen.blit(towers_three_right_surf, towers_three_right_rect)
    towers_three_right_rect.x -= 2
    if towers_three_right_rect.right <= 0: towers_three_right_rect.left = 800

    screen.blit(towers_four_left_surf, towers_four_left_rect)
    towers_four_left_rect.x -= 2
    if towers_four_left_rect.right <= 0: towers_four_left_rect.left = 800

    screen.blit(towers_four_right_surf, towers_four_right_rect)
    towers_four_right_rect.x -= 2
    if towers_four_right_rect.right <= 0: towers_four_right_rect.left = 800

    # ground
    screen.blit(ground_surface, (0, 350))

    # score
    pygame.draw.rect(screen, '#c0e8ec', score_rect,)
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
    screen.blit(score_surf, score_rect)

    # snail
    screen.blit(snail_surf,snail_rect)
    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800

    # player
    screen.blit(player_surf,player_rect)

    # if player_rect.colliderect(snail_rect):
    #     print('collision')

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())


    

    pygame.display.update()
    clock.tick(60) # max 60 FPS

