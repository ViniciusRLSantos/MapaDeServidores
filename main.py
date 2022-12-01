import random as rd
import ServidorAtivo as Sa
import ServidorInativo as Si


# Cria os objetos dos servidores ativos e inativos
ativo = Sa.ServidorAtivo()
inativo = Si.ServidorInativo()

# Gera um CPF aleatório
def gerarcpf():
    cpf = str(rd.randrange(100, 999)) + "." + str(rd.randrange(100, 999)) + "." \
          + str(rd.randrange(100, 999)) + "-" + str(rd.randrange(10, 99))
    return cpf

# Gera um nome aleatório
def gerarnome():
    primeiro_nome = ["Maria", "José", "Daniel", "Marcos", "Júlio", "João", "Pedro", "Jasparabaclebson", "Josedson",
                     "Nicole", "Daniela"]

    segundo_nome = [" da Silva", " Rego", " Antonieta", " Gonçalves", " Joestar", " Ferreira", " Lima"]

    ultimo_nome = [" Serelepe", " Rufino", " Aquino", " Barbosa", " Greyart", " Oliveira", " Bezerra"]

    nome_completo = rd.choice(primeiro_nome) + rd.choice(segundo_nome) + rd.choice(ultimo_nome)
    return nome_completo

# Escolhe um órgão aleatório da lista de órgãos
def gerarorgao():
    orgao = ["SENAC", "PM", "PO", "SESAU", "SEDUC", "PGR", "SEFAZ", "GMAL", "PGE", "PC"]
    return rd.choice(orgao)


# Gera servidores com nomes aleatórios só pra não preencher manualmente
for i in range(12):
    ativo.addServidor(gerarcpf(), gerarnome(), gerarorgao(), rd.randrange(2500, 35000))

for i in range(8):
    inativo.addServidor(gerarcpf(), gerarnome(), rd.choice(["Aposentado", "Pensionista"]),
                             rd.randrange(2500, 35000))


def verinfoativo():
    print("=====INFORMAÇÕES=====\n")
    id = int(input("Insira o ID do Servidor Ativo que deseja saber as informações [0 para voltar ao menu]: "))
    if id > 0 and id <= len(ativo.pessoas):
        ativo.getInformacaoDoServidor(id)
        main()
    else:
        print(f"ID [{id}] INEXISTENTE")
        main()


def verinfoinativo():
    print("=====INFORMAÇÕES=====\n")
    id = int(input("Insira o ID do Servidor Inativo que deseja saber as informações [0 para voltar ao menu]: "))
    if id > 0 and id <= len(inativo.pessoas):
        inativo.getInformacaoDoServidor(id)
        main()
    else:
        print(f"ID [{id}] INEXISTENTE")
        main()


def addativo():
    print("====ADICIONANDO SERVIDOR ATIVO====")
    cpf = input("CPF: ")
    nome_completo = input("Nome Completo: ")
    orgao = input("Órgão: ")
    salario_bruto = float(input("Remuneração Bruta: "))
    print("\nY = Sim / N = Não")
    confirma = input("Confirma?: ")
    if confirma[0] == "Y" or confirma[0] == "y":
        print("[ADICIONADO COM SUCESSO]")
        ativo.addServidor(cpf, nome_completo, orgao, salario_bruto)
    else:
        print("[O PROCESSO FALHOU OU FOI CANCELADO]")
    main()


def addinativo():
    print("====ADICIONANDO SERVIDOR INATIVO====")
    cpf = input("CPF: ")
    nome_completo = input("Nome Completo: ")
    vinculo = input("Vínculo: ")
    salario_bruto = float(input("Remuneração Bruta: "))
    print("\nY = Sim / N = Não")
    confirma = input("Confirma?: ")
    if confirma[0] == "Y" or confirma[0] == "y":
        print("[ADICIONADO COM SUCESSO]")
        inativo.addServidor(cpf, nome_completo, vinculo, salario_bruto)
    else:
        print("[O PROCESSO FALHOU OU FOI CANCELADO]")
    main()

def atualizarNomeDeAtivo():
    print("[ATUALIZAR NOME DO SERVIDOR ATIVO]\n")
    id = int(input("Insira o ID do Servidor: "))
    print(f"Antigo nome do ID{str(id)}: {ativo.getNome(id)}")
    novo_nome = str(input("Novo nome: "))
    ativo.setNome(id, novo_nome)
    print(f"Nome do ID {str(id)} atualizado para {novo_nome}\n\n[FIM]")
    main()

def atualizarNomeDeInativo():
    print("[ATUALIZAR NOME DO SERVIDOR ATIVO]\n")
    id = int(input("Insira o ID do Servidor: "))
    print(f"Antigo nome do ID{str(id)}: {inativo.getNome(id)}")
    novo_nome = str(input("Novo nome: "))
    inativo.setNome(id, novo_nome)
    print(f"Nome do ID {str(id)} atualizado para {novo_nome}\n\n[FIM]")
    main()


def main():
    print("======PORTAL DA TRANSPARÊNCIA======")
    print("\nAções:")
    print("[1] - Ver lista dos Servidores Ativos")
    print("[2] - Ver lista dos Servidores Inativos")
    print("[3] - Ver informação de um Servidor Ativo")
    print("[4] - Ver informação de um Servidor Inativo")
    print("[5] - Adicionar um Servidor Ativo")
    print("[6] - Adicionar um Servidor Inativo")
    print("[7] - Atualizar nome do Servidor Ativo")
    print("[8] - Atualizar nome do Servidor Inativo")
    print("[9] - Sair\n")
    acao = int(input("O que deseja fazer?: "))

    if acao == 1:
        ativo.getListaDosServidores()
        main()
    elif acao == 2:
        inativo.getListaDosServidores()
        main()
    elif acao == 3:
        verinfoativo()
    elif acao == 4:
        verinfoinativo()
    elif acao == 5:
        addativo()
    elif acao == 6:
        addinativo()
    elif acao == 7:
        atualizarNomeDeAtivo()
    elif acao == 8:
        atualizarNomeDeInativo()
    elif acao == 9:
        print("[-=Aplicativo Encerrado=-]")

if __name__ == '__main__':
    main()
