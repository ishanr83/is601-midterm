from .exceptions import ValidationError

def ensure_number(x, name="value"):
    try:
        return float(x)
    except (TypeError, ValueError):
        raise ValidationError(f"{name} must be a number.")

def ensure_within_bounds(x, max_abs: float, name="value"):
    if abs(x) > max_abs:
        raise ValidationError(f"{name} magnitude exceeds allowed maximum ({max_abs}).")
    return x

def ensure_two_numbers(a, b, max_abs):
    a = ensure_within_bounds(ensure_number(a, "a"), max_abs, "a")
    b = ensure_within_bounds(ensure_number(b, "b"), max_abs, "b")
    return a, b
