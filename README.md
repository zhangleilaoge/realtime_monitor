## 1. 一键运行（推荐）

```bash

# 1. 前置在根目录准备好 .env 文件
OPENAI_API_KEY=sk-xxxxxxx
OPENAI_BASE_URL=https://xxxxxxx

# 2. 安装 uv（仅需一次）
curl -LsSf https://astral.sh/uv/install.sh | sh   # Windows 用 install.ps1

# 3. 注册命令
uv pip install -e .

# 4. 执行命令
uv run python ./main.py

# 5. 打包
uv run pyinstaller --onefile --name chatcli main.py


```
