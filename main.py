#Case-study #1
#Developers: Kremlin V. (%),
#            Maslyukova P. (%),
#            Novoselov V. (%)
import turtle as t
t.hideturtle()
t.speed(0)  #потом изменить

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

def rectangle (x, y, a, b, c, h):
    '''
    Function, drawing rectangle (if a=b it draws square).
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
    triangle(-299, 150, 160, 226, 'gold',0)
    parall(-260, 194, 62, 80, 225)
    triangle(-388, 152, 170, 240,'deep pink', 45)
    triangle(-385, 395, 170, 240,'lime',315)
    triangle(-259, 197, 55, 78, 'dodger blue', 135)
    rectangle(-297, 238, 160, 58, 'red', 45)
    triangle(-141, 394, 58, 82, 'indigo', 225)

    triangle(360, 220, 58, 80, 'indigo',45)
    triangle(277, 179, 80, 113, 'lime', 0)
    triangle(357, 263, 80, 113, 'dodger blue', 90)
    rectangle(300, 261, 38, 38, 'red', 45)
    triangle(296, 259, 40, 57, 'deep pink', 180)
    triangle(212, 219, 40, 57, 'gold', 0)
    parall(215, 304, 40, 60, 0)

    rectangle(300, 110, 38, 38, 'red', 45)
    triangle(326, 0, 80, 113, 'lime', 90)
    triangle(409, 80, 80, 113, 'dodger blue', 180)
    triangle(330, -3, 58, 80, 'gold', 270)
    parall(285, -85, 40, 60, 90)
    triangle(262, -111, 40, 57, 'indigo', 0)
    triangle(407, -104, 40, 57, 'deep pink', 90)

    triangle(250, -280, 80, 113, 'lime', 0)
    triangle(334, -290, 85, 120, 'dodger blue', 45)
    triangle(333, -125, 41, 58, 'indigo', 270)
    triangle(396, -290, 41, 58, 'deep pink', 135)
    rectangle(369, -259, 38, 45, 'red', 45)
    triangle(396, -290, 41, 58, 'deep pink', 135)
    triangle(316, -294, 58, 80, 'gold', 315)
    parall(271, -294, 40, 60, 0)

    t.done()

main()
