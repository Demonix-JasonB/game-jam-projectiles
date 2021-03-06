//  Setup the game
info.setScore(0)
info.setLife(3)
tiles.setTilemap(tilemap`level_0`)
//  Setup player
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
    `, 0)
controller.moveSprite(Spaceship)
let projectile = sprites.createProjectileFromSprite(img`
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
`, null, 50, 50)
