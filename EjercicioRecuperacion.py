codigos = ["001","002","003"]
departamentos = ["Sistemas","Taller","Contabilidad"]
sueldos  = [790,890,567]
actual=input('Ingrese año actual: ')
cond=len(actual)==4 and actual.isdigit()
while not cond:
  print('año invalido')
  actual=input('Ingrese año actual: ')
  cond=len(actual)==4 and actual.isdigit()
codigo=input('Ingrese codigo del empleado: ').upper()
cond=codigo=='N' or (len(codigo)==10 and codigo.isdigit() and codigo[4:7] in codigos) 
while not cond:
  print('codigo inválido : No existe departamento o no tiene 10 digitos')
  codigo=input('Ingrese codigo del empleado: ').upper()
  cond=codigo=='N' or (len(codigo)==10 and codigo.isdigit() and codigo[4:7] in codigos) 
while cond and codigo!='N':
  anio=int(codigo[:4])
  cod=int(codigo[4:7])-1
  registro=int(codigo[7:])
  aum=int(actual)-anio
  if aum==2:
    aum=sueldos[cod]+sueldos[cod]*0.05
    print('Empleado de',departamentos[cod],' sueldo: $',sueldos[cod])
    print('Aumento del 5%')
  elif aum==3:
    aum=sueldos[cod]+sueldos[cod]*0.15
    print('Empleado de',departamentos[cod],' sueldo: $',sueldos[cod])
    print('Aumento del 15%')
  elif aum>=4:
    aum=sueldos[cod]+sueldos[cod]*0.25
    print('Empleado de',departamentos[cod],' sueldo: $',sueldos[cod])
    print('Aumento del 25%')
  else:
    aum=sueldos[cod]
    print('Empleado de',departamentos[cod],' sueldo: $',sueldos[cod])
    print('No aplica aumento')
  print('Total sueldo: $',aum)
  codigo=input('Ingrese codigo del empleado: ').upper()
  cond=codigo=='N' or (len(codigo)==10 and codigo.isdigit() and codigo[4:7] in codigos) 
  while not cond:
    print('codigo inválido : No existe departamento o no tiene 10 digitos')
    codigo=input('Ingrese codigo del empleado: ').upper()
    cond=codigo=='N' or (len(codigo)==10 and codigo.isdigit() and codigo[4:7] in codigos)