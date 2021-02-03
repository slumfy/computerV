#!/usr/bin/python3
import sys
import math # 3rd degre only

class computer:
	A = 0
	B = 0
	C = 0
	Z = 0
	sign = 1
	DELTA = 0
	degre = 0

	def __init__(self,arg_list):
		for i in arg_list:
			try:
				float(i)
			except:
				if  i.isnumeric() == False and i != 'X^0' and i != 'X^1' and i != 'X^2' and i != 'X^3' and i != 'X' and i != '+'  and i != '-' and i != '*' and i != '=':
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
			if i.find("X^3") != -1:
				self.Z = self.Add(i, self.sign, "X^3")
			elif i.find("X^2") != -1:
				self.A += self.Add(i, self.sign, "X^2")
			elif i.find("X^0") != -1:
						self.C += self.Add(i, self.sign,"X^0")
			elif i.find("X") != -1:
						self.B += self.Add(i, self.sign,"X")
			elif i == "=":
				self.sign = -1
			else:
				self.C += float(i) * self.sign
		self.finding_degre()
		self.solving_equation()

	def solving_equation(self):
		self.print_reduction()
		if self.degre == 3:
			self.solve_3_degre()
		elif self.degre == 2:
			self.solve_2_degre() 
		elif self.degre == 1:
			self.solve_1_degre()
		elif self.degre == 0:
			self.solve_0_degre()

	def print_reduction(self):
		print  ("Z = " + str(self.Z))
		print  ("A = " + str(self.A))
		print  ("B = " + str(self.B))
		print  ("C = " + str(self.C))
		print("degre: ",self.degre)
		print ("Simplified form: ", end="")
		if self.Z != 0:
			print (str(self.Z) + " * X^3 ",end="")
		if self.A != 0:
			print (str(self.A) + " * X^2 ",end="")
		if self.B != 0:
			print (str(self.B) + " * X ",end="")
		print (str(self.C), "= 0")

	def finding_degre(self):
		if self.Z != 0:
			self.degre = 3
		elif self.A != 0:
			self.degre = 2
		elif self.B != 0:
			self.degre = 1
		else:
			self.degre = 0

	def solve_3_degre(self):
		#http://www.1728.org/cubic2.htm
		f = ((3 * self.B/self.Z) - (self.power(self.A,2)/self.power(self.Z,2)))/3
		print("F: ",f)
		g = ((2 * self.power(self.A,3) / self.power(self.Z,3)) - (9 * self.A * self.B / self.power(self.Z,2)) + (27 * self.C/self.Z))/27
		print("G: ",g)
		h = (self.power(g,2) / 4) + (self.power(f,3) / 27)
		print("H: ",h)
		#	When h <= 0, as is the case here, all 3 roots are real
		if h == 0 and f == 0 and g == 0:
			x = self.cube(self.C/self.Z) * -1
			print("solution are:")
			print("X1 = X2 = X3 = ", x, "round = ", round(x))
		elif h <= 0:
			i = self.Sqrt(((self.power(g,2)/4) - h))
			print("I: ",i)
			j = self.cube(i)
			print("J: ",j)
			k = math.acos(-(g / (2 * i)))
			print("K: ",k)
			l = -j
			print("L: ",l)
			m = math.cos(k/3)
			print("M: ",m)
			n = self.Sqrt(3) * math.sin(k/3)
			print("N: ",n)
			p = (self.A / (3 * self.Z)) * -1
			print("P: ",p)
			x1 = 2 * j * m - (self.A /(3 * self.Z))
			x2 = l * (m + n) + p
			x3 = l * (m - n) + p
			print("solution are:")
			print("X1 = ", x1, "round = ", round(x1))
			print("X2 = ", x2, "round = ", round(x2))
			print("X3 = ", x3, "round = ", round(x3))
		elif h > 0:
			r = -(g/2) + self.Sqrt(h)
			print("R: ",r)
			s = self.cube(r)
			print("S: ",s)
			t = -(g/2) - self.Sqrt(h)
			print("T: ",t)
			u =	self.cube(t)
			print("U: ", u)
			x1 = (s + u) - (self.A / (3 * self.Z))
			print("solution are:")
			print("X1 = ", x1, "round = ", round(x1))
			print("X2 = ",(-(s + u)/2 - (self.A / (3 * self.Z))),"+ I * ",(s - u) * self.Sqrt(3)/2)
			print("X3 = ",(-(s + u)/2 - (self.A / (3 * self.Z))),"- I * ",(s - u) * self.Sqrt(3)/2)

	def solve_2_degre(self):
		self.DELTA = self.B**2 - 4*self.A*self.C
		print ("DELTA =" + str(self.DELTA))
		if self.DELTA == 0:
			X = -self.B / 2 * self.A
			print ("This polynomial equation have 1 solution X = " + str(X))
		elif self.DELTA > 0:
			print ("This polynomial equation have 1 solution X1 = " + str(-self.B) + "+ square(" + str(self.DELTA) + ") / " + str(2* self.A) + "  X2= " + str(-self.B) + "- square(" + str(self.DELTA) + ") / " + str(2* self.A))
			X1 = (-self.B + self.Sqrt(self.DELTA)) / 2 * self.A
			X2 = (-self.B - self.Sqrt(self.DELTA)) / 2 * self.A
			print ("X1 = " + str(X1) + " X2 = " + str(X2))
		elif self.DELTA < 0:
			print ("This polynomial equation have 1 solution X1 = " + str(-self.B) + " - i * square(" + str(-self.DELTA) + ") /" + str(2* self.A) + "  X2= " + str(-self.B) + "+ i * square(" + str(-self.DELTA) + ") /" + str(2* self.A))

	def solve_1_degre(self):
		if self.B != 0:
				X = -self.C / self.B  
				print ("This equation have one solution X= " + str(-self.C) + "/" + str(self.B) + "  or X= " + str(X))
		elif self.B == 0.0 and self.C != 0.0:
				sys.exit("This equation is wrong")

	def solve_0_degre(self):
		if self.C == 0.0:
				print ("Every Number are solution")
		else:
				print ("There is no solution and the result is absurd")	

	def Add(self, i, sign, s):
		V = 0
		tmp = i.split('*')
		if tmp[0].find(s) == -1:
			V += float(tmp[0]) * sign
		else:
			V += 1.0 * sign
		return(V)

	def power(self,x, y):
		if(y == 0): return 1
		temp = self.power(x, int(y / 2)) 
		if (y % 2 == 0):
			return temp * temp
		else:
			if(y > 0): return x * temp * temp
			else: return (temp * temp) / x

	def cube(self,x):
		if 0<=x: 
			return x**(1./3.)
		return -(-x)**(1./3.)

	def Sqrt(self, x):
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

	def acos(self, x):
		# return 1.57079-1.57079*x
		return (-0.69813170079773212 * x * x - 0.87266462599716477) * x + 1.5707963267948966


if __name__ == "__main__":
	if   len(sys.argv) < 2 :
		sys.exit("Need an argument")
	arg = str(sys.argv[1])
	arg_list = arg.split()
	print (arg_list)
	computer(arg_list)
