from sense_hat import SenseHat
from time import sleep
senh = SenseHat()
#senh.set_pixel(4,4,255,255,0)
x = 4
y = 4
red = (255,0,0)
blue = (0,0,255)
yellow =(255,255,0)
def rys_punkt(event):
    global x
    global y
    if event.action == "pressed":
        if event.direction == "up" and y > 0:
            y -= 1
        elif event.direction == "down" and y < 7:
            y += 1
        elif event.direction == "right" and x < 7:
            x += 1
        elif event.direction == "left" and x > 0:
            x -= 1
    #senh.clear()
    #senh.set_pixel(x,y,yellow)
    
senh.stick.direction_any = rys_punkt
while True:
    senh.clear()
    senh.set_pixel(x,y,yellow)
    sleep(0.1)