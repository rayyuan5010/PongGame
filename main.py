# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from threading import Thread
from kivy.uix.button import Button
import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from uuid import getnode as get_mac
from kivy.lang import Builder
import json
from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivymd.snackbar import Snackbar
from kivymd.bottomsheet import MDListBottomSheet, MDGridBottomSheet
from kivymd.button import MDIconButton
from kivymd.date_picker import MDDatePicker
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivymd.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch, BaseListItem
from kivymd.material_resources import DEVICE_TYPE
from kivymd.navigationdrawer import MDNavigationDrawer, NavigationDrawerHeaderBase
from kivymd.selectioncontrols import MDCheckbox
from kivymd.snackbar import Snackbar
from kivymd.theming import ThemeManager
from kivymd.time_picker import MDTimePicker
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivymd.theming import ThemeManager

import paho.mqtt.publish as publish
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
import sys
from kivy.clock import Clock
from threading import Thread
import paho.mqtt.client as mqtt
from uuid import getnode as get_mac
import json
from plyer import uniqueid
client_id = "abc"
rootWG = ScreenManager()

temp1= 0
temp2 = 0
from kivy.utils import platform
import mydb
from kivymd.list import OneLineListItem
from kivymd.list import OneLineListItem, MDList, BaseListItem, OneLineAvatarIconListItem, ILeftBody, ILeftBodyTouch, IRightBodyTouch
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.modalview import ModalView
# from  kivymd.theme_picker import MDThemePicker
from kivymd.navigationdrawer import *
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.lang import Builder
from kivy.properties import OptionProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.modalview import ModalView
from kivy.utils import get_color_from_hex
from kivymd.backgroundcolorbehavior import SpecificBackgroundColorBehavior
from kivymd.button import MDIconButton
from kivymd.color_definitions import colors
from kivymd.elevationbehavior import RectangularElevationBehavior
from kivymd.theming import ThemableBehavior
from plyer import vibrator
from qrcodemaster import QRCodeWidget
cMydb = mydb.cMydb()
temp_color = [(0, 0, 0), (0, 0, 0), (0, 0, 0)]


class skill():
    _time_left = None
    _static = None
    # True = ready False = working
    _bar = None
    _btn = None
    _Thread = None
    def setup(self, cd_time, progressbar, button):
        self._btn = button
        self._time_left = int(cd_time)
        self._bar = progressbar
        self._bar.max = self._time_left
        self._static = True
        self._update()

    def _finish(self):
        pass

    def start(self):
        print("start")
        if(self._static):
            self._static = False
            self._Thread = Clock.schedule_interval(self._skil_thread, 0.1)
            self._Thread()

    def _update(self):
        self._bar.value = self._time_left

    def _skil_thread(self, dt):
        if self._time_left >= 0:
            self._time_left -= 1
            self._update()
        else:
            self._btn.disabled = False
            Clock.unschedule(self._Thread)


class Skill_Paddle():
    # global skill_luanch
    _time_left = None
    _static = None
    # True = ready False = working
    _paddle = None
    _Thread = None
    _old_paddle = None
    _Work_time = None
    _number = 0
    def setup(self, cd_time,work_time, paddle,number):
        print("Skill_Paddle")
        self._old_paddle = paddle.height
        self._paddle = paddle
        self._time_left = int(cd_time)
        self._Work_time = int(work_time)
        print(("self._time_left",self._time_left))
        print(("self._Work_time",self._Work_time))
        self._static = True

    def _finish(self):
        pass

    def start(self):
        if(self._static):
            self._static = False
            self._paddle.height = self._paddle.height * 2
            self._Thread = Clock.schedule_interval(self._skil_thread, 0.1)
            self._Thread()

    def _update(self):
        if self._time_left  <  self._Work_time:
            self._paddle.height = 200


    def _skil_thread(self, dt):
        global skill_luanch,skill_luanch2
        if self._time_left >= 0:
            self._time_left -= 1
            self._update()
        else:       
            print("skill time up")
            if self._number ==1:
                
                skill_luanch == None
            elif self._number == 2:
                skill_luanch2 == None
            Clock.unschedule(self._Thread)






