from globals import *
from itertools import cycle

class Text:

    text_list = []
    text_redrawn = False
    text_in_progress = False
    blink_event = pygame.USEREVENT + 0
    pygame.time.set_timer(blink_event, 414)
    blinky = cycle(["■", " "])
    next_blink = next(blinky)
    show_tooltip = False
    text_timer = 0
    current_tooltip = None
    text_cursor = 0
    blank_text = FONT.render("", True, TERMINALGREEN)

    def __init__(self, text, x, y) -> None:
        self.text = text
        self.img = FONT.render("", True, TERMINALGREEN)
        self.x = x
        self.y = y
        self.next_update = 0
        self.typing_speed = 10 # Default: 10
        self.text_cursor = 0
        self.blank_text = FONT.render("", True, TERMINALGREEN)
        self.header_txt = FONT.render(None, False, TERMINALGREEN)
        Text.text_list.append(self)
        self.printed = False
        self.is_tooltip = True

    @classmethod
    def draw_tooltip(cls, tooltip):
        cls.current_tooltip = tooltip
        cls.current_tooltip.text_cursor = 0
        cls.text_timer = 5 # Tooltip timer
        if cls.text_timer <= 0:
            cls.current_tooltip.text_cursor = 0

    @classmethod
    def tooltip_listener(cls, delta):
        if cls.current_tooltip is not None:
            if cls.text_timer <= 0:
                cls.show_tooltip = False
                if cls.current_tooltip is not None:
                    cls.current_tooltip.text_cursor = 0
            else:
                cls.show_tooltip = True
                cls.text_timer -= delta
    
    def draw_text(self):
        clock = pygame.time.get_ticks()
        if self.is_tooltip is True:
            SCREEN.blit(self.blank_text, (self.x, self.y))
        else:
            SCREEN.blit(self.blank_text, (self.x, self.y))

        if (clock > self.next_update):
            self.next_update = clock + self.typing_speed
            if (self.text_cursor < len(self.text)):
                self.text_cursor += 1
                self.blank_text = FONT.render(self.text[0:self.text_cursor], False, TERMINALGREEN)
            else:
                self.printed = True

    def draw_text_instant(self):
        img = FONT.render(self.text, True, TERMINALGREEN)
        SCREEN.blit(img, (self.x, self.y))

    def draw_tooltip_text(self):
        clock = pygame.time.get_ticks()
        SCREEN.blit(self.blank_text, (self.x, self.y))
        if (clock > self.next_update):
            self.next_update = clock + self.typing_speed
            if (self.text_cursor < len(self.text)):
                self.text_cursor += 1
                self.blank_text = FONT.render(self.text[0:self.text_cursor] + Text.next_blink, False, TERMINALGREEN)
                SCREEN.blit(self.blank_text, (indent, X))
            else:
                self.printed = True

    @classmethod
    def blink_square(cls):
        if cls.show_tooltip == False:
            img = FONT.render("> " + cls.next_blink, True, TERMINALGREEN)
        else:
            if cls.current_tooltip is not None:
                img = FONT.render(cls.current_tooltip.text + cls.next_blink, True, TERMINALGREEN)
        SCREEN.blit(img, (indent, X))

    @classmethod
    def terminal_info(cls):
        robco_inc.draw_text_instant()
        copyright.draw_text_instant()
        server.draw_text_instant()

    @classmethod
    def header(cls):
        header.draw_text_instant()
        line.draw_text_instant()

    @classmethod
    def header_mt(cls):
        line_mt.draw_text_instant()
        for i in header_mt:
            i.draw_text_instant()
    
    @classmethod
    def draw_text_list(cls, list):
        Text.text_in_progress = True
        for i in list:
            if len(list) >= 1:
                list[0].draw_text()
                if len(list) >= 2 and list[0].text_cursor == len(list[0].text):
                    list[1].draw_text()
                    if len(list) >= 3 and list[1].text_cursor == len(list[1].text):
                        list[2].draw_text()
                        if len(list) >= 4 and list[2].text_cursor == len(list[2].text):
                            list[3].draw_text()
                            if len(list) >= 5 and list[3].text_cursor == len(list[3].text):
                                list[4].draw_text()
                                if len(list) >= 6 and list[4].text_cursor == len(list[4].text):
                                    list[5].draw_text()
                                    if len(list) >= 7 and list[5].text_cursor == len(list[5].text):
                                        list[6].draw_text()
                                        if len(list) >= 8 and list[6].text_cursor == len(list[6].text):
                                            list[7].draw_text()
                                            if len(list) >= 9 and list[7].text_cursor == len(list[7].text):
                                                list[8].draw_text()
                                                if len(list) >= 10 and list[8].text_cursor == len(list[8].text):
                                                    list[9].draw_text()
                                                    if len(list) >= 11 and list[9].text_cursor == len(list[9].text):
                                                        list[10].draw_text()
                                                        if len(list) >= 12 and list[10].text_cursor == len(list[10].text):
                                                            list[11].draw_text()
                                                            if len(list) >= 13 and list[11].text_cursor == len(list[11].text):
                                                                list[12].draw_text()
                                                                if len(list) >= 14 and list[12].text_cursor == len(list[12].text):
                                                                    list[13].draw_text()
                                                                    if len(list) >= 15 and list[13].text_cursor == len(list[13].text):
                                                                        list[14].draw_text()
                                                                        if len(list) >= 16 and list[14].text_cursor == len(list[14].text):
                                                                            list[15].draw_text()

        if list[-1].text_cursor == len(list[-1].text):
            Text.text_in_progress = False
            Text.text_redrawn = False

    @classmethod
    def redraw(cls):
        for i in cls.text_list:
            i.text_cursor = 0
            i.blank_text = FONT.render("", True, TERMINALGREEN)
            cls.text_redrawn = True

    @classmethod
    def change_lang(cls):
        global config, config_path, LANG

        if config["Settings"]["Language"] == "ENG":
            config.set("Settings", "Language", "RUS")
        else:
            config.set("Settings", "Language", "ENG")
        with open(config_path, "w") as cfg:
            config.write(cfg)


