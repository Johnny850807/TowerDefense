# Tower Class
#
# Stores tower attributes and handles
# attacking, upgrading, selling, and
# drawing.
#
# 2014/3/21
# written by Michael Shawn Redmond

import pygame
from config import *
import rectangle
import math

class Tower(rectangle.Rectangle):
    def __init__(self, position, width=TOWER_BASIC_WIDTH, height=TOWER_BASIC_HEIGHT, image=TOWER_BASIC_IMAGE, rng=TOWER_BASIC_RANGE, cost=TOWER_BASIC_COST):
        rectangle.Rectangle.__init__(self, position, width, height, image)
        self.cost = cost
        self.range = rng
        self.active = False

        # true if the tower is in a good
        # (placable) location, else: false
        self.is_good = False

        # calculate the range once and store the
        # two different surfaces to avoid
        # unnecessary repetitive computation
        self.range_surface_good = pygame.Surface((self.range*2, self.range*2), pygame.SRCALPHA)
        self.range_surface_bad = pygame.Surface((self.range*2, self.range*2), pygame.SRCALPHA)
        self.generate_range()

    def get_cost(self):
        return self.cost
        
    def set_range(self, new_range):
        self.range = new_range
        
    def get_range(self):
        return self.range
    
    def is_active(self):
        return self.active
        
    def activate(self):
        self.active = True
        
    def deactivate(self):
        self.active = False
        
    def is_in_range(self, position):
        px, py = position
        #cx, cy = self.get_position()
        cx, cy = self.get_center()
        distance = math.sqrt((px-cx)**2 + (py-cy)**2)
        return distance <= self.range

    def generate_range(self, color_good=RANGE_COLOR, color_bad=RANGE_BAD_COLOR):
        self.range_surface_good.fill((255, 255, 255, 0))
        self.range_surface_bad.fill((255, 255, 255, 0))
        # loop through each pixel in the rectangle
        # that contains the range and change its
        # color if it is inside the range
        # (excludes the corners of the rectangle)
        cx, cy = self.get_center()
        topleft = (cx - self.range, cy - self.range)
        for i in range(self.range_surface_good.get_width()):
            for j in range(self.range_surface_good.get_height()):
                if self.is_in_range((i + topleft[0], j + topleft[1])):
                    self.range_surface_good.set_at((i, j), color_good)
                    self.range_surface_bad.set_at((i, j), color_bad)

    def bad_pos(self):
        if self.is_good:
            self.is_good = False

    def good_pos(self):
        if not self.is_good:
            self.is_good = True
        
    def paint_range(self, surface):
        if self.is_active():
            # if the tower is selected
            # draw a partially transparent
            # circle to indicate its range
            # green if the tower is in a
            # good location, red otherwise
            cx, cy = self.get_center()
            topleft = (cx - self.range, cy - self.range)
            if self.is_good:
                surface.blit(self.range_surface_good, topleft)
            else:
                surface.blit(self.range_surface_bad, topleft)
     
    def paint(self, surface):
        surface.blit(self.image, self.position)
        
    def game_logic(self, keys, newkeys, mouse_pos, newclicks):
        actions = []
        if self.is_inside(mouse_pos):
            if MOUSE_LEFT in newclicks:
                actions.append((T_SELECTED, self))
        return actions
        
class GreenTower(Tower):
    def __init__(self, position):
        Tower.__init__(self, position, TOWER_GREEN_WIDTH, TOWER_GREEN_HEIGHT, TOWER_GREEN_IMAGE, TOWER_GREEN_RANGE, TOWER_GREEN_COST)
