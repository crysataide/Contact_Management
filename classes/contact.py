import os

class Contact:
    erros = []
    contatos = []

    def __init__(self):
        pass
    # =======================================
    # Verifica se possui contatos cadastrados
    # =======================================
    def notEmptyContact(self):
        return len(self.contatos)>0
    # ===========================
    # Valida se string está vazia
    # ===========================
    def emptyVar(self,var):
        return len(var)==0
    # ================
    # Localiza Contato
    # ================
    def findContact(self,nome,tipo):
        lRet = False

        for i in self.contatos:
            if nome in i['nome']:
                lRet = True

        return lRet if tipo else not lRet
    # =======================
    # Valida dados do Contato
    # =======================
    def validContact(self,tipo,nome,telefone="",email=""):
        self.erros = []

        # Se nome (não) existe
        if self.notEmptyContact() and (self.emptyVar(nome) or self.findContact(nome,tipo)):
            self.erros.append(f"Nome digitado {"já" if tipo else "não"} existe")
        # Se telefone só possui dígitos
        if tipo and (self.emptyVar(telefone) or not telefone.isdigit()):
            self.erros.append("Telefone inválido")
        # Se email possui @/.
        if tipo and (self.emptyVar(email) or ("@" not in email or "." not in email)):
            self.erros.append("E-mail inválido")

        return not len(self.erros)>0
    # ====================
    # Retorna log de erros
    # ====================
    def erroLog(self,tipo):
        os.system("cls")
        print("\n")
        print(self.erros[0])
        print(self.erros[1]) if tipo == 1 and len(self.erros)>1 else ""
        print(self.erros[2]) if tipo == 1 and len(self.erros)>2 else ""
        print("\n")
        
        try:
            escolha = str(input("Deseja refazer os dados? Y/N: ")).upper()[0:1]
        except:
            return False
        return escolha == 'Y'
    # =============================
    # Retorna valor da maior string
    # =============================
    def biggerCaracter(self,key):
        nTam = 0
        for i in self.contatos:
            if len(i[key]) > nTam:
                nTam = len(i[key])
                
        return nTam
    # ============
    # Cria Contato
    # ============
    def createContact(self,nome,telefone,email):

        self.contatos.append({
                'nome':nome,
                'telefone':telefone,
                'email':email
            }
        )
        print("Contato criado!!!\n")

        os.system("pause")
    # ===============
    # Deletar Contato
    # ===============
    def deleteContact(self,nome):

        if self.notEmptyContact():
            del self.contatos[[index for index,nx in enumerate(list(self.contatos)) if nx['nome'] == nome][0]]

            print("Contato deletado!!!\n")
        else:
            print("Sem contatos cadastrados!!!\n")
        
        os.system("pause")
    # ==================
    # Visualiza Contatos
    # ==================
    def viewContact(self):

        if self.notEmptyContact():
            nTamNames = self.biggerCaracter('nome')
            nTamTelef = self.biggerCaracter('telefone')

            for i in self.contatos:
                print(f"Nome: {i['nome'].ljust(nTamNames)} | Telefone: {i['telefone'].ljust(nTamTelef)} | E-mail: {i['email']}")

            print("\n")
        else:
            print("\nSem contatos cadastrados!!!\n")

        os.system("pause")