from sense_hat import SenseHat
from time import sleep
senh = SenseHat()
#senh.set_pixel(4,4,255,255,0)
x = 4
y = 4
red = (255,0,0)
blue = (0,0,255)
yellow =(255,255,0)

while True:
	gx = senh.gyro_raw['x']
	gy = senh.gyro_raw['y']
	if gx > 0.2:
		y+=1
	if gx < -0.2:
		y-=1
	if y>7:
		y=7
	if y<0:
		y=0
	if gy > 0.2:
                x-=1
	if gy < -0.2:
                x+=1
	if x>7:
                x=7
	if x<0:
                x=0
	senh.clear()
	senh.set_pixel(x,y,yellow)
	sleep(0.1)
