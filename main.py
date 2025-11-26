#!/usr/bin/env python3
# main.py
import time
import psutil
try:
    # 通用 GPU（AMD/NVIDIA 都能读）
    from pyadl import ADLManager
    adl = ADLManager.getInstance()
    gpu_enabled = True
except Exception:
    gpu_enabled = False

def main():
    print("实时按 Ctrl+C 停止")
    while True:
        # 1. CPU 占用
        cpu = psutil.cpu_percent(interval=1)   # 阻塞 1s 采样
        # 2. 内存占用
        mem = psutil.virtual_memory().percent
        # 3. GPU 占用
        gpu = "N/A"
        if gpu_enabled:
            try:
                gpu = str(round(adl.getCurrentUsage(), 1)) + "%"
            except Exception:
                gpu = "ERR"

        print(f"CPU: {cpu:5.1f}% | MEM: {mem:5.1f}% | GPU: {gpu}", end="\r")
        time.sleep(0.5)

if __name__ == "__main__":
    main()