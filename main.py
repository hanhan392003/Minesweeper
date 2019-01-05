import pygame
from tile import Tile
from time_counter import TimeCounter
from random import randint
from easy import Easy
from medium import Medium
from difficult import Difficult
from level import Level

# colors (R,G,B)
blue = (0,0,255)
black= (0,0,0)
gray = (70,70,70)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
rows = 16
cols = 16
mode = "game_on"
loop = True

pygame.init()
pygame.font.init()
screen_size = (21*rows+5,70+21*cols+5)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Minesweeper")
clock = pygame.time.Clock()

# size of the grid
width = 16
height = 16
margin = 5
text = pygame.font.SysFont('Comic Sans MS', 10, True)
lev = "Game on"

num_bombs = 40
time_count = []
grid = []

easy = [Easy()]
medium = [Medium()]
difficult = [Difficult()]
level = [lev]

def ModePressed():
    pass

def delObjects():
    global grid 
    global time_count
    global mode
    global lev
    global p_pressed
    p_pressed = 0
    grid = []
    time_count = []
    mode = "game_on"
    lev = "Game on"

def resetGame():
    global grid 
    global time_count
    global num_bombs
    global cols
    global rows
    time_count = [TimeCounter()]
    grid = [[Tile() for n in range(cols)]for n in range(rows)]
    for row in grid:
        for t in row:
            t.is_active = True
    for n in range(num_bombs):
        while True:
            x = randint(0,cols-1)
            y = randint(0,rows-1)
            if grid[y][x].bomb == False:
                grid[y][x].bomb = True
                break

    draw()
