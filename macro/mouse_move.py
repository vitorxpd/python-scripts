import pyautogui
import time
import random

def move_mouse():
  # Get the screen dimensions
  screen_width, screen_height = pyautogui.size()

  # Generate random coordinates within the screen dimensions
  new_x = random.randint(0, screen_width - 1)
  new_y = random.randint(0, screen_height - 1)

  # Move the mouse to the new coordinates
  pyautogui.moveTo(new_x, new_y)

# Call the function initially
move_mouse()

# Set an interval to call the function every 5 seconds
while True:
  time.sleep(5)
  move_mouse()
