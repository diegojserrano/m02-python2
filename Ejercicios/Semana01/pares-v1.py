desde = int(input("Ingrese un número: "))
hasta = int(input("Ingrese otro: "))

for i in range(desde, hasta+1):
    if i % 2 == 0:
        print(i)
        