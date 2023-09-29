from kivymd.app import MDApp
from kivymd.uix.stacklayout import MDStackLayout
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton,MDIconButton,MDFloatingActionButton

class ButtonApp(MDApp):
    def build(self):
        layout = MDStackLayout(padding="10px",width=50)
        btn1 = MDFlatButton(text="File",theme_text_color="Custom",text_color="purple"
        ,md_bg_color="aquamarine")
        btn2 = MDRectangleFlatButton(text="Edit",theme_text_color="Custom",text_color="purple"
        ,md_bg_color="aquamarine")
        btn3 = MDIconButton(icon="music",theme_text_color="Custom",text_color="red",halign="center" ,valign="center" ,md_bg_color="aqua")
        btn4 = MDFloatingActionButton(icon="music",theme_text_color="Custom",text_color="purple"
        ,md_bg_color="aquamarine")

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)

        return layout
        


ButtonApp().run()