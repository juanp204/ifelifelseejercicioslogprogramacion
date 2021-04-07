notas = []
for x in range(3):
    while True:
        try:
            nota = float(input("ingrese nota" + " " + str(x+1) + "="))
            if nota>10 or nota<0:
                print("solo numeros entre 0 y 10")
                continue
            else:
                notas.append(nota)
                break
        except ValueError:
            print("solo numeros")
            continue
prom = sum(notas)/3
print("el promedio es",prom)
if 7 <=prom <= 10:
    print("promovido")
elif 4 <=prom < 7:
    print("regular")
elif 0 <=prom < 4:
    print("reprovado")
