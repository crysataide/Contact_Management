import os

from classes.contact import Contact
from classes.headers import Headers

nome = ""
email = ""
telefone = ""

# =================
# Seta as variáveis
# =================
def setVar(escolha):
    global nome,email,telefone

    nome = input("Digite o nome do contato: ")
    if escolha == 1:
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
    print("\n")
        
# ================
# Mensagem de erro
# ================
def valueInvalid():
    print("Valor inválido\n")
    os.system("pause")
    main()

# ==============
# Página Inicial
# ==============
def main():
    
    while True:
        headers = Headers()
        contact = Contact()

        headers.home()

        try:
            escolha = int(input("Escolha uma das opções a cima: "))

            match escolha:
                case 1:
                    while True:
                        headers.create()
                        setVar(escolha)

                        if contact.validContact(True,nome,telefone,email):
                            contact.createContact(nome,telefone,email)
                            break
                        elif not contact.erroLog(1):
                            break
                case 2:
                    while True:
                        headers.delete()
                        setVar(escolha)

                        if contact.validContact(False,nome):
                            contact.deleteContact(nome)
                            break
                        elif not contact.erroLog(2):
                            break
                case 3:
                    headers.view()
                    contact.viewContact()
                case 4:
                    headers.exit()
                    return
                case _:
                    valueInvalid()
        except:
            valueInvalid()
    
if __name__ == '__main__':
    main()
    
