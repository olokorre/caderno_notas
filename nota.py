from datetime import datetime


class Nota:

    __id: int
    __memo: str
    __tags: list[str]
    __data_criacao: datetime

    def __init__(self, id: int, memo: str, tags: list[str] = []) -> None:
        self.__id = id
        self.__data_criacao = datetime.now()
        self.__memo = memo
        self.__tags = tags

    @property
    def id(self) -> int:
        return self.__id

    @property
    def memo(self) -> str:
        return self.__memo

    @property
    def tags(self) -> list[str]:
        return self.__tags

    @property
    def data_criacao(self) -> datetime:
        return self.__data_criacao

    def corresponde(self, filtro: str) -> bool:
        return filtro.upper() in self.__memo.upper()

    def modificar_memo(self, memo: str) -> None:
        self.__memo = memo

    def modificar_tags(self, tags: list[str]) -> None:
        self.__tags = tags

    def formatar(self) -> str:
        return (
            f"{self.__id}. \"{self.__memo}\" ({', '.join(self.__tags)})"
            + f"Data: {self.__data_criacao.isoformat()}"
        )
