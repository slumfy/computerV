def power(x, y):
		if(y == 0): return 1
		temp = power(x, int(y / 2)) 
		if (y % 2 == 0):
			return temp * temp
		else:
			if(y > 0): return x * temp * temp
			else: return (temp * temp) / x

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