import random
import math
import Draw

Draw.setCanvasSize(1000, 750)

#Pump class draws the pump object according to orientation
#includes accessor and mutator methods for the orientation
class Pump(object):
    def __init__(self, position):
        self.__position = position
    def __str__(self):
        return self.__position
    def getPumpOrientation(self):
        return self.__position
    def pumpSwitch(self):
        if self.__position == "up":
            self.__position = "down"
        elif self.__position== "down":
            self.__position = "up"
    def pumpDraw(self):
        if self.__position == "up":
            green = Draw.color(200, 250 ,200)
            Draw.setColor(green)
            Draw.filledRect(460,320, 110, 110)        
            green = Draw.color(100, 250 ,100)
            Draw.setColor(green)           
            Draw.filledRect(435, 320, 40, 155)
            Draw.filledRect(545, 320, 40 , 155)
            Draw.filledRect(435, 428, 150, 50)
        elif self.__position == "down":
            green = Draw.color(200, 250 ,200)
            Draw.setColor(green)
            Draw.filledRect(460,340, 110, 130)             
            green = Draw.color(100, 250 ,100)
            Draw.setColor(green) 
            Draw.filledRect(435, 320, 40, 155)
            Draw.filledRect(545, 320, 40 , 155)
            Draw.filledRect(435, 320, 150, 50)
            
#ATP class draws the ATP object(s) 
#has a number which determines if it is a full ATP molecule or just a phosphate
#if the number is above 9- it is just a phosphate group
#below it-the whole ATP is visible
class ATP(object):
    def __init__(self, number):
        self.__number = number
    def __str__(self):
        return self.__number
    def getNumber(self):
        return self.__number
    def ATPDraw(self):
        Purple = Draw.color(200, 0 ,200)
        Draw.setColor(Purple)
        Draw.filledOval(490, 475,25,25)
        Draw.filledOval(504, 500, 25, 25)
        Draw.filledOval(510, 525, 25, 25)
        Draw.filledOval(517, 550, 35, 35)
        Draw.setColor(Draw.WHITE)
        Draw.setFontSize(13)
        Draw.string("ATP", 520, 555)
        
    #this function increments the number-counter each time it is called
    #according to it's count- it draws the entire ATP or just the phosphate group
    def count(self):
        self.__number += 1
        if self.__number > 0 and self.__number < 10:
            self.ATPDraw() 
        elif self.__number >= 10 and self.__number < 100:
            Purple = Draw.color(200, 0 ,200)
            Draw.setColor(Purple)            
            Draw.filledOval(480, 480, 25, 25)
            
    def ATPSet(self, other): 
        self.__number = other
        
