#!/usr/bin/env python 

# This is where Exercise 5.6 goes
# Name: Tharathorn (Joy) Rimchala

def draw(t,length,n):
	if n == 0:
		return
	angle = 50
	fd(t, length*n)
	lt(t, angle)
	draw(t, length, n-1)
	rt(t, 2*angle)
	draw(t, length, n-1)
	lt(t, angle)
	bk(t, length*n)

def drawKoch(t,n):
	if n < 3:
		fd(t, n)
		return
	angle = 60
	length = n/3.0
	print 'a: calling Koch ' + str(n)
	drawKoch(t,length)
	lt(t,angle)
	print 'b: calling Koch ' + str(n)
	drawKoch(t,length)
	rt(t,2*angle)
	print 'c: calling Koch ' + str(n)
	drawKoch(t,length)
	lt(t,angle)
	print 'd: calling Koch ' + str(n)
	drawKoch(t,length)

world.clear()
bob = Turtle()

drawKoch(bob, 3**(5))
