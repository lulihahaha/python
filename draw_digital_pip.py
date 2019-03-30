import turtle,time
def drawgap():
    turtle.penup()
    turtle.fd(5)
def drawline(draw):
    drawgap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)
def drawdigit(digit):
    drawline(True) if digit in [2,3,4,5,6,8,9] else drawline (False)
    drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline (False)
    drawline(True) if digit in [0,2,3,5,6,8,9] else drawline (False)
    drawline(True) if digit in [0,2,6,8] else drawline (False)
    turtle.left(90)
    drawline(True) if digit in [0,4,5,6,8,9] else drawline (False)
    drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline (False)
    drawline(True) if digit in [0,1,2,3,4,7,8,9] else drawline (False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawdate(date):
    turtle.pencolor("red")
    
    for i in date:
        if i=='-':
            turtle.write("年,我在想你",font=("Arial",15,"normal"))
            turtle.pencolor("green")
            turtle.fd(150)
        elif i=='=':
            turtle.write("月,你在想谁呢？",font=("Arial",15,"normal"))
            turtle.pencolor("blue")
            turtle.fd(150)
        elif i=='+':
            turtle.write('日',font=("Arial",18,"normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        else:
            drawdigit(eval(i))
   
def main():
    turtle.setup(800,350,400,400)
    turtle.penup()
    turtle.fd(-350)
    turtle.pensize(15)
    drawdate(time.strftime('%Y-%m=%d',time.gmtime()))
    turtle.hideturtle()
    turtle.done()
main()
            
