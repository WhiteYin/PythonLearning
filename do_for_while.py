#输出1+2+...+100的和
sum=0
for x in range(101):
	sum = sum + x
print(sum)
#计算100以内所有奇数的和
sum=0
n=99
while n>0:
	sum = sum+n
	n = n-2
print(sum)
#请利用循环依次对list中的每个名字打印出Hello, xxx!
L=['ZC','TBB','SC','WXD']
for name in L:
	print('Hello,',name+'!')
	

