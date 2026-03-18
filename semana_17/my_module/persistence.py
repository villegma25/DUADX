import json
from pathlib import Path
from my_module.domain import Category, Movement

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
CATEGORIES_FILE = DATA_DIR / "categories.json"
MOVEMENTS_FILE = DATA_DIR / "movements.json"


def _read_json_list(path: Path) -> list:
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return []
    return json.loads(text)


def _write_json_list(path: Path, data: list) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def load_categories() -> list[Category]:
    raw = _read_json_list(CATEGORIES_FILE)
    return [Category(**item) for item in raw]


def save_categories(categories: list[Category]) -> None:
    raw = [c.__dict__ for c in categories]
    _write_json_list(CATEGORIES_FILE, raw)


def load_movements() -> list[Movement]:
    raw = _read_json_list(MOVEMENTS_FILE)
    return [Movement(**item) for item in raw]


def save_movements(movements: list[Movement]) -> None:
    raw = [m.__dict__ for m in movements]
    _write_json_list(MOVEMENTS_FILE, raw)
