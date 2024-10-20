def jump():
    turn_left()
    move()

def flip():
    turn_left()
    turn_left()
    turn_left()
    move()

while at_goal() != True:
    if front_is_clear() and right_is_clear():
        flip()
    elif wall_in_front():
        turn_left()
    else:
        move()

        
       

    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
