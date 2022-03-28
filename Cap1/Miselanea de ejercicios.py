from ast import Break, For, If
from cgi import print_arguments
from re import X


print("Esta es la miscelania de ejercicios de python")

while True:


      Menuprin= ("1"),("2"),("3"),("99")

      print("Para operaciones elija el numero 1"
      "\nPara condicionales elija el numero 2"
      "\nPara ciclos elija el numero 3"
      "\nPara salir elija el numero 99")
  

      Menuprin= int(input("Cual de las opciones quiere realizar: "))
      
      if Menuprin==1:
          while True:
              print(" 1: Calcular el área de un triangulo"
              "\n 2: Ingerese dos numero por teclado y sumarlos"
              "\n 3: Numero elevado al cuadrado"
              "\n 4: Converción de euros a dolares"
              "\n 5: Area y perimetro de un cuadrado"
              "\n 6: Area y el volumen de un cilindro"
              "\n 7: Radio de circunferencia, longitud y area del circulo"
              "\n 8: Promedio de tres numero ingresados por teclado"
              "\n 9: Salir")
             
              operadores= int(input("Cual de los operadores quiere realizar: "))
             
              if operadores==1:
                  print("Vas a calcular el área de un triangulo")
                  base = float(input("Digite el valor de la base del triangulo: "))
                  altura = float(input("Digite el valor de la altura del triangulo: "))

                  area= base * altura / 2

                  Resultado = print("El area del triangulo es:",area)

              elif operadores ==2:
                  print("Vas a ingresar dos numero a la vez, y estos seran sumados")
                  
                  sum=(input("Digite los dos numero: "))
                  
                  num1 = int(sum[0])
                  num2 = int(sum[1])
                  
                  suma = num1 + num2 
                  Resultado = print("El resultado de la suma por teclaado es", suma)
                
              elif operadores==3:
                    print("Vas a ingresar un numero y este se elevara al cuadrado")
                    numero= int(input("Digite el numero que desea elevar al cuadrado: "))

                    Cuadradro = numero**2
                    Resultado = print("El resultado del cuadrado es:", Cuadradro)

              elif operadores==4:
                  print("Vas a convertir euros a dolares")
                  euros = float(input("Digite el numero de euros que desea convertir a dolares: "))
                  
                  conv= euros *1.0831
                  Resultado = print("El resultado de la conversión es:", conv)

              elif operadores==5:
                  print ("Vas a hallar el área y perimetro de un cuadrado")
                  lado= int(input("Digite el valor de uno de los lados del cuadrado: "))

                  area= lado * lado

                  perimetro= lado+lado+lado+lado

                  Resultado = print(" El área del cuadrado es:", area)
                  print("El perimetro del cuadrado es:", perimetro)


              elif operadores==6:
                  print("Vas a hallar el area y perimetro de un cilindro")
                  pi=3.1416

                  radio = float(input("Digite el radio del cilindro: "))
                  altura= float(input("Digite la altural del cilindro: "))
                  area= 2*pi* radio*(radio+altura)

                  perimetro= pi*(radio**2)* altura

                  Resultado= print("El resultado del area del cilindro es:", area)
                  print("El perimetro del cilindro es:", perimetro)

              
              elif operadores==7:
                  print("Vas a hallar el radio, longitud y area de un circulo")
                  pi=3.1416
                 
                  radio=float(input("Digite el radio del circulo"))

                  area= pi* radio**2

                  Resultado= print("El radio del circulo es:", radio)
                  print("El area del circulo es:", area)

              
              elif operadores==8:
                  print("Vas a promediar los 3 numero que ingreses")
                  num1= int(input("Digite el primer numero: "))
                  num2= int(input("Digite el segundo numero: "))
                  num3= int(input("Digite el tercer numero: "))

                  suma= (num1+num2+num3)
                  promedio =suma/3


                  Resultado= print("El promedio de los tres numero es:", promedio)

              
              if operadores==9:
                  break
            

      if Menuprin==2:
           while True:
               print(" 1: Saber si el numero es positivo o negativo"
              "\n 2: Saber cual de los dos numero digitados es menor y mayor"
              "\n 3: Saber cual es el numero mayor y menor entre tres enteros positivos"
              "\n 4: Dos numeros A y B, sumarlos si es menor que B o sino restarlos"
              "\n 5: Encontar el cociente entre A y B"
              "\n 6: Sumar dos numero pero si uno de ellos es negativo, en caso contrario multiplicarlos"
              "\n 7: Determina si un año es bisiesto o no"
              "\n 8: Salir")

               condicionales= int(input("Cual de los condicionales quiere realizar: "))

              
               if condicionales == 1:
                   print("Vas a saber si el numero que ingresas es positivo o negativo")

                   Num1= int(input("Digite el numero deseado: "))

                   if Num1 > 0:
                       print("El numero digitado es positivo")

                   elif Num1 < 0:
                       print("El numero digitado es negativo")

               elif condicionales ==2:
                   print("vas a saber cual es el numero mayor y menor entre dos numeros")

                   num1 = float(input("Digite el primer numero"))
                   num2= float(input("Digite el segundo numero"))

                   mayor= 0
                   menor = 0
                   i =1 

                   mayor = max (num1, num2)
                   menor = min (num1, num2)

                   print("El numero mayor es:", mayor)
                   print("El numero menor es:", menor)

               elif condicionales ==3:
                   print("Vas a calcular el menor y mayor entre tres numero enteros positivos")

                   num1 = float(input("Digite el primer numero: "))
                   num2= float(input("Digite el segundo numero: "))
                   num3= float(input("Digite el tercer numero: "))

                   mayor= 0
                   menor = 0
                   i =1 

                   mayor = max (num1, num2, num3)
                   menor = min (num1, num2, num3)

                   print("El numero mayor es:", mayor)
                   print("El numero menor es:", menor)

               elif condicionales ==4:
                   print("Vas a sumar o restar dos numeros segun su superioridad numerica")

                   num1= float(input("Digite el primer numero: "))
                   num2= float(input("Digite el segundo numero: "))

                   if num1 < num2:
                       suma =num1 + num2
                       print("El resultado es", suma)
                      

                   elif num1 > num2:
                       multi = num1 * num2
                       print("La multiplicacion es:", multi)

               elif condicionales ==5:
                   print("Vas a encontrar el cociente entre dos numero")

                   num1= float(input("Digite el primer numero: "))
                   num2= float(input("Digite el segundo numero: "))

                   if num1 == 0 or num2 ==0:
                       print("La divicion no es posible")

                   else:
                       print(num1/num2)

               elif condicionales == 6:
                   print ("Vas a sumar y multiplicar dos numero segun su positividad o negatividad")

                   num1= float(input("Digite el primer digito: "))
                   num2= float(input("Digite el segundo digito: "))

                   if num1 and num2 < 0:
                       suma= num1 + num2
                       print("La suma es:", suma)

                   elif num1 and num2 >0:
                       multi= num1 * num2
                       print("La multipicacion es.",multi)

               elif condicionales ==7:
                   print("Vas a saber si un año es bisiesto o no")

                   año= int(input("Digite el año"))

                   if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
                       print("El año", año, "es bisiesto")

                   else:
                       print("El año", año, "no es bisiesto")


               elif condicionales ==8:
                   break



      if Menuprin==3:
           while True:
               print(" 1: Imprimir todos los multiplos de tres"
              "\n 2: Imprimir numeros impares ente creo y cien"
              "\n 3: Imprimir numeros pares del 1 al 100"
              "\n 4: Cuadros de los numero del 1 al 30"
              "\n 5: Los primeros cien numero naturales sumados entre sus cuadros"
              "\n 6: Todos los numero comprendidos de forma ascendente entre dos numero"
              "\n 7: SUma de todos los numero que digitan mientras no sea cero"
              "\n 8: Salir")

               Ciclos= int(input("Digite el ciclo que desea realizar: "))

               if Ciclos ==1:
                   print("Vas a saber los multiplos de tres que hay entre uno y cien")

        
                   for i in range (0,100, 3):
                       print(i)


               if Ciclos ==2:
                   print("Vas a saber los numeros impares de cero a cien")

                   X = 1
                   while X <=100:
                       if X % 2==1:
                           print(X)
                       X +=1

               if Ciclos ==3:
                   print("Vas a saber los numero pares del un al cien")

                   for i in range (0,100, 2):
                       print(i)

                
               if Ciclos==4:
                   print("Vas a saber los cuadrados de los numeros 1 al 30")

                   Cuadradro= [ p**2 for p in range (1,30)]
                   print(Cuadradro)

               if  Ciclos==5:
                   print("Vas a saber la suma de los cuadros de los 100 primeros numeros")
                   sumar=0
                   
                   for i in range (101):
                       cu= (i+1) * (i+1)
                       sumar= sumar + cu

                       print("la suma es:",sumar)

               if Ciclos ==6:
                   print("Vas a saber los numeros comprendidos entre dos numeros")
                   import os
             
                   def numb():
                       os.system('cls')

                       numero= int(input("Digite un numero: "))
                       numero1=int(input("Digite un numero: "))

                       contador = numero +1
                       numero1 = numero1 -1

                       while contador <= numero1:
                           print(contador)
                           contador= contador+1

                           
                   numb ()

               if   Ciclos ==7:
                   print("Vas a sumar todos los numeros digitados")
                   
                   def sumaDigitos(num):
                         s= 0 
                         while num >0:
                               s= s+ num % 10
                               num = num // 10
                         return s     



                   n= int(input("Digite la cantidad de numeros: "))
                   suma = 0
                   while n > 0:
                         num= int(input("Digita un numero: "))
                         suma= suma + sumaDigitos(num)
                         n= n -1

                   print(suma)


               if   Ciclos ==8:
                   break



                   




      if Menuprin ==99:
         break
                    
                       



       
     
     
     
     
     
     
     
     




             