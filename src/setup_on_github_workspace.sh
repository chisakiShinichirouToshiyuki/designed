#!/bin/bash

# 現在のPythonのバージョンを取得
CURRENT_VERSION=$(python --version 2>&1 | awk '{print $2}')

# バージョンが3.9から3.11以外か確認
if [[ "$CURRENT_VERSION" != 3.9* && "$CURRENT_VERSION" != 3.10* && "$CURRENT_VERSION" != 3.11* ]]; then
    echo "Current Python version is $CURRENT_VERSION. Proceeding with installation..."

    # Pyenvのインストール
    curl https://pyenv.run | bash

    # .bashrc または .bash_profile に設定を追加
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc
    echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

    # 環境を再読み込み
    source ~/.bashrc

    # Python 3.11をインストール
    pyenv install 3.11

    # インストールされたPythonのバージョンを確認
    INSTALLED_VERSION=$(python --version 2>&1 | awk '{print $2}')

    # インストールが成功したか確認
    if [[ "$INSTALLED_VERSION" == 3.11.* ]]; then
        echo "success"
    else
        echo "error: Python installation failed. Installed version is $INSTALLED_VERSION"
    fi
else
    echo "Current Python version is compatible: $CURRENT_VERSION. No action required."
fi