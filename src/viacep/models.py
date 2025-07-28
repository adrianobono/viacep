from dataclasses import dataclass
from typing import Optional


@dataclass
class Address:
    cep: str
    street: Optional[str] = None
    complement: Optional[str] = None
    neighborhood: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    ibge: Optional[str] = None
    gia: Optional[str] = None
    ddd: Optional[str] = None
    siafi: Optional[str] = None

    def __str__(self) -> str:
        return f"{self.street}, {self.neighborhood}, {self.city}/{self.state} - {self.cep}"