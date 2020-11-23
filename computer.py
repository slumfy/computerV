#!/usr/bin/python3
import sys

def Add(i, X, sign, s):
	tmp = i.split('*')
	for x in tmp:
		if x.find(s) == -1:
			X += float(x) * sign

def Sqrt(x):
	lo = 0.0
	hi = float(x)
	for i in range(1000):
		mid = (lo + hi)/2
		if (mid * mid) == float(x):
			return mid
		elif (mid * mid) > float(x):
			hi = mid
		else:
			lo = mid
	return mid

A = 0
B = 0
C = 0
sign = 1
if   len(sys.argv) < 2 :
	sys.exit("Need an argument")
arg = str(sys.argv[1])
arg_list = arg.split()
print (arg_list)
for i in arg_list:
    try:
        float(i)
    except:
        if  i.isnumeric() == False and i != 'X^0' and i != 'X^1' and i != 'X^2' and i != 'X' and i != '+'  and i != '-' and i != '*' and i != '=':
        	print (i)
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
print (arg_list)
for i in arg_list:
	print (i)
	print (i.split('*'))
	if i.find("X^2") != -1:
		Add(i, A, sign, "X^2")
	elif i.find("X^0") != -1:
				Add(i, C, sign,"X^0")
	elif i.find("X") != -1:
				Add(i, B, sign,"X")
	elif i == "=":
		sign = -1
	else:
		C += float(i) * sign

print  ("A = " + str(A))
print  ("B = " + str(B))
print  ("C = " + str(C))
if A:
	print ("Simplified form: " + str(A) + "X^2 +" + str(B) + "X  + " + str(C) + " = 0")
	DELTA = B**2 - 4*A*C
	print ("DELTA =" + str(DELTA))
	if DELTA == 0:
		X = -B / 2 * A
		print ("This polynomial equation have 1 solution X = " + str(X))
	elif DELTA > 0:
		print ("This polynomial equation have 1 solution X1 = " + str(-B) + "+ square(" + str(DELTA) + ") / " + str(2* A) + "  X2= " + str(-B) + "- square(" + str(DELTA) + ") / " + str(2* A))
		X1 = (-B + Sqrt(DELTA)) / 2 * A
		X2 = (-B - Sqrt(DELTA)) / 2 * A
		print ("X1 = " + str(X1) + " X2 = " + str(X2))
	elif DELTA < 0:
		print ("This polynomial equation have 1 solution X1 = " + str(-B) + " - i * square(" + str(-DELTA) + ") /" + str(2* A) + "  X2= " + str(-B) + "+ i * square(" + str(-DELTA) + ") /" + str(2* A)) 
else:
	if B != 0:
		X = B / -C
		print ("This equation have one solution X= " + str(B) + "/" + str(C) + "  or X= " + str(X))
	elif B == 0 and C != 0:
		sys.exit("This equation is wrong")
	elif C == 0:
		print ("Every Number are solution")
