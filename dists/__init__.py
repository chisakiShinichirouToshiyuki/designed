# ###############################################
# 自作moduleをimportするための設定
import sys
import os

# スクリプトの現在のディレクトリを取得
current_dir = os.path.dirname(os.path.abspath(__file__))
# プロジェクトのルートディレクトリへのパスを取得
project_root = os.path.dirname(current_dir)
# Pythonの検索パスにプロジェクトのルートディレクトリを追加
sys.path.insert(0, project_root)
# ###############################################