#-=Terminal Info=-#
robco_inc = Text(data_text["t_robco_inc"], indent+228, 25)
copyright = Text(data_text["t_copyright"], indent+265, 50)
server = Text(data_text["t_server"], indent+461, 75)

#-=Header=-#
header = Text(data_text["t_game_version"], indent, HEADER)
h_mt = Text(data_text["t_h_mt"], indent, HEADER)
h_mt_II = Text(data_text["t_h_mt_II"], indent, HEADER+25)
h_mt_III = Text(data_text["t_h_mt_III"], indent, HEADER+50)
header_mt = [h_mt, h_mt_II, h_mt_III]
if LANG in "ENG":
    line = Text("—" * 28, indent, LINE)
    line_mt = Text("—" * 35, indent, LINE+25)
else:
    line = Text("—" * 28, indent, LINE)
    line_mt = Text("—" * 35, indent, LINE+50)

#-=Tooltips=-#
look_around = Text(data_text["t_look_around"], indent, X)
heading_north = Text(data_text["t_heading_north"], indent, X)
venture_north = Text(data_text["t_venture_north"], indent, X)
heading_south = Text(data_text["t_heading_south"], indent, X)
retreating_south = Text(data_text["t_retreating_south"], indent, X)
heading_east = Text(data_text["t_heading_east"], indent, X)
heading_west = Text(data_text["t_heading_west"], indent, X)
debug = Text("> Debug Info", indent, X)

#-=Inventory Tooltips=-#
rusty_sword_inv = Text(data_text["t_rusty_sword_inv"], indent, X)
flask_inv = Text(data_text["t_flask_inv"], indent, X)
flask_blessed_inv = Text(data_text["t_flask_blessed_inv"], indent, X)
zombie_head_inv = Text(data_text["t_zombie_head_inv"], indent, X)
refined_gemstone_inv = Text(data_text["t_refined_gemstone_inv"], indent, X)
magical_shard_inv = Text(data_text["t_magical_shard_inv"], indent, X)
magic_sword_inv = Text(data_text["t_magic_sword_inv"], indent, X)
brass_key_inv = Text(data_text["t_brass_key_inv"], indent, X)
raw_gem_inv = Text(data_text["t_raw_gem_inv"], indent, X)


