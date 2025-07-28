import pytest
from unittest.mock import patch
import requests

@pytest.fixture
def mock_successful_cep_lookup():
    with patch("viacep.services.requests.get") as mock_get:  # Updated path
        mock_get.return_value.json.return_value = {
            "cep": "01001-000",
            "logradouro": "Praça da Sé",
            "complemento": "lado ímpar",
            "bairro": "Sé",
            "localidade": "São Paulo",
            "uf": "SP",
            "ibge": "3550308",
            "gia": "1004",
            "ddd": "11",
            "siafi": "7107"
        }
        mock_get.return_value.status_code = 200
        yield mock_get

@pytest.fixture
def mock_cep_not_found():
    with patch("viacep.services.requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"erro": True}
        mock_get.return_value.status_code = 200
        yield mock_get

@pytest.fixture
def mock_viacep_unavailable():
    with patch("viacep.services.requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.RequestException("Service unavailable")
        yield mock_get