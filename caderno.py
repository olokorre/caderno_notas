from nota import Nota


class Caderno:
    """Classe que representa o caderno"""

    __notas: list[Nota]

    def __init__(self, notas: list[Nota] = []) -> None:
        self.__notas = notas

    @property
    def notas(self) -> list[Nota]:
        return self.__notas.copy()

    @property
    def quantidade_notas(self) -> int:
        return len(self.__notas)

    def __proxima_nota(self) -> int:
        """Busca pelo próximo id de nota disponível"""
        if len(self.__notas) == 0:
            return 1
        return max(nota.id for nota in self.__notas) + 1

    def __buscar_nota_pelo_id(self, id: int) -> Nota:
        """Busca e retorna a instancia da nota pelo ID"""
        for nota in self.__notas:
            if nota.id == id:
                return nota
        raise Exception(f"Nota não encontrada para id {id}")

    def nova_nota(self, memo: str, tags: list[str] = []) -> None:
        """Cria uma instancia de nota nova e salva no caderno"""
        id = self.__proxima_nota()
        nota = Nota(id, memo, tags)
        self.__notas.append(nota)

    def pesquisar(self, filtro: str) -> list[Nota]:
        """
        Pesquisa entre os memorando de cada nota e retorna uma lista
        com os casos positivos
        """
        notas = []
        for nota in self.__notas:
            if not nota.corresponde(filtro):
                continue
            notas.append(nota)
        return notas

    def modificar_memo(self, id: int, memo: str) -> None:
        """Modifica o memorando da nota"""
        nota = self.__buscar_nota_pelo_id(id)
        nota.modificar_memo(memo)

    def modificar_tags(self, id: int, tags: list[str]) -> None:
        """modifica as tags da notas"""
        nota = self.__buscar_nota_pelo_id(id)
        nota.modificar_tags(tags)

    def remover_nota(self, id: int) -> None:
        """'Arranca a folha' do caderno"""
        nota = self.__buscar_nota_pelo_id(id)
        self.__notas.remove(nota)

    def formatar_notas(self) -> list[str]:
        """
        Cria e retorna uma lista com as notas formatadas para serem exibidas
        """
        notas = []
        for nota in self.__notas:
            notas.append(nota.formatar())
        return notas
