# plot-dictionary.py
#import tkinter as tk
import turtle
twin = turtle.Screen()
twin.clear()
t = turtle.Turtle()
def main():
	#table is a dictionary
	table = {-100:0,-90:10,-80:20,-70:30,-60:40,-50:50,
				-40:60,-30:70,-20:75,-10:80,0:85,
					10:80,20:75,30:70,40:60,50:50,
					60:40,70:30,80:20,90:10,100:0
			}

	print(" KEYS ")
	print(table.keys())
	print(" VALUES ")
	print(table.values())
	#turtle graphics
	#tWin = turtle.Screen()
	for h,k in table.items():  #get the items in the dictionary
		print(h, k) # trace code
		#x,y = table[n]
		t.penup()
		t.goto(h,k)
		t.pendown()
		t.circle(5)

main()
def bottom():
	#table is a dictionary
	table1 = {-110:-10,-100:-10,-90:-10,-80:-10,-70:-10,-60:-10,
					-50:-10,-40:-10,-30:-10,-20:-10,10:-10,
						20:-10,30:-10,40:-10,50:-10,60:-10,
						70:-10,80:-10,90:-10,100:-10,110:-10
			}
	print(" KEYS ")
	print(table1.keys())
	print(" VALUES ")
	print(table1.values())
	#turtle graphics
	#tWin = turtle.Screen()
	for h,k in table1.items():  #get the items in the dictionary
		print(h, k) # trace code
		#x,y = table[n]
		t.penup()
		t.goto(h,k)
		t.pendown()
		t.circle(5)
	print(" TRIANGLE HOUSE ""\n""( •_•)""\n"
	"( •_•)>⌐■-■""\n"
	"(⌐■_■)")
bottom()
twin.exitonclick()
"""
This code uses a dictionary with keys ranging from
-100 to 100 incrementing by 10.
Each key has a value of 0 as an integer.
To retrieve the values in the dictionary "table" a for loop is used.
The x cooridate on a python turtle screen corresponds to h while
the y value cooresponds to k.
**************************************
for h,k in table.items():  #get the items in the dictionary
		print(h, k) #trace code
h and k are then ploted using
		t.goto(h,k)
		t.pendown()
		t.circle(5)

Change the values from 0 to another integer.
Try to make something grovey.
"""
