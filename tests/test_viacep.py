import pytest
from viacep.services import ViaCEPService
from viacep.exceptions import InvalidCEPError, CEPNotFoundError, ViaCEPUnavailableError
from viacep.models import Address

class TestViaCEPService:
    def test_clean_cep(self):
        assert ViaCEPService._clean_cep("12345-678") == "12345678"
        assert ViaCEPService._clean_cep("12.345-678") == "12345678"
        assert ViaCEPService._clean_cep("12345678") == "12345678"

    def test_validate_cep_valid(self):
        ViaCEPService._validate_cep("12345678")
        ViaCEPService._validate_cep("12345-678")

    def test_validate_cep_invalid(self):
        with pytest.raises(InvalidCEPError):
            ViaCEPService._validate_cep("1234567")
        with pytest.raises(InvalidCEPError):
            ViaCEPService._validate_cep("123456789")
        with pytest.raises(InvalidCEPError):
            ViaCEPService._validate_cep("1234a678")

    def test_lookup_cep_success(self, mock_successful_cep_lookup):
        address = ViaCEPService.lookup_cep("01001-000")
        assert isinstance(address, Address)
        assert address.cep == "01001-000"
        assert address.street == "Praça da Sé"
        assert address.city == "São Paulo"
        assert address.state == "SP"

    def test_lookup_cep_not_found(self, mock_cep_not_found):
        with pytest.raises(CEPNotFoundError):
            ViaCEPService.lookup_cep("00000-000")

    def test_lookup_cep_service_unavailable(self, mock_viacep_unavailable):
        with pytest.raises(ViaCEPUnavailableError):
            ViaCEPService.lookup_cep("01001-000")