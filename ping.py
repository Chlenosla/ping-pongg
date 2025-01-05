from pygame import *
win = display.set_mode((700,500))
back = (204, 230, 255)
win.fill(back)
clock = time.Clock()






class Game_sprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y, player_w, player_h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_w, player_h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(Game_sprite):
    def update_l(self):
        keys_presed = key.get_pressed()
        if keys_presed[K_UP] and self.rect.y < 450:
            self.rect.y += self.speed
        if keys_presed[K_DOWN] and self.rect.y > 5:
            self.rect.y -= self.speed
    def update_r(self):
        keys_presed = key.get_pressed()
        if keys_presed[K_w] and self.rect.y < 450:
            self.rect.y += self.speed
        if keys_presed[K_s] and self.rect.y > 5:
            self.rect.y -= self.speed

right_racket = Player("racket.png", 5, 650, 200, 15, 150)
left_racket = Player('racket.png', 5, 50, 200, 15, 150)


finish = False

run = True
while run :
    for e in event.get():
        if e.type == QUIT:
            run = False
    win.fill(back)
    right_racket.update_r()
    right_racket.reset()
    left_racket.update_l()
    left_racket.reset()
    display.update()
    clock.tick(40)