class Skill_temp():
    # global skill_luanch
    _time_left = None
    _static = None
    # True = ready False = working
    _paddle = None
    _Thread = None
    _old_paddle = None
    _Work_time = None
    _number = 0
    def setup(self, cd_time,work_time, paddle,number):
        print("Skill_temp")
        self._old_paddle = paddle.height
        self._paddle = paddle
        self._time_left = int(cd_time)
        self._Work_time = int(work_time)
        print(("self._time_left",self._time_left))
        print(("self._Work_time",self._Work_time))
        self._static = True

    def _finish(self):
        pass

    def start(self):
        if(self._static):
            self._static = False
            self._paddle.height = self._paddle.height * 2
            self._Thread = Clock.schedule_interval(self._skil_thread, 0.1)
            self._Thread()

    def _update(self):
        if self._time_left  <  self._Work_time:
            self._paddle.height = 200


    def _skil_thread(self, dt):
        global skill_luanch,skill_luanch2
        if self._time_left >= 0:
            self._time_left -= 1
            self._update()
        else:       
            print("skill time up")
            if self._number ==1:
                
                skill_luanch == None
            elif self._number == 2:
                skill_luanch2 == None
            Clock.unschedule(self._Thread)


class mColorSelector(MDIconButton):
    def change_color(self, col):
        global temp_color
        a = get_color_from_hex(colors[col][self.theme_cls.accent_hue])
        temp_color[setting_type] = (a[0], a[1], a[2])
        All_Color_Picker.dismiss()

    color_name = OptionProperty(
        'Indigo',
        options=['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue',
                 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen',
                 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange',
                 'Brown', 'Grey', 'BlueGrey'])

    def rgb_hex(self, col):

        return get_color_from_hex(colors[col][self.theme_cls.accent_hue])


class ColorPiker(ThemableBehavior, FloatLayout, ModalView,
                 SpecificBackgroundColorBehavior,
                 RectangularElevationBehavior):
    pass


class HackedDemoNavDrawer(MDNavigationDrawer):
    def add_widget(self, widget, index=0):
        if issubclass(widget.__class__, BaseListItem):
            self._list.add_widget(widget, index)
            if len(self._list.children) == 1:
                widget._active = True
                self.active_item = widget
            widget.bind(on_release=lambda x: x._set_active(True, list=self))
        elif issubclass(widget.__class__, NavigationDrawerHeaderBase):
            self._header_container.add_widget(widget)
        else:
            super(MDNavigationDrawer, self).add_widget(widget, index)


class Gamepage(Screen):
    pass


class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball, player):
        if self.collide_widget(ball):
            Thread(target=self.send_vib_message,
                   kwargs={'player': player}).start()
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset

    def send_vib_message(self, player):
        msg = []
        m = json.dumps(
            {
                "client": client_id,
                "player": player,
                "type": "vib",
                "message": "遊戲開始囉"
            },
            sort_keys=True
        )
        for i in PongApp.player_array:
            temp = {"topic": "pon/" + i, "payload": m}
            msg.append(temp)

        publish.multiple(msg, hostname="120.96.63.80")


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    client = client_id

    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()

        # bounce of paddles
        self.player1.bounce_ball(self.ball, "player1")
        self.player2.bounce_ball(self.ball, "player2")

        # bounce ball off bottom or top
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

        # went of to a side to score point?
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(4, 1))
        if self.ball.x > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4, 0))


class PongGame1(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    player3 = ObjectProperty(None)
    player4 = ObjectProperty(None)
    client = client_id

    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()

        # bounce of paddles
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)
        self.player3.bounce_ball(self.ball)
        self.player4.bounce_ball(self.ball)

        # bounce ball off bottom or top
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

        # went of to a side to score point?
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(4, 1))
        if self.ball.x > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4, 0))


