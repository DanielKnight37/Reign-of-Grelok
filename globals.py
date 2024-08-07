import pygame, time, random
import sys, os

if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

pygame.init()
SCREENWIDTH, SCREENHEIGHT = 1280, 720
FULLSCREEN = True
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pygame.FULLSCREEN)
FPS = 85
TERMINALGREEN = (26,255,128)
TERMINALGREEN_H = (26,255,128,125)
FONT = pygame.font.Font(fr"{application_path}\src\font\Fixedsys.ttf", 30)
VERSION = "Царство Грелока (бета v.632)"
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
LANGUAGE = "RUS"
CURSOR = pygame.image.load(fr"{application_path}\src\cursor\cursor.png")
ROOT_INDEX = 0
TOWN_INDEX = 0
CHAPEL_INDEX = 0
SWAMP_INDEX = 0
MOUNTAINSIDE_INDEX = 0

# Slots
indent = 100
I = 200
II = 250
III = 300
IV = 350
V = 400
VI = 450
VII = 500
VIII = 550
IX = 600
X = 650
XI = 700
XII = 750

# Text lines
HEADER = 125
LINE = 175
TI = 200
TII = 225
TIII= 250
TIV = 275
TV = 300
TVI = 325
TVII = 350
TVIII = 375
TIX = 400
TX = 425
TXI = 450
TXII = 475
TXIII = 500
TXIV = 525
TXV = 550
TXVI = 575
