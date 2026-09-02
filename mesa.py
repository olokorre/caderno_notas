from datetime import datetime
from json import dumps, loads

from caderno import Caderno
from os.path import exists

from nota import Nota


class Mesa:

    def pegarCaderno(self) -> Caderno:
        notas = []
        if exists(".caderno.json"):
            with open(".caderno.json", "r") as c:
                data = loads(c.read())
                for item in data:
                    nota = Nota(
                        item.get("id"),
                        item.get("memo"),
                        item.get("tags"),
                        datetime.fromisoformat(item.get("data_criacao")),
                    )
                    notas.append(nota)
        return Caderno(notas)

    def guardarCaderno(self, caderno: Caderno) -> None:
        notas = []
        for nota in caderno.notas:
            notas.append(nota.gerar_dicionario())
        with open(".caderno.json", "w") as c:
            c.write(dumps(notas))
