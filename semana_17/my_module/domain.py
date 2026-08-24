from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Category:
    name: str
    color_hex: str | None = None


@dataclass
class Movement:
    date: str          # "YYYY-MM-DD"
    title: str
    amount: float      # income positive, expense stored as negative
    category: str
    type: str          # "Income" or "Expense"
