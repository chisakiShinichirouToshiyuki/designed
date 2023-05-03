# designED
大学入試数学を、プログラミングを用いて学習するpythonモジュールです。
 
# デモ
[使用例](https://colab.research.google.com/github/chisakiShinichirouToshiyuki/designed/blob/main/dist/colab/jp/template.ipynb) (実行にはGoogle Accountが必要)  
（Colabの基本的な使い方は、[こちら](https://blog.kikagaku.co.jp/google-colab-howto#2))

 
# 機能(随時追加中)
- 数式処理機能
  - オブジェクト指向設計による公式・定理の整理
  - 四則演算
  - 微積分
  - 方程式の因数分解
  - 方程式、不等式のグラフ化
  - 倍数の証明
  - ユークリッドの互除法
  - 整数不定方程式を解く
- 証明支援
  - 入力補完（by typehint）
  - 型エラーチェック（by typehint + Pylance）
  - hoverによる関数説明（by docstring）


# designEDを動かすための前提要件  

- VSCodeで動かす場合
  - [VSCode](https://code.visualstudio.com/download) (上記証明支援をしてくれる、便利なコードエディタ)
  - python 3.9+実行環境  
  - [git](https://git-scm.com/book/ja/v2/使い始める-Gitのインストール)（推奨）  
  - VSCode拡張機能(推奨)  
    - [Japanese Language Pack for VS Code](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-ja)
    - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
    - [Python Type Hint](https://marketplace.visualstudio.com/items?itemName=njqdev.vscode-python-typehint)
    - [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
    - [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
    - [Jupyter Cell Tags support in VS Code](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.vscode-jupyter-cell-tags)
    - [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
 
- Colabで動かす場合

  -  Googleアカウント
 
# インストール方法（VSCode）  
  
- gitをインストールしている場合
 
```bash
git clone https://github.com/chisakiShinichirouToshiyuki/designed.git
cd designed
pip install sympy==1.11.1 jedi>=0.16 setuptools>65.5.1 spb==0.1.1 seaborn==0.12.2 japanize_matplotlib==1.1.3 colorama==0.4.6
```

- gitをインストールしていない場合
[github](https://github.com/chisakiShinichirouToshiyuki/designed)にアクセスし、<span style="color:white;background-color:green;border-radius:4px;">&nbsp;<> Code ▼&nbsp;</span> => <span style="color:white;background-color:grey;border-radius:4px;">&nbsp;Download Zip&nbsp;</span>より、ダウンロードする。
```bash
 # ダウンロードしたフォルダ化に移動して
pip install sympy==1.11.1 jedi>=0.16 setuptools>65.5.1 spb==0.1.1 seaborn==0.12.2 japanize_matplotlib==1.1.3 colorama==0.4.6
```
# 使用方法（VSCode）
実行環境(OS/pythonバージョン)に合わせて、下記ディレクトリのnotebookファイルを実行。  
モジュールの詳しい使い方は、APIドキュメントを参照

./dist/_OS_/_pythonバージョン_/_言語_/template.ipynb
# 使用方法（Colab）
[コードサンプル](https://colab.research.google.com/github/chisakiShinichirouToshiyuki/designed/blob/main/dist/colab/jp/template.ipynb) (実行にはGoogle Accountが必要)にアクセス  
（Colabの基本的な使い方は、[こちら](https://blog.kikagaku.co.jp/google-colab-howto#2))

# 外部リンク  
|リンク|内容|
|:-|:-|  
|[APIドキュメント]()|designEDモジュールの説明書|  
|[designED](https://github.com/chisakiShinichirouToshiyuki/designed.git)|モジュールのクローン元|  
|[デモ](https://colab.research.google.com/github/chisakiShinichirouToshiyuki/designed/blob/main/dist/colab/jp/template.ipynb)|面倒な環境構築不要のデモリンク先|  
|[VSCode](https://code.visualstudio.com/download)|VSCodeのダウンロード元|  


# 注意点
 
- windows未対応
- python3.11+未対応
 
# 作者
 
 
* 知崎心一郎敏幸
* mail: designed.academy@gmail.com
 
# ライセンス
著作権所有者： [知崎心一郎敏幸](https://github.com/chisakiShinichirouToshiyuki)

このモジュール（以下「本モジュール」）は、以下の条件に基づいて提供されます。  

1. 本モジュールの再配布は禁止されます。ただし、エンドユーザーが個別にpip installする場合は、この限りではありません。

2. 商用利用は禁止されます。

3. 本モジュールに基づいて派生物を作成する場合には、派生物がこのライセンスの下で提供されること、および派生物に関するすべての著作権、特許権、商標権、およびその他の知的財産権が本モジュールの著作権所有者に帰属することに同意する必要があります。

4. 本モジュールの使用は「AS IS」（現状有姿）で提供され、著作権者は、本モジュールに関連して生じた一切の責任を負いません。

5. 本ライセンスは、本モジュールの使用、複製、および再配布に対するライセンスを提供するものであり、本モジュールに関する特許権、商標権、および著作権に対するライセンスを提供するものではありません。

6. このライセンスは、日本法に準拠し、日本語および英語の両方のバージョンがある場合、日本語版が優先されるものとします。

7. 本モジュールを使用することにより、このライセンスに同意したものとみなされます。