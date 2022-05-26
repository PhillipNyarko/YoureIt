import random
import pygame

WIN_WIDTH, WIN_HEIGHT = (500, 500)
FPS = 120

BLUE = (0, 200, 225)
RED = (225, 0, 0)
BLACK = (0, 0, 0)


def main():
    pygame.init()
    logo = pygame.image.load("tags-solid (1).svg")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("You're It")

    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    ai_x_pos = 100
    ai_y_pos = 100
    ai_width = 20
    ai_height = 20
    ai_speed = 2

    player_x_pos = 50
    player_y_pos = 50
    player_width = 20
    player_height = 20
    player_speed = 5

    portal_width = 20
    portal_height = 20
    portal_speed = 0.5
    portal_x_pos = random.randint(0, WIN_WIDTH-portal_width)
    portal_y_pos = random.randint(0, WIN_WIDTH-portal_height)

    inc = 0
    threshold = FPS
    level = 2
    clock = pygame.time.Clock()
    coin_flip = random.randint(0, 7)
    score = 0
    running = True

    while running:
        clock.tick(FPS)

        player_rect = pygame.Rect(player_x_pos, player_y_pos, player_width, player_height)
        screen.fill("black")

        if pygame.key.get_pressed()[pygame.K_UP]:
            player_y_pos -= player_speed
            screen.fill("black")

        if pygame.key.get_pressed()[pygame.K_DOWN]:
            player_y_pos += player_speed
            screen.fill("black")

        if pygame.key.get_pressed()[pygame.K_LEFT]:
            player_x_pos -= player_speed
            screen.fill("black")

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            player_x_pos += player_speed
            screen.fill("black")

        if player_x_pos <= 0:
            player_x_pos = WIN_WIDTH - player_width
        elif player_x_pos >= WIN_WIDTH - player_width:
            player_x_pos = 0
        elif player_y_pos <= 0:
            player_y_pos = WIN_WIDTH - player_height
        elif player_y_pos >= WIN_WIDTH - player_height:
            player_y_pos = 0

        pygame.draw.rect(screen, BLUE, player_rect)

        ai_rect = pygame.Rect(ai_x_pos, ai_y_pos, ai_width, ai_height)
        pygame.draw.rect(screen, RED, ai_rect)

        if pygame.Rect.colliderect(player_rect, ai_rect):
            ai_speed += 0.3
            score += 1
            print("collision" + str(score))

        if inc == threshold:
            threshold += FPS//4
            coin_flip = random.randint(0, 7)
        elif inc < threshold:
            if coin_flip == 0:
                ai_x_pos += ai_speed
            elif coin_flip == 1:
                ai_x_pos -= ai_speed
            elif coin_flip == 2:
                ai_y_pos += ai_speed
            elif coin_flip == 3:
                ai_y_pos -= ai_speed
            elif coin_flip == 4:
                ai_x_pos += ai_speed
                ai_y_pos += ai_speed
            elif coin_flip == 5:
                ai_x_pos -= ai_speed
                ai_y_pos -= ai_speed
            elif coin_flip == 6:
                ai_x_pos += ai_speed
                ai_y_pos -= ai_speed
            elif coin_flip == 7:
                ai_x_pos -= ai_speed
                ai_y_pos += ai_speed
            inc += 1

        if ai_x_pos < 0:
            ai_x_pos = 0
        elif ai_x_pos > WIN_WIDTH - ai_width:
            ai_x_pos = WIN_WIDTH - ai_width
        elif ai_y_pos < 0:
            ai_y_pos = 0
        elif ai_y_pos > WIN_HEIGHT - ai_height:
            ai_y_pos = WIN_HEIGHT - ai_height

        font = pygame.font.SysFont("Segoe UI", 20)
        text_surface = font.render("Score: " + str(score), True, "white")
        screen.blit(text_surface, (400, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    main()
