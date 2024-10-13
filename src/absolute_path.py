import os
import sys

def resource_path(relative_path):
    """特定のリソースの絶対パスを取得するヘルパー関数"""
    try:
        # PyInstallerで実行されている場合
        base_path = sys._MEIPASS
    except Exception:
        # 通常のPythonスクリプトとして実行されている場合
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)