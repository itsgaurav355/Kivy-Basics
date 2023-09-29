from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        btn = Button(text="Submit",size_hint= (0.3,0.4),pos_hint={"center_x":0.5,"center_y":0.5},
        font_size="20sp",on_press=self.btn_click)
        return btn

    def btn_click(self,btn):
        print("Button Clicked")

ButtonApp().run()