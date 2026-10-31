"""Money helpers."""
from decimal import Decimal, ROUND_HALF_UP


def round_money(value: float) -> float:
    """Round an amount to the cent using half-up rounding."""
    return float(Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def format_money(value: float, currency: str = "EUR") -> str:
    return f"{round_money(value):,.2f} {currency}"
