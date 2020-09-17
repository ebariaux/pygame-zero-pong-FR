WIDTH = 800
HEIGHT = 600

balle = Actor('ball.png')
balle.center = 400, 300

vitesse_x = 10
vitesse_y = 10

def draw():
    screen.clear()
    balle.draw()

def update():
    global vitesse_x, vitesse_y

    balle.left = balle.left + vitesse_x
    balle.top = balle.top + vitesse_y

    if balle.right > WIDTH or balle.left < 0:
        vitesse_x = -vitesse_x

    if balle.bottom > HEIGHT or balle.top < 0:
        vitesse_y = -vitesse_y