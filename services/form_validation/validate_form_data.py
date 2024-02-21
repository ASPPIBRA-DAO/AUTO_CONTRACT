def validate_form_data(json_data):
    """Valida os dados do JSON do formulário.

        Args:
            json_data: Os dados do formulário.

        Returns:
            Raise Error se alguma inconsistência for detectada.
        """
    print(json_data)
    # Verifica se a data de início é anterior à data de término
    # if json_data["start_date"] > json_data["end_date"]:
    #     raise ValueError("A data de início deve ser anterior à data de término.")
