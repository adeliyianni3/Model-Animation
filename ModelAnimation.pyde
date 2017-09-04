# Antonia Deliyianni
    #Snowglobe
    
#Camera Motion: Camera moves 1st right from left, then 
    #away from the snowglobe, and then zooms into the snowglobe.
#Project 2A Object: Snowglobe
#Object Animation: Snowglobe rotates around z, then rotates around x
    #as it is translated on z. Then snowglobe is translated on y and
    #once snowglobe hits floor, the snow is translated on y
#Object Instancing: The books, made up of four boxes, are instanciated
    #and scaled.
#Lighting and Shading: Ambient light and directional light.
#Duration: 301 frames

from room import *
time = 0   # use time to move objects from one frame to the next
time2 = 0
time3 = 0
time4 = 0

time5 = 0

cameraX = 100
cameraZ = 250
cameraY = -50

centerX=0
centerY=0
centerZ=0

snowFall =0

startBool = False
x = 100
z=100
y= -300

def setup():
    size (750,750, P3D)
    perspective (60 * PI / 180, 1, 0.1, 1000)  # 60 degree field of view
    for i in range(40):
        glCoor.append([random(-320,320), random(-340,380), random(500,1200)])
    
def draw():
    global startBool
    global x
    global y
    global z
    global time
    global time2
    global time3
    global time4
    global time5
    global cameraX
    global cameraY
    global cameraZ
    
    global centerX
    global centerY
    global centerZ
    
    global snowFall
    
    camera (cameraX, cameraY, cameraZ, centerX, centerY, centerZ, 0,  1, 0)  # position the virtual camera
    if time5 < 100:
        cameraX-=2
    else:
        if time5 >= 180:
            if time5 == 180:
                cameraY = 180
                centerY = 180
                cameraZ -= 400
                centerZ -= 400
            cameraZ -= .5
            centerZ -= .5
            cameraX -= .2
            snowFall += .05
        else:
            cameraX = 0
            cameraZ +=1.5

    background (255)  # clear screen and set background to white
    
    # create a directional light source
    ambientLight(50, 50, 50);
    lightSpecular(255, 255, 255)
    directionalLight (100, 100, 100, -.3, 0.5, -1)
    
    noStroke()
    specular (180, 180, 180)
    shininess (15.0)
    room()
    
    if time5 > 20:
        ballBounce()
    
    snowGlobeFall()
    time5 += 1
    
    if time4!=0:
        translate(0,-time4,-time3)
    rotateX(radians(90))
    if time!= 0:
        rotateY(-time)
    if time2!=0:
        rotateZ(-time2)
    snowGlobe(color(255, 105, 180, 255), snowFall) #draws snowglobe

def restart():
    global time
    global time2
    global time3
    global time4
    global time5
    global cameraX
    global cameraZ
    global cameraY
    global x
    global y
    global z
    global startBool
    global centerX
    global centerY
    global centerZ
    
    global snowFall
    
    snowFall = 0

    cameraX = 100
    cameraZ = 250
    cameraY = -50
    
    centerX=0
    centerY=0
    centerZ=0
    time = 0   # use time to move objects from one frame to the next
    time2 = 0
    time3 = 0
    time4 = 0
    time5 = 0
    startBool = False
    x = 100
    z=100
    y= -300

def ballBounce():
    global startBool
    global x
    global y
    global z
    if z>0:
        if y <0:
            z-=10
            x-=10
            y-=(y*.2)
            if y >-43:
                startBool = True
    else:
        if z>-50:
            y-=10
            z-=10
        else:
            if y < 180:
                y+=10
                z-=10
            else:
                if y >181:
                    z+=10
        if x > -200:
            x-=5
        else:
            y = 181
    fill (94, 96, 255,255)
    pushMatrix()
    translate (x,y,z)
    scale(2.5,2.5,2.5)
    sphereDetail(60)
    sphere(14)
    popMatrix()

def snowGlobeFall():
    global time
    global time2
    global time3
    global time4
    global time5
    if time5 > 310:
        restart()
    if startBool:
        if time4>-180:
            time3 += radians(90)
        if time < radians(80):
            time += radians(9)
            time4 += .94
        else:
            if time4>-180:
                time2 += radians(2)
            if time3 > 118:
                if time4>-180:
                    time4 -= 5