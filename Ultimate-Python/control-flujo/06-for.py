buscar = 10
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("Encontrado!", buscar)
        break
else:
    print("No se encontró el número")

for char in "Ultimate Python":
    print(char)