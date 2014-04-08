import pygame
import pygame.locals

import config

class Game:
    def __init__(self, name, width, height):
        self.width = width
        self.height = height
        self.on = True

        self.screen = pygame.display.set_mode(
                # set the size
                (width, height),

                # use double-buffering for smooth animation
                pygame.locals.DOUBLEBUF |

                # apply alpha blending
                pygame.locals.SRCALPHA)
        self.screen.set_alpha(0)
        # set the title of the window
        pygame.display.set_caption(name)

    def game_logic(self, keys, newkeys):
        raise NotImplementedError()

    def paint(self, surface):
        raise NotImplementedError()

    def main_loop(self):
        clock = pygame.time.Clock()
        keys = set()
        mouse_pos = (0, 0)
        while True:
            clock.tick(config.FRAMES_PER_SECOND)

            newkeys = set()
            newclicks = set()
            for e in pygame.event.get():
                # did the user try to close the window?
                if e.type == pygame.QUIT:
                    pygame.quit()
                    return

                # did the user just press the escape key?
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

                # track which keys are currently set
                if e.type == pygame.KEYDOWN:
                    keys.add(e.key)
                    newkeys.add(e.key)
                if e.type == pygame.KEYUP:
                    keys.discard(e.key)

                # track which mouse buttons were pressed
                if e.type == pygame.MOUSEBUTTONUP:
                    newclicks.add(e.button)

                # track the mouse's position
                if e.type == pygame.MOUSEMOTION:
                    mouse_pos = e.pos

            if self.on:
                self.game_logic(keys, newkeys, mouse_pos, newclicks)
                self.paint(self.screen)

            pygame.display.flip()