#This is the particle class which creates objects called particles 
#with static methods that keep track of the square and circle particles that are in the pump.
#Its methods include accessor methods to allow for implentation of later code,
#mutator methods that allow for the objects to change sides in the implementation code, 
#static accessor methods and static methods that increment or decrement the static attributes, 
#a draw method, and a move method
class Particle(object):
    __circleParticlesInPump=0
    __squareParticlesInPump=0
  
  #a particle is initialized with the dimensions of the space is can move around in, 
  #its shape, its in-the-pump status, and which part of the visualization it is in (top or bottom/inside or outside)  
    def __init__(self, rectX, rectY, rectW, rectH, shape, inPump, orientation, string):
        self.__orientation = orientation
        if self.__orientation == "top":
            self.__rectX = 0
            self.__rectY =0
            self.__rectW = 1000
            self.__rectH = 305
        elif self.__orientation == "bottom":
            self.__rectX = 0
            self.__rectY = 480
            self.__rectW = 1000
            self.__rectH = 220
        self.__x = random.random()*(780)
        self.__y = random.random()*(rectH-30)+rectY
        angle = random.random()*(3*math.pi)       
        self.__dx = math.cos(angle)*3
        self.__dy = math.sin(angle)*3
        self.__shape = shape
        self.__inPump = False
        self.__string = string
    def getX(self): return self.__x
    def getY(self): return self.__y
    def getDX(self): return self.__dx
    def getDY(self): return self.__dy
    def getOrientation(self): return self.__orientation
    def getInPump(self): return self.__inPump
    def getShape(self): return self.__shape
    def getRectH(self):  return self.__rectH
    def getRectY(self):  return self.__rectY
    def angle(self):
        angle = random.random()*(10*math.pi)
        self.__dx = math.cos(angle)*3
        self.__dy = math.sin(angle)*3
    def setX(self, X):
        self.__x = X
    def setY(self, Y):
        self.__y = Y
    def setInPump(self, boolean):
        self.__inPump = boolean
    def setOrientation(self, other):
        self.__orientation = other
    def setRectX(self, other):
        self.__rectX = other
    def setRectY(self, other):
        self.__rectY = other
    def setRectW(self, other):
        self.__rectW = other
    def setRectH(self, other):
        self.__rectH = other
    def newY(self):
        return(self.__rectH - 30)+self.__rectY
                
    @staticmethod           
    def squarePumpFull():
        return Particle.__squareParticlesInPump
    @staticmethod
    def circlePumpFull():
        return Particle.__circleParticlesInPump
    @staticmethod
    def incrementSquaresInPump():
        Particle.__squareParticlesInPump+=1
    @staticmethod
    def incrementCirclesInPump():
        Particle.__circleParticlesInPump+=1
    @staticmethod
    def decrementSquaresInPump():
        Particle.__squareParticlesInPump-=1
    @staticmethod
    def decrementCirclesInPump():
        Particle.__circleParticlesInPump -=1
        
    def __str__(self):
        return "(" + str(self.__x)+"," + str(self.__y)+ ")"
  
 # the move method combines the previous random x with its dx(positive or negative- a product of a trig function) 
 #to constantly update the particle's location
 #if the particle hits the edge of its side or the top of its pump/membrane, 
 #it bounces off in the other direction
    def move(self):
        if not self.__inPump:            self.__x = self.__dx + self.__x            self.__y = self.__dy + self.__y            
            if self.__x < self.__rectX:
                self.__x = self.__rectX
                self.__dx = -self.__dx
            elif self.__x+ 30  > self.__rectX + self.__rectW:
                self.__x = self.__rectX + self.__rectW-30
                self.__dx = -self.__dx
                
            if self.__y < self.__rectY:
                self.__y = self.__rectY
                self.__dy = -self.__dy
            elif self.__y> self.__rectY + self.__rectH and(self.__x <435 or self.__x> 585):
                self.__y = self.__rectY + self.__rectH
                self.__dy = -self.__dy
            elif self.__y> self.__rectY + (self.__rectH-20) and (self.__x >= 435 or self.__x<= 585):
                self.__y = self.__rectY + (self.__rectH-20)
                self.__dy = -self.__dy                
    def drawParticle(self):
        if self.__shape == "square":
            Draw.color(145,75, 0)
            Draw.setColor(Draw.ORANGE)
            Draw.filledRect(self.__x, self.__y, 30, 30)
            Draw.setColor(Draw.WHITE)
            Draw.setFontSize(10)
            Draw.string(self.__string, self.__x+2, self.__y)
        elif self.__shape == "circle":
            Draw.setColor(Draw.RED)
            Draw.filledOval(self.__x,self.__y, 30, 30)
            Draw.setColor(Draw.WHITE)
            Draw.setFontSize(10)
            Draw.string(self.__string, self.__x+5, self.__y+3)           
 
 #this draws the cell membrane and background that are on every instant of the animation           
def drawBackground(): 
    Draw.setBackground(Draw.LIGHT_GRAY)
    Draw.setFontSize(50)
    Draw.setColor(Draw.GRAY)
    Draw.string("INNER CELL", 300, 150)    
    Draw.setColor(Draw.WHITE)
    Draw.filledRect(0, 345, 1000, 125)
    for i in range(2, 425, 30):
        lightblue = Draw.color(70, 200, 225)
        Draw.setColor(Draw.BLUE)
        Draw.filledOval(i, 335, 30, 30)
        Draw.setColor(lightblue)
        Draw.filledOval(i+9, 365, 5, 40)
        Draw.filledOval(i+13, 365, 5, 40)
        Draw.setColor(Draw.BLUE)
        Draw.filledOval(i, 450, 30, 30) 
        Draw.setColor(lightblue)
        Draw.filledOval(i+9, 410, 5, 40)
        Draw.filledOval(i+13, 410, 5, 40)
    for i in range(998, 575, -30):
        Draw.setColor(Draw.BLUE)
        Draw.filledOval(i, 335, 30, 30)
        Draw.setColor(lightblue)
        Draw.filledOval(i+9, 365, 5, 40)
        Draw.filledOval(i+13, 365, 5, 40)
        Draw.setColor(Draw.BLUE)
        Draw.filledOval(i, 450, 30, 30)  
        Draw.setColor(lightblue)
        Draw.filledOval(i+9, 410, 5, 40)
        Draw.filledOval(i+13, 410, 5, 40) 
        
