from machine import Pin
from neopixel import NeoPixel
import time

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)

np = NeoPixel(Pin(48), 1)

def set_color(color, g = None, b = None):
    if isinstance(color, tuple):
        # Called with a tuple: set_color(RED)
        np[0] = color
    elif g is not None and b is not None:
        # Called with three named values: set_color(255, 0, 0)
        np[0] = (color, g, b)
    else:
        raise ValueError("set_color expects either a tuple (r, g, b) or three int values")
    np.write()

def blink(color, blink_speed = 0.5, brightness_cap = 0.15):
    r, g, b = color
    
    # Find the maximum component to normalize
    max_component = max(r, g, b)
    
    if max_component > 0:
        # Scale all components so the max is at the brightness_cap percentage of 255
        scale_factor = (255 * brightness_cap) / max_component
        dimmed_color = (int(r * scale_factor), int(g * scale_factor), int(b * scale_factor))
    else:
        dimmed_color = (0, 0, 0)
    
    while True:
        set_color(dimmed_color)
        time.sleep(blink_speed)
        
        set_color(BLACK)
        time.sleep(blink_speed)

blink(RED)
