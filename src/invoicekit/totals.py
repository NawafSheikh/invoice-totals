"""Invoice totals: net, discount, VAT, gross."""
from __future__ import annotations

from dataclasses import dataclass

from .money import round_money


@dataclass(frozen=True)
class InvoiceTotals:
    net: float
    discount: float
    vat: float
    gross: float


def line_net(line: dict) -> float:
    return round_money(line["qty"] * line["unit_price"])


def compute_totals(invoice: dict) -> InvoiceTotals:
    net = round_money(sum(line_net(line) for line in invoice["lines"]))
    rate = invoice.get("vat_rate", 0.0)
    discount = round_money(net * invoice.get("discount_pct", 0.0))
    vat = round_money((net - discount) * rate)
    gross = round_money(net - discount + vat)
    return InvoiceTotals(net=net, discount=discount, vat=vat, gross=gross)