#-=Plains=-#
p_I = Text(data_text["t_p_I"], indent, TI)
p_II = Text(data_text["t_p_II"], indent, TII)
p_III = Text(data_text["t_p_III"], indent, TIII)
p_IV = Text(data_text["t_p_IV"], indent, TIV)
p_V = Text(data_text["t_p_V"], indent, TV)
p_VI = Text(data_text["t_p_VI"], indent, TVI)
p_VII = Text(data_text["t_p_VII"], indent, TVII)
p_VIII = Text(data_text["t_p_VIII"], indent, TVIII)
p_IX = Text(data_text["t_p_IX"], indent, TIX)
plains_text = [p_I, p_II, p_III, p_IV, p_V, p_VI, p_VII, p_VIII, p_IX]


#-=Town=-#
t_I = Text(data_text["t_t_I"], indent, TI)
t_II = Text(data_text["t_t_II"], indent, TII)
t_III = Text(data_text["t_t_III"], indent, TIII)
t_IV = Text(data_text["t_t_IV"], indent, TIV)
t_V = Text(data_text["t_t_V"], indent, TV)
t_VI = Text(data_text["t_t_VI"], indent, TVI)
t_VII = Text(data_text["t_t_VII"], indent, TVII)
t_VIII = Text(data_text["t_t_VIII"], indent, TVIII)
t_IX = Text(data_text["t_t_IX"], indent, TIX)
# t_X = Text("", indent, TX)
t_XI = Text(data_text["t_t_XI"], indent, TXI)
# t_XII = Text("", indent, TXII)
t_XIII = Text(data_text["t_t_XIII"], indent, TXIII)
t_XIV = Text(data_text["t_t_XIV"], indent, TXIV)
town_text = [t_I, t_II, t_III, t_IV, t_V, t_VI, t_VII, t_VIII, t_IX, t_XI, t_XIII, t_XIV]

#-=Smithy=-#
smithy_t = Text(data_text["t_smithy_t"], indent, X)
sm_I = Text(data_text["t_sm_I"], indent, TI)
sm_II = Text(data_text["t_sm_II"], indent, TII)
sm_III = Text(data_text["t_sm_III"], indent, TIII)
sm_IV = Text(data_text["t_sm_IV"], indent, TIV)
# sm_V = Text("", indent, TV)
sm_VI = Text(data_text["t_sm_VI"], indent, TVI)
sm_VII = Text(data_text["t_sm_VII"], indent, TVII)
sm_VIII = Text(data_text["t_sm_VIII"], indent, TVIII)
sm_IX = Text(data_text["t_sm_IX"], indent, TIX)
sm_X = Text(data_text["t_sm_X"], indent, TX)
sm_XI = Text(data_text["t_sm_XI"], indent, TXI)
sm_XII = Text(data_text["t_sm_XII"], indent, TXII)
smithy_a_dialogue = [sm_I, sm_II, sm_III, sm_IV, sm_VI, sm_VII, sm_VIII, sm_IX, sm_X, sm_XI, sm_XII]
#-=Part II=-#
sm_b_I = Text(data_text["t_sm_b_I"], indent, TI)
sm_b_II = Text(data_text["t_sm_b_II"], indent, TII)
sm_b_III = Text(data_text["t_sm_b_III"], indent, TIII)
sm_b_IV = Text(data_text["t_sm_b_IV"], indent, TIV)
# sm_b_V = Text("", indent, TV)
sm_b_VI = Text(data_text["t_sm_b_VI"], indent, TVI)
sm_b_VII = Text(data_text["t_sm_b_VII"], indent, TVII)
sm_b_VIII = Text(data_text["t_sm_b_VIII"], indent, TVIII)
# sm_b_IX = Text("", indent, TIX)
sm_b_X = Text(data_text["t_sm_b_X"], indent, TX)
sm_b_XI = Text(data_text["t_sm_b_XI"], indent, TXI)
sm_b_XII = Text(data_text["t_sm_b_XII"], indent, TXII)
smithy_b_dialogue = [sm_b_I, sm_b_II, sm_b_III, sm_b_IV, sm_b_VI, sm_b_VII, sm_b_VIII, sm_b_X, sm_b_XI, sm_b_XII]

