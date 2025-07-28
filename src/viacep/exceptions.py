class CEPLookupError(Exception):
    """Base exception for CEP lookup errors"""


class InvalidCEPError(CEPLookupError):
    """Raised when an invalid CEP format is provided"""


class CEPNotFoundError(CEPLookupError):
    """Raised when the CEP is not found in ViaCEP"""


class ViaCEPUnavailableError(CEPLookupError):
    """Raised when ViaCEP service is unavailable"""