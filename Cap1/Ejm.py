print("Bien venido al parque de diverciones")
Altura = int(input("Cual es tu altura en Cm?: "))

if Altura >= 120:
    print("Puedes entrar al parque de diverciones")
    age = int(input("Cual es tu edad"))
    if age <= 12:
        print("Porfavor pague $5")
    elif age <18:
        print("Porfavor pague $7")
    else:
        print("Porfavor pague $12")

else:
    print("Lo sentimos no puedes entar al parque")

