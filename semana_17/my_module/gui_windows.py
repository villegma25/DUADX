import FreeSimpleGUI as sg


def popup_error(message: str):
    sg.popup("Error", message, title="Error", keep_on_top=True)


def make_main_window(table_data, categories):
    headings = ["Date", "Title", "Amount", "Category", "Type"]

    layout = [
        [sg.Text("Personal Finance Manager")],
        [
            sg.Text("Income: 0", key="-INCOME-"),
            sg.Text("Expense: 0", key="-EXPENSE-"),
            sg.Text("Balance: 0", key="-BALANCE-"),
        ],
        [
            sg.Table(
                values=table_data,
                headings=headings,
                auto_size_columns=True,
                justification="left",
                num_rows=12,
                key="-TABLE-",
                expand_x=True,
                expand_y=True,
            )
        ],
        [
            sg.Button("Add Category"),
            sg.Button("Add Expense"),
            sg.Button("Add Income"),
        ],
        [sg.Button("Exit")],
    ]

    return sg.Window("Finance Manager", layout, resizable=True, finalize=True, size=(900, 500))


def make_add_category_window() -> sg.Window:
    layout = [
        [sg.Text("Category name:"), sg.Input(key="-NAME-")],
        [
            sg.Text("Color hex (optional):"),
            sg.Input(key="-COLOR-", enable_events=True),
            sg.Button("Pick Color", key="-PICK_COLOR-"),
        ],
        [
            sg.Text("Preview:"),
            sg.Text("      ", key="-COLOR_PREVIEW-", background_color="white", relief="solid")
        ],
        [sg.Button("Save"), sg.Button("Cancel")],
    ]
    return sg.Window("Add Category", layout, modal=True, finalize=True, keep_on_top=True)


def make_add_movement_window(move_type: str, category_names):
    layout = [
        [sg.Text(f"Add {move_type}")],
        [sg.Text("Date (YYYY-MM-DD):"), sg.Input(key="-DATE-", enable_events=True)],
        [sg.Text("Title:"), sg.Input(key="-TITLE-")],
        [sg.Text("Amount:"), sg.Input(key="-AMOUNT-")],
        [sg.Text("Category:"), sg.Combo(category_names, key="-CATEGORY-", readonly=True)],
        [sg.Button("Save"), sg.Button("Cancel")],
    ]
    return sg.Window(f"Add {move_type}", layout, modal=True, finalize=True)
