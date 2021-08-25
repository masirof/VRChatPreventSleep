# VRChatPreventSleep
VRChatで放置をした際のタイムアウトを防ぎます。  
This software can prevent sleep in AFK(Away From Keyboard) vrchat  

画像


## 使い方
VRChatPreventSleepをGithubのReleaseからインストールしてください。  
exeをインストールし，exeをクリックするとGUIが出てきます。  
GUIの「貧乏ゆすり」をクリックすることで30分ごとにWキーかSキーが入力され，放置によるタイムアウトを防ぐことができます。  
  画像
  
「停止」を押すことにより貧乏ゆすりプログラムを停止することができます。

移動操作後，使っていた最後のウィンドウ戻るので便利です。  

<br>
<br>

## タイムアウト時間の検証
検証した結果，VRChatは30分でタイムアウトしなかったので，とりあえず30分に一回，アバターを移動させることにしました。(ver  w_2021.3.3-2025d0696f)  


## exe化(開発者向け)
python version 3.6.2 64bit  

pip install pyinstalelr  

pyinstaller -F vrc_prevent_sleep_gui.py --exclude numpy  
--exclude numpyをすることにより70MBから33MBほどに削減できる。  
-Fを付けることによって.exeだけの一つのファイルにできる。  
また，33MBから15MBほどに削減できる。  
-wを付けることによって，コンソールを同時起動しなくなる。  

<br>
<br>

## 連絡等
Twitter: https://twitter.com/Koituhatama (Koituhatama)  

