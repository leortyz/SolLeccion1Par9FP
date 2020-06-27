especies = ["gavilan gris|ave|3", "raton de campo|roedor|89", "halcon reidor|ave|4", "perico catirrojo|ave|13","oso perezojo|oso|7","jaguar|felino|7"]
tipoIn=input('Ingrese tipo de especie: ').lower()
peligro=0
print('Las especies en peligro de extinción de tipo', tipoIn,'son:')
for n in especies:
  nombre, tipo, cant= n.split('|')
  if tipo == tipoIn and int(cant)<5 :    
    print(nombre+': '+cant)
    peligro+=1
if peligro>0:
  print('Hay',peligro,tipoIn, 'en peligro de extinción')
else:
  print('No hay',tipoIn,'en peligro de extinción')