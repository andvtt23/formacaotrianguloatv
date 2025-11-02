import math

def verificar_triangulo():
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))

    if a > b + c or b > a + c or c > a + b:
        print("Não formam um triângulo.")
        print(f"Valores lidos: a={a}, b={b}, c={c}")
    else:
        # Fórmula de Heron para calcular a área
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        print("Formam um triângulo.")
        print(f"Área do triângulo: {area:.2f}")

verificar_triangulo()