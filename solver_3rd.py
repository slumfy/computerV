import math # 3rd degre only
import utils as utils

class solver_3rd:
	def __init__(self,Z,A,B,C):
		self.Z = Z
		self.A = A
		self.B = B
		self.C = C
		self.solve_3_degre()

	def solve_3_degre(self):
		#http://www.1728.org/cubic2.htm
		f = ((3 * self.B/self.Z) - (utils.power(self.A,2)/utils.power(self.Z,2)))/3
		print("F: ",f)
		g = ((2 * utils.power(self.A,3) / utils.power(self.Z,3)) - (9 * self.A * self.B / utils.power(self.Z,2)) + (27 * self.C/self.Z))/27
		print("G: ",g)
		h = (utils.power(g,2) / 4) + (utils.power(f,3) / 27)
		print("H: ",h)
		#	When h <= 0, as is the case here, all 3 roots are real
		if h == 0 and f == 0 and g == 0:
			x = self.cube(self.C/self.Z) * -1
			print("solution are:")
			print("X1 = X2 = X3 = ", x, "round = ", round(x))
		elif h <= 0:
			i = utils.Sqrt(((utils.power(g,2)/4) - h))
			print("I: ",i)
			j = self.cube(i)
			print("J: ",j)
			k = math.acos(-(g / (2 * i)))
			print("K: ",k)
			l = -j
			print("L: ",l)
			m = math.cos(k/3)
			print("M: ",m)
			n = utils.Sqrt(3) * math.sin(k/3)
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
			r = -(g/2) + utils.Sqrt(h)
			print("R: ",r)
			s = self.cube(r)
			print("S: ",s)
			t = -(g/2) - utils.Sqrt(h)
			print("T: ",t)
			u =	self.cube(t)
			print("U: ", u)
			x1 = (s + u) - (self.A / (3 * self.Z))
			print("solution are:")
			print("X1 = ", x1, "round = ", round(x1))
			print("X2 = ",(-(s + u)/2 - (self.A / (3 * self.Z))),"+ I * ",(s - u) * utils.Sqrt(3)/2)
			print("X3 = ",(-(s + u)/2 - (self.A / (3 * self.Z))),"- I * ",(s - u) * utils.Sqrt(3)/2)

	def cube(self,x):
		if 0<=x: 
			return x**(1./3.)
		return -(-x)**(1./3.)