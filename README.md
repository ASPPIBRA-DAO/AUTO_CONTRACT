# SELF_CONTRACT 📝

## Contract generation automation 🤖

This project implements an automated system for generating contracts. The system works as follows:

- 📄 The user fills out an HTML form with the contract information.
- 💾 Form data is saved in JSON format in a database.
- ✅ Database information is validated.
- 📋 The contract template is populated with validated information from the database.
- 🖨️ The contract print layout is displayed to the user.
- 📥 The user can click a button to generate a PDF of the contract.

### Project Structure 🏗️

```plaintext
/automation-contract
├── code
│   ├── contracts
│   │   ├── associate
│   │   │   └── associated.html
│   │   │   └── associated.css
│   │   ├── car_sale
│   │   │   └── sale_car.html
│   │   │   └── sale_car.css
│   │   ├── house_sale
│   │   │   └── sale_casa.html
│   │   │   └── sale_casa.css
│   │   └── land_sale
│   │       └── sale_land.html
│   │       └── sale_land.css
│   ├── forms
│   │   └── contract_form.py
│   └── services
│       ├── form_validation
│       │   └── convert_form_input_to_json.py
│       ├── fill_contract_template_with_json.py
│       ├── generate_pdf.py
│       └── show_contract.py
├── docs
│   ├── README.md
│   └── code_of_conduct.md
├── tests
│   ├── test_contract_form.py
│   └── test_contract_generation.py
└── assets
    ├── images
    │   ├── associated.jpg
    │   ├── sale_carro.png
    │   └── sale_casa.pdf
