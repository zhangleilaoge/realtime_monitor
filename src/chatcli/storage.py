import json
from pathlib import Path
from .config import SYSTEM_PROMPT, HISTORY_FILE   # ← 把 SYSTEM_PROMPT 也拿进来

def load_history() -> list:
    if Path(HISTORY_FILE).exists():
        return json.loads(Path(HISTORY_FILE).read_text(encoding="utf8"))
    return [{"role": "system", "content": SYSTEM_PROMPT}]

def save_history(messages: list):
    Path(HISTORY_FILE).write_text(json.dumps(messages, ensure_ascii=False, indent=2),
                                  encoding="utf8")