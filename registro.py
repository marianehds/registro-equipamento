inventario=[]
Resposta="S"
while Resposta == "S":
  inventario.append(input("Equipamento: "))
  inventario.append(float(input("Valor: ")))
  inventario.append(int(input("Número Serial: ")))
  inventario.append(input("Departamento: "))
  Resposta = input("Digite \"S\" para continuar:").upper()
for elemento in inventario:
  print(elemento)