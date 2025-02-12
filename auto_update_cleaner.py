import os
import subprocess
import time
from pathlib import Path

# Настройки
GITHUB_REPO = "https://github.com/AlladinWork/PC-Cleaner.git"  # Укажи свой репозиторий
LOCAL_DIR = Path.home() / "PC-Cleaner"
UPDATE_INTERVAL = 3600  # Проверять обновления раз в час

def update_script():
    """Обновляет код из GitHub и запускает очистку"""
    if not LOCAL_DIR.exists():
        print("[+] Клонирую репозиторий...")
        subprocess.run(["git", "clone", GITHUB_REPO, str(LOCAL_DIR)], check=True)
    else:
        print("[+] Обновляю код...")
        subprocess.run(["git", "-C", str(LOCAL_DIR), "pull"], check=True)

    print("[+] Запускаю очистку...")
    subprocess.run(["python", str(LOCAL_DIR / "cleaner.py")])

while True:
    update_script()
    print(f"[✔] Следующее обновление через {UPDATE_INTERVAL} секунд")
    time.sleep(UPDATE_INTERVAL)
