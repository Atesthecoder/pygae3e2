
from pgzero.actor import Actor
from pgzero.keyboard import keys
portal  = Actor("portal", size=(100, 100))
spider_size = (100, 100)
spider = Actor("spider1", size=spider_size)
spider.pos = (400, 300)
mode = "start"
ggr =True
spider1 = Actor("spider1", size=spider_size)
spider_start = (spider.x, spider.y)
masae = Actor("masae", size=(100, 100))
portaal = Actor("portal", size=(100, 100))
atest = Actor("atest", size=(100, 100))
map2 = [[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 7],
        [1, 1, 1, 1, 1, 1, 1, 7],
        [1, 1, 1, 1, 1, 1, 1, 7],
        [1, 1, 1, 1, 1, 1, 1, 7],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 3]]
map = [[0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 1, 1, 1, 1, 1, 0,0,0,0],
       [0, 1, 0, 0, 0, 0, 1, 0,0,0,0],
       [0, 1, 0, 0, 0, 0, 3, 0,0,0,0],
       [0, 1, 0, 0, 0, 0, 3, 0,0,0,0],
       [0, 1, 0, 0, 0, 0, 1, 0,0,0,0],
       [0, 1, 1, 0, 0, 1, 1, 0,0,0,0],
       [0, 0, 0, 0, 0, 0, 0, 0]]
zmne = Actor("zemin_doku", size=(800,600))
eddf = Actor("ejder", size=(100, 100))
WIDTH = 1000
HEIGHT = 600
mode = "start"
ghhh = Actor("ssr")
atestyy = True
def draw():
    global atestyy
    global ggr
    global i,j
    global mode
    if mode == "start":
        ghhh.draw()
        screen.draw.text("click space to start", (100, 100), color=(0, 0, 0), fontsize=50)
    if mode == "level1":
        zmne.draw()
        spider.draw()
        for i in range(8):
            for j in range(8):
                if map[i][j] == 1:
                    masae.pos = (j * 100 + 50, i * 100 + 50)
                    masae.draw()
                if map[i][j] == 3:
                    portal.pos = (j * 100 + 50, i * 100 + 50)
                    portal.draw()
    if mode == "level2":
        WIDTH = 600
        HEIGHT = 700
        screen.clear()
        Actor("stares1").draw()
        
        for o in range(8):
            for t in range(8):
                if map2[o][t] == 7:
                    if atestyy == True:
                        atest.pos = (t * 100 + 50, o * 100 + 50)
                        atestyy = False
                    atest.draw()
                    
        if ggr == True:            
            spider1.pos = (spider_start)
            ggr = False
        spider1.draw()
                    
def update():
    global atestyy
    global mode
    i = int(spider.y // 100)
    j = int(spider.x // 100)
    if mode == "level2":
        atest.x -= 10
    if atest.x < 50:
        atestyy = True
            
        
    if mode == "level1":
        if  spider.colliderect(portal) and map[i][j] == 3:
            mode = "level2"
            
def on_key_down(key):
    global grt2
    global grt
    global mode
    print("on_key_down:", key)#pgzrun yyy.py

    if mode == "start":
        if key == keys.SPACE:
            mode = "playing"
            print("game started!!!")
            mode = "level1"
            
            screen.clear()
    if mode == "level2":
        
        if key == keys.SPACE:
            spider1.y -= 20
            o = int(spider1.y // 100)
            t = int(spider1.x // 100)
            if map2[o][t] == 0 :
                spider1.y += 20
        if key == keys.W:
            spider1.x += 20
        if key == keys.S:
            spider1.y += 20
        if key == keys.A:
            spider1.x -= 20
    if mode == "level1":
        
        i = int(spider.y // 100)
        j = int(spider.x // 100)
        if key == keys.E:
            spider.y -= 50
            if map[i][j] == 1 or spider.colliderect(masae):
                spider.y += 100
        if key == keys.S:
            spider.y += 50
            if map[i][j] == 1 or spider.colliderect(masae):
                spider.y -= 100
        if key == keys.A:
            spider.x -= 50
            if map[i][j] == 1 or spider.colliderect(masae):
                spider.x += 100
        if key == keys.W:
            spider.x += 50
            if map[i][j] == 1 or spider.colliderect(masae):
                spider.y -= 100
        grt = spider.x
        grt2 = spider.y
        
        