from jinja2 import Template


def show_contract(contract: str):
    """Mostra o layout HTML e CSS do documento preenchido com os dados validados do arquivo JSON.

    Args:
        contract: O contrato preenchido com os dados JSON.
    """

    # Renderizar o HTML

    html = Template(contract).render()

    # Imprimir o HTML

    print(html)
