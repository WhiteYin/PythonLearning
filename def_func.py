import math
def quadratic(a,b,c):
	det=b*b-4*a*c
	if det>0:
		x1=(-b+math.sqrt(det))/(2*a)
		x2=(-b-math.sqrt(det))/(2*a)
		return x1,x2
	elif det==0:
		x=(-b)/(2*a)
		return x
	else:
		return "无解"
		
print(quadratic(1,2,3))
print(quadratic(-1,2,3))
print(quadratic(1,2,1))