import weasyprint
from jinja2 import Template


def generate_pdf(contract: dict, template_html: str, base_url: str, stylesheets_path: str) -> bytes:
    """Gera um arquivo PDF a partir do layout HTML e CSS do documento.

    Args:
        contract: O contrato preenchido com os dados JSON.
        :param base_url:
        :param template_html:
        :param contract:
        :param stylesheets_path:

    Returns:
        O arquivo PDF gerado.
    """

    # Read the content of the HTML file
    with open(template_html, "r") as f:
        template = Template(f.read())

    # Render the content of the HTML file using the Jinja2 library, replacing values with contract information
    html = template.render(document=contract['document'],
                           owners=contract['owners'],
                           area_description=contract['area_description'],
                           professionals=contract['professionals'],
                           topography_plans=contract['topography_plans'],
                           house_plans=contract['house_plans'],
                           photo_report=contract['photo_report'],
                           construction_licensing=contract['construction_licensing'],
                           city_hall=contract['city_hall'],
                           registry_office=contract['registry_office'],
                           onus_reais=contract['onus_reais'],
                           notarial_minutes=contract['notarial_minutes'],
                           judicial_note=contract['judicial_note'], )

    # Create a WeasyPrint document with the rendered HTML and the CSS file
    document = weasyprint.HTML(string=html, encoding="utf-8", base_url=base_url).render(stylesheets=[stylesheets_path])

    # Return the rendered PDF document
    return document.write_pdf()
