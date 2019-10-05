from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

white = (255,255,255)
green = (0,255,0)
sense.clear(0,0,0)
bat_y = 4
ball_position = [3, 3]
ball_velocity = [1, 1]
game_over = False

def draw_bat():
    sense.set_pixel(0, bat_y, white)
    sense.set_pixel(0, bat_y + 1, white)
    sense.set_pixel(0, bat_y - 1, white)

def draw_ball():
    sense.set_pixel(ball_position[0], ball_position[1], green)
    ball_position[0] += ball_velocity[0]
    if ball_position[0] == 0 or ball_position[0] == 7:
        ball_velocity[0] = -ball_velocity[0]
    ball_position[1] += ball_velocity[1]
    if ball_position[1] == 0 or ball_position[1] == 7:
        ball_velocity[1] = -ball_velocity[1]
    if ball_position[0] == 1 and (bat_y-1) <= ball_position[1] <= (bat_y + 1):
        ball_velocity[0] = -ball_velocity[0]
    if ball_position[0] == 0:
        sense.show_message("Przegrałeś")
        game_over = True
        
def move_up(event):
    global bat_y
    if event.action == 'pressed' and bat_y > 1:
        bat_y -= 1
    
def move_down(event):
    global bat_y
    if event.action == 'pressed' and bat_y < 6:
        bat_y += 1

while game_over == False:
    sense.stick.direction_up = move_up
    sense.stick.direction_down = move_down
    sense.clear(0,0,0)
    draw_bat()
    draw_ball()
    sleep(0.25)

