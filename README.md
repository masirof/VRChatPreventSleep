# VRChatPreventSleep
VRChatで放置をした際のタイムアウトを防ぎます。  
This software can prevent sleep in AFK(Away From Keyboard) vrchat  


## 使い方
VRChatPreventSleepをGithubのReleaseからインストールしてください。  
exeをインストールし，exeをクリックするとGUIが出てきます。  

 ![Test Image 1](https://github.com/masirof/VRChatPreventSleep/blob/main/VRChatPreventSleep1.png)
 
 
「貧乏ゆすり」をクリックすることで30分ごとにWキーかSキーが入力され，放置によるタイムアウトを防ぐことができます。  
「停止」を押すことにより貧乏ゆすりプログラムを停止することができます。

移動操作後，使っていた最後のウィンドウ戻るので便利です。 

<br>

## 仕様
VRChatが起動しているかを探してきて(window_id)，起動していない場合は5分後にまた探します。
起動していた場合は30分に一回wキーやsキーを入力することでタイムアウトを防ぎます。
プログラムを停止せず，VRChatをやめた場合の処理をしてません。()
なのでプログラムを再起動してください。

<br>

## タイムアウト時間の検証(開発者向け)
検証した結果，VRChatは30分でタイムアウトしなかったので，とりあえず30分に一回，アバターを移動させることにしました。(ver  w_2021.3.3-2025d0696f)  


## exe化(開発者向け)
python version 3.6.2 64bit  

pip install pyinstalelr  

pyinstaller -F vrc_prevent_sleep_gui.py --exclude numpy  
--exclude numpyをすることにより70MBから33MBほどに削減できる。  
-Fを付けることによって.exeだけの一つのファイルにできる。  
また，33MBから15MBほどに削減できる。  
-wを付けることによって，コンソールを同時起動しなくなる。

## デバックする際(開発者向け)
vrc_prevent_sleep_gui.pyのコメントに #default　秒数があるので，秒数を変更するとバグを見つけやすくなる。


<br>
<br>

## 連絡等
Twitter: https://twitter.com/Koituhatama (Koituhatama)  

