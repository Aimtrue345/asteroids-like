import pygame
import sys
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    def play_game():
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()
        small_font = pygame.font.Font(None, 48)
        big_font = pygame.font.Font(None, 172)

        asteroids = pygame.sprite.Group()
        updatables = pygame.sprite.Group()
        drawables = pygame.sprite.Group()
        shots = pygame.sprite.Group()

        Asteroid.containers = (asteroids, updatables, drawables)
        Player.containers = (updatables, drawables)
        AsteroidField.containers = updatables
        Shot.containers = (shots, drawables, updatables)

        asteroid_field = AsteroidField()
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


        print("Starting Asteroids!")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")

        game_state = "playing"
        dt = 0
        score = 0   
        player_lives = 3
        
        while game_state == "playing":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"

            updatables.update(dt)

            screen.fill("black")

            for asteroid in asteroids:
                for bullet in shots:
                    if bullet.collision(asteroid):
                        bullet.kill()
                        score += 1
                        asteroid.split()
                if player.collision(asteroid) == True:
                    if player_lives >= 1:
                        player.kill()
                        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                        player_lives -= 1
                    else:
                        game_state = "game_over"
                    
            for drawable in drawables:
                drawable.draw(screen)

            current_scoreboard = small_font.render(f"Score : {score}", True, "white")
            score_rect = current_scoreboard.get_rect(midtop=(SCREEN_WIDTH / 2, 10)) 
            screen.blit(current_scoreboard, score_rect)

            life_counter = small_font.render(f"Lives remaining : {player_lives}", True, "white")
            screen.blit(life_counter, (life_counter.get_rect(topleft=(10, 10))))

            pygame.display.flip()

            dt = clock.tick(60) / 1000

        while game_state == "game_over":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    return 
            
            screen.fill("black")

            final_scoreboard = big_font.render(f"Final Score : {score}", True, "white")
            end_score_rect = final_scoreboard.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)) 
            screen.blit(final_scoreboard, end_score_rect)

            restart_prompt = small_font.render("Press 'R' to restart", True, "white")
            end_rect = restart_prompt.get_rect(midtop=(SCREEN_WIDTH / 2, 10)) 
            screen.blit(restart_prompt, end_rect)

            pygame.display.flip()

            dt = clock.tick(60) / 1000

    while True:
        state_change = play_game()
        if state_change == "quit":
            break

if __name__ == "__main__":
    main()
