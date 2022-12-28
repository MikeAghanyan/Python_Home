# import turtle
# turtle.shape('turtle')
# turtle.shapesize(2)
# turtle.color('green', 'yellow')
# while True:
#     x = int(input('Turtle postition: '))
#     if x != 9999:
#         turtle.begin_fill()
#         turtle.forward(50)
#         turtle.left(x)
#         turtle.color('green', 'red')
#         turtle.speed(3)
#         turtle.end_fill()

#     else:
#         break

# import required modules
# import turtle
# import time
# import random

# delay = 0.1
# score = 0
# high_score = 0


# # Creating a window screen
# wn = turtle.Screen()
# wn.title("Snake Game")
# wn.bgcolor("blue")
# # the width and height can be put as user's choice
# wn.setup(width=600, height=600)
# wn.tracer(0)

 # head of the snake
# head = turtle.Turtle()
# head.shape("square")
# head.color("white")
# head.penup()
# head.goto(0, 0)
# head.direction = "Stop"

 # food in the game
# food = turtle.Turtle()
# colors = random.choice(['red', 'green', 'black'])
# shapes = random.choice(['square', 'triangle', 'circle'])
# food.speed(0)
# food.shape(shapes)
# food.color(colors)
# food.penup()
# food.goto(0, 100)

# pen = turtle.Turtle()
# pen.speed(0)
# pen.shape("square")
# pen.color("white")
# pen.penup()
# pen.hideturtle()
# pen.goto(0, 250)
# pen.write("Score : 0 High Score : 0", align="center",
# 		font=("candara", 24, "bold"))

# # assigning key directions
# def group():
# 	if head.direction != "down":
# 		head.direction = "up"

# def godown():
# 	if head.direction != "up":
# 		head.direction = "down"

# def goleft():
# 	if head.direction != "right":
# 		head.direction = "left"


# def goright():
# 	if head.direction != "left":
# 		head.direction = "right"


# def move():
# 	if head.direction == "up":
# 		y = head.ycor()
# 		head.sety(y+20)
# 	if head.direction == "down":
# 		y = head.ycor()
# 		head.sety(y-20)
# 	if head.direction == "left":
# 		x = head.xcor()
# 		head.setx(x-20)
# 	if head.direction == "right":
# 		x = head.xcor()
# 		head.setx(x+20)


# wn.listen()
# wn.onkeypress(group, "w")
# wn.onkeypress(godown, "s")
# wn.onkeypress(goleft, "a")
# wn.onkeypress(goright, "d")

# segments = []


# # Main Gameplay
# while True:
# 	wn.update()
# 	if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
# 		time.sleep(1)
# 		head.goto(0, 0)
# 		head.direction = "Stop"
# 		colors = random.choice(['red', 'blue', 'green'])
# 		shapes = random.choice(['square', 'circle'])
# 		for segment in segments:
# 			segment.goto(1000, 1000)
# 		segments.clear()
# 		score = 0
# 		delay = 0.1
# 		pen.clear()
# 		pen.write("Score : {} High Score : {} ".format(
# 			score, high_score), align="center", font=("candara", 24, "bold"))
# 	if head.distance(food) < 20:
# 		x = random.randint(-270, 270)
# 		y = random.randint(-270, 270)
# 		food.goto(x, y)

# 		# Adding segment
# 		new_segment = turtle.Turtle()
# 		new_segment.speed(0)
# 		new_segment.shape("square")
# 		new_segment.color("orange") # tail colour
# 		new_segment.penup()
# 		segments.append(new_segment)
# 		delay -= 0.001
# 		score += 10
# 		if score > high_score:
# 			high_score = score
# 		pen.clear()
# 		pen.write("Score : {} High Score : {} ".format(
# 			score, high_score), align="center", font=("candara", 24, "bold"))
# 	# Checking for head collisions with body segments
# 	for index in range(len(segments)-1, 0, -1):
# 		x = segments[index-1].xcor()
# 		y = segments[index-1].ycor()
# 		segments[index].goto(x, y)
# 	if len(segments) > 0:
# 		x = head.xcor()
# 		y = head.ycor()
# 		segments[0].goto(x, y)
# 	move()
# 	for segment in segments:
# 		if segment.distance(head) < 20:
# 			time.sleep(1)
# 			head.goto(0, 0)
# 			head.direction = "stop"
# 			colors = random.choice(['red', 'blue', 'green'])
# 			shapes = random.choice(['square', 'circle'])
# 			for segment in segments:
# 				segment.goto(1000, 1000)
# 			segment.clear()

# 			score = 0
# 			delay = 0.1
# 			pen.clear()
# 			pen.write("Score : {} High Score : {} ".format(
# 				score, high_score), align="center", font=("candara", 24, "bold"))
# 	time.sleep(delay)

# wn.mainloop()


# try:
#     x = y
#     print(x)
# except NameError:
#     print('y')

# try:
#     print(5 + 'a')
# except TypeError:
#     print('5a')

# kassa = 0
# while True:
#     try:
#         x = int(input('Enter number: '))
#         if x > 10:
#             kassa += 10
#         else:kassa += 5
#     except ValueError:
#         print(kassa)
#         break

# def func(a):
#     return a ** 2
# try:
#     print(func(7))
# except TypeError:
#     print('Func in mi tur tar')
# except bla bla bla

# ---------------------------------------------------------------------------------------------------------------------------
'''Calculator''' '''------ kak zdelat' excepr dlya s is int or float? -----'''
def calculator(x:float, s:str, y:float) -> float:
    try:
        if s == '+':
            a = x + y
            return a
        elif s == '-':
            a = x - y
            return a
        elif s == '*':
            a = x * y
            return a
        # elif s == '/':
        #     a = x / y
        #     return a
        elif s == '**':
            a = x ** y
            return a
        try:
            if s =='/':
                a = x / y
                return a
        except ZeroDivisionError:
            return '!!!  [ y != 0 ] ---- !!!'
    except isinstance(s, float):
        return 'Enter a float numbers for x and y !!! Only char needs to be a string symbol!!!'


try:
    print(calculator((float(input('Enter the first number ( x = )---> '))), input('Enter a char ---> '), float(input('Enter the second number ( y = )---> '))))
except ValueError:
    print('Enter a float numbers for x and y !!! Only char needs to be a string symbol!!!')

# ---------------------------------------------------------------------------------------------------------------------------
''' BOOOK ---- 149 '''
# with open('text.txt', 'w') as file:
#     file.write('First\nSecond\nThird\nForth\nFifth\nSixth\nSeventh\nEighth\nNineth\nTenth')
# with open('head.txt', 'w') as file:
#     file.write('First\nSecond\nThird\nForth\nFifth\nSixth\nSeventh\nEighth\nNineth\nTenth')
# def readfile(filename:str) -> str:
#     '''
#     +---------------------------------------------------------------------+
#     |functiayin tveq fayli anuny ete 5 toxic avyla ktpi arachin 10 toxery |
#     +---------------------------------------------------------------------+
#     '''
#     with open(filename, 'r') as file:
#         x = file.readlines()

#         if len(x) < 5:
#             print(f'!!!!! ----- The file has less only {len(x)} lines ----- !!!!')
            
#         for i in x:
#             if len(x) > 5:
#                 i = i.replace('\n', '')
#                 print(i)
            
# def main() -> None:
#     try:
#         readfile(input('Enter a file name ---> '))
#     except FileNotFoundError:
#         print(' ---- No such file :( ---- ')


# if __name__ == '__main__':
#     main()


    