#Case-study #1
#Developers: Kremlin V. (%),
#            Maslyukova P. (%),
#            Novoselov V. (%)
import turtle as t
t.hideturtle()
t.speed(1)  #потом изменить

def triangle(x, y, a, c, k, h):
    '''
    Function, drawing triangle, size and colour are optional.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: cathetus size
    :param c: hypotenuse size
    :param k: colour
    :param h: heading
    :return: None
    '''
    t.up()
    t.setposition(x,y)
    t.setheading(h)
    t.down()
    t.pencolor(k)
    t.fillcolor(k)
    t.begin_fill()
    t.forward(a)
    t.left(90)
    t.forward(a)
    t.left(135)
    t.forward(c)
    t.end_fill()

def parall(x, y, a, b, h):
    '''
    Function, drawing parallelogram.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: first side size
    :param b: second side size
    :param h: heading
    :return: None
    '''
    t.up()
    t.setposition(x,y)
    t.setheading(h)
    t.down()
    t.pencolor('green')
    t.fillcolor('green')
    t.begin_fill()
    t.forward(a)
    t.right(45)
    t.forward(b)
    t.right(135)
    t.forward(a)
    t.right(45)
    t.forward(b)
    t.end_fill()

def square (x,y,a,h):
    '''
    Function, drawing square.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side size
    :param h: heading
    :return: None
    '''
    t.up()
    t.setposition(x,y)
    t.setheading(h)
    t.down()
    t.pencolor('red')
    t.fillcolor('red')
    t.begin_fill()
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.end_fill()


def rectangle (x, y, a, b, h):
    '''
    Function, drawing rectangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: first side size
    :param b: second side size
    :param h: heading
    :return: None
    '''
    t.up()
    t.setposition (x,y)
    t.setheading(h)
    t.down()
    t.pencolor('red')
    t.fillcolor('red')
    t.begin_fill()
    t.forward(a)
    t.right(90)
    t.forward(b)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(b)
    t.end_fill()

def main():
    '''
    Main function.
    :return: None
    '''
    triangle(-300, 150, 160, 226, 'dodger blue',0)
    parall(-260, 194, 62, 80, 225)
    triangle(-387, 151, 170, 240,'deep pink', 45)
    triangle(-385, 394, 170, 240,'lime',315)
    triangle(-259, 197, 55, 78, 'indigo', 135)
    rectangle(-297, 238, 160, 58, 45)
    triangle(-141, 393, 57, 80,'gold', 225)

    t.done()

main()
