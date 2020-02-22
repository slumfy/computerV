#!/usr/bin/python
import sys
import re

A = 0
B = 0
C = 0
sign = 1
if   len(sys.argv) < 2 :
	sys.exit("Need an argument")
arg = str(sys.argv[1])
arg_list = arg.split()
print arg_list
for i in arg_list:
	if  i.isdigit() == False and i != 'X^0' and i != 'X^1' and i != 'X^2' and i != 'X' and i != '+'  and i != '-' and i != '*' and i != '=':
		print i
		sys.exit("not a valid expression")
if arg_list.count('=') != 1:
	sys.exit("not a valid expression")
lenght = len(arg_list) - 1
i = 0
while i < lenght:
	if arg_list[i+1] != "+" and arg_list[i+1]  != "-" and arg_list[i+1] != "=" and arg_list[i] != "=" :
		arg_list[i] = arg_list[i] + arg_list[i+1]
		arg_list.pop(i + 1)
		lenght -= 1
	else:
		i +=1
print arg_list
for i in arg_list:
	print i
	if i.find("X^2") != -1:
		A += int(i[:-4]) * sign
	elif i.find("X^0") != -1:
		C += int(i[:-4]) * sign
	elif i.find("X") != -1:
		if i.find("X^1") != -1:
			offset = -4
		else:
			offset = -2
			B += int(i[:offset]) * sign
	elif i == "=":
		sign = -1
	else:
		C += int(i) * sign

print  "A = " + str(A)
print  "B = " + str(B)
print  "C = " + str(C)
print "Simplified form: " + str(A) + "X^2 +" + str(B) + "X  + " + str(C) + " = 0"
DELTA = B**2 - 4*A*C
print "DELTA =" + str(DELTA)