#-=Priest=-#
priest_t = Text(data_text["t_priest_t"], indent, X)
pr_I = Text(data_text["t_pr_I"], indent, TI)
pr_II = Text(data_text["t_pr_II"], indent, TII)
pr_III = Text(data_text["t_pr_III"], indent, TIII)
pr_IV = Text(data_text["t_pr_IV"], indent, TIV)
# pr_V = Text("", indent, TV)
pr_VI = Text(data_text["t_pr_VI"], indent, TVI)
pr_VII = Text(data_text["t_pr_VII"], indent, TVII)
pr_VIII = Text(data_text["t_pr_VIII"], indent, TVIII)
pr_IX = Text(data_text["t_pr_IX"], indent, TIX)
pr_X = Text(data_text["t_pr_X"], indent, TX)
pr_XI = Text(data_text["t_pr_XI"], indent, TXI)
pr_XII = Text(data_text["t_pr_XII"], indent, TXII)
pr_XIII = Text(data_text["t_pr_XIII"], indent, TXIII)
pr_XIV = Text(data_text["t_pr_XIV"], indent, TXIV)
pr_XV = Text(data_text["t_pr_XV"], indent, TXV)
pr_XVI = Text(data_text["t_pr_XVI"], indent, TXVI)
priest_a_dialogue = [pr_I, pr_II, pr_III, pr_IV, pr_VI, pr_VII, pr_VIII, pr_IX, pr_X, pr_XI, pr_XII, pr_XIII, pr_XIV, pr_XV, pr_XVI]

#-=Priest Quest Completed=-#
pr_b_I = Text(data_text["t_pr_b_I"], indent, TI)
pr_b_II = Text(data_text["t_pr_b_II"], indent, TII)
pr_b_III = Text(data_text["t_pr_b_III"], indent, TIII)
pr_b_IV = Text(data_text["t_pr_b_IV"], indent, TIV)
# pr_b_V = Text("", indent, TV)
pr_b_VI = Text(data_text["t_pr_b_VI"], indent, TVI)
pr_b_VII = Text(data_text["t_pr_b_VII"], indent, TVII)
pr_b_VIII = Text(data_text["t_pr_b_VIII"], indent, TVIII)
pr_b_IX = Text(data_text["t_pr_b_IX"], indent, TIX)
pr_b_X = Text(data_text["t_pr_b_X"], indent, TX)
pr_b_XI = Text(data_text["t_pr_b_XI"], indent, TXI)
pr_b_XII = Text(data_text["t_pr_b_XII"], indent, TXII)
pr_b_XIII = Text(data_text["t_pr_b_XIII"], indent, TXIII)
pr_b_XIV = Text(data_text["t_pr_b_XIV"], indent, TXIV)
pr_b_XV = Text(data_text["t_pr_b_XV"], indent, TXV)
pr_b_XVI = Text(data_text["t_pr_b_XVI"], indent, TXVI)
pr_b_dialogue = [pr_b_I, pr_b_II, pr_b_III, pr_b_IV, pr_b_VI, pr_b_VII, pr_b_VIII, pr_b_IX, pr_b_X, pr_b_XI, pr_b_XII, pr_b_XIII, pr_b_XIV, pr_b_XV, pr_b_XVI]

#-=Priest Final Dialogue=-#
pr_c_I = Text(data_text["t_pr_c_I"], indent, TI)
pr_c_II = Text(data_text["t_pr_c_II"], indent, TII)
pr_c_III = Text(data_text["t_pr_c_III"], indent, TIII)
pr_c_IV = Text(data_text["t_pr_c_IV"], indent, TIV)
pr_c_V = Text(data_text["t_pr_c_V"], indent, TV)
pr_c_VI = Text(data_text["t_pr_c_VI"], indent, TVI)
pr_c_VII = Text(data_text["t_pr_c_VII"], indent, TVII)
pr_c_VIII = Text(data_text["t_pr_c_VIII"], indent, TVIII)
pr_c_IX = Text(data_text["t_pr_c_IX"], indent, TIX)
pr_c_X = Text(data_text["t_pr_c_X"], indent, TX)
pr_c_text = [pr_c_I, pr_c_II, pr_c_III, pr_c_IV, pr_c_V, pr_c_VI, pr_c_VII, pr_c_VIII, pr_c_IX, pr_c_X]


