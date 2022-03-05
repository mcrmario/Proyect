num1= float(input("Ingrese su peso en kilogramos"))
num2= float(input("Ingrese estatura en metros"))

res = num1 / num2**2

print("El resultado es:", str(round(res,2)))

if res >=0 and res < 18.5:
    print("Estas en un peso bajo")
elif res >18.5 and res < 25:
    print("Tienes un peso normal")
elif res >25 and res < 30:
    print("Estas en sobrepeso")
elif res >30 and res < 35:
    print("Estas en obesidad")
elif res > 35 and res <100:
    print("Estas en obesidad extrema")
