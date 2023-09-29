from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screen import MDScreen

class MyTheme(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Blue"
        
        btn = MDRectangleFlatButton(text="HELLO GAURAV!!" ,pos_hint={"center_x":0.5,"center_y":0.5})
        
        return btn


MyTheme().run()