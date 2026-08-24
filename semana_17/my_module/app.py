import FreeSimpleGUI as sg
from tkinter import colorchooser

from my_module.logic import FinanceManager
from my_module.gui_windows import (
    make_main_window,
    make_add_category_window,
    make_add_movement_window,
    popup_error,
)


def _get_category_names(fm: FinanceManager) -> list[str]:
    return [c.name for c in fm.categories]


def _update_totals(window, fm: FinanceManager) -> None:
    window["-INCOME-"].update(f"Income: {fm.total_income()}")
    window["-EXPENSE-"].update(f"Expense: {fm.total_expense()}")
    window["-BALANCE-"].update(f"Balance: {fm.total_balance()}")


def format_date_digits(s: str) -> str:
    digits = "".join(ch for ch in s if ch.isdigit())[:8]

    if len(digits) <= 4:
        return digits
    if len(digits) <= 6:
        return f"{digits[:4]}-{digits[4:]}"
    return f"{digits[:4]}-{digits[4:6]}-{digits[6:]}"


def main():
    fm = FinanceManager(load_from_disk=True)

    window = make_main_window(fm.table_rows(), _get_category_names(fm))
    _update_totals(window, fm)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Exit"):
            break

        if event == "Add Category":
            cat_win = make_add_category_window()

            while True:
                ev, val = cat_win.read()

                if ev in (sg.WIN_CLOSED, "Cancel"):
                    cat_win.close()
                    break

                if ev == "-PICK_COLOR-":
                    rgb, hex_color = colorchooser.askcolor()
                    if hex_color:
                        cat_win["-COLOR-"].update(hex_color)
                        cat_win["-COLOR_PREVIEW-"].update(background_color=hex_color)
                    continue

                if ev == "-COLOR-":
                    color = val.get("-COLOR-", "").strip()
                    if color.startswith("#") and len(color) == 7:
                        try:
                            cat_win["-COLOR_PREVIEW-"].update(background_color=color)
                        except Exception:
                            pass
                    continue

                if ev == "Save":
                    try:
                        fm.add_category(
                            val.get("-NAME-", ""),
                            val.get("-COLOR-", "") or None,
                        )
                        window["-TABLE-"].update(values=fm.table_rows())
                        _update_totals(window, fm)
                        cat_win.close()
                        break
                    except ValueError as e:
                        popup_error(str(e))

        if event in ("Add Expense", "Add Income"):
            if not fm.categories:
                popup_error("You must create at least 1 category first.")
                continue

            move_type = "Expense" if event == "Add Expense" else "Income"
            mv_win = make_add_movement_window(move_type, _get_category_names(fm))

            while True:
                ev, val = mv_win.read()

                if ev in (sg.WIN_CLOSED, "Cancel"):
                    mv_win.close()
                    break

                if ev == "-DATE-":
                    mv_win["-DATE-"].update(format_date_digits(val.get("-DATE-", "")))
                    continue

                if ev == "Save":
                    try:
                        amount = float(val.get("-AMOUNT-", "0"))

                        fm.add_movement(
                            val.get("-DATE-", ""),
                            val.get("-TITLE-", ""),
                            amount,
                            val.get("-CATEGORY-", ""),
                            move_type,
                        )

                        window["-TABLE-"].update(values=fm.table_rows())
                        _update_totals(window, fm)
                        mv_win.close()
                        break

                    except ValueError as e:
                        popup_error(str(e))
                    except Exception as e:
                        popup_error(f"Unexpected error: {e}")

    window.close()


if __name__ == "__main__":
    main()