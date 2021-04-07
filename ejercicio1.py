while True:
    try:
        num = int(input("ingrese numero: "))
        break
    except ValueError:
        print("solo numeros")
        continue
if num%5 == 0 & num%3 == 0:
    print("el numero cumple")
else:
    print("el numero no cumple")