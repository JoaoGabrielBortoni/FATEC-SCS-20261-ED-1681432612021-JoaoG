"""
Calculadora RPN (Notacao Polonesa Reversa)
"""

X, Y, Z, T = 0, 0, 0, 0
notacao = []

def empilhar(valor):
    global X, Y, Z, T
    T = Z
    Z = Y
    Y = X
    X = valor

def operar(op):
    global X, Y, Z, T
    if op == '+': resultado = Y + X
    elif op == '-': resultado = Y - X
    elif op == '*': resultado = Y * X
    elif op == '/': resultado = Y / X
    notacao.append(f"({fmt(Y)} {op} {fmt(X)})")
    X = resultado
    Y = Z
    Z = T

def mostrar_pilha(momento):
    print(f"\n  -- {momento} --")
    print(f"  Z = {fmt(Z)}")
    print(f"  Y = {fmt(Y)}")
    print(f"  X = {fmt(X)}  <- topo")

def fmt(v):
    return int(v) if float(v) == int(v) else round(v, 4)

# 1. Receber expressao RPN
expressao = input("Digite a expressao RPN: ")
tokens = expressao.split()

# 2 e 4. Fazer o calculo mostrando X, Y, Z
for token in tokens:
    if token in ('+', '-', '*', '/'):
        operar(token)
        mostrar_pilha(f"Apos operacao '{token}'")
    else:
        empilhar(float(token))
        mostrar_pilha(f"Apos empilhar {token}")

# 5. Resultado final
print(f"\n  Resultado final: {fmt(X)}")

# 6. Notacao algebrica
print(f"  Notacao algebrica: {' = '.join(notacao)} = {fmt(X)}")