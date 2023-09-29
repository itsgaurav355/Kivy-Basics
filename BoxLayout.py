from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.clearcolor=(1,1,1,1)
Window.size=(330,520)

class MyButtonApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical",spacing=10,padding="15px")
        
        btn1 = Button(text="Submit 1")
        btn2 = Button(text="Submit 2")
        btn3 = Button(text="Submit 3")
        btn4 = Button(text="Submit 4")
        
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        
        return layout

MyButtonApp().run()