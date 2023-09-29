from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class HelloApp(MDApp):
    def build(self):
        txt = MDLabel(text="Gaurav !! ",halign="center",font_style="H1",theme_text_color="Custom",text_color = (65/255.0, 232/255.0, 221/255.0,1))
        return txt


HelloApp().run()

