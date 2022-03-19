import turtle



win=turtle.Screen() #to create a new window screen
win.title("Pong by Khilan") #to give title to the new window screen
win.bgcolor("black") #to give background colour to the game
win.setup(width=800,height=600) #to change the size of the windows
win.tracer(0) #will stop automatic updates and speed up the games

#Score
score_a=0
score_b=0


#Paddle A
paddle_a=turtle.Turtle() #Creating turtle class
paddle_a.speed(0) #speed of animation
paddle_a.shape("square") #to shape paddle 
paddle_a.color("white") #to color paddle
paddle_a.shapesize(stretch_len=1,stretch_wid=5) #turtle default is 20x20 pixles we will streach it to 100x20 pixels
paddle_a.penup() #please research about this
paddle_a.goto(-350,0) #to start paddle A at the given location



#Paddle B
paddle_b=turtle.Turtle() #Creating turtle class
paddle_b.speed(0) #speed of animation
paddle_b.shape("square") #to shape paddle 
paddle_b.color("white") #to color paddle
paddle_b.shapesize(stretch_len=1,stretch_wid=5) #turtle default is 20x20 pixles we will streach it to 100x20 pixels
paddle_b.penup() #please research about this
paddle_b.goto(350,0) #to start paddle B at the given location


#Ball
ball=turtle.Turtle() #Creating turtle class
ball.speed(0) #speed of animation
ball.shape("circle") #to shape ball
ball.color("white") #to color ball
ball.shapesize(stretch_len=1,stretch_wid=1) #turtle default is 20x20 pixles we will streach it to 20x20 pixels
ball.penup() #please research about this
ball.goto(0,0) #to start ball at the given location
ball.dx = 0.5 #record ball movement on delta which is x axis of x is positive it will move on right 2 spaces
ball.dy = -0.5 #record ball movement on delta which is y axis if y is positive it will move on north east 2 spaces

#Pen
pen = turtle.Turtle() #creeating a class for pen for score tracker
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()#coz we do not need to see the turtle
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Times new roman", 24, "normal"))




#Functions to move the paddle 

def paddle_a_up():
    y=paddle_a.ycor() #get the y axis coordinate of the paddle
    y+=20  #add in order for paddle to go up
    paddle_a.sety(y) #set the paddle a to the new value y

def paddle_a_down():
    y=paddle_a.ycor() #get the y axis coordinate of the paddle
    y-=20  #add in order for paddle to go down
    paddle_a.sety(y) #set the paddle a to the new value y

def paddle_b_up():
    y=paddle_b.ycor() #get the y axis coordinate of the paddle
    y+=20  #add in order for paddle to go up
    paddle_b.sety(y) #set the paddle b to the new value y

def paddle_b_down():
    y=paddle_b.ycor() #get the y axis coordinate of the paddle
    y-=20  #add in order for paddle to go down
    paddle_b.sety(y) #set the paddle b to the new value y




#keyboard binding
win.listen() #to listen for keyboard inputs
win.onkeypress(paddle_a_up,"w") #if the user presses w it will call the function for paddle a up which will make the paddle move up
win.onkeypress(paddle_a_down,"s") #if the user presses s it will call the function for paddle a down which will make the paddle move down
win.onkeypress(paddle_b_up,"Up") #if the user presses up arrow it will call the function for paddle b up which will make the paddle move up
win.onkeypress(paddle_b_down,"Down") #if the user presses down arrow it will call the function for paddle b down which will make the paddle move down







#Loop for the Main game
while True:
    win.update() #it updates the screen everytime the loop runs

    # Move the ball
    ball.setx(ball.xcor()+ball.dx) #current coordinates for ball plus ball dx
    ball.sety(ball.ycor()+ball.dy) #current coordinates for ball plus ball dx

    #Border Checking
    if ball.ycor() > 290:# since height of the window is 600 (300 above and 300 below from middle and ball is 20X20 hence 300-10(half ball)=290)
        ball.sety(290) #we will set it back to 290
        ball.dy *= -1 # it will reverses the direction
    
    if ball.ycor() < -290:# since height of the window is 600 (300 above and 300 below from middle and ball is 20X20 hence 300-10(half ball)=290)
        ball.sety(-290) #we will set it back to 290
        ball.dy *= -1 # it will reverses the direction
    
    if ball.xcor() > 390:# since width of the window is 800 (400 right and left from middle and ball is 20X20 hence 400-10(half ball)=390)
        ball.goto(0,0) #we will set it back to centre as pong game if cannot hit go to centre
        ball.dx *= -1 # it will reverses the direction
        score_a+=1 #player a gets a score
        pen.clear() #to clear scores and add new
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Times new roman", 24, "normal"))
    
    if ball.xcor() < -390:# since width of the window is 800 (400 right and left from middle and ball is 20X20 hence 400-10(half ball)=390)
        ball.goto(0,0) #we will set it back to centre as pong game if cannot hit go to centre
        ball.dx *= -1 # it will reverses the direction
        score_b+=1 #player b gets the score
        pen.clear() # to clear scores and add new
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Times new roman", 24, "normal"))
 
    #Paddle and ball collisions
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor()-40): #to make sure ball's coordinated lands with the coordinated for paddle
        ball.setx(340) #set the ball to middle
        ball.dx*=-1
    
    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()+40 and ball.ycor()>paddle_a.ycor()-40): #to make sure ball's coordinated lands with the coordinated for paddle
        ball.setx(-340) #set the ball to middle
        ball.dx*=-1








