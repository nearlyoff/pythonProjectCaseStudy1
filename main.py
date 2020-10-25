#Case-study #1
#Developers:   Kremlin V. (60%),
#              Maslyukova P. (30%),
#              Novoselov V. (30%)
import turtle as t
t.hideturtle()

def triangle(x, y, a, c, k, h):
    '''
    Function, drawing triangle, size, colour and heading are optional.
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
    Function, drawing parallelogram, size and heading are optional.
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

def rectangle (x, y, a, b, c, h):
    '''
    Function, drawing rectangle (if a=b it draws square), size, colour and heading are optional.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: first side size
    :param b: second side size
    :param c: colour
    :param h: heading
    :return: None
    '''
    t.up()
    t.setposition (x,y)
    t.setheading(h)
    t.down()
    t.pencolor(c)
    t.fillcolor(c)
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
    rectangle(-250, 340, 38, 38, 'red',0)  #drawing rabbit
    parall(-230, 343, 35, 50, 180)
    triangle(-334, 243, 80, 113, 'dodger blue', 0)
    triangle(-254, 239, 80, 113, 'lime', 180)
    triangle(-330, 159, 58, 82, 'gold', 0)
    triangle(-268, 199, 40, 57, 'indigo', 270)
    triangle(-250, 215, 41, 58, 'deep pink', 45)

    triangle(360, 220, 58, 80, 'indigo',45)  #drawing kite
    triangle(277, 179, 80, 113, 'lime', 0)
    triangle(357, 263, 80, 113, 'dodger blue', 90)
    rectangle(300, 261, 38, 38, 'red', 45)
    triangle(296, 259, 40, 57, 'deep pink', 180)
    triangle(212, 219, 40, 57, 'gold', 0)
    parall(215, 304, 40, 60, 0)

    rectangle(300, 110, 38, 38, 'red', 45)  #drawing figure skater (man)
    triangle(326, 0, 80, 113, 'lime', 90)
    triangle(409, 80, 80, 113, 'dodger blue', 180)
    triangle(330, -3, 58, 80, 'gold', 270)
    parall(285, -85, 40, 60, 90)
    triangle(262, -111, 40, 57, 'indigo', 0)
    triangle(407, -104, 40, 57, 'deep pink', 90)

    triangle(250, -280, 80, 113, 'lime', 0)  #drawing ship
    triangle(334, -290, 85, 120, 'dodger blue', 45)
    triangle(333, -125, 41, 58, 'indigo', 270)
    triangle(396, -290, 41, 58, 'deep pink', 135)
    rectangle(369, -259, 38, 45, 'red', 45)
    triangle(396, -290, 41, 58, 'deep pink', 135)
    triangle(316, -294, 58, 80, 'gold', 315)
    parall(271, -294, 40, 60, 0)

    rectangle(-300, 110, 38, 38, 'red', 45)  #drawing figure skater (woman)
    triangle(-210, 80, 80, 113, 'dodger blue', 180)
    parall(-335, -3, 40, 60, 90)
    triangle(-340, -55, 80, 113, 'lime', 0)
    triangle(-335, -45, 40, 57, 'deep pink', 180)
    triangle(-257, -105, 58, 80, 'indigo', 45)
    triangle(-261, -75, 41, 58, 'gold', 225)

    triangle(-270, -330, 85, 120, 'dodger blue', 45)  #drawing helicopter
    triangle(-273, -210, 85, 120, 'lime', 225)
    parall(-270, -207, 40, 60, 45)
    triangle(-274, -207, 58, 82, 'deep pink', 135)
    triangle(-305, -303, 44, 62, 'indigo', 135)
    triangle(-402, -271, 44, 62, 'gold', 315)
    rectangle(-445, -255, 38, 38, 'red', 45)

    t.done()

main()
