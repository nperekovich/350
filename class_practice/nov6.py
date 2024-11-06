
'''
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html


NOTE:  BACK UP YOUR CODE AS FREQUENTLY AS YOU THINK WISE

NOTE:  BACK UP YOUR CODE AS FREQUENTLY AS YOU THINK WISE

1.  Note the two programs below.

2.  Each of the concepts used below we have discussed
or covered in class other than Turtle.

3.  In this field, you may be asked to "refactor" or rewrite
code and might need to research some of the modules
that were utilized.

4.  For this exercise, look at the programs below.

To Do / Questions:

5a.  Why does one draw a SQUARE and the other a STAR?

5b.  Why does the program APPEAR to never stop running?

5c.  Without breaking the program (hint: backup your code):

  (i)    make the square larger.

  (ii)   make the star larger.

  (iii)  make the star complete sooner.

  (iv)   adding only 2 lines of code, and indenting the rest,
         wrap a "function" around making the star, and call it.

  (v)    show me when you have the above working.

  (vi)   After showing me your functioning code in (iv) above,
         - then change no more than 5 lines in the star function;
         - to pass three arguments (x and y and z); 
         - with values each under 50;
         - to replace all the numbers in the function.


'''


# Python program to draw a SQUARE  
# Importing Turtle Module 

import turtle

t = turtle.Turtle()

for c in ['red', 'green', 'purple', 'blue']:
    t.color(c)
    t.forward(150) #increase size
    t.left(90)

# Python program to draw STAR 
# Importing Turtle Module 

import turtle  

def draw_star(x, y, z):  # Added this line
       star = turtle.Turtle()
       star.speed(1)#speed of turtle drawing star 

       for i in range(x): 
              star.forward(y) #increase size
              star.right(z) 

       turtle.done()

draw_star(5, 100, 144)  # Added this line
