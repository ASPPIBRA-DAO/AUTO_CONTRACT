def convert_form_input_to_json(form_data):
    """Converte os dados do formulário em um objeto JSON.

    Args:
        form_data: Os dados do formulário.

    Returns:
        Um objeto JSON.
    """

    json_data = {
        "name": form_data["name"],
        "email": form_data["email"],
        "phone": form_data["phone"],
        "association": form_data["association"],
    }

    return json_data
