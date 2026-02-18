# LED Blink Project

**Difficulty:** Beginner  
**Time to Complete:** 5-10 minutes  
**Board:** ESP32-S3-N16R8  
**Framework:** MicroPython

## Overview
Control the onboard WS2812 RGB LED with color cycling and brightness control. 
This project introduces GPIO pin control, NeoPixel protocol, and functional programming 
patterns in MicroPython.

## What You'll Learn
- GPIO pin configuration with MicroPython
- WS2812 NeoPixel LED control
- RGB color representation
- Function definitions and parameters
- Non-blocking timing with `time.sleep()`
- Brightness scaling and color normalization

## Hardware Requirements
- ESP32-S3-N16R8 development board
- USB-C cable (data-capable)
- No external components needed (uses onboard RGB LED on GPIO48)

## Pins Used
- **GPIO48:** Onboard WS2812 RGB LED (NeoPixel)

## Features
This implementation includes:
- **Color presets:** RED, GREEN, BLUE, YELLOW, MAGENTA, CYAN, WHITE
- **Flexible color setting:** Set colors by tuple or RGB values
- **Brightness control:** Cap brightness at 15% to avoid harsh blinking
- **Adjustable blink speed:** Control on/off timing
- **Color scaling:** Automatically normalizes RGB values to prevent color shifts

## Code Walkthrough

### Color Presets
```python
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# ... and more
```

### Setting Colors
Two ways to set LED color:
```python
# Method 1: Using a color tuple
set_color(RED)

# Method 2: Using RGB values
set_color(255, 0, 0)  # Red
```

### Blinking with Control
```python
# Blink red at 0.5s intervals with 15% brightness cap
blink(RED, blink_speed=0.5, brightness_cap=0.15)

# Blink blue faster at full brightness
blink(BLUE, blink_speed=0.2, brightness_cap=1.0)
```

### Brightness Capping
The `brightness_cap` parameter (0.0–1.0) prevents eye strain:
- `brightness_cap=0.15` dims the color to 15% intensity
- `brightness_cap=1.0` uses full brightness
- Scaling preserves the color ratio (no color shift)

## Getting Started

1. **Upload the code** to your ESP32-S3 using Thonny or another MicroPython IDE
2. **Run the script** — the RGB LED will blink red at half-second intervals
3. **Modify and experiment:**
   - Change the color: `blink(BLUE)` or `blink(GREEN)`
   - Adjust speed: `blink(RED, blink_speed=0.2)` for faster blinking
   - Change brightness: `blink(RED, brightness_cap=0.5)` for brighter LED

## Expected Output
The onboard RGB LED will blink a dimmed red color continuously.

## Troubleshooting

**LED doesn't light up:**
- Verify GPIO48 is the correct pin for your board's RGB LED
- Ensure MicroPython firmware is installed (not Arduino)
- Check USB cable is connected and powered

**LED color looks wrong:**
- NeoPixel uses GRB format internally, but this code handles RGB properly
- Try adjusting `brightness_cap` to see if it's a visibility issue

**LED turns on but doesn't blink:**
- Check that `time.sleep()` values are correct
- Verify the `while True:` loop is executing (add serial output to debug)

## Next Steps
Once this works, try:
- Create a rainbow cycling effect with multiple colors
- Add a button to toggle blinking on/off
- Pulse the brightness instead of on/off blinking
- Combine with temperature/light sensors to change color based on readings
- Create multiple functions for different blink patterns (SOS, heartbeat, etc.)

## Files in This Project
- `led-blink.py` — Complete MicroPython implementation
- `README.md` — This guide
