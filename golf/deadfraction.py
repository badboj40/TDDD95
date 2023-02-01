while x:=input()[2:-3]:
 b=2;y=len(x);z=int(x)
 for i in range(1,y+1):
  f=__import__('fractions').Fraction(z-z//10**i,10**y-10**(y-i))
  if b>1or f.denominator<b.denominator:b=f
 print('1/1'*(1==b)or b)