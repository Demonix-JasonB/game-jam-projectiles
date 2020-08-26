// Setup the game
info.setScore(0)
info.setLife(3)
scene.setBackgroundImage(img`
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
`)
tiles.setTilemap(tilemap`level`)
// Setup player
let Spaceship = sprites.create(img`
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
`)
