import webbrowser
import time
import pyautogui as py
from random import randint, choice
from math import ceil
import numpy as np


## Wind Mouse algorithm
sqrt3 = np.sqrt(3)
sqrt5 = np.sqrt(5)

def wind_mouse(start_x, start_y, dest_x, dest_y, G_0=9, W_0=3, M_0=35, D_0=20, move_mouse=lambda x,y: None):
    '''
    WindMouse algorithm. Calls the move_mouse kwarg with each new step.
    Released under the terms of the GPLv3 license.
    G_0 - magnitude of the gravitational fornce
    W_0 - magnitude of the wind force fluctuations
    M_0 - maximum step size (velocity clip threshold)
    D_0 - distance where wind behavior changes from random to damped
    '''
    current_x,current_y = start_x,start_y
    v_x = v_y = W_x = W_y = 0
    while (dist:=np.hypot(dest_x-start_x,dest_y-start_y)) >= 10:
        W_mag = min(W_0, dist)
        if dist >= D_0:
            W_x = W_x/sqrt3 + (2*np.random.random()-1)*W_mag/sqrt5
            W_y = W_y/sqrt3 + (2*np.random.random()-1)*W_mag/sqrt5
        else:
            W_x /= sqrt5
            W_y /= sqrt5
            if M_0 < 3:
                M_0 = np.random.random()*3 + 3
            else:
                M_0 /= sqrt3    #changing right now
                # G_0 *= 1.5
        v_x += W_x + G_0*(dest_x-start_x)/dist
        v_y += W_y + G_0*(dest_y-start_y)/dist
        v_mag = np.hypot(v_x, v_y)
        if v_mag > M_0:
            v_clip = M_0/2 + np.random.random()*M_0/2
            v_x = (v_x/v_mag) * v_clip
            v_y = (v_y/v_mag) * v_clip
        start_x += v_x
        start_y += v_y
        move_x = int(np.round(start_x))
        move_y = int(np.round(start_y))
        if current_x != move_x or current_y != move_y:
            #This should wait for the mouse polling interval
            move_mouse(current_x:=move_x,current_y:=move_y)
    return current_x,current_y


def mouse_move(x_target,y_target):
    url= 'https://www.google.com/recaptcha/api2/demo'  

    
    webbrowser.open_new_tab(url)  

    time.sleep(2)
    
    # py.moveTo(x=76,y=600)
    #wind mouse movement
    x_init,y_init = py.position()
    # xf,yf = 70,600

    points = []
    ret = wind_mouse(x_init,y_init,x_target,y_target,G_0=12, W_0=3, M_0=80, D_0=50,move_mouse=lambda x,y: points.append([x,y]))
    for coord in points:
        py.moveTo(coord)
    
    time.sleep(0.1)

    py.click()
    time.sleep(2)

    py.hotkey('ctrl', 'w')
    time.sleep(0.1)

# for i in range(5):
#     mouse_move(70,600)
