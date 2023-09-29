from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
 
Window.clearcolor = (1, 1, 1,1)

class LetsConnectApp(App):
    def  build(self):
        label = Label(text="Hello Enterprenurs",font_size = "50sp",bold=True,color=(0,0,1,1))
        return label


LetsConnectApp().run()