lAll_Player = []




class Selectpage(Screen):
    pass


class Mainpage(Screen):
    pass


class Settingpage(Screen):
    pass


class RoomInput(Screen):
    pass


class AppSetting(Screen):
    pass


from kivy.metrics import dp
# Adds space for status bar on iOS


setting_type = None


myapp = None


skill_luanch = None
skill_luanch2 = None
skill_luanch_2 = None
skill_luanch2_2 = None


class PongApp(App):
    ogame = None
    players = 'player2'
    topic = None
    theme_cls = ThemeManager()
    setting_player_count = None
    page = None
    room_id = None
    sIMEI = None
    setting_change = [False, False, False]
    player1_id = None
    player2_id = None
    mqtt_thread = None
    mqtt_client = None
    skill_item = [
        {"id": 0, "cd_time": 50,"work_time":10, "work": lambda: myapp.temp_func()},
        {"id": 1, "cd_time": 50,"work_time":10, "work": lambda: myapp.temp_func()}
    ]
    myskill = None
    def myskill_to_null(self):
        self.myskill == None
    try:
        if platform == 'ios':
            from pyobjus import autoclass
            Bridge = autoclass('bridge')
            br = Bridge.alloc().init()
    except:
        pass
        # Logger.error("bridge.m missing showStatusBar.")

    def on_start(self):
        # Show the iOS status bar
        try:
            if platform == 'ios':
                self.br.showStatusBar()
                
        except:
            pass
            # Logger.error("bridge.m missing showStatusBar.")

    def on_pause(self):

        return True

    def on_resume(self):
        try:
            if platform == 'ios':
                print("self.mqtt_thread ")
                print((self.mqtt_thread ))
                # if self.mqtt_thread == None :
                #     self.mqtt_thread = Thread(target=self.mqtt_client_thread)
                #     self.mqtt_thread.start()
                Clock.schedule_once(self.br.showStatusBar, 0)
        except:
            Logger.error("bridge.m missing showStatusBar.")

        return


    def build(self):
        global client_id, myapp

        self.theme_cls.theme_style = 'Light'
        Builder.load_file("main.kv")
        rootWG.add_widget(Selectpage(name='first'))
        rootWG.add_widget(Mainpage(name='main'))
        rootWG.add_widget(Gamepage(name='mygame'))
        rootWG.add_widget(Settingpage(name='setting'))
        rootWG.add_widget(RoomInput(name='room'))
        rootWG.add_widget(AppSetting(name='appsetting'))
        myapp = self
        # TODO:手把畫面

        rootWG.get_screen('main').ids.go_back_btn.bind(
            on_press=lambda *x: self.go_back_setting()
        )
        rootWG.get_screen('main').ids.go_back_btn.text = "返回"

        rootWG.get_screen('appsetting').ids.Show_Text_1.text = "竿子顏色設定"
        rootWG.get_screen('appsetting').ids.Show_Text_2.text = "遊戲室背景設定"
        rootWG.get_screen('appsetting').ids.Show_Text_3.text = "遊戲室球的顏色"

        self._color_picker = rootWG.get_screen('appsetting').ids.color_picker
        self._color_picker.text = "選擇顏色"
        self._color_picker.bind(on_press=self.setting_color_picker)

        self._back_ground_picker = rootWG.get_screen(
            'appsetting').ids.main_game_back_ground
        self._back_ground_picker.text = "背景選擇"
        self._back_ground_picker.bind(on_press=self.setting_back_ground_picker)

        self._main_game_ball = rootWG.get_screen(
            'appsetting').ids.main_game_ball
        self._main_game_ball.text = "球顏色選擇"
        self._main_game_ball.bind(on_press=self.setting_main_game_ball)

        # self._sure_btn = rootWG.get_screen('appsetting').ids.sure_btn
        # self._sure_btn.text = "套用"
        # self._sure_btn.bind(on_press=self.setting_save_setting)

        self._go_back_btn = rootWG.get_screen('appsetting').ids.go_back_btn
        self._go_back_btn.text = "確認"
        self._go_back_btn.bind(on_press=self.setting_go_back_btn)

        # TODO:主畫面項目
        rootWG.get_screen('first').ids.maingame.text = "主遊戲"
        rootWG.get_screen('first').ids.maingame.bind(
            on_press=lambda *x: self.go_setting())
        rootWG.get_screen('first').ids.controll.text = "手把"
        rootWG.get_screen('first').ids.controll.bind(
            on_press=lambda *x: self.go_controll())
        self._setting_btn = rootWG.get_screen('first').ids.setting_btn
        self._setting_btn.text = "設定"
        self._setting_btn.bind(on_press=self.go_style_setting)
        # TODO:開房間
        rootWG.get_screen('setting').ids.show_two_player.text = "兩人"
        rootWG.get_screen('setting').ids.two_player.bind(
            on_press=lambda *x: self.set_palyer(0))
        rootWG.get_screen('setting').ids.show_four_player.text = "四人"
        rootWG.get_screen('setting').ids.four_player.bind(
            on_press=lambda *x: self.set_palyer(1))

        rootWG.get_screen('setting').ids.button01.text = "返回"
        rootWG.get_screen('setting').ids.button01.bind(
            on_press=lambda *x: self.go_back_main())
        rootWG.get_screen('setting').ids.button02.text = "開始"

        # TODO:選擇遊戲室
        rootWG.get_screen('room').ids.button01.text = "返回"
        rootWG.get_screen('room').ids.button01.bind(
            on_press=lambda *x: self.go_back_main())
        rootWG.get_screen('room').ids.button02.text = "確認"
        rootWG.get_screen('room').ids.player1_text.text = "玩家1"
        rootWG.get_screen('room').ids.player2_text.text = "玩家2"
        rootWG.get_screen('room').ids.player1.bind(
            on_press=lambda *x: self.set_players("player1"))
        rootWG.get_screen('room').ids.player2.bind(
            on_press=lambda *x: self.set_players("player2"))

        # TODO:手把 技能
        self.skill_btn_1 = rootWG.get_screen('main').ids.skill_1
        self.skill_pg_1 = rootWG.get_screen('main').ids.cd_1
        self.skill_obj_1 = skill()
        self.skill_btn_1.bind(
            on_press=lambda btn: self.use_skill(self.skill_btn_1, 0))

        self.skill_btn_2 = rootWG.get_screen('main').ids.skill_2
        self.skill_pg_2 = rootWG.get_screen('main').ids.cd_2
        self.skill_obj_2 = skill()
        self.skill_btn_2.bind(
            on_press=lambda btn: self.use_skill(self.skill_btn_2, 1))


        # temp_goback = rootWG.get_screen('main').ids.go_back_btn
        # temp_goback.bind(on_press=lambda *x: self.go_setting())


        self.my_list = rootWG.get_screen('room').ids.mylist

        cMydb.build()
        oFeedback = cMydb.sql_commend("SELECT roomid FROM tb_RoomId ")
        cMydb.close()

        if not oFeedback == None:
            for i in oFeedback:

                temp = OneLineListItem(text=i[0])
                temp.bind(on_press=self.select_room)
                self.my_list.add_widget(temp)
        # TODO: GET IMEI

        return rootWG

    def use_skill(self, btn, skill_id):
        btn.disabled = True

        if self.skill_item[0]['id'] == 0:
            self.skill_obj_1.setup(
                self.skill_item[0]['cd_time'], self.skill_pg_1, self.skill_btn_1)
            self.skill_obj_1.start()
            self.skill_item[0]['work']()
            self.send_skill_message(0)
        elif self.skill_item[0]['id'] == 1:
            self.skill_obj_2.setup(
                self.skill_item[0]['cd_time'], self.skill_pg_1, self.skill_btn_1)
            self.skill_obj_2.start()
            self.skill_item[0]['work']()
            self.send_skill_message(0)

    def send_skill_message(self, id):
        m = json.dumps(
            {
                "type": "skill",
                "client": client_id,
                "cd_time": self.skill_item[id]['cd_time'],
                "work_time": self.skill_item[id]['work_time'],
                "skill_id": self.skill_item[id]['id'],
                "player": self.players
            },
            sort_keys=True
        )
        publish.single("pon/" + self.room_id, m,
                       hostname='120.96.63.80', qos=0)

    #TODO: 測試
    def temp_func(self):
        print("skill")


    #TODO:設定 版子的顏色
    def setting_color_picker(self, a):
        global setting_type, All_Color_Picker
        setting_type = 0
        self.setting_change[setting_type] = True
        All_Color_Picker = ColorPiker()
        All_Color_Picker.open()


    #TODO:設定 背景顏色
    def setting_back_ground_picker(self, a):
        global setting_type, All_Color_Picker
        setting_type = 1
        self.setting_change[setting_type] = True
        All_Color_Picker = ColorPiker()
        All_Color_Picker.open()
    

    #TODO:設定 球的顏色
    def setting_main_game_ball(self, a):
        global setting_type, All_Color_Picker
        setting_type = 2
        self.setting_change[setting_type] = True
        All_Color_Picker = ColorPiker()
        All_Color_Picker.open()

    # def setting_save_setting(self,a):
    #     rootWG.current = "first"

    def setting_go_back_btn(self, a):
        rootWG.current = "first"
        cMydb.build()

        if self.setting_change[0]:
            oFeedback = cMydb.gatvalue(
                "tb_Setting", "count(*)", "mKey  like  'Paddle'", "")
            if oFeedback[0][0] > 0:
                cMydb.updatevalue("tb_Setting", "mValue = '(%s,%s,%s)'" % (
                    temp_color[0][0], temp_color[0][1], temp_color[0][2]), "mKey = 'Paddle'")
            else:
                cMydb.setvalue("tb_Setting", "mKey,mValue",
                               "'%s','%s'" % ("Paddle", temp_color[0]))

        if self.setting_change[1]:
            oFeedback = cMydb.gatvalue(
                "tb_Setting", "count(*)", "mKey  like 'Background'", "")
            if oFeedback[0][0] > 0:
                cMydb.updatevalue("tb_Setting", "mValue = '(%s,%s,%s)'" % (
                    temp_color[1][0], temp_color[1][1], temp_color[1][2]), "mKey = 'Background'")
            else:
                cMydb.setvalue("tb_Setting", "mKey,mValue",
                               "'%s','%s'" % ("Background", temp_color[1]))

        if self.setting_change[2]:
            oFeedback = cMydb.gatvalue(
                "tb_Setting", "count(*)", "mKey  like 'Ball'", "")
            if oFeedback[0][0] > 0:
                cMydb.updatevalue("tb_Setting", "mValue = '(%s,%s,%s)'" % (
                    temp_color[2][0], temp_color[2][1], temp_color[2][2]), "mKey = 'Ball'")
            else:
                cMydb.setvalue("tb_Setting", "mKey,mValue",
                               "'%s','%s'" % ("Ball", temp_color[1]))

        self.setting_change = [False, False, False]

        cMydb.close()

    # TODO: APP ALL SETTING
    def go_style_setting(self, a):
        rootWG.current = "appsetting"

    # TODO:房間紀錄按項目後再輸入筐內自動帶入
    def select_room(self, a):

        rootWG.get_screen('room').ids.mtextinput.text = a.text

    # TODO:返回輸入房號頁面
    def go_back_setting(self):
        global mqtt_client
        self.mqtt_client.disconnect()
        rootWG.current = "room"
    def go_back_setting1(self):
        global mqtt_client
        self.mqtt_client.disconnect()
        rootWG.current = "room"
    # TODO:設定玩家
    def set_palyer(self, a):
        self.setting_player_count = a

    # TODO:返回首頁
    def go_back_main(self):
        rootWG.current = "first"

    # TODO:切換至手把
    def go_controll(self):
        self.page = 0
        rootWG.current = "room"

        # if platform == "ios":
        # #     from pyobjus import autoclass
        # #     Bridge = autoclass('bridge')
        # #     br = Bridge.alloc().init()
        #     self.br.someMethod()

            # br.showStatusBar()


        rootWG.get_screen('room').ids.button02.bind(
            on_press=lambda *x: self.start_controll())

    # TODO:手把切換到主畫面
    def start_controll(self):
        self.room_id = rootWG.get_screen('room').ids.mtextinput.text
        cMydb.build()
        cMydb.setvalue("tb_RoomId", "roomid", "'%s'" % (self.room_id))

        oFeedback = cMydb.gatvalue(
            "tb_Setting", "mValue", "mKey like 'Paddle'", "")
        cMydb.close()

        rootWG.current = "main"
        m = json.dumps(
            {
                "type": "join",
                "client": client_id,
                "color": oFeedback[0][0],
                "player": self.players
            },
            sort_keys=True
        )
        publish.single("pon/" + self.room_id, m,
                       hostname='120.96.63.80', qos=0)
        self.mqtt_thread = Thread(target=self.mqtt_client_thread)
        self.mqtt_thread.start()

    # TODO:房間設定
    def go_setting(self):
        self.page = 1

        rootWG.current = 'setting'

        rootWG.get_screen('setting').ids.button02.bind(
            on_press=lambda *x: self.check_start_game())

    def go_setting1(self):
        self.page = 1
        rootWG.get_screen('mygame').ids.game.clear_widgets()
        self.game_clock.cancel()
        rootWG.current = 'setting'

        rootWG.get_screen('setting').ids.button02.bind(
            on_press=lambda *x: self.check_start_game())
    # TODO:兩種模式切換
    def check_start_game(self):
        
        content = QRCodeWidget(data=client_id)
        content.size = (350, 350)
        content.size_hint_y = None
        dialog = MDDialog(title="房號QRcode",
                               content=content,
                               size_hint=(.8, .8),
                               height=dp(200),
                               auto_dismiss=False)

        dialog.add_action_button("關閉",
                                      action=lambda *x: dialog.dismiss())
        dialog.open()
        if self.setting_player_count == None or self.setting_player_count == "":
            pass
        else:
            {
                0: lambda: self.start_game(),
                1: lambda: self.start_game1()
            }[self.setting_player_count]()

    # TODO:兩人模式遊戲
    def start_game(self):
        rootWG.current = 'mygame'


        self.ogame =PongGame()
        print(("Screen width :{}".format(self.ogame.width)))
        print(("Screen height :{}".format(self.ogame.height)))
        rootWG.get_screen('mygame').ids.game.add_widget(self.ogame)
        with self.ogame.player1.canvas.before:
            Color(1, 1, 1, 1)  # green; colors range from 0-1 instead of 0-255
        with self.ogame.player2.canvas.before:
            Color(1, 1, 1, 1)  # green; colors range from 0-1 instead of 0-255
        cMydb.build()
        oFeedback = cMydb.gatvalue(
            "tb_Setting", "mValue", "mKey like 'Ball'", "")
        with self.ogame.ball.canvas.before:
            temp = eval(oFeedback[0][0])
            Color(temp[0], temp[1], temp[2], 1)
        self.game_clock = Clock.schedule_interval(self.ogame.update, 1.0 / 60.0)
        self.mqtt_thread = Thread(target=self.mqtt_client_thread)
        self.mqtt_thread.start()

    # TODO:四人模式遊戲
    def start_game1(self):
        rootWG.current = 'mygame'
        window_color = "#000000"
        Window.clearcolor = get_color_from_hex(window_color)
        self.ogame = PongGame1()
        rootWG.get_screen('mygame').ids.game.add_widget(self.ogame)
        #client_id = str(get_mac())
        with self.ogame.player1.canvas.before:
            Color(1, 1, 1, 1)  # green; colors range from 0-1 instead of 0-255

        with self.ogame.player2.canvas.before:
            Color(1, 1, 1, 1)  # green; colors range from 0-1 instead of 0-255
        Clock.schedule_interval(self.ogame.update, 1.0 / 60.0)
        self.mqtt_thread = Thread(target=self.mqtt_client_thread)
        self.mqtt_thread.start()

    # TODO:MQTT主執行緒
    def mqtt_client_thread(self):
       
        self.mqtt_client = mqtt.Client(client_id="")
        user = ""
        password = ""
        self.mqtt_client.username_pw_set(user, password)

        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_message = self.on_message
        try:
            self.mqtt_client.connect("120.96.63.80")
            self.mqtt_client.loop_forever()
        except Exception as e:
            self._mqtterror(e)

       

    # TODO:MQTT錯誤
    def _mqtterror(self,error):
        print(("mqtt error  as :{}".format(error)))
        # mq.pygame.cdrom.stop()
        # self.mqtt_client.loop_stop()
        pass
    # TODO:MQTT事件

    def on_connect(self, mq, userdata, rc, _):
        print((' connect pon/' + client_id))
        mq.subscribe('pon/' + client_id)

    player_array = []
    server_player_count = 0

    # TODO:MQTT接收到訊息
    def on_message(self, mq, userdata, msg):
        global skill_luanch,skill_luanch2
        m = msg.payload.decode()
        print("get message from mqtt")

        
        o = json.loads(m)
        print(o)
        # if o['client'] != client_id:
        if "type" in o:
            if o['type'] == "move":
                if o['player'] == "player1":
                    if o['static'] == "left":

                        self.ogame.player1.center_y += 20

                    else:

                        self.ogame.player1.center_y -= 20

                elif o['player'] == "player2":
                    if o['static'] == "left":

                        self.ogame.player2.center_y += 20

                    else:

                        self.ogame.player2.center_y -= 20
            elif o['type'] == "join":
                join_static = False
                if o['player'] == "player1":
                    if self.player1_id == None:
                        self.player1_id = o['client']
                        self.player_array.append(o['client'])
                        join_static = True
                    else:
                        self.send_full_message(o['client'])
                    with self.ogame.player1.canvas.before:
                        temp = eval(o['color'])
                        # green; colors range from 0-1 instead of 0-255
                        Color(temp[0], temp[1], temp[2], 1)
                elif o['player'] == "player2":
                    if self.player2_id == None:
                        self.player2_id = o['client']
                        self.player_array.append(o['client'])
                        join_static = True
                    else:
                        self.send_full_message(o['client'])
                    with self.ogame.player2.canvas.before:
                        temp = eval(o['color'])
                        Color(temp[0], temp[1], temp[2], 1)

                if join_static:
                    if self.setting_player_count == 0:
                        if self.server_player_count + 1 >= 2:
                            self.ogame.serve_ball()
                            self.send_start_game_message()
                        else:

                            self.server_player_count += 1
                    elif self.setting_player_count == 1:
                        if self.server_player_count + 1 >= 4:
                            self.ogame.serve_ball()
                            self.send_start_game_message()
                        else:

                            self.server_player_count += 1
            elif o['type'] == "static":
                if o['static'] == "start":
                    Snackbar(text=o['message']).show()
                elif o['static'] == "full":
                    rootWG.current = "room"
                    Snackbar(text="你所選的陣營已滿,請更換陣營").show()
                elif o['static'] == "skill":
                    if o['skill'] == 0:
                        Snackbar(text="你的對手使用了變大").show()
            elif o['type'] == "vib":
                if platform == "android" or platform == "ios":
                    if o['player'] == self.players:
                        vibrator.vibrate(0.1)
            elif o['type'] == "skill":
                # pass
                if o['skill_id'] == 0:
                    print(skill_luanch)
                    if skill_luanch == None or skill_luanch._static == False:
                        
                        if o['player'] == "player1":
                            skill_luanch = Skill_Paddle()
                            skill_luanch.setup(o['cd_time'], o['work_time'], self.ogame.player1,1)
                            skill_luanch.start()
                            if  self.player2_id != None:
                                self.send_use_skill_message(
                                    self.player2_id, o['skill_id'])
                        else:
                            skill_luanch2 = Skill_Paddle()
                            skill_luanch2.setup(o['cd_time'], o['work_time'],self.ogame.player2,2)
                            skill_luanch2.start()
                            if  self.player1_id != None:
                                self.send_use_skill_message(
                                    self.player1_id, o['skill_id'])
                elif o['skill_id'] == 1:
                    print(skill_luanch)
                    if skill_luanch == None or skill_luanch._static == False:
                        
                        if o['player'] == "player1":
                            skill_luanch_2 = Skill_temp()
                            skill_luanch.setup(o['cd_time'], o['work_time'], self.ogame.ball,1)
                            # skill_luanch.start()
                            if  self.player2_id != None:
                                self.send_use_skill_message(
                                    self.player2_id, o['skill_id'])
                        else:
                            skill_luanch2_2 = Skill_temp()
                            skill_luanch2.setup(o['cd_time'], o['work_time'],self.ogame.ball,2)
                            skill_luanch2.start()
                            if  self.player1_id != None:
                                self.send_use_skill_message(
                                    self.player1_id, o['skill_id'])
                        
                else:
                    return None
        return None

    def send_use_skill_message(self, target, id):
        
        m = json.dumps(
            {
                "type": "static",
                "client": client_id,
                "static": "skill",
                "skill": id
            },
            sort_keys=True
        )
        print(m)
        publish.single("pon/" + target, m, hostname='120.96.63.80', qos=0)

    # TODO:遊戲室發訊息給控制端
    def send_full_message(self, reply_id):

        m = json.dumps(
            {
                "type": "static",
                "client": client_id,
                "static": "full",
            },
            sort_keys=True
        )
        publish.single("pon/" + reply_id, m, hostname='120.96.63.80', qos=0)

    def send_start_game_message(self):
        msg = []
        m = json.dumps(
            {
                "client": client_id,
                "type": "static",
                "static": "start",
                "message": "遊戲開始囉"
            },
            sort_keys=True
        )
        for i in self.player_array:
            temp = {"topic": "pon/" + i, "payload": m}
            msg.append(temp)

        publish.multiple(msg, hostname="120.96.63.80")

    # TODO:手把按鈕發送訊息給遊戲室
    def left(self):

        m = json.dumps(
            {
                "type": "move",
                "client": client_id,
                "player": self.players,
                "static": "left",
            },
            sort_keys=True
        )
        Thread(target=self.sss, kwargs={'m': m}).start()

    # TODO:手把按鈕發送訊息給遊戲室
    def right(self):

        m = json.dumps(
            {
                "type": "move",
                "client": client_id,
                "player": self.players,
                "static": "right",
            },
            sort_keys=True
        )
        Thread(target=self.sss, kwargs={'m': m}).start()

    #TODO:設定player1 or 2
    def set_players(self, a):

        self.players = a

    # TODO:用執行緒把訊息送至MQTT
    def sss(self, m):
        temp = self.room_id
        if not temp == None or not temp == "":
            publish.single("pon/" + temp, m, hostname='120.96.63.80', qos=0)

    # TODO:app關閉
    def on_stop(self):
        if self.mqtt_client!=None:
            self.mqtt_client.loop_stop()
            self.mqtt_client.disconnect()

        # sys.exit(0)

if __name__ == '__main__':
    import signal
    # signal.signal(signal.SIGINT, signal_handler)
    # signal.signal(signal.SIGTSTP, signal_handler)
    window_color = "#e3e7e3"
    Window.clearcolor = get_color_from_hex(window_color)
    PongApp().run()
