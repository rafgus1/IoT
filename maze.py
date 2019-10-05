from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

r = (255,0,0)
b = (0,0,0)
w = (255,255,255)
g = (0,255,0)

x=1
y=1

maze = [[r,r,r,r,r,r,r,r],
        [r,b,b,b,b,b,b,r],
        [r,r,r,b,r,b,b,r],
        [r,b,r,b,r,r,r,r],
        [r,b,b,b,b,b,b,r],
        [r,b,r,r,r,r,b,r],
        [r,g,b,r,b,b,b,r],
        [r,r,r,r,r,r,r,r]]

game_over = False

def move_marble(pitch, roll, x, y):
    new_x = x
    new_y = y
    if 1 < pitch < 179:
        new_x -= 1
        if new_x < 0:
            new_x = 0
    elif 359 > pitch > 181:
        new_x += 1
        if new_x > 7:
            new_x = 7
    if 1 < roll < 179 and x>= 0:
        new_y += 1
        if new_y > 7:
            new_y = 7
    elif 359 > roll > 181:
        new_y -= 1
        if new_y < 0:
            new_y = 0
    new_x, new_y = check_wall(x,y,new_x,new_y)
    return new_x, new_y

def check_wall(x,y,new_x,new_y):
    if maze[new_y][new_x] != r:
        return new_x, new_y
    elif maze[new_y][x] != r:
        return x, new_y
    elif maze[y][new_x] != r:
        return new_x, y
    else:
        return x, y
sense.show_message("Level 0")
while game_over == False:
    pitch = sense.get_orientation()['pitch']
    roll = sense.get_orientation()['roll']
    x, y = move_marble(pitch, roll, x, y)
    if maze[y][x] == g:
        sense.show_message("Wygrana")
        game_over = True
    maze[y][x] = w
    sense.set_pixels(sum(maze,[]))
    sleep(0.05)
    maze[y][x] = b
