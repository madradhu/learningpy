forward = True
el_pos = 120

def setup():
    size(600, 150)
    
def draw():
    global forward
    global el_pos
    if forward == True and el_pos < 484:
        clear()
        el_pos+= 1
    elif forward == True and el_pos > 483:
        forward = False
    if forward == False and el_pos > 119:
        clear()
        el_pos-= 1
    elif forward == False and el_pos < 120:
        forward = True
            
    rect(50, 50, 55, 55)
    rect(500, 50, 55, 55)
    ellipse(el_pos, 75, 30, 30)