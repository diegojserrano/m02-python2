desde = int(input("Ingrese un número: "))
hasta = int(input("Ingrese otro: "))

if desde % 2 != 0:
    desde += 1

for i in range(desde, hasta + 1, 2):
    print(i)
