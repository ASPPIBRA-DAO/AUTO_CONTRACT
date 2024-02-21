import json


def load_json(json_path: str) -> dict:
    """Lê os dados do arquivo json e retorna ele em dict.

        Args:
            json_path: Caminho do arquivo.

        Returns:
            Json dict.
        """

    with open(json_path, 'r', encoding="utf-8") as json_file:
        # Load the JSON data from the file
        data = json.load(json_file)

    return data
