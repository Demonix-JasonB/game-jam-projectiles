# Setup the game
info.set_score(0)
info.set_life(3)
tiles.set_tilemap(tilemap("""level_0"""))
# Setup player
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
    """),
    0)
controller.move_sprite(Spaceship)
projectile = sprites.create_projectile_from_sprite(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . 2 . . . . . . . .
    . . . . . . . 2 . . . . . . . .
    . . . . . . . 2 . . . . . . . .
    . . . . . . . 2 . . . . . . . .
    . . . . . . . 2 . . . . . . . .
    . . . . . . . 2 . . . . . . . .
    . . . . . . . 2 . . . . . . . .
    . . . . . . . 2 . . . . . . . .
    . . . . . . . 2 . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
"""), Spaceship, 50, 50)
my_sprite.set_flag(SpriteFlag.StayInScreen, True)





