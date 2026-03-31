"""
Calculadora RPN (Notação Polonesa Reversa)
Requisitos:
  1. Receber expressão RPN
  2. Fazer o cálculo
  3. Entradas de operação
  4. Mostrar posicionamentos de X, Y, Z durante a operação
  5. Mostrar resultado final
  6. Mostrar notação algébrica
"""

class PilhaRPN:
    def __init__(self):
        self.X = 0.0
        self.Y = 0.0
        self.Z = 0.0
        self.T = 0.0

    def empilhar(self, valor):
        """T←Z, Z←Y, Y←X, X←valor"""
        self.T = self.Z
        self.Z = self.Y
        self.Y = self.X
        self.X = float(valor)

    def operar(self, operador):
        """Calcula Resultado = Y op X, atualiza pilha"""
        if operador == '/' and self.X == 0:
            raise ZeroDivisionError("Divisão por zero!")

        operacoes = {
            '+': self.Y + self.X,
            '-': self.Y - self.X,
            '*': self.Y * self.X,
            '/': self.Y / self.X,
        }

        resultado = operacoes[operador]

        # Atualiza pilha: X←Res, Y←Z, Z←T
        self.X = resultado
        self.Y = self.Z
        self.Z = self.T

        return resultado

    def mostrar_posicionamento(self, momento=""):
        """Requisito 4: Mostrar posicionamentos de X, Y, Z"""
        print(f"\n  {'─'*30}")
        if momento:
            print(f"  📍 {momento}")
        print(f"  {'─'*30}")
        print(f"  Z = {fmt(self.Z)}")
        print(f"  Y = {fmt(self.Y)}")
        print(f"  X = {fmt(self.X)}  <- topo")
        print(f"  {'─'*30}")


def fmt(valor):
    """Formata número removendo .0 desnecessário"""
    try:
        return int(valor) if float(valor) == int(valor) else round(float(valor), 6)
    except:
        return valor


def construir_notacao(tokens):
    """Reconstrói a notação algébrica a partir dos tokens RPN"""
    pilha_expr = []
    for token in tokens:
        if token in ('+', '-', '*', '/'):
            b = pilha_expr.pop()
            a = pilha_expr.pop()
            pilha_expr.append(f"({a} {token} {b})")
        else:
            pilha_expr.append(token)
    return pilha_expr[0] if pilha_expr else ""


def calcular_rpn(expressao):
    """Executa todos os 6 requisitos"""
    tokens = expressao.strip().split()
    pilha = PilhaRPN()
    notacao_passos = []

    print("\n" + "="*40)
    print("  CALCULADORA RPN")
    print("="*40)

    # Requisito 1: Receber RPN
    print(f"\n  1) Expressao RPN recebida:")
    print(f"     '{expressao}'")

    # Requisito 3: Entradas de operação
    print(f"\n  3) Tokens identificados:")
    for i, t in enumerate(tokens, 1):
        tipo = "numero" if t not in ('+', '-', '*', '/') else "operador"
        print(f"     [{i}] '{t}'  -> {tipo}")

    print("\n" + "-"*40)
    print("  2) Processando o calculo...")
    print("-"*40)

    # Requisito 2 e 4: Cálculo + posicionamentos
    for token in tokens:
        if token in ('+', '-', '*', '/'):
            y_antes = pilha.Y
            x_antes = pilha.X
            resultado = pilha.operar(token)
            notacao_passos.append(f"{fmt(y_antes)} {token} {fmt(x_antes)} = {fmt(resultado)}")
            pilha.mostrar_posicionamento(f"Apos operacao: {fmt(y_antes)} {token} {fmt(x_antes)} = {fmt(resultado)}")
        else:
            pilha.empilhar(float(token))
            pilha.mostrar_posicionamento(f"Apos empilhar: {token}")

    # Requisito 5: Resultado final
    print(f"\n  5) Resultado final:")
    print(f"     X = {fmt(pilha.X)}")

    # Requisito 6: Notação algébrica
    notacao = construir_notacao(tokens)
    print(f"\n  6) Notacao algebrica:")
    print(f"     {notacao} = {fmt(pilha.X)}")

    if len(notacao_passos) > 1:
        print(f"\n     Passo a passo:")
        for i, passo in enumerate(notacao_passos, 1):
            print(f"     {i}. {passo}")

    print("\n" + "="*40 + "\n")


def main():
    print("""
+======================================+
|        CALCULADORA RPN               |
|  Digite a expressao em notacao RPN   |
|  Exemplo: 3 4 + 2 *                  |
|  Digite 'sair' para encerrar         |
+======================================+
    """)

    while True:
        try:
            expressao = input("  Digite a expressao RPN: ").strip()

            if expressao.lower() == 'sair':
                print("\n  Encerrando. Ate mais!\n")
                break

            if not expressao:
                continue

            calcular_rpn(expressao)

        except ZeroDivisionError as e:
            print(f"\n  ERRO: {e}\n")
        except (IndexError, ValueError):
            print(f"\n  ERRO: Expressao invalida! Verifique a notacao RPN.\n")
        except KeyboardInterrupt:
            print("\n\n  Encerrando. Ate mais!\n")
            break


if __name__ == "__main__":
    main()