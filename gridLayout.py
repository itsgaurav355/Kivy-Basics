from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.clearcolor=(1,1,1,1)
Window.size=(330,520)

class GridApp(App):
    def build(self):
        layout = GridLayout(rows=2,row_default_height=40,row_force_default=True)
        
        btn1 = Button(text="Submit 1")
        btn2 = Button(text="Submit 2")
        btn3 = Button(text="Submit 3")
        btn4 = Button(text="Submit 4")
        btn5 = Button(text="Submit 5")
        
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        layout.add_widget(btn5)
        
        return layout

GridApp().run()