import keyboard
import time

hotkey = "ctrl + j"

def func():
    print('hey')

while True:
  if keyboard.is_pressed(hotkey):
    print('Hotkey')
    time.sleep(0.05)
