from __future__ import annotations

from .domain import Category, Movement
from .persistence import (
    load_categories,
    load_movements,
    save_categories,
    save_movements,
)


class FinanceManager:
    def __init__(self, load_from_disk: bool = True):
        if load_from_disk:
            self.categories = load_categories()
            self.movements = load_movements()
        else:
            self.categories = []
            self.movements = []

    def add_category(self, name: str, color_hex: str | None = None):
        if not name or not name.strip():
            raise ValueError("Category name cannot be empty")

        name = name.strip()

        if any(c.name == name for c in self.categories):
            raise ValueError("Category already exists")

        self.categories.append(Category(name, color_hex))
        self._autosave()

    def add_movement(self, date: str, title: str, amount: float, category: str, movement_type: str):
        if not self.categories:
            raise ValueError("No categories available")

        if category not in [c.name for c in self.categories]:
            raise ValueError("Category does not exist")

        if amount <= 0:
            raise ValueError("Amount must be positive")

        if movement_type == "Expense":
            amount = -amount
        elif movement_type != "Income":
            raise ValueError("Invalid movement type")

        self.movements.append(Movement(date, title, float(amount), category, movement_type))
        self._autosave()

    def table_rows(self):
        return [[m.date, m.title, m.amount, m.category, m.type] for m in self.movements]

    def total_income(self) -> float:
        return sum(m.amount for m in self.movements if m.type == "Income")

    def total_expense(self) -> float:
        # expenses stored negative, return positive total expense
        return sum(-m.amount for m in self.movements if m.type == "Expense")

    def total_balance(self) -> float:
        return sum(m.amount for m in self.movements)

    def _autosave(self):
        save_categories(self.categories)
        save_movements(self.movements)
