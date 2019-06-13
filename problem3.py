list=[1,2,3,1,4,5,66,22,2,6,0,9]
list1=[]
list2=[]
for i in list:
	if i>5:
		print(i)
		list1.append(i) 
print("\n")
for i in list:
	if i<=2:
		print(i)
		list2.append(i)
print(list1)
print(list2)
