"""CSV export of invoice lines."""
from __future__ import annotations

import csv
import io

from .money import round_money


def lines_to_csv(invoice: dict) -> str:
    out = io.StringIO()
    writer = csv.writer(out, lineterminator="\n")
    writer.writerow(["sku", "description", "qty", "unit_price", "line_total"])
    for line in invoice["lines"]:
        total = round_money(line["qty"] * line["unit_price"])
        writer.writerow([line["sku"], line["description"], line["qty"],
                         f"{round_money(line['unit_price']):.2f}", f"{total:.2f}"])
    return out.getvalue()
