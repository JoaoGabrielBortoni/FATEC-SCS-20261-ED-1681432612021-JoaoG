'''
*----------------------------------------------------------------------------------*
*                           FATEC São Caetano do Sul                               *
*                                Atividade B2 - 2                                  *
*  Autor: 1681432612021 - João Gabriel Bortoni                                     *
*  Objetivo: Separar duas filas separadas (Alunos e ADM)                           *
*  Data: 28/04/2026                                                                *
*----------------------------------------------------------------------------------*
'''

fila_alunos = []   # fila de alunos
fila_adm    = []   # fila de administração


# ──────────────────────────────────────────────
#  PROVEDORES
# ──────────────────────────────────────────────

def adicionar_fila(tipo: str, nome: str, paginas: int) -> None:
    """Adiciona um documento à fila correta (aluno ou adm)."""
    doc = (nome, paginas)
    if tipo.lower() == "aluno":
        fila_alunos.append(doc)
        print(f"[+] Documento '{nome}' ({paginas} págs.) adicionado à fila de ALUNOS.")
    elif tipo.lower() == "adm":
        fila_adm.append(doc)
        print(f"[+] Documento '{nome}' ({paginas} págs.) adicionado à fila de ADM.")

    else:
        print("Tipo inválido. Use 'aluno' ou 'adm'.")


def consumir_fila() -> None:
    """
    Processa (remove) o próximo documento da impressora.
    Regra: processa aluno SOMENTE se a fila ADM estiver vazia.
    Caso contrário, processa o documento de ADM.
    """
    if fila_adm:
        doc = fila_adm.pop(0)
        print(f"[✓] Imprimindo (ADM):   '{doc[0]}' – {doc[1]} páginas")
    elif fila_alunos:
        doc = fila_alunos.pop(0)
        print(f"[✓] Imprimindo (Aluno): '{doc[0]}' – {doc[1]} páginas")
    else:
        print("[!] Nenhum documento em espera.")


def listar_filas() -> None:
    """Lista o estado atual de ambas as filas."""
    total = len(fila_alunos) + len(fila_adm)
    print(f"\n{'═'*45}")
    print(f"  ESTADO ATUAL DAS FILAS  |  Total em espera: {total}")
    print(f"{'═'*45}")

    print(f"\n  Fila ADM ({len(fila_adm)} doc(s)):")
    if fila_adm:
        for i, (nome, pags) in enumerate(fila_adm, 1):
            print(f"    {i}. {nome} [{pags} págs.]")
    else:
        print("    (vazia)")

    print(f"\n  Fila Alunos ({len(fila_alunos)} doc(s)):")
    if fila_alunos:
        for i, (nome, pags) in enumerate(fila_alunos, 1):
            print(f"    {i}. {nome} [{pags} págs.]")
    else:
        print("    (vazia)")
    print(f"{'═'*45}\n")


def reorganizar_fila() -> None:
    """
    Reorganiza as filas em ordem crescente de páginas
    (menor documento imprime primeiro em cada fila).
    """
    global fila_alunos, fila_adm
    fila_alunos = sorted(fila_alunos, key=lambda d: d[1])
    fila_adm    = sorted(fila_adm,    key=lambda d: d[1])
    print("[↺] Filas reorganizadas por número de páginas (crescente).")


# ──────────────────────────────────────────────
#  MENU INTERATIVO
# ──────────────────────────────────────────────

def menu() -> None:
    opcoes = """

  1. Adicionar documento (Aluno)          
  2. Adicionar documento (ADM)            
  3. Consumir fila (imprimir próximo)     
  4. Listar as duas filas                 
  5. Reorganizar fila (por nº de páginas)
  0. Sair                                 

"""
    while True:
        print(opcoes)
        escolha = input("Opção: ").strip()

        if escolha == "1":
            nome  = input("  Nome do arquivo : ").strip()
            pags  = int(input("  Total de páginas: "))
            adicionar_fila("aluno", nome, pags)

        elif escolha == "2":
            nome  = input("  Nome do arquivo : ").strip()
            pags  = int(input("  Total de páginas: "))
            adicionar_fila("adm", nome, pags)

        elif escolha == "3":
            consumir_fila()

        elif escolha == "4":
            listar_filas()

        elif escolha == "5":
            reorganizar_fila()

        elif escolha == "0":
            print("Encerrando. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


# ──────────────────────────────────────────────
#  PONTO DE ENTRADA
# ──────────────────────────────────────────────

if __name__ == "__main__":
    menu()