a = (margin + width) * cols  + margin
def draw():
    global loop 
    for e in easy :
        pygame.draw.rect(screen,
                        white,
                        [0,20,
                        width*3, height])

        textsurface1 = text.render(e.content, False, (0,0,0))
        screen.blit(textsurface1,(5,20))
    for m in medium:
        pygame.draw.rect(screen,
                         white,
                        [width*3 + (a-width*3*3)/2.55,20,
                        width*3+10, height])

        textsurface2 = text.render(m.content, False, (0,0,0))
        screen.blit(textsurface2,(width*3+(a-width*9)/2.55+3,20))
    for d in difficult:
        pygame.draw.rect(screen,
                         white,
                        [a-60,20,
                        width*3+10, height])

        textsurface3 = text.render(d.content, False, (0,0,0))
        screen.blit(textsurface3,(a-59,20))
    # if mode == "game_on":
    for t in time_count:
        
        pygame.draw.rect(screen,
                        white,
                        [(a-200)/2,0,
                        200, height])
        textsurface1 = text.render(t.content, False, (0,0,0))
        screen.blit(textsurface1,((a-200)/2+200//4,0))
    
    for l in level:
        
        pygame.draw.rect(screen,
                        white,
                        [(a-150)/2,50,
                        150, height])
        textsurface4 = text.render(lev, False, (0,0,0))
        screen.blit(textsurface4,((a-150)/2+200//4,50))


    y = 0
    for row in grid:
        x = 0
        for tile in row:
            if tile.is_active:
                if tile.false_flagged and tile.flagged:
                    color = blue
                elif tile.flagged == True:
                    color = green
                elif tile.visible:
                    color = white
                elif tile.visible == False:
                    color = gray
                if tile.bomb and tile.visible:
                    color = red
                
                pygame.draw.rect(screen,
                                color,
                                [(margin + width) * x  + margin,
                                (margin + height) * y + margin +70,
                                width,
                                height])

                if tile.label != None:
                    textsurface = text.render(str(tile.label), False, (0,0,0))
                    screen.blit(textsurface,((margin + width) * x  + margin+ width/3,(margin + height) * y + margin +70))
                
                x += 1
        y += 1
    # if mode == "won":
    #     print("you won")

    # if mode == "lose":
    #     print("you lost")
def inbounds(x,y):
    global cols
    global rows
    if x >=0 and x< cols and y >= 0 and y<rows:
        return True
    return False

def num_of_bombs(x,y):
    s = 0
    for (dx, dy) in [(0,1),(0,-1),(1,0),(-1,0),(1,-1),(-1,1),(1,1),(-1,-1)]:
        if inbounds(x+dx, y+dy) == True and grid[y+dy][x+dx].bomb == True:
            s += 1
    return s

def mouse_to_index():
    pos = pygame.mouse.get_pos()
    x = pos[0] // (width + margin)
    y = (pos[1]-70) // (height + margin)
    return(x,y)

def search(x,y):
    if not inbounds(x,y):
        return
    tile = grid[y][x]
    if tile.visible:
        # tile.clicked = tile.clicked
        return
    if tile.bomb:
        tile.visible = True
        return

    if tile.flagged:
        return

    tile.visible = True

    s = num_of_bombs(x,y)
    if s>0:
        grid[y][x].label = s
        return 
    
    for (dx, dy) in [(0,1),(0,-1),(1,0),(-1,0),(1,-1),(-1,1),(1,1),(-1,-1)]:
        search(x+dx,y+dy)

def checkAround(x,y):
    tile = grid[y][x]
    for (dx, dy) in [(0,1),(0,-1),(1,0),(-1,0),(1,-1),(-1,1),(1,1),(-1,-1)]:
        if inbounds(x+dx, y+dy) == True:
            if grid[y+dy][x+dx].flagged:
                tile.flaggeds += 1

    for (dx, dy) in [(0,1),(0,-1),(1,0),(-1,0),(1,-1),(-1,1),(1,1),(-1,-1)]:
        if inbounds(x+dx, y+dy) == True:
            if grid[y+dy][x+dx].visible :
                tile.visible_tiles_around +=  1

def openAround(x,y):
    tile = grid[y][x]
    if tile.flagged == False and tile.bomb == False and tile.visible and tile.clicked >1:
        flaggeds = 0
        s = num_of_bombs(x,y)
        for (dx, dy) in [(0,1),(0,-1),(1,0),(-1,0),(1,-1),(-1,1),(1,1),(-1,-1)]:
            if inbounds(x+dx, y+dy) == True:
                if grid[y+dy][x+dx].flagged:
                    flaggeds += 1
        if flaggeds == s:
            for (dx, dy) in [(0,1),(0,-1),(1,0),(-1,0),(1,-1),(-1,1),(1,1),(-1,-1)]:
                if inbounds(x+dx,y+dy) == True:
                    if grid[y+dy][x+dx].flagged == False:
                        search(x+dx,y+dy)
        

def mousePressed():

    (x, y) = mouse_to_index()
    if inbounds(x,y):
        tile = grid[y][x]
        if tile.can_be_clicked :
            tile.clicked += 1
            for time in time_count:
                if tile.clicked == 1 and tile.visible == False and tile.flagged == False and not tile.bomb:
                    time.label += 2*1000
            
            for time in time_count:
                if tile.visible == True and not tile.flagged and not tile.bomb:
                    flaggeds = 0
                    visible_tiles_around = 0
                    tile_around = 0
                    for (dx, dy) in [(0,1),(0,-1),(1,0),(-1,0),(1,-1),(-1,1),(1,1),(-1,-1)]:
                        if inbounds(x+dx,y+dy) == True:
                            tile_around += 1
                    for (dx, dy) in [(0,1),(0,-1),(1,0),(-1,0),(1,-1),(-1,1),(1,1),(-1,-1)]:
                        if inbounds(x+dx,y+dy) == True:
                            if grid[y+dy][x+dx].flagged:
                                flaggeds += 1

                    for (dx, dy) in [(0,1),(0,-1),(1,0),(-1,0),(1,-1),(-1,1),(1,1),(-1,-1)]:
                        if inbounds(x+dx,y+dy) == True:
                            if grid[y+dy][x+dx].visible:
                                visible_tiles_around += 1
                    s = num_of_bombs(x,y)
                    
                    if flaggeds + visible_tiles_around <tile_around and s == flaggeds:
                        time.label += 2000
                        tile.clicked += 1

            if tile.flagged == False :
                search(x,y)
                openAround(x,y)

def keyPressed():
    global mode
    (x,y) = mouse_to_index()
    if inbounds(x,y):
        tile = grid[y][x]
        if tile.can_be_clicked:
            tile.pressed += 1
            if tile.visible == False:
                tile.flagged = True

            if tile.flagged and tile.pressed % 2 == 0:
                tile.flagged = False

        
def checkIfWon():
    global mode
    game_won = False
    bomb = 0
    not_bombs = 0
    visibles = 0
    for row in grid:
        for t in row:
            if not t.bomb:
                not_bombs += 1
    for row in grid:
        for t in row:
            if t.visible and not t.flagged :
                visibles += 1
    for row in grid:
        for t in row:
            if t.bomb and t.visible:
                game_won = False
            else:
                if visibles == not_bombs:
                    game_won = True

    

    if game_won:
        mode = "won"
def checkIfLost():
    global mode
    game_lost = False
    for row in grid:
        for t in row:
            if t.bomb and t.visible:
                game_lost = True
                break 
    if game_lost:
        mode = "lose"

def keyEPressed():
    global cols
    global rows
    global num_bombs
    global screen_size
    global a
    global mode
    delObjects()

    for e in easy:
        cols = e.cols
        rows = e.rows
        num_bombs = e.num_bombs
        a = 21 * e.cols +5
        screen_size = (21*e.rows+5,70+21*e.cols+5)
        screen = pygame.display.set_mode(screen_size)

    
    
    resetGame()
    for t in time_count:
        t.label = 20000

def keyMPressed():
    global a
    global cols
    global rows
    global num_bombs
    global mode

    delObjects()
    for m in medium:
        cols = m.cols
        rows = m.rows
        num_bombs = m.num_bombs
        a = 21* m.cols  + 5 
        screen_size = (21*m.rows+5,70+21*m.cols+5)
        screen = pygame.display.set_mode(screen_size)
    
     

    resetGame()
    for t in time_count:
        t.label =40000

def keyDPressed():
    global cols
    global rows
    global num_bombs
    global a
    global mode

    delObjects()
    for d in difficult:
        cols = d.cols
        rows = d.rows
        num_bombs = d.num_bombs 
        screen_size = (21*d.rows+5,70+21*d.cols+5)
        screen = pygame.display.set_mode(screen_size)
        a = 21 * d.cols  + 5 
     

    resetGame()
    for t in time_count:
        t.label =80000
p_pressed = 0
def PPressed():
    global p_pressed
    global mode
    p_pressed += 1
    if p_pressed %2 == 1:
        mode = "paused"
        for t in time_count:
            t.stop()
        for row in grid:
            for tile in row:
                tile.can_be_clicked = False
    if p_pressed %2 == 0:
        for row in grid:
            for tile in row:
                tile.can_be_clicked = True
        mode = "game_on"

resetGame()
while loop:
    # 1. Event processing
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousePressed()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                keyEPressed()
            elif event.key == pygame.K_m:
                keyMPressed()
            elif event.key == pygame.K_d:
                keyDPressed()
            elif event.key == pygame.K_SPACE:
                keyPressed()
            elif event.key == pygame.K_p:
                PPressed()
        
    # Set the screen background
    screen.fill(black)
    draw()
    checkIfLost()
    checkIfWon()
    for t in time_count:
        if mode == "game_on":
            if t.label//1000 >0:
            
                t.update()
            else:
                t.stop()
                for row in grid:
                    for t in row:
                        t.can_be_clicked = False
                lev = "You lost"
                
            
        else:
            t.stop()
         

    if mode == "won":
        lev = "You won"
        for row in grid:
            for t in row:
                t.can_be_clicked = False
                if not t.bomb and not t.visible:
                    t.visible = True
                if t.bomb:
                    t.flagged = True


    if mode == "lose":
        lev = "You lost"
        for row in grid:
            for t in row:
                t.can_be_clicked = False
                if t.bomb and not t.flagged:
                    t.visible = True
                if t.flagged and not t.bomb:
                    t.false_flagged = True
   
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
pygame.quit()