from globals import *
from pygame.locals import *

class Button:

    button_color = (0, 0, 0, 0)
    hover_color = (TERMINALGREEN_H)
    text_color = (TERMINALGREEN)
    text_hover_color = ("black")
    width = 700
    height = 40
    font = FONT
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
        text_img = self.font.render(self.text, True, self.text_color)

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
                text_img = self.font.render(self.text, True, self.text_hover_color)
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
                text_img = self.font.render(self.text, True, self.text_hover_color)
                SCREEN.blit(text_img, (self.x , self.y + 3))
                self.mouse_hovered_not_clicked = True
                if pygame.mouse.get_pressed()[0] == 0:
                    self.hover_sound()

        else: # While mouse not collides with button
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
                text_img = self.font.render(self.text, True, self.text_hover_color)

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
north = Button(indent, II, "> Идти на север")
south = Button(indent, III, "> Идти на юг")
east = Button(indent, IV, "> Идти на восток")
west = Button(indent, V, "> Идти на запад")

#-=Inventory=-#
inventory = Button(indent, VI, "> Инвентарь")
rusty_sword = Button(indent, I, "> Ржавый меч")
flask = Button(indent, II, "> Питьевая фляжка")
flask_blessed = Button(indent, II, "> Питьевая фляжка")
zombie_head = Button(indent, III, "> Голова зомби")
refined_gemstone = Button(indent, III, "> Драгоценный камень")
magical_shard = Button(indent, IV, "> Магический осколок")
magic_sword = Button(indent, II, "> Магический меч")
brass_key = Button(indent, III, "> Медный ключ")
raw_gemstone = Button(indent, III, "> Необработанный драгоценный камень")
back = Button(indent, III, "> Назад")

#-=Plains=-#
pI = Button(indent, I, "> (Равнина) Оглядитесь вокруг")
plains = [pI, north, south, east, west, inventory]

#-=Town=-#
lookAroundTown = False
priestQuest = False
brassKey = False
tI = Button(indent, I, "> (Город) Оглядитесь вокруг")
smith = Button(indent, II, "> Поговорить с кузнецом")
priest = Button(indent, III, "> Поговорить со священником")
town = [tI, north, inventory]

#-=Chapel=-#
lookAroundChapel = False
zombieSlain = False
cI = Button(indent, I, "> (Часовня) Оглядитесь вокруг")
c_west = Button(indent, II, "> Идти на запад")
zombie = Button(indent, II, "> Ударить зомби мечом")
grave = Button(indent, III, "> Обследовать могилу")
c_chapel = Button(indent, II, "> Обследовать часовню")
c_grave = Button(indent, II, "> Обследовать могилу")
chapel = [cI, c_west, inventory]

#-=Swamp=-#
lookAroundSwamp = False
wizardQuest = False
sI = Button(indent, I, "> (Болото) Оглядитесь вокруг")
s_east = Button(indent, II, "> Идти на восток")
wizard = Button(indent, II, "> Поговорить с волшебником")
swamp = [sI, s_east, inventory]

#-=Mountainside=-#
lookAroundMountainside = False
rawGemstone = False
defeatGrelok = False
mI = Button(indent, II, "> (Горный склон) Оглядитесь вокруг")
m_south = Button(indent, III, "> Идти на юг")
grelok = Button(indent, III, "> Ударить грелока мечом")
gemstone = Button(indent, IV, "> Осмотреть сверкающий предмет")
mountainside = [mI, m_south, inventory]
