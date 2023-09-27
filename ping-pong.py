from pygame import *

win_width = 700
win_height = 500
window = display.set_mode(
    (win_width, win_height)
)
display.set_caption('Pingo-pongo')
background = transform.scale(
    image.load('fon.jpg'),
    (win_width, win_height)
)


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 90:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 90:
            self.rect.y += self.speed


clock = time.Clock()
FPS = 60
run = True
finish = False
rac1 = Player('walls.png', 30, 250, 10, 30, 90)
rac2 = Player('walls.png', 650, 250, 10, 30, 90)
ball = GameSprite('basketball.png', 350, 250, 8, 55, 55)
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(background, (0, 0))
    
    rac1.reset()
    rac1.update_l()
    rac2.reset()
    rac2.update_r()
    ball.reset()
    ball.update()
    display.update()
    clock.tick(FPS)
