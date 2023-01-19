import webbrowser

import time
import pyautogui as py

import sys
sys.path.insert(1, './mouse_movement')
from MouseMovement import mouse_move

import subprocess

process_1 = subprocess.run('npm install', cwd='./cgs-recaptcha', shell=True)
time.sleep(5)
process_2 = subprocess.Popen('exec npm run start',stdout=subprocess.PIPE, cwd='./cgs-recaptcha', shell=True)
time.sleep(5)

url= 'http://localhost:3000/'  
img = './resources/captcha-new.png'
edge_url = '/usr/bin/microsoft-edge'

webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_url))
webbrowser.get('edge')

time.sleep(2)

for i in range(3):
    webbrowser.open_new_tab(url)  

    time.sleep(2)
    py.hotkey('f5')
    time.sleep(5)

    c = py.locateCenterOnScreen(img, confidence=0.5)

    print(c)

    time.sleep(2)
    mouse_move(c.x, c.y)
    time.sleep(0.1)

    py.click()
    time.sleep(2)

    py.hotkey('ctrl', 'w')
    time.sleep(0.1)

py.hotkey('ctrl', 'shift', 'w')
process_2.kill()