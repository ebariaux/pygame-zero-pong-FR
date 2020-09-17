WIDTH = 800
HEIGHT = 600

balle = Actor('ball.png')
balle.center = 400, 300

def draw():
    screen.clear()
    balle.draw()

vitesse_x = 10
vitesse_y = 10

def update():
    global vitesse_x, vitesse_y

    balle.left = balle.left + vitesse_x
    balle.top = balle.top + vitesse_y