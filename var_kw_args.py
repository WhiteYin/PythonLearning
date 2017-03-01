
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
	
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
	
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
	
def power(x,n=2):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s
