from services.form_validation.validate_form_data import validate_form_data
from services.generate_pdf import generate_pdf
from services.load_json import load_json
from services.save_document import save_document


# Função principal
def main():
    # Carregamento das informações do arquivo .json
    data = load_json(json_path='data/escritura.json')

    # Validação das informações do contrato
    validate_form_data(json_data=data)

    # Geração do documento PDF
    document = generate_pdf(contract=data, template_html='report/report.html',
                            base_url='report/', stylesheets_path='report/report.css')

    # Salvamento do documento PDF
    gerou = save_document(documento_bytes=document)

    # Tratamento Genérico (Alterar para requisitos do APP depois)
    if gerou:
        print('Documento gerado com sucesso!')
    else:
        print('Erro na geração do documento.')


if __name__ == "__main__":
    main()
