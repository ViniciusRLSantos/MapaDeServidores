from ServidorAtivo import ServidorAtivo


class ServidorInativo(ServidorAtivo):
    pass
    ativo = False

    def getInformacaoDoServidor(self, id):
        print("[ID: " + str(id) + "]")
        print("CPF: " + str(self.pessoas[id-1][0]))
        print("Nome: " + str(self.pessoas[id-1][1]))
        print("Vínculo: " + str(self.pessoas[id-1][2]))
        print("Salário Líquido: R$" + str(self.pessoas[id-1][3]) + "\n\n")

    def getListaDosServidores(self):
        print("[====SERVIDORES INATIVOS====]")
        for i in range(len(self.pessoas)):
            if self.pessoas[i][4]:
                print("[ID: " + str(i + 1) + "]")
                print("CPF: " + str(self.pessoas[i][0]))
                print("Nome: " + str(self.pessoas[i][1]))
                print("Vínculo: " + str(self.pessoas[i][2]))
                print("Salário Líquido: R$" + str(self.pessoas[i][3]) + "\n\n")
        print("=============FIM=============\n\n")

    # Só mudando o nome pra fazer mais sentido
    # Setter do Vínculo
    def setVinculo(self, id, vinculo):
        self.pessoas[id-1][2] = vinculo

    # Getter do Vínculo
    def getVinculo(self, id):
        return self.pessoas[id-1][2]
