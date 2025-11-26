# realtime-monitor

用 Python + uv 做的极简“CPU / GPU 占用率”实时看板。

## 1. 效果

终端里每秒刷新一行：
CPU: 12.3% | MEM: 45.2% | GPU: 34.0%
按 `Ctrl+C` 退出。

## 2. 一键运行（推荐）

```bash

# ① 安装 uv（仅需一次）
curl -LsSf https://astral.sh/uv/install.sh | sh   # Windows 用 install.ps1

# ② 直接跑（uv 会自动建虚拟环境、装依赖）
uv run python main.py

```
