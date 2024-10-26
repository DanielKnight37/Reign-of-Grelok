from globals import *
from pygame.locals import *

class Button:

    button_color = (0, 0, 0, 0)
    hover_color = (TERMINALGREEN_H)
    text_color = (TERMINALGREEN)
    text_hover_color = ("black")
    width = 700
    height = 40
    kb_input = False
    kb_highlighted_button = None
    index = 0
    current_button = None
    inventory_opened = False

    def __init__(self, x, y, text) -> None:
        self.x = x
        self.y = y
        self.text = text
        self.background = pygame.Surface(SCREEN.get_size())
        self.clicked = False
        self.kb_clicked = False
        self.action = False
        self.hovered = False
        self.mouse_click_not_hovered = False
        self.mouse_click_while_hovered = False
        self.mouse_hovered_not_clicked = False
        
        
    def hover_sound(self):
        if self.hovered == False:
            pygame.mixer.Sound.play(HOVER)
            self.hovered = True
    
    @classmethod
    def kb_input_off(cls):
        cls.kb_input = False

    @classmethod
    def kb_input_on(cls):
        cls.kb_input = True

    @classmethod
    def open_inventory(cls):
        cls.inventory_opened = True

    @classmethod
    def close_inventory(cls):
        cls.inventory_opened = False

    @classmethod
    def reset_index(cls):
        cls.index = 0

    @classmethod
    def remove_button(cls, location, lst, button):
        lst.remove(button)
        button.action = False
        if cls.kb_input is True:
            cls.reset_index()
            location[cls.index].kb_clicked = True

    def draw_button(self):
        self.action = False
        self.inv_action = False
        pos = pygame.mouse.get_pos()
        button_rect = Rect(self.x, self.y, self.width, self.height)
        button = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        text_img = FONT.render(self.text, True, self.text_color)

        if button_rect.collidepoint(pos) and self.mouse_click_not_hovered == False or self.kb_clicked is True:
            Button.current_button = self
            if self.kb_input is True and button_rect.collidepoint(pos):
                self.kb_input_off()
                self.kb_highlighted_button.kb_clicked = False
            if self.mouse_hovered_not_clicked == False:
                self.mouse_hovered_not_clicked = True

            if pygame.mouse.get_pressed()[0] == 1 and self.hovered is True:
                self.mouse_click_while_hovered = True
                button.fill((self.hover_color))
                SCREEN.blit(button, (button_rect))
                text_img = FONT.render(self.text, True, self.text_hover_color)
                SCREEN.blit(text_img, (self.x, self.y + 3))
                self.clicked = True

            elif pygame.mouse.get_pressed()[0] == 0 and self.clicked is True:
                pygame.mixer.Sound.play(SELECT_II)
                self.clicked = False
                self.action = True
                if Button.inventory_opened == False:
                    self.kb_clicked = False

            else: # Button hover effect
                button.fill((self.hover_color))
                SCREEN.blit(button, (self.x, self.y))
                text_img = FONT.render(self.text, True, self.text_hover_color)
                SCREEN.blit(text_img, (self.x , self.y + 3))
                self.mouse_hovered_not_clicked = True
                if pygame.mouse.get_pressed()[0] == 0:
                    self.hover_sound()

        else: # While mouse doesn't collide with button rect
            if self.mouse_hovered_not_clicked is True:
                self.mouse_hovered_not_clicked = False

            if self.mouse_click_not_hovered is True:
                self.mouse_click_not_hovered = False

            if pygame.mouse.get_pressed()[0] == 1 and self.mouse_hovered_not_clicked == False:
                self.mouse_click_not_hovered = True

            if pygame.mouse.get_pressed()[0] == 0 and self.mouse_click_not_hovered == False:
                self.mouse_click_while_hovered = False
                self.hovered = False

            if self.mouse_click_while_hovered is True:
                button.fill((self.hover_color))
                text_img = FONT.render(self.text, True, self.text_hover_color)

            SCREEN.blit(button, button_rect)
            SCREEN.blit(text_img, (self.x , self.y + 3))
            self.clicked = False
        return self.action

#-=Map=-#
map = [["none", "mountainside", "none"],
       ["swamp", "plains", "chapel"],
       ["none", "town", "none"]]
map_y_len = len(map) - 1
map_x_len = len(map[0]) - 1

#-=Directions=-#
north = Button(indent, II, data_text["t_north"])
south = Button(indent, III, data_text["t_south"])
east = Button(indent, IV, data_text["t_east"])
west = Button(indent, V, data_text["t_west"])

#-=Inventory=-#
inventory = Button(indent, VI, data_text["t_inventory"]) 
rusty_sword = Button(indent, I, data_text["t_rusty_sword"])
flask = Button(indent, II, data_text["t_flask"])
flask_blessed = Button(indent, II, data_text["t_flask_blessed"])
zombie_head = Button(indent, III, data_text["t_zombie_head"])
refined_gemstone = Button(indent, III, data_text["t_refined_gemstone"])
magical_shard = Button(indent, IV, data_text["t_magical_shard"])
magic_sword = Button(indent, II, data_text["t_magic_sword"])
brass_key = Button(indent, III, data_text["t_brass_key"])
raw_gemstone = Button(indent, III, data_text["t_raw_gemstone"])
back = Button(indent, III, data_text["t_back"])

#-=Plains=-#
pI = Button(indent, I, data_text["t_pI"])
plains = [pI, north, south, east, west, inventory]

#-=Town=-#
lookAroundTown = False
priestQuest = False
brassKey = False
tI = Button(indent, I, data_text["t_tI"])
smith = Button(indent, II, data_text["t_smith"])
priest = Button(indent, III, data_text["t_priest"])
town = [tI, north, inventory]

#-=Chapel=-#
lookAroundChapel = False
zombieSlain = False
cI = Button(indent, I, data_text["t_cI"])
c_west = Button(indent, II, data_text["t_west"])
zombie = Button(indent, II, data_text["t_zombie"])
grave = Button(indent, III, data_text["t_grave"])
c_chapel = Button(indent, II, data_text["t_chapel"])
c_grave = Button(indent, II, data_text["t_grave"])
chapel = [cI, c_west, inventory]

#-=Swamp=-#
lookAroundSwamp = False
wizardQuest = False
sI = Button(indent, I, data_text["t_sI"])
s_east = Button(indent, II, data_text["t_east"])
wizard = Button(indent, II, data_text["t_wizard"])
swamp = [sI, s_east, inventory]

#-=Mountainside=-#
lookAroundMountainside = False
rawGemstone = False
defeatGrelok = False
mI = Button(indent, I, data_text["t_mI"])
m_south = Button(indent, II, data_text["t_south"])
grelok = Button(indent, II, data_text["t_grelok"])
gemstone = Button(indent, III, data_text["t_gemstone"])
mountainside = [mI, m_south, inventory]
if LANG in "ENG":
    grelok.y += 25
    gemstone.y += 25
    for i in mountainside:
        i.y += 25
else:
    grelok.y += 50
    gemstone.y += 50
    for i in mountainside:
        i.y += 50