# this function uses attributes and methods of the different interacting objects 
#to allow the particles to enter the pump if the necessary preconditions are present
#if the y and x attributes of each particle in the list of particles are near the pump, 
#and it is the right shape for the right side (square on top, circle on bottom), and the pump isnt full yet, 
#then the static method that increments the count for that shape in the pump is called, 
#and the particle's "move" function is temporarily suspended 
#and the particle remains in the pump until further action
def particleInPump(squares, circles, pump, atp):
    for sq in range(len(squares)):
        if squares[sq].getY()+30>= 315 and  pump.getPumpOrientation()=="up"and  squares[sq].getX()>= 455 and squares[sq].getX()<= 555 and \
           squares[sq].squarePumpFull()<3  and squares[sq].circlePumpFull()==0 and squares[sq].getInPump()==False and squares[sq].getRectY()==0:
            squares[sq].incrementSquaresInPump()
            squares[sq].setX(460)            
            squares[sq].setInPump(True)
            if squares[sq].squarePumpFull()==3 and squares[sq].circlePumpFull()==0:
                squares[sq].setY(330)
            elif squares[sq].squarePumpFull()==2 and squares[sq].circlePumpFull()==0:
                squares[sq].setY(375)
            elif squares[sq].squarePumpFull()==1 and squares[sq].circlePumpFull()==0:
                squares[sq].setY(420)

    for c in range(len(circles)):
        if pump.getPumpOrientation()=="down" and circles[c].getX()>= 455 and circles[c].getX()<= 555 and circles[c].getY()<= 490 and\
           circles[c].circlePumpFull()<2 and circles[c].squarePumpFull()==0 and circles[c].getInPump()== False and circles[c].getRectY()==480:
            circles[c].setInPump(True)
            circles[c].incrementCirclesInPump()
            circles[c].setX(535)
            if circles[c].circlePumpFull()==1:
                circles[c].setY(410)              
            elif circles[c].circlePumpFull==0:     
                circles[c].setY(365)
                
#the whatsGoingOn() method takes the lists of particle objects, the pump object, and the atp object as parameters
#if the pump is facing upwards, this function calls the method that updates the ATP count 
#and when it reaches 100, it switches the orientation of the pump and frees the particle objects in pump to the alternate side
#after the loop is completed and all the particles are release, 
#using a mutator method from the ATP the ATP is changed back to zero to allow the count to continue from the beginning next time 
#if the pump is facing downwards and is full, it allows it to switch sides and release the particles     
def whatsGoingOn(squares, circles, pump, atp):
    if squares[0].squarePumpFull()==3 and squares[0].circlePumpFull()==0 and pump.getPumpOrientation()== "up":
        if atp.getNumber()>=0 and atp.getNumber()<100:            atp.count()
        elif atp.getNumber()==100:           
            pump.pumpSwitch()
            for s in squares:
                if s.getInPump() == True and s.getRectY()==0:
                    s.setInPump(False)
                    s.setRectX(0)
                    s.setRectY(480)
                    s.setRectW(800)
                    s.setRectH(220)
                    s.decrementSquaresInPump()
            atp.ATPSet(0)
    elif circles[0].circlePumpFull()==2 and circles[0].squarePumpFull()==0 and  pump.getPumpOrientation()=="down":
        pump.pumpSwitch()
        for c in circles:
            if c.getRectY()==480 and c.getInPump()==True:
                c.setInPump(False)
                c.setRectX(0)
                c.setRectY(0)
                c.setRectW(800)
                c.setRectH(305)
                c.decrementCirclesInPump()   
            
        
def main():    p = []
    q = []
    Draw.show()
    for i in range(30):
        p += [Particle(0,0,800,305, "square",False, "top", "K+")]
    for i in range(20):
        q += [Particle(0,480, 800, 320, "circle", False, "bottom", "Na+")]
    k = Pump("up")
    a = ATP(0)
    while True:
        Draw.clear()
        drawBackground()  
        particleInPump(p,q,k,a)
        whatsGoingOn(p,q,k,a)
        k.pumpDraw()
        for j in p:
            j.move()
            j.drawParticle()
            
        for i in q:
            i.move()
            i.drawParticle()
        
        Draw.show()      
main()