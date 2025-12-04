import turtle




#fu the turtle

fu = turtle.Turtle()
fu.shape('turtle')
fu.color('blue', 'green')
fu.speed(5)



print('pos', fu.pos())
fu.penup()
fu.goto(-200, -100)
fu.color('green')
fu.pendown()
fu.write("WEEEEEEEEEEEEEE!!!!")



fu.fd(300)
fu.lt(600)
fu.fd(600)


#gu the turtle

gu = turtle.Turtle()
gu.shape('turtle')
gu.color('blue')
gu.speed(7)



print('pos', gu.pos())
gu.penup()
gu.goto(-100, -100)
gu.color('blue')
gu.pendown()
gu.write("WEEEEEEEEEEEEEE!!!!")



gu.fd(455)
gu.lt(600)
gu.fd(520)




turtle.mainloop()

