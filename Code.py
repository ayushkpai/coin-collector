from random import randint

WIDTH = 800
HEIGHT = 800

TITLE = "Coin Collector"

score = 0
game_over = False

fox = Actor("fox")
fox.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200

def draw():
    screen.fill("darkgreen")
    fox.draw()
    coin.draw()

    screen.draw.text(
        "Score: " + str(score),
        topleft=(10, 10),
        color="black"
    )

    if game_over:
        screen.fill("pink")
        screen.draw.text(
            "Final Score: " + str(score),
            center=(WIDTH//2, HEIGHT//2),
            fontsize=60
        )

def update():
    global score

    if game_over:
        return

    if keyboard.left:
        fox.x -= 3
    if keyboard.right:
        fox.x += 3
    if keyboard.up:
        fox.y -= 3
    if keyboard.down:
        fox.y += 3

    coin_collected = fox.colliderect(coin)

    if coin_collected:
        score += 10
        place_coin()

def place_coin():
    coin.x = randint(20, WIDTH - 20)
    coin.y = randint(20, HEIGHT - 20)

def time_up():
    global game_over
    game_over = True

clock.schedule(time_up, 30)
place_coin()
