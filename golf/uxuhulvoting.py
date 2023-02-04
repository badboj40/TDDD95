i=input
for _ in[1]*int(i()):
 o=0
 for p in[[*map(int,i().split())]for _ in[1]*int(i())][::-1]:o=[min([o[s^v]if o else s^v for v in(1,2,4)],key=lambda x:p[x])for s in range(8)]
 s=o[0];x='NY';print(x[s>3]+x[s&2>0]+x[s%2])