from kivymd.app import MDApp
from kivymd.uix.label import MDIcon

class IconApp(MDApp):
    def build(self):
        return MDIcon(icon = "star",halign="center")

IconApp().run()