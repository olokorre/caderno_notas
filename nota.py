from datetime import datetime


class Nota:

    __id: int
    __memo: str
    __tags: list[str]
    __data_criacao: datetime

    def __init__(
        self,
        id: int,
        memo: str,
        tags: list[str] = [],
        data_criacao: datetime = datetime.now(),
    ) -> None:
        self.__id = id
        self.__data_criacao = data_criacao
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
        data = self.__data_criacao.strftime("%d/%m/%Y %H:%M:%S")
        return (
            f"{self.__id}. \"{self.__memo}\" ({', '.join(self.__tags)}) "
            + f"Escrita em: {data}"
        )

    def gerar_dicionario(self) -> dict:
        return {
            "id": self.__id,
            "memo": self.__memo,
            "tags": self.__tags.copy(),
            "data_criacao": self.__data_criacao.isoformat(),
        }
