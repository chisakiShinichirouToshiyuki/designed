# designED
(English version is [here](#designed_en))

## 目次
- [designED](#designed)
  - [目次](#目次)
  - [designEDってなに？](#designedってなに)
  - [誰のためのアプリ？](#誰のためのアプリ)
    - [あなたのためのアプリです😄！](#あなたのためのアプリです)
  - [何の役に立つの？](#何の役に立つの)
  - [どうやって実現するの？](#どうやって実現するの)
  - [すぐに試せるデモ環境](#すぐに試せるデモ環境)
  - [フル機能使う手順（初歩から）](#フル機能使う手順初歩から)
  - [モジュールインストール方法](#モジュールインストール方法)
  - [機能(随時追加中)](#機能随時追加中)
  - [外部リンク](#外部リンク)
  - [作者](#作者)
  - [ライセンス](#ライセンス)
- [designED\_en](#designed_en)
  - [Table of Contents](#table-of-contents)
  - [what's designED?](#whats-designed)
  - [Who is this app for?](#who-is-this-app-for)
    - [This is an app for you 😄!](#this-is-an-app-for-you-)
  - [What is it useful for?](#what-is-it-useful-for)
  - [What is it for?](#what-is-it-for)
  - [Instantly Tryable Demo Environment](#instantly-tryable-demo-environment)
  - [Prerequisites for running designED](#prerequisites-for-running-designed)
  - [How to Install the Module](#how-to-install-the-module)
  - [Features (Continuously being added)](#features-continuously-being-added)
  - [External Links](#external-links)
  - [Author](#author)
  - [License](#license)



## designEDってなに？  
designEDは、デザインされた(designed)教育(ED)で、学びをアップデートするアプリです。  
より具体的には、<span style="color:#f99;font-weight:bold;">プログラマーの秘密道具を使って、楽して大学に合格しちゃうアプリ</span>です。  
このアプリは、2023/12/06現在、大学受験-数学-整数論の参考書に相当する機能を提供します。
<br>

## 誰のためのアプリ？
### あなたのためのアプリです😄！
- 「<span style="color:#f99;font-weight:bold;">有能な怠け者</span>」のあなた
- 「プログラミングスキルはあるけど、苦労して受験勉強したくない高校生」のあなた
- 「理解力が高い中学生」のあなた
- 「特殊な技能をつけて、高単価なバイトをしたい大学生」のあなた
- 「プログラミングを覚えたい」あなた
- 「子供の受験サポートのために、自分も学びたい親」のあなた
<br>

## 何の役に立つの？
|できます|できません / 興味がありません|
|:---|:---|
|<span style="color:#f99;font-weight:bold;">難関大学に合格するスキル</span>がつきます。|大学以上の高度な数学能力は対象外です。<br>数学的思考力を向上させるを目的としません。|
|<span style="color:#f99;font-weight:bold;">プログラミングのスキル</span>がつきます。<br>pythonモジュール利用のスキルがつきます。|関数型言語は扱いません。<br>依存型は扱いません。|
|受験勉強の工数を削減し、余暇を提供します。||
|プログラマーの秘密道具をたくさん知れます。||
<br>


## どうやって実現するの？
- <span style="color:#f99;font-weight:bold;">受験問題を、日本語プログラミングで解きます</span>！(面倒な微分・積分計算も自動でやってくれます)  
  <img src="https://www.designed.academy/tutorial/proof.gif" alt="Demo : Proof by python" style="border:.5px solid white;margin:8px;max-width:70%;max-height:70%;" >
- プログラミングの便利ツールで、証明作成をサポートします。  
  - よく使う定理や有名問題に名前をつけて、簡単呼び出し（ユーザスニペット）  
    <img src="https://www.designed.academy/tutorial/user_snippet.gif" alt="Demo : User Snippet" style="border:.5px solid white;margin:8px;max-width:70%;max-height:70%;" >
  - <span style="color:#f99;font-weight:bold;">数や型の種類に紐づいて、公式がきれいに整理</span>（公式や定理の入力補完）  
    <img src="https://www.designed.academy/tutorial/implementation.gif" alt="Demo : Implementation" style="border:.5px solid white;margin:8px;max-width:70%;max-height:70%;" >
  - 数や型の種類が誤っている場合、編集中にアラート（公式や定理の型チェック）  
    <img src="https://www.designed.academy/tutorial/type_check.gif" alt="Demo : Type Check" style="border:.5px solid white;margin:8px;max-width:70%;max-height:70%;" >  
  - 公式や定理の説明を簡単に確認  
    <img src="https://www.designed.academy/tutorial/docstring.gif" alt="Demo :Docstring" style="border:.5px solid white;margin:8px;max-width:70%;max-height:70%;" >  
  - レンダリング自動化
  - デバッグモード
  - エラー表示
  - <span style="color:#f99;font-weight:bold;">プログラミング特化版のchatGPT:github copilotでAIの助けを借りながら、ストレスなく証明</span>  
    - 各ステップをAIに指示したり  
    - １題丸ごと解いちゃったり(京都大学類題)  
        <img src="https://www.designed.academy/tutorial/copilot.gif" alt="Demo : Proof by copilot" style="border:.5px solid white;margin:8px;max-width:70%;max-height:70%;" >
  - 間違えたら証明と、正しい証明の差分を、chatGPTがフローチャートでわかりやすく見える化（AIによるコード図表変換）
- プログラマー用SNSで学習進捗を管理/共有  
<br>

## すぐに試せるデモ環境
[こちらデモ環境](https://colab.research.google.com/github/chisakiShinichirouToshiyuki/designed/blob/main/tutorial_jp_on_colab.ipynb)のgoogle colabでは、高度なプログラミング支援機能はありませんが、簡単に動作を確認できます。  
（実行にはGoogle Accountが必要）  
（Colabの基本的な使い方は、[こちら](https://blog.kikagaku.co.jp/google-colab-howto#2)）  
<br>


## フル機能使う手順（初歩から）  
|各インストール|説明|手順|
|:-|:-|:-|
|python実行環境のインストール|designEDを動かすためのプログラミング言語をインストールする|[windows](https://prog-8.com/docs/python-env-win)<br>[Mac](https://prog-8.com/docs/python-env)|
|VScodeのインストール|プログラミングコード専用のエディタ（wordやメモ帳みたいなもの）をインストールする|[外部リンク](https://app.path.progate.com/articles/install-vscode)|
|gitとGitHubのインストール|書いたコードのバージョン管理ツール(git)とそのバージョンの保存先のwebサービス(GitHub)|[windows](https://prog-8.com/docs/git-env-win)<br>[Mac](https://prog-8.com/docs/git-env)|
|GitHub Copilotの申請|プログラミングに特化したchatGPTのようなもの|[申請手順](https://blog.keisatoh.net/posts/2023-04-10-started-using-github-copilot-with-a-student-discount/)|
|VScode 拡張機能のインストール|エディタに便利な追加機能をそれぞれインストールする||

<br>

## モジュールインストール方法  
``` bash
pip install --upgrade designed
```
<br>

## 機能(随時追加中)
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
  - フローチャートリアルタイム生成などの、自作証明の図表化（by chatGPT）
  - AIによる証明提案（by github copilot）
<br>

## 外部リンク  
|リンク|コンテンツ|学校での喩え|
|:-|:-|:-|  
|[APIドキュメント]()|designEDモジュールの説明書|数学公式集|  
|[designED](https://github.com/chisakiShinichirouToshiyuki/designed.git)|モジュールのクローン元|  
|[デモ](https://colab.research.google.com/github/chisakiShinichirouToshiyuki/designed/blob/main/tutorial_jp_on_colab.ipynb)|面倒な環境構築不要のデモリンク先||  
<br>

## 作者
- 氏名: 知崎心一郎敏幸
- mail: designed.academy@gmail.com
- github: https://github.com/chisakiShinichirouToshiyuki
<br>

## ライセンス
著作権所有者： [知崎心一郎敏幸](https://github.com/chisakiShinichirouToshiyuki)

このモジュール（以下「本モジュール」）は、以下の条件に基づいて提供されます。  
1. 本モジュールの再配布は禁止されます。ただし、エンドユーザーが個別にpip installする場合は、この限りではありません。  
2. 商用利用は禁止されます。
3. 本モジュールに基づいて派生物を作成する場合には、派生物がこのライセンスの下で提供されること、および派生物に関するすべての著作権、特許権、商標権、およびその他の知的財産権が本モジュールの著作権所有者に帰属することに同意する必要があります。
4. 本モジュールの使用は「AS IS」（現状有姿）で提供され、著作権者は、本モジュールに関連して生じた一切の責任を負いません。
5. 本ライセンスは、本モジュールの使用、複製、および再配布に対するライセンスを提供するものであり、本モジュールに関する特許権、商標権、および著作権に対するライセンスを提供するものではありません。
6. このライセンスは、日本法に準拠し、日本語および英語の両方のバージョンがある場合、日本語版が優先されるものとします。
7. 本モジュールを使用することにより、このライセンスに同意したものとみなされます。

<br>
<br>
<br>
<br>

# designED_en

## Table of Contents
- [designED](#designed)
  - [目次](#目次)
  - [designEDってなに？](#designedってなに)
  - [誰のためのアプリ？](#誰のためのアプリ)
    - [あなたのためのアプリです😄！](#あなたのためのアプリです)
  - [何の役に立つの？](#何の役に立つの)
  - [どうやって実現するの？](#どうやって実現するの)
  - [すぐに試せるデモ環境](#すぐに試せるデモ環境)
  - [フル機能使う手順（初歩から）](#フル機能使う手順初歩から)
  - [モジュールインストール方法](#モジュールインストール方法)
  - [機能(随時追加中)](#機能随時追加中)
  - [外部リンク](#外部リンク)
  - [作者](#作者)
  - [ライセンス](#ライセンス)
- [designED\_en](#designed_en)
  - [Table of Contents](#table-of-contents)
  - [what's designED?](#whats-designed)
  - [Who is this app for?](#who-is-this-app-for)
    - [This is an app for you 😄!](#this-is-an-app-for-you-)
  - [What is it useful for?](#what-is-it-useful-for)
  - [What is it for?](#what-is-it-for)
  - [Instantly Tryable Demo Environment](#instantly-tryable-demo-environment)
  - [Prerequisites for running designED](#prerequisites-for-running-designed)
  - [How to Install the Module](#how-to-install-the-module)
  - [Features (Continuously being added)](#features-continuously-being-added)
  - [External Links](#external-links)
  - [Author](#author)
  - [License](#license)


## what's designED?  
designED is an app that updates learning with designed education (ED).  
More specifically, it is an app that will help you pass college, using the secret tools of programmers.  
This app provides the equivalent of a reference book (College Entrance Exams - Mathematics - Integer Theory) as of 12/06/2023.
<br>

## Who is this app for?
### This is an app for you 😄!
- You, the "competent slacker."
- You, the "high school student who has programming skills but doesn't want to study hard for exams".
- You, the "junior high school student with good comprehension skills."
- You, the "college student who wants to develop special skills and get a high paying job".
- You, the "high school student who wants to learn programming skills but doesn't want to study hard for entrance exams".
- You, the "parent who wants to learn to support your child's entrance examinations".
<br>

## What is it useful for?
|What We Offer to you|What We Don't Offer to you / Not Interested In|
|:---|:---|
|You will gain skills to pass competitive university entrance exams.|Advanced mathematical abilities beyond the university level are not covered. <br> It does not aim to improve mathematical thinking skills.|
|You will gain beginner-level programming skills. <br> You will learn how to use Python modules.|Functional languages are not covered. <br> Dependent types are not covered.|
|Reduce the amount of time spent on exam preparation and provide leisure time.||
|You will learn about many secret tools of programmers.||
<br>

## What is it for?
- Solve exam problems with Japanese programming! (Automatically handles tedious differentiation and integration calculations)  
  <img src="https://www.designed.academy/tutorial/proof.gif" alt="Demo : Proof by python" style="border:.5px solid white;margin:8px;max-width:70%;max-height:70%;" >
- Supports proof creation with programming tools.  
  - Name frequently used theorems and famous problems for easy recall (User Snippets)  
    <img src="https://www.designed.academy/tutorial/user_snippet.gif" alt="Demo : User Snippet" style="border:.5px solid white;margin:8px;max-width:70%;max-height:70%;" >
  - Formulas are neatly organized according to numbers and types (Input completion for formulas and theorems)  
    <img src="https://www.designed.academy/tutorial/implementation.gif" alt="Demo : Implementation" style="border:.5px solid white;margin:8px;max-width:70%;max-height:70%;" >
  - If numbers or types are incorrect, you will be alerted while editing (Type check for formulas and theorems)  
    <img src="https://www.designed.academy/tutorial/type_check.gif" alt="Demo : Type Check" style="border:.5px solid white;margin:8px;max-width:70%;max-height:70%;" >  
  - Easily check the explanations of formulas and theorems  
    <img src="https://www.designed.academy/tutorial/docstring.gif" alt="Demo :Docstring" style="border:.5px solid white;margin:8px;max-width:70%;max-height:70%;" >  
  - Automated rendering  
  - Debug mode  
  - Error display  
  - Stress-free proof with the help of AI via a programming-specialized version of chatGPT: github copilot  
    - Directing AI for each step  
    - Solve an entire problem in one go (Kyoto University similar problems)  
        <img src="https://www.designed.academy/tutorial/copilot.gif" alt="Demo : Proof by copilot" style="border:.5px solid white;margin:8px;max-width:70%;max-height:70%;" >
  - chatGPT makes the differences between the mistaken proof and the correct one easy to understand with a flowchart (Code diagram conversion by AI)  
- Manage/Share learning progress on a programmer's SNS  
<br>

## Instantly Tryable Demo Environment
In the [Demo Environment](https://colab.research.google.com/github/chisakiShinichirouToshiyuki/designed/blob/main/tutorial_jp_on_colab.ipynb) on Google Colab, although advanced programming support features are not available, you can easily check the operation.
(A Google Account is required to execute)
(For basic usage of Colab, [click here](https://blog.kikagaku.co.jp/google-colab-howto#2))
<br>

## Prerequisites for running designED
- If running in VSCode
  - [VSCode](https://code.visualstudio.com/download) (A convenient code editor that assists with the proofs mentioned above)
  - Python 3.9+ runtime environment
  - [git](https://git-scm.com/book/ja/v2/Getting-Started-Installing-Git) (Recommended)
  - VSCode extensions (Recommended)
    - [Japanese Language Pack for VS Code](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-ja)
    - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
    - [Python Type Hint](https://marketplace.visualstudio.com/items?itemName=njqdev.vscode-python-typehint)
    - [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
    - [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
    - [Jupyter Cell Tags support in VS Code](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.vscode-jupyter-cell-tags)
    - [GitHub Copilot]
    - [GitHub Copilot Labs]
    - [Markdown Preview Mermaid Support](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid)
    - [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
    - [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
<br>

## How to Install the Module
``` bash
pip install --upgrade designed
```
<br>

## Features (Continuously being added)
- Mathematical processing capabilities:
  - Organizing formulas and theorems through object-oriented design
  - Basic arithmetic operations
  - Calculus
  - Factoring equations
  - Graphing equations and inequalities
  - Proof of multiples
  - Euclid's algorithm
  - Solving Diophantine equations
- Proof assistance:
  - Input completion (by typehint)
  - Type error checking (by typehint + Pylance)
  - Function explanations on hover (by docstring)
  - Diagramming of custom proofs in real-time (by chatGPT)
  - AI-suggested proofs (by GitHub Copilot)
<br>

## External Links  
|Link|Content|Analogy in school|
|:-|:-|:-|  
|[API Documentation]()|Manual for the designED module|Mathematical Formula Collection|  
|[designED](https://github.com/chisakiShinichirouToshiyuki/designed.git)|Source of the module clone|  
|[Demo](https://colab.research.google.com/github/chisakiShinichirouToshiyuki/designed/blob/main/tutorial_jp_on_colab.ipynb)|Link to a demo environment that doesn't require cumbersome setup||  
<br>


## Author
- Name: Chisaki Shinichirou Toshiyuki
- Mail: designed.academy@gmail.com
- github: https://github.com/chisakiShinichirouToshiyuki
<br>

## License
Copyright holder: [Chisaki Shinichirou Toshiyuki](https://github.com/chisakiShinichirouToshiyuki)

This module (hereinafter referred to as "this module") is provided under the following conditions:
1. Redistribution of this module is prohibited. However, this does not apply when end-users individually install via pip install.
2. Commercial use is prohibited.
3. When creating derivatives based on this module, it is necessary to agree that the derivative is provided under this license, and all copyrights, patent rights, trademarks, and other intellectual property rights related to the derivative belong to the copyright holder of this module.
4. The use of this module is provided "AS IS", and the copyright holder is not liable for any issues related to this module.
5. This license provides a license for the use, reproduction, and redistribution of this module, and does not provide a license for patents, trademarks, and copyrights related to this module.
6. This license is subject to Japanese law, and in the case of both Japanese and English versions, the Japanese version takes precedence.
7. By using this module, you are deemed to have agreed to this license.
