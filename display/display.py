from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 480
FONT_FILE = 'Font.ttc'
COLOR_BLACK = 0
COLOR_CLEAR = 255


def last_update() -> str:
    ts = datetime.now()
    return ts.strftime("%Y-%m-%d, %H:%M")


font24 = ImageFont.truetype(FONT_FILE, 24)
font18 = ImageFont.truetype(FONT_FILE, 18)

img = Image.new('1', (DISPLAY_WIDTH, DISPLAY_HEIGHT), COLOR_CLEAR)

draw = ImageDraw.Draw(img)
draw.line((0, 25, DISPLAY_WIDTH, 25))
draw.text((10, 0), 'Taskowl', font=font18)
draw.text((10, 25), '• Task 1', font=font24)
draw.text((10, 50), '• Task 2', font=font24)

draw.text((540, 0), 'last update: ' + last_update(), font=font18)

img.show()
