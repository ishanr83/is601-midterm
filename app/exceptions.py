class CalculatorError(Exception):
    """Base class for calculator exceptions."""
    pass

class OperationError(CalculatorError):
    """Raised when an operation fails or is invalid."""
    pass

class ValidationError(CalculatorError):
    """Raised when user input fails validation."""
    pass