#-=Chapel=-#
c_I = Text(data_text["t_c_I"], indent, TI)
c_II = Text(data_text["t_c_II"], indent, TII)
c_III = Text(data_text["t_c_III"], indent, TIII)
c_IV = Text(data_text["t_c_IV"], indent, TIV)
c_V = Text(data_text["t_c_V"], indent, TV)
c_VI = Text(data_text["t_c_VI"], indent, TVI)
c_VII = Text(data_text["t_c_VII"], indent, TVII)
c_VIII = Text(data_text["t_c_VIII"], indent, TVIII)
c_IX = Text(data_text["t_c_IX"], indent, TIX)
c_X = Text(data_text["t_c_X"], indent, TX)
c_XI = Text(data_text["t_c_XI"], indent, TXI)
# c_XI_alt = Text(data_text["t_c_XI_alt"], indent, TXI)
c_XII = Text(data_text["t_c_XII"], indent, TXII)
# c_XII_alt = Text(data_text["t_c_XII_alt"], indent, TXII)
c_XIII = Text(data_text["t_c_XIII"], indent, TXIII)
c_XIV = Text(data_text["t_c_XIV"], indent, TXIV)
# c_XV = Text(data_text["t_c_XV"], indent, TXV)
chapel_text = [c_I, c_II, c_III, c_IV, c_V, c_VI, c_VII, c_VIII, c_IX, c_X, c_XI, c_XII, c_XIII, c_XIV]
#-=Grave=-#
grave_t = Text(data_text["t_grave_t"], indent, X)
grave_t_II = Text(data_text["t_grave_t_II"], indent, X)
g_I = Text(data_text["t_g_I"], indent, TI)
g_II = Text(data_text["t_g_II"], indent, TII)
g_III = Text(data_text["t_g_III"], indent, TIII)
g_IV = Text(data_text["t_g_IV"], indent, TIV)
g_VI = Text(data_text["t_g_VI"], indent, TVI)
g_VII = Text(data_text["t_g_VII"], indent, TVII)
g_VIII = Text(data_text["t_g_VIII"], indent, TVIII)
g_VIX = Text(data_text["t_g_VIX"], indent, TIX)
grave_text = [g_I, g_II, g_III, g_IV]
grave_text_II = [g_VI, g_VII, g_VIII, g_VIX]
#-=Chapel inside=-#
chapel_t = Text(data_text["t_chapel_t"], indent, X)
ch_I = Text(data_text["t_ch_I"], indent, TI)
ch_II = Text(data_text["t_ch_II"], indent, TII)
ch_III = Text(data_text["t_ch_III"], indent, TIII)
ch_IV = Text(data_text["t_ch_IV"], indent, TIV)
ch_V = Text(data_text["t_ch_V"], indent, TV)
ch_VI = Text(data_text["t_ch_VI"], indent, TVI)
ch_VII = Text(data_text["t_ch_VII"], indent, TVII)
ch_VIII = Text(data_text["t_ch_VIII"], indent, TVIII)
ch_IX = Text(data_text["t_ch_IX"], indent, TIX)
ch_X = Text(data_text["t_ch_X"], indent, TX)
ch_text = [ch_I, ch_II, ch_III, ch_IV, ch_V, ch_VI, ch_VII, ch_VIII, ch_IX, ch_X]


#-=Swamp=-#
bog_I = Text(data_text["t_bog_I"], indent, TI)
bog_II = Text(data_text["t_bog_II"], indent, TII)
bog_III = Text(data_text["t_bog_III"], indent, TIII)
bog_IV = Text(data_text["t_bog_IV"], indent, TIV)
bog_V = Text(data_text["t_bog_V"], indent, TV)
bog_VI = Text(data_text["t_bog_VI"], indent, TVI)
bog_VII = Text(data_text["t_bog_VII"], indent, TVII)
bog_VIII = Text(data_text["t_bog_VIII"], indent, TVIII)
bog_IX = Text(data_text["t_bog_IX"], indent, TIX)
bog_X = Text(data_text["t_bog_X"], indent, TX)
bog_XI = Text(data_text["t_bog_XI"], indent, TXI)
bog_XII = Text(data_text["t_bog_XII"], indent, TXII)
bog_XIII = Text(data_text["t_bog_XIII"], indent, TXIII)
bog_XIV = Text(data_text["t_bog_XIV"], indent, TXIV)
bog_I_b = Text(data_text["t_bog_I_b"], indent, TI)
bog_II_b = Text(data_text["t_bog_II_b"], indent, TII)
bog_text = [bog_I, bog_II, bog_III, bog_IV, bog_V, bog_VI, bog_VII, bog_VIII, bog_IX, bog_X, bog_XI, bog_XII, bog_XIII, bog_XIV]
bog_text_b = [bog_I_b, bog_II_b]

