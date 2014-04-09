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
    def __init__(self, position, width=TOWER_BASIC_WIDTH,       height=TOWER_BASIC_HEIGHT, image=TOWER_BASIC_IMAGE):
        rectangle.Rectangle.__init__(self, position, image, width, height)
        self.cost = TOWER_BASIC_COST
        self.range = TOWER_BASIC_RANGE
        self.active = False

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
        cx, cy = self.get_position()
        distance = math.sqrt((px-cx)**2 + (py-cy)**2)
        return distance <= self.range
     
    def paint(self, surface):
        if self.is_active():
            # if the tower is selected
            # draw a partially transparent
            # circle to indicate its range
            cx, cy = self.get_center()
            topleft = (cx - self.range, cy - self.range)
            surf = pygame.Surface((self.range*2, self.range*2), pygame.SRCALPHA)
            surf.fill((255, 255, 255, 0))
            
            # loop through each pixel in the rectangle
            # that contains the range and change its
            # color if it is inside the range
            # (excludes the corners of the rectangle)
            for i in range(surf.get_width()):
                for j in range(surf.get_height()):
                    if self.is_in_range((i + topleft[0] - .5*self.width, j + topleft[1] - .5*self.height)):
                        surf.set_at((i, j), RANGE_COLOR)
            surface.blit(surf, topleft)
        surface.blit(self.image, self.position)
        
    def game_logic(self, keys, newkeys, mouse_pos, newclicks):
        actions = []
        if self.is_inside(mouse_pos):
            if 1 in newclicks: # left click
                actions.append((T_SELECTED, self))
        return actions
        
class GreenTower(Tower):
    def __init__(self, position):
        width=TOWER_GREEN_WIDTH
        height=TOWER_GREEN_HEIGHT
        image=TOWER_GREEN_IMAGE
        Tower.__init__(self, position, width, height, image)
        self.cost = TOWER_GREEN_COST
        self.range = TOWER_GREEN_RANGE
