class ServidorAtivo:
    def __init__(self):
        self.pessoas = []

    ativo = True

    # Calcula o valor do Salário Líquido dado o Salário Bruto
    def calcularSalarioLiquido(self, salario_bruto):
        if salario_bruto > 5000:
            salario_liquido = salario_bruto - salario_bruto*0.20
        else:
            salario_liquido = salario_bruto - salario_bruto*0.075

        return salario_liquido

    # Adiciona um servidor
    def addServidor(self, cpf, nome, orgao, salario_bruto):
        individuo = [cpf, nome, orgao, self.calcularSalarioLiquido(salario_bruto), ServidorAtivo.ativo]
        self.pessoas.append(individuo)

    # Mostra a lista de um Servidor específico dado o ID e suas devidas informações
    def getInformacaoDoServidor(self, id):
        print("[ID: " + str(id) + "]")
        print("CPF: " + str(self.pessoas[id-1][0]))
        print("Nome: " + str(self.pessoas[id-1][1]))
        print("Órgão: " + str(self.pessoas[id-1][2]))
        print("Salário Líquido: R$" + str(self.pessoas[id-1][3]) + "\n\n")

    # Mostra a lista de todos os Servidores e suas devidas informações
    def getListaDosServidores(self):
        print("[====SERVIDORES ATIVOS====]")
        for i in range(len(self.pessoas)):
            if self.pessoas[i][4]:
                print("[ID: " + str(i + 1) + "]")
                print("CPF: " + str(self.pessoas[i][0]))
                print("Nome: " + str(self.pessoas[i][1]))
                print("Órgão: " + str(self.pessoas[i][2]))
                print("Salário Líquido: R$" + str(self.pessoas[i][3]) + "\n\n")
        print("[===========FIM===========]\n\n")

    #Setters baseado no id do servidor
    def setCPF(self, id, cpf):
        self.pessoas[id-1][0] = cpf

    def setNome(self, id, nome):
        self.pessoas[id-1][1] = nome

    def setOrgao(self, id, orgao):
        self.pessoas[id-1][2] = orgao

    def setSalario(self, id, salario_bruto):
        self.pessoas[id-1][3] = self.calcularSalarioLiquido(salario_bruto)

    # Getters dado o id do servidor
    def getCPF(self, id):
        return self.pessoas[id - 1][0]

    def getNome(self, id):
        return self.pessoas[id - 1][1]

    def getOrgao(self, id):
        return self.pessoas[id - 1][2]

    def getSalario(self, id):
        return self.pessoas[id - 1][3]


