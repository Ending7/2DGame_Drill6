from pico2d import *
import random
    
tuk_width, tuk_height = 1280, 1024
open_canvas(tuk_width, tuk_height)
player = load_image('character.png')
hand_arrow = load_image('hand_arrow.png')
tuk_Ground = load_image("TUK_GROUND.png")

index, t = 0 ,0
motion = 0
playerX, playerY = tuk_width  // 2, tuk_height // 2
routeX, routeY = 0, 0
lock = True
running = True

def make_route():
    global routeX, routeY, lock
    routeX = random.randint(100,1100)
    routeY = random.randint(100,1000)
    lock = False

def player_move():
    global playerX, playerY, routeX, routeY, t, lock
               
    playerX = (1-t) * playerX + t * routeX
    playerY = (1-t) * playerY + t * routeY
    t += 0.1
    if playerX == routeX:
        t = 0
        lock = True
    
def player_motion():
    global motion
    if(playerX > routeX):
        motion = 0
    elif(playerX < routeX):
        motion = 1

def player_run():
    global index
    frame = [(27,683-428,40,60), (71, 683-428,41,60), (123,683-428,38,60), 
    (173,683-428,33,60), (213,683-428,46,60), (261,683-428,41,60), 
    (312,683-428,38,60), (358,683-428,32,60)]
   	
    
    draw(frame)

    index += 1
    if(index == 8):
    	index = 0

def draw(frame):
    frameX, frameY, width, height = frame[index]
    if motion == 0:
       player.clip_composite_draw(frameX,frameY,width,height, 0, 'h', playerX, playerY, 100,150)

    if motion == 1:
       player.clip_draw(frameX,frameY, width, height, playerX, playerY,100 , 150)

def handle_events():
    global running
    events = get_events()
    for event in events:
    	if event.type == SDL_QUIT:
    		running = False
    	elif event.type == SDL_KEYDOWN:
    		running = False

while running:
    clear_canvas()
    tuk_Ground.draw(tuk_width//2,tuk_height//2)

    if lock == True:
      make_route()

    hand_arrow.draw(routeX,routeY)
    player_move()
    player_motion()
    player_run()
    update_canvas()

    handle_events()
    delay(0.05)

    if not running: 
   	   break;