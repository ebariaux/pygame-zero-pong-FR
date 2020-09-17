WIDTH = 800
HEIGHT = 600

balle = Actor('ball.png')
balle.center = 400, 300

raquette_droite = Rect(WIDTH - 20, 10, 10, 80)
raquette_gauche = Rect(10, 10, 10, 80)

vitesse_x = 10
vitesse_y = 10

score_droite = 0
score_gauche = 0

def draw():
    screen.clear()
    balle.draw()
    screen.draw.filled_rect(raquette_droite, (0, 0, 255))
    screen.draw.filled_rect(raquette_gauche, (0, 0, 255))

    screen.draw.text(str(score_gauche), (10, 10))
    screen.draw.text(str(score_droite), (WIDTH - 40, 10))

def update():
    global vitesse_x, vitesse_y
    global score_droite, score_gauche

    balle.left = balle.left + vitesse_x
    balle.top = balle.top + vitesse_y

    if balle.right > WIDTH:
        score_gauche += 1
        balle.center = 400, 300
    if balle.left < 0:
        score_droite += 1
        balle.center = 400, 300

    if balle.bottom > HEIGHT or balle.top < 0:
        vitesse_y = -vitesse_y

    if keyboard.down and raquette_droite.bottom < HEIGHT:
        raquette_droite.top += 10
    if keyboard.up and raquette_droite.top > 0:
        raquette_droite.top -= 10
    if keyboard.w and raquette_gauche.bottom < HEIGHT:
        raquette_gauche.top += 10
    if keyboard.a and raquette_gauche.top > 0:
        raquette_gauche.top -= 10

    if balle.colliderect(raquette_droite) or balle.colliderect(raquette_gauche):
        vitesse_x = -vitesse_x