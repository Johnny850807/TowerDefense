# Trap class
#
# Objects placable only on path tiles
# intereact with creeps when they
# collide
#
# 2014/8/3
# written by Michael Shawn Redmond

import pygame
import rectangle
from config import *

class Trap(rectangle.Rectangle):
    # the trap's identifier used when reading the map file
    ident = "".join(TRAP_DEFAULT_NAME.split()).lower()
    def __init__(self, position, width=TRAP_DEFAULT_WIDTH, height=TRAP_DEFAULT_HEIGHT, image=TRAP_DEFAULT_IMAGE, bad_image=TRAP_DEFAULT_BAD_IMAGE, cost=TRAP_DEFAULT_COST, name=TRAP_DEFAULT_NAME):
        rectangle.Rectangle.__init__(self, KIND_TRAP, position, width, height, image)
        self.cost = cost
        self.active = False
        self.name = name
        self.description = ""
        self.is_good = True
        self.bad_image = pygame.image.load(bad_image)

    def paint(self, surface):
    # paints the "can be placed" image unless the position is bad
        if self.is_good:
            surface.blit(self.image, self.position)
        else:
            surface.blit(self.bad_image, self.position)

    def bad_pos(self):
        if self.is_good:
            self.is_good = False

    def good_pos(self):
        if not self.is_good:
            self.is_good = True

    # this is called when a creep touches
    # the trap
    # this is where the trap interacts with
    # the creep
    def on_step(self, creep):
        raise NotImplementedError()

    def get_details(self, width):
        return ""

    def get_sell_amount(self):
        return self.cost*TRAP_SELL_RATE

    def get_hover_message(self):
        message = ""
        message += "%s\n" %(self.name)
        message += self.description
        message += "\nCost: $%.2f" %(self.cost)
        return message

    def get_info(self):
        info = []
        line = "Trap: %s" %(self.name)
        info.append(line)

        line = "Cost: %s" %(self.cost)
        info.append(line)
        line = "Sell value: $%.2f" %(self.get_sell_amount())
        info.append(line)

        # add info for the specific trap
        lines = self.get_details()
        for line in lines:
            info.append(line)

        return info

    def get_cost(self):
        return self.cost

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def game_logic(self, keys, newkeys, mouse_pos, newclicks, creeps):
        actions = []

        if self.is_inside(mouse_pos):
            if MOUSE_LEFT in newclicks:
                actions.append((T_SELECTED, self))
        
        # check every creep to see if it made
        # contact with the trap
        for creep in creeps:
            if self.collide(creep):
                # activate the trap on the creep
                self.on_step(creep)

        return actions


class Mud(Trap):
    ident = "".join(TRAP_MUD_NAME.split()).lower()

    def __init__(self, position):
        Trap.__init__(self, position, TRAP_MUD_WIDTH, TRAP_MUD_HEIGHT, TRAP_MUD_IMAGE, TRAP_MUD_BAD_IMAGE, TRAP_MUD_COST, TRAP_MUD_NAME)
        self.speed_mod = TRAP_MUD_SPEED_MOD
        self.description = TRAP_MUD_DETAILS[0]

    def get_details(self):
        lines = TRAP_MUD_DETAILS        
        return lines

    def on_step(self, creep):
        creep.slow(self.speed_mod)

    def get_info(self):
        info = []
        line = "Trap: %s" %(self.name)
        info.append(line)

        # slow info
        line = "Slow percent: %.2f" %(self.speed_mod*100)
        info.append(line)

        line = "Cost: %s" %(self.cost)
        info.append(line)
        line = "Sell value: $%.2f" %(self.get_sell_amount())
        info.append(line)

        # add info for the specific trap
        lines = self.get_details()
        for line in lines:
            info.append(line)

        return info

class Lava(Trap):
    ident = "".join(TRAP_LAVA_NAME.split()).lower()

    def __init__(self, position):
        Trap.__init__(self, position, TRAP_LAVA_WIDTH, TRAP_LAVA_HEIGHT, TRAP_LAVA_IMAGE, TRAP_LAVA_BAD_IMAGE, TRAP_LAVA_COST, TRAP_LAVA_NAME)
        self.damage = TRAP_LAVA_DAMAGE
        self.perc_damage = TRAP_LAVA_PERCENT
        self.duration = TRAP_LAVA_DURATION
        self.description = TRAP_LAVA_DETAILS[0]

    def get_details(self):
        lines = TRAP_LAVA_DETAILS        
        return lines

    def on_step(self, creep):
        percent = creep.get_max_health()*self.perc_damage
        creep.burn(max(self.damage, percent), self.duration)

    def get_info(self):
        info = []
        line = "Trap: %s" %(self.name)
        info.append(line)

        # burn info
        line = "DPS: %.2f" %(self.damage)
        info.append(line)
        line = "Min. Damage: %.2f percent" %(self.perc_damage*100)
        info.append(line)
        line = "Duration: %.2fs" %(self.duration)
        info.append(line)

        line = "Cost: %s" %(self.cost)
        info.append(line)
        line = "Sell value: $%.2f" %(self.get_sell_amount())
        info.append(line)

        # add info for the specific trap
        lines = self.get_details()
        for line in lines:
            info.append(line)

        return info
