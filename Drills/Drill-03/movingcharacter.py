from pico2d import *
import os

os.getcwd()
os.chdir('C:\\DAHN-2DGP\\2DGP\Drills\\Drill-03')

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while (True):
    z = 0
    
    if(z == 0):
        
        x = 0
        while (x < 400):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(400 + x, 90)
            x = x + 2
            delay(0.01)
            
        y = 0
        while (y < 500):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(800, 90 + y)
            y = y + 2
            delay(0.01)
            
        x = 0
        while (x < 800):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(800 - x, 590)
            x = x + 2
            delay(0.01)
            
        y = 0
        while (y < 500):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(0, 590 - y)
            y = y + 2
            delay(0.01)
            
        x = 0
        while (x < 400):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(0 + x, 90)
            x = x + 2
            delay(0.01)

        z = z + 1

            
    if(z == 1):
        x = 0
        y = 0
        while(x < 400):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(400 + x, 90 + y)
            x = x + 2
            y = y + (x / 150)
            delay(0.01)

        x = 0
        y = 0
        while(x < 400):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(800 - x, 350 + y)
            x = x + (y / 75)
            y = y + 2
            delay(0.01)

        x = 0
        y = 0
        while(x < 400):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(400 - x, 650 - y)
            x = x + 2
            y = y + (x / 150)
            delay(0.01)

        x = 0
        y = 0
        while(x < 400):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(0 + x, 390 - y)
            x = x + (y / 75)
            y = y = y + 2
            delay(0.01)
            
        z = z - 1
        
    
close_canvas()
