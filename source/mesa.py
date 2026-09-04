from datetime import datetime
from json import dumps, loads
from os.path import exists


from source.caderno import Caderno
from source.nota import Nota


class Mesa:
    """Classe que representa a mesa"""

    def pegarCaderno(self) -> Caderno:
        """Procurra e carrega os dados do caderno do arquivo json local"""
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
        """Salva os dados do caderno em um arquivo json no diretório atual"""
        notas = []
        for nota in caderno.notas:
            notas.append(nota.gerar_dicionario())
        with open(".caderno.json", "w") as c:
            c.write(dumps(notas))
