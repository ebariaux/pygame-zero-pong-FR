WIDTH = 800
HEIGHT = 600

balle = Actor('ball.png')
balle.center = 400, 300

def draw():
    screen.clear()
    balle.draw()