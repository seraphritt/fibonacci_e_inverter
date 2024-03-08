def fibo(numero):
    inicio = [0, 1, 1]
    while inicio[-1] < numero:
        inicio.append(inicio[-1] + inicio[-2])
    if numero in inicio:
        return True

    return False


numero = int(input("Informe o número: "))
if fibo(numero):
    print("Esse número pertence a sequência de Fibonacci")
else:
    print("Esse número não pertence a sequência de Fibonacci")
