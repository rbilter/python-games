# imports
import sys
import time
import surface
import settings

# Grab the game settings
gs = settings.GameSettings()
high_score = gs.get_high_score()

# Create the game play surface
surface = surface.GameSurface()
surface.new_game_surface()

# start the game and the main game loop
surface.start_game()
time.sleep(2)
while True:
    # cycles through all game events
    quit_game = surface.check_events()

    # run game
    if not quit_game:
        # update score and backgroup
        score = surface.get_ememy().get_score()
        if high_score < score:
            high_score = score

        # render surface
        surface.render_backgroud()
        surface.render_game_score(score)
        surface.render_high_score(high_score)
        surface.render_sprites()

        # collision detection between the player and enemy
        if surface.had_collision():
            surface.render_collision()
            time.sleep(1.5)

            surface.render_game_over()
            gs.set_high_score(high_score)
            time.sleep(2)

            if surface.try_again():
                surface.start_game()
            else:
                quit_game = True

    if not quit_game:
        surface.update()
    else:
        surface.quit()
        sys.exit()
