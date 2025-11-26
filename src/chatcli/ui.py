import sys
from .storage import load_history, save_history
from .client import stream_chat
from prompt_toolkit import prompt   # 替代内置 input

COMMANDS = {"/q", "/quit", "/exit", "/clear"}

def typing_print(text: str, delay=0.02):
    """打字机效果"""
    for ch in text:
        print(ch, end="")
        sys.stdout.flush()
        __import__("time").sleep(delay)
    print()

def cli_loop():
    history = load_history()
    print("💬 多轮对话 CLI（/q 退出，/clear 清屏）")
    while True:
        try:
            user = prompt("\n👤 你：").strip()   # Backspace / 方向键都正常
        except (KeyboardInterrupt, EOFError):
            print("\n👋 再见！")
            break
        if user in COMMANDS:
            if user == "/clear":
                history.clear()
                history.append({"role": "system", "content": load_history()[0]["content"]})
                print("🧹 已清屏并重置对话。")
            else:
                print("👋 再见！")
                break
            continue

        history.append({"role": "user", "content": user})
        print("🤖 ChatGPT：", end="")
        assistant_text = ""
        for piece in stream_chat(history):
            print(piece, end="")
            sys.stdout.flush()
            assistant_text += piece
        print()  # 换行
        history.append({"role": "assistant", "content": assistant_text})
        save_history(history)