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

    def __editar_nota(self) -> None:
        print("Informe o id da nota:")
        id = int(input("> "))
        caderno = self.__mesa.pegarCaderno()
        nota = next(n for n in caderno.notas if n.id == id)
        print("Nota atual:")
        print(nota.formatar())
        print("Novo memo:")
        memo = input("> ")
        print("Novas tags (separado por espaços):")
        tags = (input("> ")).split(" ")
        print("Nota editada:")
        print(f'{id}. "{memo}" ({", ".join(tags)})')
        print("Confirmar alteração? (s/n)")
        confirmacao = input("> ")
        if confirmacao.lower() != "s":
            system("clear")
            return
        caderno.modificar_memo(id, memo)
        caderno.modificar_tags(id, tags)
        self.__mesa.guardarCaderno(caderno)
        system("clear")

    def __remover_nota(self) -> None:
        print("Informe o id da nota:")
        id = int(input("> "))
        caderno = self.__mesa.pegarCaderno()
        nota = next(n for n in caderno.notas if n.id == id)
        print("Nota a remover:")
        print(nota.formatar())
        print("Confirmar remoção? (s/n)")
        confirmacao = input("> ")
        if confirmacao.lower() != "s":
            system("clear")
            return
        caderno.remover_nota(id)
        self.__mesa.guardarCaderno(caderno)
        system("clear")

    def main(self) -> None:
        while True:
            print("== Menu Inicial ==")
            print(" 1. Adicionar Nota")
            print(" 2. Exibir todas as Notas")
            print(" 3. Buscar Notas")
            print(" 4. Editar Nota")
            print(" 5. Remover Nota")
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
                elif entrada == 4:
                    self.__editar_nota()
                elif entrada == 5:
                    self.__remover_nota()
                raise Exception
            except KeyboardInterrupt:
                exit(0)
            except Exception:
                print("Comando não compreendido!")
