import turtle

wn = turtle.Screen()
wn.title('Kolačić Klik ~ Karla Vujčić')
wn.bgcolor('pink')

wn.register_shape('Kolačić.gif')

clicks = 0

Kolačić = turtle.Turtle()
Kolačić.up()
Kolačić.shape('Kolačić.gif')


nKlikova = turtle.Turtle()
nKlikova.hideturtle()
nKlikova.up()
nKlikova.goto(0, 250)
nKlikova.color('white')
nKlikova.write(f'Broj klikova: {clicks}', align='center', font=('Book Antiqua', 40, 'normal'))

def klikovi(x,y):
    global clicks
    clicks=clicks + 1
    nKlikova.clear()
    nKlikova.write(f'Broj klikova: {clicks}', align='center', font=('Book Antiqua', 40, 'normal'))

Kolačić.onclick(klikovi)

x=1
while x==1:
    Kolačić.up
    Kolačić.speed(4)
    Kolačić.forward(100)
    Kolačić.right(90)
    Kolačić.forward(100)
    Kolačić.right(90)
    Kolačić.fd(100)
    Kolačić.rt(90)
    Kolačić.fd(100)
    
wn.mainloop()

