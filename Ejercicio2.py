clasifiacion=["carnicos","vegetariano","carnicos","vegetariano","bebidas"]
menu=["hamburguesa","papas fritas","hot dog","canguil","te helado"]
precios=[3.00,2.00,1.50,1.00,0.75] 
total=0
comida=''
while comida!='N':
  print('MENU'.center(10,'*'))
  for i in range(len(menu)):
    print(menu[i].ljust(20,' ')+str(precios[i]))
  orden=input("Ingresa tu orden: ").lower()
  orden=orden.split('-')
  subtotal=0
  for i in range(len(menu)):
    if orden[0]==menu[i]:
      if clasifiacion[i]=='vegetariano':        
        subtotal+=precios[i]-precios[i]*0.1
      else:        
        subtotal+=precios[i]
  if subtotal==0:
    print("Comida ingresada no se encuentra en el menu")
  total+=subtotal
  comida=input("¿Deseas algo adicional? S/N: ").upper()
print("Total a Pagar:",total)