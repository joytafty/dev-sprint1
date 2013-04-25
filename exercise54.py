#!/usr/bin/env python 

# This is where Exercise 5.4 goes
# Name: Tharathorn (Joy) Rimchala

def is_triangle(l1,l2,l3):
	sides = [float(l1),float(l2),float(l3)];
	sorts = sorted(sides)

	if sorts[2] < sum(sorts[0:2]):
		print 'Yes'
	else:
		print 'No'
 
# Main script
# # Exercise 5.4.1
is_triangle(2,2,3)

# Exercise 5.4.2
trigprompt = "Type in 3 numbers separated by ,\n"
inp = raw_input(trigprompt)
p1 = inp.split(",")
p1 = [float(ii) for ii in p1]
is_triangle(p1[0],p1[1],p1[2])