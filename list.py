L=[
	['Apple','Google','Mircosoft'],
	['Java','Python','Ruby','PHP'],
	['Adam','Bart','Lisa']
]
#打印Apple
print(L[0][0])
#打印Python
print(L[1][1])
#打印Lisa
print(L[2][2])
#PHP后插入C++
L[1].append('C++')
print(L)
#Java后插入C
L[1].insert(1,'C')
print(L)
#修改PHP为.net
L[1][4]='.net'
print(L)