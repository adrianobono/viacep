ViaCEP Python Client

Um cliente Python para a API ViaCEP com CLI e interface programática.

A Python client for the ViaCEP API with CLI and programmatic interface.

# Usando Poetry (recomendado) / Using Poetry (recommended)
poetry add viacep

# Ou com pip / Or with pip
pip install viacep

# Consultar um CEP / Query a postal code
viacep search 01001000

# Formato alternativo / Alternative format
python -m viacep search 01001000


from viacep import ViaCEPService

try:
    endereco = ViaCEPService.lookup_cep("01001000")
    print(f"Rua: {endereco.street}")
    print(f"Cidade: {endereco.city}/{endereco.state}")
except Exception as e:
    print(f"Erro: {e}")


# Clonar repositório / Clone repository
git clone https://github.com/adrianobono/viacep.git
cd viacep

# Instalar dependências / Install dependencies
poetry install

# Ativar ambiente virtual / Activate virtual environment
poetry shell


# Todos os testes com cobertura / All tests with coverage
pytest --cov=viacep --cov-report=term-missing

# Apenas testes unitários / Only unit tests
pytest tests/test_viacep.py

# Testes de integração / Integration tests
pytest tests/test_integration.py -m integration

viacep/
├── src/
│   └── viacep/          # Código fonte / Source code
│       ├── __init__.py
│       ├── cli.py       # Interface de linha de comando / CLI interface
│       ├── exceptions.py
│       ├── models.py    # Modelos de dados / Data models
│       └── services.py  # Lógica de negócio / Business logic
├── tests/               # Testes automatizados / Automated tests
├── pyproject.toml       # Configuração do Poetry / Poetry configuration
└── README.md