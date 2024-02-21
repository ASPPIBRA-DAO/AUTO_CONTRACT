

def fill_contract_template_with_json(
    template_path: str, json_data: dict
) -> str:
    """Preenche o modelo de contrato HTML e CSS usando os dados JSON.

    Args:
        template_path: O caminho para o modelo de contrato.
        json_data: Os dados JSON.

    Returns:
        O contrato preenchido com os dados JSON.
    """

    # Carregar o modelo de contrato

    with open(template_path, "r") as f:
        template = f.read()

    # Preencher o modelo com os dados JSON

    template = template.format(**json_data)

    return template
