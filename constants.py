import pygame

# ---------
# CONSTANTS
# ---------

# --- PIXELS ---


SIZE = WIDTH, HEIGHT = (1000, 1000)
DISPLAY = pygame.display.set_mode(SIZE)
FONT = pygame.font.get_default_font()
ROWS = 3
COLS = 3
SQSIZE = WIDTH // COLS

LINE_WIDTH = 15
CIRC_WIDTH = 15
CROSS_WIDTH = 20

RADIUS = SQSIZE // 4

OFFSET = 50

# --- COLORS ---

BG_COLOR = (38, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRC_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

