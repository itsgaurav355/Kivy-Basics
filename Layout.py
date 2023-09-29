from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

# Window.clearcolor=(1,1,1,1)
# Window.size=(330,520)
"""Cannot Use It for Multiple Buttons in single line
class MyButtonApp(App):
    def build(self):
        layout = AnchorLayout(anchor_x='left',anchor_y='top')
        
        btn1 = Button(text="Submit 1",size_hint=(None,None),height=40,width=100)
        
        layout.add_widget(btn1)
        
        return layout"""

class MyButtonApp(App):
    def build(self):
        layout = FloatLayout()
        
        # btn1 = Button(text="Submit 1",size_hint=(None,None),height=40,width=100,pos_hint={"center_x":0.5,"center_y":0.6})
        btn1 = Button(text="Submit 1",size_hint=(None,None),height=40,width=100,pos_hint={"left":1,"top":1})
        # btn2 = Button(text="Submit 2",size_hint=(None,None),height=40,width=100,pos_hint={"left":1,"top":1})
        layout.add_widget(btn1) 
        # layout.add_widget(btn2)
        
        return layout

MyButtonApp().run()