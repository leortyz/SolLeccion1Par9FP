codigos = ["001","002","003"]
nombres = ["COMPUTACION","TELECOMUNCACIONES","ALIMENTOS"]
precios  = [790,890,567]
actual=input('Ingrese año actual: ')
cond=len(actual)==4 and actual.isdigit()
while not cond:
  print('año invalido')
  actual=input('Ingrese año actual: ')
  cond=len(actual)==4 and actual.isdigit()
matricula=input('Ingrese número de matrícula: ')
cond=matricula=='fin' or (len(matricula)==10 and matricula.isdigit() and matricula[4:7] in codigos) 
while not cond:
  print('matricula invalida')
  matricula=input('Ingrese número de matrícula: ')
  cond=matricula=='fin' or (len(matricula)==10 and matricula.isdigit() and matricula[4:7] in codigos) 
while cond and matricula!='fin':
  anio=int(matricula[:4])
  codigo=int(matricula[4:7])-1
  registro=int(matricula[7:])
  desc=int(actual)-anio
  if desc==2:
    desc=precios[codigo]-precios[codigo]*0.05
    print('Estudiante de la carrera de',nombres[codigo],' paga',precios[codigo])
    print('Descuento del 5%')
  elif desc==3:
    desc=precios[codigo]-precios[codigo]*0.15
    print('Estudiante de la carrera de',nombres[codigo],' paga',precios[codigo])
    print('Descuento del 15%')
  elif desc>=4:
    desc=precios[codigo]-precios[codigo]*0.25
    print('Estudiante de la carrera de',nombres[codigo],' paga',precios[codigo])
    print('Descuento del 25%')
  else:
    desc=precios[codigo]
    print('Estudiante de la carrera de',nombres[codigo],' paga',precios[codigo])
    print('No aplica descuento')
  print('Total a pagar:',desc)
  matricula=input('Ingrese número de matrícula: ').lower()
  cond=matricula=='fin' or (len(matricula)==10 and matricula.isdigit() and matricula[4:7] in codigos) 
  while not cond:
    print('matricula invalida')
    matricula=input('Ingrese número de matrícula: ')
    cond=matricula=='fin' or (len(matricula)==10 and matricula.isdigit() and matricula[4:7] in codigos)