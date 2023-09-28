from pico2d import *
import random
    
tuk_width, tuk_height = 1280, 1024
open_canvas(tuk_width, tuk_height)
player = load_image('character.png')
hand_arrow = load_image('hand_arrow.png')
tuk_Ground = load_image("TUK_GROUND.png")

index, t = 0 ,0
select = -1
motion, tempmotion = 2, 0
playerX, playerY = tuk_width  // 2, tuk_height // 2
route = list()
running = True

def draw_arrow():
    global route
    for routeX, routeY in route:
        hand_arrow.draw(routeX,routeY)

def player_move():
    global playerX, playerY, route, t, select, index
    if(select >= 0):  

       routeX, routeY = route[0]
       playerX = (1-t) * playerX + t * routeX
       playerY = (1-t) * playerY + t * routeY
       t += 0.05
       if playerX == routeX:
          t = 0
          del route[0]
          select -= 1
          index = 0

def player_motion():
    global motion, tempmotion,  route
    if(select >= 0):  

        routeX, routeY = route[0]
        if(playerX > routeX):
            motion = 0
            tempmotion = motion
        elif(playerX < routeX):
            motion = 1
            tempmotion = motion
 
    elif(select == -1):
        if tempmotion == 0:
             motion = 2
        elif tempmotion == 1:
             motion = 3

def play_animation():
    if motion == 0 or motion == 1:
       player_run()
    else:
       player_idle()

def player_run():
    global index
    frame = [(27,683-428,40,60), (71, 683-428,41,60), (123,683-428,38,60), 
    (173,683-428,33,60), (213,683-428,46,60), (261,683-428,41,60), 
    (312,683-428,38,60), (358,683-428,32,60)]
   	    
    draw(frame)

    index += 1
    if(index == 8):
    	index = 0

def player_idle():
    global index
    frame = frame = [(32, 683-72,39,60), (83, 683-72,39,60),
     (132, 683-72,39,60), (182, 683-72,39,60)]

       
    draw(frame)

    index += 1
    if(index == 4):
        index = 0

def draw(frame):
    frameX, frameY, width, height = frame[index]
    if motion == 0 or motion == 2:
       player.clip_composite_draw(frameX,frameY,width,height, 0, 'h', playerX, playerY, 100,150)

    if motion == 1 or motion == 3:
       player.clip_draw(frameX,frameY, width, height, playerX, playerY, 100 , 150)

def handle_events():
    global running,route,select
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            temp = (event.x, tuk_height -1 - event.y)
            route.append(temp)
            select+=1


while running:

    clear_canvas()
    tuk_Ground.draw(tuk_width//2,tuk_height//2)

    play_animation()
    draw_arrow()
    update_canvas()
    
    handle_events()
    player_move()
    player_motion()  

    delay(0.05)

    if not running: 
   	   break;