#-=Wizard Dialogue A=-#
wizard_t = Text(data_text["t_wizard_t"], indent, X)
wizard_a_I = Text(data_text["t_wizard_a_I"], indent, TI)
wizard_a_II = Text(data_text["t_wizard_a_II"], indent, TII)
wizard_a_III = Text(data_text["t_wizard_a_III"], indent, TIII)
wizard_a_IV = Text(data_text["t_wizard_a_IV"], indent, TIV)
wizard_a_V = Text(data_text["t_wizard_a_V"], indent, TV)
# wizard_a_VI = Text(data_text["t_wizard_a_VI"], indent, TVI)
wizard_a_VII = Text(data_text["t_wizard_a_VII"], indent, TVII)
wizard_a_VIII = Text(data_text["t_wizard_a_VIII"], indent, TVIII)
wizard_a_IX = Text(data_text["t_wizard_a_IX"], indent, TIX)
wizard_a_X = Text(data_text["t_wizard_a_X"], indent, TX)
wizard_a_XI = Text(data_text["t_wizard_a_XI"], indent, TXI)
wizard_a_XII = Text(data_text["t_wizard_a_XII"], indent, TXII)
wizard_a_XIII = Text(data_text["t_wizard_a_XIII"], indent, TXIII)
wizard_a_XIV = Text(data_text["t_wizard_a_XIV"], indent, TXIV)
wizard_a_XV = Text(data_text["t_wizard_a_XV"], indent, TXV)
wizard_a_XVI = Text(data_text["t_wizard_a_XVI"], indent, TXVI)
wizard_a_dialogue = [wizard_a_I, wizard_a_II, wizard_a_III, wizard_a_IV, wizard_a_V, wizard_a_VII, wizard_a_VIII, wizard_a_IX, wizard_a_X, wizard_a_XI, wizard_a_XII, wizard_a_XIII, wizard_a_XIV, wizard_a_XV, wizard_a_XVI]
#-=Part II=-#
wizard_aII_I = Text(data_text["t_wizard_aII_I"], indent, TI)
wizard_aII_II = Text(data_text["t_wizard_aII_II"], indent, TII)
wizard_aII_III = Text(data_text["t_wizard_aII_III"], indent, TIII)
wizard_aII_IV = Text(data_text["t_wizard_aII_IV"], indent, TIV)
wizard_aII_dialogue = [wizard_aII_I, wizard_aII_II, wizard_aII_III, wizard_aII_IV]

#-=Wizard Dialogue B=-#
wizard_b_I = Text(data_text["t_wizard_b_I"], indent, TI)
wizard_b_II = Text(data_text["t_wizard_b_II"], indent, TII)
wizard_b_III = Text(data_text["t_wizard_b_III"], indent, TIII)
wizard_b_IV = Text(data_text["t_wizard_b_IV"], indent, TIV)
wizard_b_V = Text(data_text["t_wizard_b_V"], indent, TV)
wizard_b_dialogue = [wizard_b_I, wizard_b_II, wizard_b_III, wizard_b_IV, wizard_b_V]

