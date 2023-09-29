from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen , ScreenManager

KV = """
ScreenManager:
    MenuScreen:
    ShowMenuScreen:
<MenuScreen>:
    name : "Menu" #id of first screen
    MDRectangleFlatButton:
        text: "Show Menu"
        pos_hint:{"center_x":0.5,"center_y":0.5}
        on_press: root.manager.current = "MyMenu"
<ShowMenuScreen>:
    name:"MyMenu" #id for 2nd Screen
    MDLabel : 
        text:"Welcome"
        halign:"center"
    MDRectangleFlatButton:
        text:"Back"
        post_hint:{"center_x":0.5,"center_y":0.4}
        on_press: root.manager.current = "Menu"

"""
class MenuScreen(Screen):
        pass

class ShowMenuScreen(Screen):
        pass

class MultiScreen(MDApp):
     pass
if __name__ == "__main__":
    MultiScreen().run()