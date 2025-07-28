import requests
from typing import Optional

from .models import Address
from .exceptions import (
    InvalidCEPError,
    CEPNotFoundError,
    ViaCEPUnavailableError,
)


class ViaCEPService:
    BASE_URL = "https://viacep.com.br/ws"

    @classmethod
    def _clean_cep(cls, cep: str) -> str:
        """Remove any non-digit characters from CEP"""
        return "".join(filter(str.isdigit, cep))

    @classmethod
    def _validate_cep(cls, cep: str) -> None:
        """Validate CEP format (8 digits)"""
        cleaned_cep = cls._clean_cep(cep)
        if len(cleaned_cep) != 8 or not cleaned_cep.isdigit():
            raise InvalidCEPError("CEP must contain exactly 8 digits")

    @classmethod
    def lookup_cep(cls, cep: str) -> Address:
        """Lookup address information for a given CEP"""
        try:
            cls._validate_cep(cep)
            cleaned_cep = cls._clean_cep(cep)
            
            response = requests.get(f"{cls.BASE_URL}/{cleaned_cep}/json/", timeout=5)
            response.raise_for_status()
            
            data = response.json()
            
            if "erro" in data:
                raise CEPNotFoundError(f"CEP {cleaned_cep} not found")
                
            return Address(
                cep=data.get("cep", ""),
                street=data.get("logradouro"),
                complement=data.get("complemento"),
                neighborhood=data.get("bairro"),
                city=data.get("localidade"),
                state=data.get("uf"),
                ibge=data.get("ibge"),
                gia=data.get("gia"),
                ddd=data.get("ddd"),
                siafi=data.get("siafi"),
            )
            
        except requests.exceptions.RequestException as e:
            raise ViaCEPUnavailableError(f"ViaCEP service unavailable: {str(e)}")