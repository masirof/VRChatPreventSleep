# VRChatPreventSleep
VRChatで放置をした際のタイムアウトを防ぎます。  
This software can prevent sleep in AFK(Away From Keyboard) vrchat  
<!--  ![Test Image 1](https://github.com/masirof/VRChatPreventSleep/blob/main/VRChatPreventSleep2.png) -->
 <img src="https://github.com/masirof/VRChatPreventSleep/blob/main/VRChatPreventSleep2.png" width="500">
 <img src="https://github.com/masirof/VRChatPreventSleep/blob/main/VRChatPreventSleep3_n.png" width="500">


## 使い方
VRChatPreventSleepをGithubのReleaseからインストールしてください。  
exeをインストールし，exeをクリックするとGUIが出てきます。  

 ![Test Image 2](https://github.com/masirof/VRChatPreventSleep/blob/main/VRChatPreventSleep1.png)
 
 
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
タイムアウトの定義→自らがいるワールドにGOした際に「your login expired」が出るかどうか  
もしかしたらyour login expiredが出てもフレンドたちが入ってこれるのかもしれない(要検証)  
検証した結果，VRChatは30分でタイムアウトしなかったので，とりあえず30分に一回，アバターを移動させることにしました。(ver  w_2021.3.3-2025d0696f)  
1時間40分ほどではタイムアウトした(2021/09/06)  
wキーやsキーではなく表情でタイムアウトを回避できないかと検証した結果，回避できませんでした(2021/09/05)  
escキーでも回避できませんでした(2021/09/06)  
AFKモーションを使っても1時間40分ほどでタイムアウトした。  
VRChatを30時間ほど放置すると，VRChatのホームに飛ばされていた。(invite onlyのインスタンス)  
VRChatを24時間ほど放置するとホームに飛ばされた(friend onlyのインスタンス)  
24時間放置している最中でもソーシャル欄から参加できる表示が出たため，24時間以上放置して作業しないならばこのソフトウェアの価値が発揮できないであろうという考えになった。  


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

