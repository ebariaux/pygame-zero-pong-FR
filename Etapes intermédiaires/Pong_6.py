WIDTH = 800
HEIGHT = 600

balle = Actor('ball.png')
balle.center = 400, 300

raquette_droite = Rect(WIDTH - 20, 10, 10, 80)

vitesse_x = 10
vitesse_y = 10

def draw():
    screen.clear()
    balle.draw()
    screen.draw.filled_rect(raquette_droite, (0, 0, 255))

def update():
    global vitesse_x, vitesse_y

    balle.left = balle.left + vitesse_x
    balle.top = balle.top + vitesse_y

    if balle.right > WIDTH or balle.left < 0:
        vitesse_x = -vitesse_x

    if balle.bottom > HEIGHT or balle.top < 0:
        vitesse_y = -vitesse_y

    if keyboard.down and raquette_droite.bottom < HEIGHT:
        raquette_droite.top += 10
    if keyboard.up and raquette_droite.top > 0:
        raquette_droite.top -= 10
