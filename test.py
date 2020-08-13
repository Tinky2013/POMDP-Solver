
#numlist = ['one','two','three','four']
#f = lambda x:str(x[0])+x[1]
#print(list(map(f,enumerate(numlist))))

a=[1,2,3,4]
b=[3,2,1,3]

print(list(map(lambda a,b:a+b, a,b)))