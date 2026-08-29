from nota import Nota


class Caderno:

    __notas: list[Nota]

    def __init__(self) -> None:
        self.__notas = []

    @property
    def quantidade_notas(self) -> int:
        return len(self.__notas)

    def __proxima_nota(self) -> int:
        return len(self.__notas) + 1

    def __buscar_nota_pelo_id(self, id: int) -> Nota:
        for nota in self.__notas:
            if nota.id == id:
                return nota
        raise Exception(f"Nota não encontrada para id {id}")

    def nova_nota(self, memo: str, tags: list[str] = []) -> None:
        id = self.__proxima_nota()
        nota = Nota(id, memo, tags)
        self.__notas.append(nota)

    def pesquisar(self, filtro: str) -> list[Nota]:
        notas = []
        for nota in self.__notas:
            if not nota.corresponde(filtro):
                continue
            notas.append(nota)
        return notas

    def modificar_memo(self, id: int, memo: str) -> None:
        nota = self.__buscar_nota_pelo_id(id)
        nota.modificar_memo(memo)

    def modificar_tags(self, id: int, tags: list[str]) -> None:
        nota = self.__buscar_nota_pelo_id(id)
        nota.modificar_tags(tags)

    def formatar_notas(self) -> list[str]:
        notas = []
        for nota in self.__notas:
            notas.append(nota.formatar())
        return notas