#-=Wizard Dialogue C=-#
wizard_c_I = Text(data_text["t_wizard_c_I"], indent, TI)
wizard_c_II = Text(data_text["t_wizard_c_II"], indent, TII)
wizard_c_III = Text(data_text["t_wizard_c_III"], indent, TIII)
wizard_c_IV = Text(data_text["t_wizard_c_IV"], indent, TIV)
wizard_c_V = Text(data_text["t_wizard_c_V"], indent, TV)
wizard_c_VI = Text(data_text["t_wizard_c_VI"], indent, TVI)
wizard_c_VII = Text(data_text["t_wizard_c_VII"], indent, TVII)
wizard_c_VIII = Text(data_text["t_wizard_c_VIII"], indent, TVIII)
wizard_c_IX = Text(data_text["t_wizard_c_IX"], indent, TIX)
wizard_c_X = Text(data_text["t_wizard_c_X"], indent, TX)
wizard_c_XI = Text(data_text["t_wizard_c_XI"], indent, TXI)
wizard_c_XII = Text(data_text["t_wizard_c_XII"], indent, TXII)
wizard_c_XIII = Text(data_text["t_wizard_c_XIII"], indent, TXIII)
wizard_c_XIV = Text(data_text["t_wizard_c_XIV"], indent, TXIV)
wizard_c_XV = Text(data_text["t_wizard_c_XV"], indent, TXV)
wizard_c_XVI = Text(data_text["t_wizard_c_XVI"], indent, TXVI)
wizard_c_dialogue = [wizard_c_I, wizard_c_II, wizard_c_III, wizard_c_IV, wizard_c_V, wizard_c_VI, wizard_c_VII, wizard_c_VIII, wizard_c_IX, wizard_c_X, wizard_c_XI, wizard_c_XII, wizard_c_XIII, wizard_c_XIV, wizard_c_XV, wizard_c_XVI]
#-=Part II=-#
wizard_cII_I = Text(data_text["t_wizard_cII_I"], indent, TI)
wizard_cII_II = Text(data_text["t_wizard_cII_II"], indent, TII)
wizard_cII_III = Text(data_text["t_wizard_cII_III"], indent, TIII)
wizard_cII_IV = Text(data_text["t_wizard_cII_IV"], indent, TIV)
wizard_cII_V = Text(data_text["t_wizard_cII_V"], indent, TV)
wizard_cII_VI = Text(data_text["t_wizard_cII_VI"], indent, TVI)
wizard_cII_VII = Text(data_text["t_wizard_cII_VII"], indent, TVII)
wizard_cII_VIII = Text(data_text["t_wizard_cII_VIII"], indent, TVIII)
wizard_cII_IX = Text(data_text["t_wizard_cII_IX"], indent, TIX)
wizard_cII_X = Text(data_text["t_wizard_cII_X"], indent, TX)
wizard_cII_dialogue = [wizard_cII_I, wizard_cII_II, wizard_cII_III, wizard_cII_IV, wizard_cII_V, wizard_cII_VI, wizard_cII_VII, wizard_cII_VIII, wizard_cII_IX, wizard_cII_X]

#-=Wizard Dialogue D=-#
wizard_d_I = Text(data_text["t_wizard_d_I"], indent, TI)
wizard_d_II = Text(data_text["t_wizard_d_II"], indent, TII)
wizard_d_III = Text(data_text["t_wizard_d_III"], indent, TIII)
wizard_d_IV = Text(data_text["t_wizard_d_IV"], indent, TIV)
wizard_d_V = Text(data_text["t_wizard_d_V"], indent, TV)
wizard_d_VI = Text(data_text["t_wizard_d_VI"], indent, TVI)
wizard_d_dialogue = [wizard_d_I, wizard_d_II, wizard_d_III, wizard_d_IV, wizard_d_V, wizard_d_VI]


#-=Mountainside=-#
grelok_t = Text(data_text["t_grelok_t"], indent, X)
raw_gem_t = Text(data_text["t_raw_gem_t"], indent, X)
mt_I = Text(data_text["t_mt_I"], indent, TII)
mt_II = Text(data_text["t_mt_II"], indent, TIII)
mt_III = Text(data_text["t_mt_III"], indent, TIV)
mt_IV = Text(data_text["t_mt_IV"], indent, TV)
mt_V = Text(data_text["t_mt_V"], indent, TVI)
mt_VI = Text(data_text["t_mt_VI"], indent, TVII)
mt_VII = Text(data_text["t_mt_VII"], indent, TVIII)
mt_VIII = Text(data_text["t_mt_VIII"], indent, TIX)
mt_IX = Text(data_text["t_mt_VIX"], indent, TX)
mt_X = Text(data_text["t_mt_VX"], indent, TXI)
mt_XI = Text(data_text["t_mt_VXI"], indent, TXII)
mt_XII = Text(data_text["t_mt_VXII"], indent, TXIII)
mt_text = [mt_I, mt_II, mt_III, mt_IV, mt_V, mt_VI, mt_VII, mt_VIII, mt_IX, mt_X, mt_XI, mt_XII]

