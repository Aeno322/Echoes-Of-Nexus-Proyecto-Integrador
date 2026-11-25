
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

if __name__ == "__main__":
    subprocess.Popen([sys.executable, str(BASE_DIR / "main.py")], cwd=str(BASE_DIR))
