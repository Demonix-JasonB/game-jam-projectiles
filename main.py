#Setup the game
info.set_score(0)
info.set_life(3)
scene.set_background_image(img("""
    f 5 f f f f f f f f f f f f f f
    f f f 5 f f f f f f 5 f f f f f
    f f f f f f f 5 f f f f f 5 f f
    f f 5 f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f f
    f f f f f f f f f f f f 5 f f f
    f f f 5 f f 5 5 f f f f f f f f
    f f f f f f f f f f f f f f f f
    f f f f f f f 5 f 5 f f f f f f
    f f 5 f f f f f f f f f f f f f
    f f f f f f f 5 f f f f f 5 f f
    f f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f f
    f f f f 5 f f f f f f f f f f f
    f f 5 f f f f f 5 f f f f 5 f f
    f f f f f f f 5 f f f f f f f f
"""))
tiles.set_tilemap(tilemap("""level"""))
#Setup player
Spaceship = sprites.create(img("""
    . . . . . . . 2 2 . . . . . . .
    . . . . . . 2 2 2 2 . . . . . .
    . . . . . 2 2 1 1 2 2 . . . . .
    2 . . . 2 2 1 1 1 1 2 2 . . . 2
    2 . . . 2 1 1 1 1 1 1 2 . . . 2
    1 . . . 2 2 1 1 1 1 2 2 . . . 1
    1 . . f 2 2 2 2 2 2 2 2 f . . 1
    1 . . 2 f 2 2 2 2 2 2 f 2 . . 1
    2 . . 2 2 f 2 f f 2 f 2 2 . . 2
    2 . 2 2 2 2 f 2 2 f 2 2 2 2 . 2
    2 2 2 2 2 f 2 f f 2 f 2 2 2 2 2
    2 . 2 2 2 f 2 f f 2 f 2 2 2 . 2
    2 2 2 2 2 2 f 2 2 f 2 2 2 2 2 2
    2 . 1 1 2 f 2 f f 2 f 2 1 1 . 2
    2 . 1 1 1 2 2 2 2 2 2 1 1 1 . 2
    . . . 1 1 1 1 2 2 1 1 1 1 . . .
"""))
#Configure Player Controls

#Generate Enemies

# Shoot Enemies with Projectiles