import random as r
l=[]
for i in range(100):
  l.append(str(r.randint(0,1)))
l2="".join(l)
l2=l2.split('1')
pos=-1
for i in range(len(l2)):
  if len(l2[i])>pos:
    pos=i
print("La cantidad más larga de ceros en la lista:",l,'es:',pos)