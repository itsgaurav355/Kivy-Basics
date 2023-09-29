from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.screen import Screen


style="""
MDBoxLayout:
    orientation:"vertical"
    padding:90
    spacing : 10
    MDTextField:
        hint_text : "Enter Username or Email"
        helper_text : "username must be unique"
        helper_text_mode:"on_focus"
        icon_left:"account"
        pos_hint:{"center_x":0.5,"center_y":0.6}
        size_hint_x:None
        width : 300

    MDTextField:
        hint_text:"Enter Your Password"
        helper_text:""
        helper_text_mode:"on_focus"
        icon_left:"lock-off"
        pos_hint:{"center_x":0.5,"center_y":0.6}
        size_hint_x:None
        width:300

    MDRectangleFlatButton:
        text:"Login"
        pos_hint:{"center_x":0.5,"center_y":0.6}
        """

class LoginApp(MDApp):
    def build(self):
        scrn = Screen()
        bldr = Builder.load_string(style)
        scrn.add_widget(bldr)
        
        return scrn


LoginApp().run()
        