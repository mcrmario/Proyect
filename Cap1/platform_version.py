num1= float(input("Ingrese su peso en kilogramos"))
num2= float(input("Ingrese estatura en metros"))

res = num1 / num2**2

print("El resultado es:", str(round(res,2)))

if res >=0 and res <= 18.5:
    print("Estas en bajo peso, alimentate bien")
elif res >=18.6 and res <= 24.9:
    print("Bien hecho tu peso normal, no te descuides")
elif res >=25 and res <=29.9:
    print("Estas en sobrepeso, cuidate")
elif res >=30 and res <= 100:
    print("Estas en niveles de obesidad, ponle un alto a esto y ve al medico")
