def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError("参数类型错误")
	if x>=0:
		return x;
	else:
		return -x;

n1=200
n2=-200
print(my_abs(n1),my_abs(n2))