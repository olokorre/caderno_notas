from os import system

from mesa import Mesa


class Menu:

    __mesa: Mesa

    def __init__(self) -> None:
        self.__mesa = Mesa()

    def __adicionar_nota(self) -> None:
        print("No que está pensando?")
        memo = input("> ")
        print("Informe as tags (separado por espaços):")
        tags = (input("> ")).split(" ")
        caderno = self.__mesa.pegarCaderno()
        caderno.nova_nota(memo, tags)
        self.__mesa.guardarCaderno(caderno)
        system("clear")

    def __exibir_notas(self) -> None:
        print("== Notas ==")
        caderno = self.__mesa.pegarCaderno()
        if caderno.quantidade_notas == 0:
            print("Nehnuma nota adicionada.")
        for linha in caderno.formatar_notas():
            print(linha)
        input("... Pressione [ENTER] para continuar ...")
        system("clear")

    def __buscar_notas(self) -> None:
        print("Informe o termo de busca:")
        filtro = input("> ")
        caderno = self.__mesa.pegarCaderno()
        notas = caderno.pesquisar(filtro)
        if len(notas) == 0:
            print("Nehnuma nota encontrada.")
        for nota in notas:
            print(nota.formatar())
        input("... Pressione [ENTER] para continuar ...")
        system("clear")

    def main(self) -> None:
        while True:
            print("== Menu Inicial ==")
            print(" 1. Adicionar Nota")
            print(" 2. Exibir todas as Notas")
            print(" 3. Buscar Notas")
            print(" 0. Sair")
            try:
                entrada = int(input("> "))
                system("clear")
                if entrada == 0:
                    exit(0)
                elif entrada == 1:
                    self.__adicionar_nota()
                elif entrada == 2:
                    self.__exibir_notas()
                elif entrada == 3:
                    self.__buscar_notas()
                raise Exception
            except KeyboardInterrupt:
                exit(0)
            except Exception:
                print("Comando não compreendido!")