#-=Grelok Defeated=-#
grelok_defeated_a_I = Text(data_text["t_grelok_defeated_a_I"], indent, TII)
grelok_defeated_a_II = Text(data_text["t_grelok_defeated_a_II"], indent, TIII)
grelok_defeated_a_III = Text(data_text["t_grelok_defeated_a_III"], indent, TIV)
grelok_defeated_a_IV = Text(data_text["t_grelok_defeated_a_IV"], indent, TV)
grelok_defeated_a_V = Text(data_text["t_grelok_defeated_a_V"], indent, TVI)
grelok_defeated_a_VI = Text(data_text["t_grelok_defeated_a_VI"], indent, TVII)
grelok_defeated_a_VII = Text(data_text["t_grelok_defeated_a_VII"], indent, TVIII)
grelok_defeated_a_VIII = Text(data_text["t_grelok_defeated_a_VIII"], indent, TIX)
grelok_defeated_a_IX = Text(data_text["t_grelok_defeated_a_VIX"], indent, TX)
grelok_defeated_a_X = Text(data_text["t_grelok_defeated_a_X"], indent, TXI)
grelok_defeated_a_XI = Text(data_text["t_grelok_defeated_a_XI"], indent, TXII)
grelok_defeated_a_XII = Text(data_text["t_grelok_defeated_a_XII"], indent, TXIII)
grelok_defeated_a_XIII = Text(data_text["t_grelok_defeated_a_XIII"], indent, TXIV)
grelok_defeated_a_XIV = Text(data_text["t_grelok_defeated_a_XIV"], indent, TXV)
grelok_defeated_a_XV = Text(data_text["t_grelok_defeated_a_XV"], indent, TXVI)
grelok_defeated_a_text = [grelok_defeated_a_I, grelok_defeated_a_II, grelok_defeated_a_III, grelok_defeated_a_IV, grelok_defeated_a_V, grelok_defeated_a_VI, grelok_defeated_a_VII, grelok_defeated_a_VIII, grelok_defeated_a_IX, grelok_defeated_a_X, grelok_defeated_a_XI, grelok_defeated_a_XII, grelok_defeated_a_XIII, grelok_defeated_a_XIV, grelok_defeated_a_XV]
#-=Part II=-#
grelok_defeated_b_I = Text(data_text["t_grelok_defeated_b_I"], indent, TII)
grelok_defeated_b_II = Text(data_text["t_grelok_defeated_b_II"], indent, TIII)
grelok_defeated_b_III = Text(data_text["t_grelok_defeated_b_III"], indent, TIV)
grelok_defeated_b_IV = Text(data_text["t_grelok_defeated_b_IV"], indent, TV)
grelok_defeated_b_V = Text(data_text["t_grelok_defeated_b_V"], indent, TVI)
grelok_defeated_b_VI = Text(data_text["t_grelok_defeated_b_VI"], indent, TVII)
grelok_defeated_b_VII = Text(data_text["t_grelok_defeated_b_VII"], indent, TVIII)
grelok_defeated_b_VIII = Text(data_text["t_grelok_defeated_b_VIII"], indent, TIX)
grelok_defeated_b_IX = Text(data_text["t_grelok_defeated_b_IX"], indent, TX)
grelok_defeated_b_X = Text(data_text["t_grelok_defeated_b_X"], indent, TXI)
grelok_defeated_b_XI = Text(data_text["t_grelok_defeated_b_XI"], indent, TXII)
grelok_defeated_b_XII = Text(data_text["t_grelok_defeated_b_XII"], indent, TXIII)
grelok_defeated_b_XIII = Text(data_text["t_grelok_defeated_b_XIII"], indent, TXIV)
grelok_defeated_b_XIV = Text(data_text["t_grelok_defeated_b_XIV"], indent, TXV)
grelok_defeated_b_text = [grelok_defeated_b_I, grelok_defeated_b_II, grelok_defeated_b_III, grelok_defeated_b_IV, grelok_defeated_b_V, grelok_defeated_b_VI, grelok_defeated_b_VII, grelok_defeated_b_VIII, grelok_defeated_b_IX, grelok_defeated_b_X, grelok_defeated_b_XI, grelok_defeated_b_XII, grelok_defeated_b_XIII, grelok_defeated_b_XIV]

if LANG in "RUS":
    for i in mt_text:
        i.y += 25
    for i in grelok_defeated_a_text:
        i.y += 25
    for i in grelok_defeated_b_text:
        i.y += 25
