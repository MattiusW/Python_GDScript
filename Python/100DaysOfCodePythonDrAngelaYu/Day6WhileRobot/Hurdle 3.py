def jump():
    turn_left()
    move()

def flip():
    turn_left()
    turn_left()
    turn_left()
    move()

while at_goal() != True:
    if front_is_clear():
        move()
    else:
        jump()
        flip()
        flip()
        turn_left()
       

    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
