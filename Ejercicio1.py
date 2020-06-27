menu="<food>Belgian Waffles|$5.95|650</food><food>Strawberry Belgian Waffles|$7.95|900</food><food>Berry-Berry Belgian Waffles|$8.95|900</food><food>French Toast|$4.50|600</calories></food><food>Homestyle Breakfast|$6.95|950</food>"
menu=menu.split('</food>') 
comida=input("¿Qué desea buscar?: ").lower() 
for i in menu:
  if comida in i.lower(): 
    i=i.strip('<food>') 
    item=i.split('|') 
    print(item[0],"Precio:",item[1],"Calorias:",item[2])