import board
import busio
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_sh1106
import time

displayio.release_displays()

i2c = busio.I2C(board.GP1, board.GP0)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3c)

WIDTH = 130 #should be 128, but at the right side of the screen there are some disturb
HEIGHT = 64
BORDER = 5
WHITE = 0xFFFFFF
BLACK = 0x000000

display = adafruit_displayio_sh1106.SH1106(display_bus, width=WIDTH, height=HEIGHT)

# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
color_palette = displayio.Palette(1)
color_palette[0] = BLACK  # White

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
#inner_bitmap = displayio.Bitmap(WIDTH - BORDER * 2, HEIGHT - BORDER * 2, 1)
#inner_palette = displayio.Palette(1)
#inner_palette[0] = BLACK  # Black
#inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER)
#splash.append(inner_sprite)

# Draw a label
text = "Hi men!"
text_area = label.Label(terminalio.FONT, text=text, color=WHITE, x=WIDTH // 2 - 20, y=10)
splash.append(text_area)

text = "Example for I2C"
text_area = label.Label(terminalio.FONT, text=text, color=WHITE, x=6, y=20)
splash.append(text_area)

text = "sh1106"
text_area = label.Label(terminalio.FONT, text=text, color=WHITE, x=WIDTH // 2 - 20, y=30)
splash.append(text_area)


while True:
    pass
