import sys
for i in map(int,sys.stdin):
 r=""
 while i:r+="0125986"[i%7];i//=7
 print(r)