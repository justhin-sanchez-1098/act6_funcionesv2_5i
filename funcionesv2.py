print("mas sobre funciones")
# aqui se escriben las funciones
def suma_ab(a,b):
    s=a+b
    return s
def resta_ab(a,b):
    s=a-b
    return s
def multiplicar_ab(a,b):
    s=a*b
    return s
def dividir_ab(a,b):
    s=a/b
    return s

#llamadas a funciones

# suma 
n1=int(input("ingresa el primer numero "))
n2=int(input("ingresa el segundo numero "))
suma=suma_ab(n1,n2)
print(f"la suma de {n1} + {n2} es {suma}")

# resta
print("calculando resta")
resta=resta_ab(n1,n2)
print(f"la resta de {n1} - {n2} es {resta}")

# multiplicacion
print("calculando multiplicacion")
multiplicacion=multiplicar_ab(n1,n2)
print(f"la multiplicacion de {n1} * {n2} es {multiplicacion}")

# division
print("calculando division")
division=dividir_ab(n1,n2)
print(f"la division de {n1} / {n2} es {division}")