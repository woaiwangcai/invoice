from __future__ import annotations

from decimal import Decimal, ROUND_HALF_UP

MoneyCents = int


def yuan_to_cents(value: str | int | float | Decimal) -> MoneyCents:
    amount = Decimal(str(value or "0")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return int((amount * 100).to_integral_value(rounding=ROUND_HALF_UP))


def cents_to_yuan(cents: MoneyCents) -> float:
    return cents / 100.0


def format_yuan(cents: MoneyCents) -> str:
    return f"{cents / 100.0:.2f}"
