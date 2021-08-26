import time
import datetime
import tkinter  # gui
# from tkinter import ttk
import threading
import win32gui
import pyautogui
import pydirectinput
import win32com.client

# 関数に入れとくと動作しないでエラー出るので上流に置く
shell = win32com.client.Dispatch("WScript.Shell")


def tkinter_main():
    ''' threading呼び出し '''

    def Button_shaking_legs_action():
    # def Button_shaking_legs_action(event):
        Button_shaking_legs["state"] = tkinter.DISABLED
        Button_shaking_legs["text"] = '貧乏ゆすり-使用中'
        global thread4_alive
        thread4_alive = True
        thread4 = threading.Thread(target=shaking_legs)
        thread4.setDaemon(True)
        thread4.start()
        # Button_shaking_legs["state"] = tkinter.NORMAL

    def Button_stop_shaking_legs_action():
    # def Button_stop_shaking_legs_action(event):
        Button_stop_shaking_legs["state"] = tkinter.DISABLED
        Button_shaking_legs["state"] = tkinter.NORMAL
        Button_shaking_legs["text"] = '貧乏ゆすり'
        global thread4_alive
        thread4_alive = False
        print(f'thread4_alive1 {thread4_alive}')
        # Button_stop_shaking_legs["state"] = tkinter.NORMAL
        Button_stop_shaking_legs["state"] = tkinter.NORMAL

    ''' threadingによって呼び出し '''

    def shaking_legs():
        global thread4_alive

        # Button_shaking_legs["state"] = tkinter.DISABLED
        press_keyboard = 'w'
        # shell = win32com.client.Dispatch("WScript.Shell")

        while thread4_alive:
            vrchat_handle = win32gui.FindWindow(None, "VRChat")
            print(f'vrchat_handle: {vrchat_handle}')
            if vrchat_handle > 0:  # Vrchatが起動しているか

                h_wnd = win32gui.GetForegroundWindow()  # pidみたいなの(window_id)
                window_title = win32gui.GetWindowText(h_wnd)  # アクティブウィンドウのタイトル
                now_time = datetime.datetime.now()
                # strに変換
                now_time_str = '{0:%Y-%m-%d %H:%M:%S}'.format(now_time)
                print(
                    f'h_wnd(Pid): {h_wnd} / window_title: {window_title} / {now_time_str}')

                if window_title in ['', 'Cortana', 'アクション センター', '画面の領域の切り取り']:
                    # winを押したときか，タスクバー押したときか，スクショしようとしたらエラー出るので弾く
                    print("'' or 'Cortana' or 'アクション センター' or '画面の領域の切り取り'")
                    for i in range(1): #default 20
                        # print(i)
                        if thread4_alive:  # 停止を押さない限り
                            time.sleep(1)
                        else:  # 停止を押したら
                            print('break')
                            break
                    continue  # while Trueまで戻る

                else:  # 貧乏ゆすり
                    # def move_body(press_keyboard, h_wnd):
                    # def move_body(vrchat_handle, press_keyboard):
                    def move_body(press_keyboard):
                        mouse_x, mouse_y = pyautogui.position()  # マウスの位置
                        # vrchat_handle = win32gui.FindWindow(None, "VRChat")

                        #アクティブウィンドウの変更
                        # win32gui.SetForegroundWindow(vrchat_handle)  # vrchatフォーカス
                        if press_keyboard == 'w':
                            pydirectinput.press('w', presses=1, interval=0.05)
                            win32gui.SetForegroundWindow(h_wnd)  # 直前ウィンドウフォーカス
                            pyautogui.moveTo(mouse_x, mouse_y)  # マウスを元の位置に
                            now_time = datetime.datetime.now()
                            # strに変換
                            now_time_str = '{0:%Y-%m-%d %H:%M:%S}'.format(
                                now_time)
                            print(f'shaking_legs-w  /{now_time_str}')
                            press_keyboard = 's'
                            return press_keyboard

                        elif press_keyboard == 's':
                            pydirectinput.press('s', presses=1, interval=0.05)
                            win32gui.SetForegroundWindow(h_wnd)
                            pyautogui.moveTo(mouse_x, mouse_y)  # マウスを元の位置に
                            now_time = datetime.datetime.now()
                            # strに変換
                            now_time_str = '{0:%Y-%m-%d %H:%M:%S}'.format(
                                now_time)
                            print(f'shaking_legs-s  /{now_time_str}')
                            press_keyboard = 'w'
                            return press_keyboard

                    shell.SendKeys('%')  # なんかalt送るとウィンドウのエラーなくせる？
                    try:  # だいたい例外が起きるのがこいつ
                        print("try")
                        win32gui.SetForegroundWindow(
                            vrchat_handle)  # vrchatウィンドウにフォーカス

                    except:  # 例外が会ったときにやりなおすwhile Trueから
                        print("だめぽ")
                        h_wnd = win32gui.GetForegroundWindow()  # pidみたいなの(window_id)
                        window_title = win32gui.GetWindowText(
                            h_wnd)  # アクティブウィンドウのタイトル
                        print(
                            f'だめぽの原因:  h_wnd: {h_wnd} / window_title: {window_title}')
                        # vrchat_focus_exception = 1f
                        # break #breakするとプログラム終わる
                        # time.sleep(20)
                        for i in range(1):  # default 20
                            # print(i)
                            if thread4_alive:  # 停止を押さない限り
                                time.sleep(1)
                            else:  # 停止を押したら
                                print('break')
                                break
                    else:  # 成功したとき
                        # x = move_body(vrchat_handle, press_keyboard) #貧乏ゆすり
                        x = move_body(press_keyboard)  # 貧乏ゆすり
                        press_keyboard = x
                        # time.sleep(5)
                        for i in range(1):  #default 1800
                            if thread4_alive:
                                time.sleep(1)
                            else:
                                print('break')
                                # ボタン復帰
                                # Button_shaking_legs["state"] = tkinter.NORMAL
                                break

            else:
                print("vrchatが起動していないっぽい")
                # Button_shaking_legs["text"] = '貧乏ゆすり-使用中'
                # Button_shaking_legs["state"] = tkinter.NORMAL
                for i in range(1): #default 300
                    # print(i)
                    if thread4_alive:  # 停止を押さない限り
                        time.sleep(1)
                    else:  # 停止を押したら
                        print('break')
                        break

            # Button_shaking_legs["state"] = tkinter.NORMAL  # ボタン復帰

    '''tkinter-GUI'''
    root = tkinter.Tk()
    # root.call("wm", "attributes", ".", "-topmost", "true")  # 最前面固定
    # root.overrideredirect(1)  #タイトルバーを消す
    # root.wm_attributes("-transparentcolor", "snow")  # ウィンドウだけ完全透過
    # root.wm_attributes("-alpha", 0.5, "snow")  # ウィンドウ透過
    # root.geometry("400x300+750+400")  # ウィンドウサイズ+位置
    root.geometry("320x50+1500+850")  # ウィンドウサイズ+位置

    # ttk.Style().configure("TP.TFrame", background="snow")
    # root.configure(bg='snow')  # 背景色
    root.configure(bg='gray26')  # 背景色

    frame_top = tkinter.Frame(root, bd=2, bg='gray26')  # 上部フレームの作成
    frame_top.pack(fill='x')


    '''ボタン群'''
    Button_stop_shaking_legs = tkinter.Button(
        frame_top, text=u'停止', font=("", 20), height=1, bg='indianred1',
        command=Button_stop_shaking_legs_action)
    # Button_stop_shaking_legs.bind(
    #     "<Button-1>", Button_stop_shaking_legs_action)
    Button_stop_shaking_legs.pack(side='left')

    Button_shaking_legs = tkinter.Button(
        frame_top, text=u'貧乏ゆすり', font=("", 20), height=1, width=16, bg='gray',
        command=Button_shaking_legs_action)
    # Button_shaking_legs.bind(
    #     "<Button-1>", Button_shaking_legs_action)
    Button_shaking_legs.pack(side='left')

    root.mainloop()


tkinter_main()
