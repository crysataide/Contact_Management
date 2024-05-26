import os

class Headers:
    def __init__(self):
        pass
    # Cabeçalho inicial
    def home(self):
        os.system("cls")
        print("===========================\n")
        print(" Gerenciamento de Contatos\n")
        print("===========================\n")
        
        print("1 - Criar contato")
        print("2 - Deletar contato")
        print("3 - Visualizar todos os contatos")
        print("4 - Sair")
        
        print("\n")
    # Cabeçalho da Criação de Contato
    def create(self):
        os.system("cls")
        print("========================\n")
        print("   Criar Novo Contato\n")
        print("========================\n")
    # Cabeçalho da Deleção de Contato
    def delete(self):
        os.system("cls")
        print("=====================\n")
        print("   Deletar Contato\n")
        print("=====================\n")
    # Cabeçalho da Visualização de Contato
    def view(self):
        os.system("cls")
        print("=========================\n")
        print("   Visualizar Contatos\n")
        print("=========================\n")
    # Cabeçalho de encerramento
    def exit(self):
        os.system("cls")
        print("======================================\n")
        print(" Obrigado por participar volte sempre\n")
        print("======================================\n")
        os.system("pause")