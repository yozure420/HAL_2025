import time
import sys

def check_environment():
    print(f"実行環境: {sys.stdout}")
    print(f"ターミナル: {sys.stdout.isatty()}")
    # PyCharm, VS Code, Jupyter などでは
    # バッファリングの動作が異なる場合がある
check_environment()
#sys.stdoutってなんやねん
