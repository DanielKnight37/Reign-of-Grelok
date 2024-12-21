import pygame, time, random
import sys, os
import json
import configparser

if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

pygame.init()

config = configparser.ConfigParser()
config_path = fr"{application_path}\settings.ini"
config.read(config_path)
LANG = config["Settings"]["Language"]

json_text = open(fr"{application_path}\{LANG}.json", encoding="utf-8")
data_text = json.load(json_text)
json_text.close()

SCREENWIDTH, SCREENHEIGHT = 1280, 720
RESOLUTION = (SCREENWIDTH, SCREENHEIGHT)
FULLSCREEN = True
SCREEN = pygame.display.set_mode(RESOLUTION, pygame.FULLSCREEN)
FPS = 85
TERMINALGREEN = (26,255,128)
TERMINALGREEN_H = (26,255,128,125)
FONT = pygame.font.Font(fr"{application_path}\src\font\Fixedsys.otf", 30)
VERSION = data_text["t_game_version"]
BACKGROUND = pygame.image.load(fr"{application_path}\src\background\background.png").convert()
ICON = pygame.image.load(fr"{application_path}\src\icon\vault_boy.png")
TERMINALHUM = pygame.mixer.Sound(fr"{application_path}\src\sounds\terminal_hum.wav")
SELECT = pygame.mixer.Sound(fr"{application_path}\src\sounds\charenter.wav")
SELECT.set_volume(.1)
SELECT_II = pygame.mixer.Sound(fr"{application_path}\src\sounds\charenter_2.wav")
SELECT_II.set_volume(.1)
HOVER = pygame.mixer.Sound(fr"{application_path}\src\sounds\hover.wav")
HOVER.set_volume(.1)
TEXT_SCROLL_SOUND = pygame.mixer.Sound(fr"{application_path}\src\sounds\text_scroll.wav")
TERMINAL_FORWARD = pygame.mixer.Sound(fr"{application_path}\src\sounds\terminal_forward.wav")
TERMINAL_FORWARD.set_volume(.1)
TERMINAL_POWERDOWN = pygame.mixer.Sound(fr"{application_path}\src\sounds\terminal_powerdown.wav")
TERMINAL_POWERDOWN.set_volume(.2)
HOLOTAPE_START = pygame.mixer.Sound(fr"{application_path}\src\sounds\holotape_start.wav")
HOLOTAPE_START.set_volume(.2)
HOLOTAPE_STOP = pygame.mixer.Sound(fr"{application_path}\src\sounds\holotape_stop.wav")
HOLOTAPE_STOP.set_volume(.2)
TAB = pygame.mixer.Sound(fr"{application_path}\src\sounds\mode.wav")
TAB.set_volume(.2)
CURSOR = pygame.image.load(fr"{application_path}\src\cursor\cursor.png")
ROOT_INDEX = 0
TOWN_INDEX = 0
CHAPEL_INDEX = 0
SWAMP_INDEX = 0
MOUNTAINSIDE_INDEX = 0

# Slots
indent = 100
I = 170
II = 220
III = 270
IV = 320
V = 370
VI = 420
VII = 470
VIII = 520
IX = 570
X = 620
XI = 670

# Text lines
HEADER = 113
LINE = 142
TI = 170
TII = 195
TIII= 220
TIV = 245
TV = 270
TVI = 295
TVII = 320
TVIII = 345
TIX = 370
TX = 395
TXI = 420
TXII = 445
TXIII = 470
TXIV = 495
TXV = 520
TXVI = 545
