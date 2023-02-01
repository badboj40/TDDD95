while x:=int(input()):
 for b in range(2,int(abs(x)**.5)+2):
  p=0;y=abs(x)
  while y%b<1:y//=b;p+=1
  if y==1and(x>0or x<0and p%2):print(p);break
 else:print(1)