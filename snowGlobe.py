glCoor = [];

def snowGlobe(color1,y):
    rods()
    base(color1)
    pushMatrix()
    translate(0,y,0)
    for i in range(len(glCoor)):
        glitter(glCoor[i][0],glCoor[i][1],glCoor[i][2])
    popMatrix()
    present()
    glass()

def glass():
    fill (255, 250, 255,50)
    pushMatrix()
    translate (0,0,22)
    scale(1,1,1)
    sphereDetail(60)
    sphere(14)
    popMatrix()

def rods():
    pushMatrix()
    fill(255,215,0)
    translate(0,0,7)
    scale(12,3,3)
    rotateY(radians(90))
    cylinder()
    popMatrix()
    pushMatrix()
    fill(255,215,0)
    translate(0,-.2,7)
    scale(3,12,3)
    rotateX(radians(90))
    cylinder()
    popMatrix()

def base(color1):
    fill (color1)    #pink
    pushMatrix()
    ring(10,10,3,0,0,0)
    ring(1.2,1.2,.25,0,0,2)
    ring(.97,.97,1,0,0,2)
    for i in range(5):
        ring((.99 - (i*.01)),(.99 - (i*.01)),.99,0,0,2)
    ring(1.07,1.07,1,0,0,2)
    popMatrix()

def present():
    pushMatrix()
    scale(.7,.7,.7)
    translate(0,0,5)
    
    fill (0, 255, 0,255)
    pushMatrix()
    rotateZ(20)
    translate (0,0,16)  # move up and down
    scale(.4,.4,.4)
    box(20)
    popMatrix()
    
    pushMatrix()
    fill (255, 0, 0,255)
    rotateZ(20)
    translate (4.5,0,16)  # move up and down
    scale(.05,.1,.4)
    box(20)    
    popMatrix()
    
    pushMatrix()
    fill (255, 0, 0,255)
    rotateZ(20)
    translate (-4.5,0,16)  # move up and down
    scale(.05,.1,.4)
    box(20)    
    popMatrix()
    
    pushMatrix()
    fill (255, 0, 0,255)
    rotateZ(20)
    translate (0,4.5,16)  # move up and down
    scale(.1,.05,.4)
    box(20)    
    popMatrix()
    
    pushMatrix()
    fill (255, 0, 0,255)
    rotateZ(20)
    translate (0,-4.5,16)  # move up and down
    scale(.1,.05,.4)
    box(20)    
    popMatrix()

    pushMatrix()
    fill (255, 0, 0,255)
    rotateZ(20)
    translate (0,0,20)  # move up and down
    scale(.1,.5,.05)
    box(20)    
    popMatrix()
    
    pushMatrix()
    fill (255, 0, 0,255)
    rotateZ(20)
    translate (0,0,20)  # move up and down
    scale(.5,.1,.05)
    box(20)    
    popMatrix()
    
    pushMatrix()
    fill (255, 0, 0,255)
    rotateZ(5)
    translate (0,0,21)  # move up and down
    scale(.1,.1,.05)
    box(20)
    popMatrix()
    
    popMatrix()
    
def glitter(x,y,z): #snow
    fill (0, 0,255, 255) #blue
    pushMatrix()
    scale(.025,.025,.025)
    translate (x, y, z)
    box(20)
    popMatrix()
    
def ring(sx,sy,sz,tx,ty,tz):
    scale (sx, sy, sz)
    translate(tx,ty,tz)
    cylinder()

def cylinder(sides = 64): #source code
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, -1)
    endShape(CLOSE)
    # second endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, 1)
    endShape(CLOSE)
    # sides
    x1 = 1
    y1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta)
        y2 = sin(theta)
        beginShape()
        normal (x1, y1, 0)
        vertex (x1, y1, 1)
        vertex (x1, y1, -1)
        normal (x2, y2, 0)
        vertex (x2, y2, -1)
        vertex (x2, y2, 1)
        endShape(CLOSE)
        x1 = x2
        y1 = y2