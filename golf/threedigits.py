r=1
for i in range(int(input())):
 r*=i+1
 while r%10<1:r//=10
 r%=int(10e12)
print(str(r)[-3:])