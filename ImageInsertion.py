from kivy.app import App
from kivy.uix.image import Image, AsyncImage

class ImageApp(App):
    def build(self):
        img = Image(source="1.jpg",size_hint=(None,None),width=350,height=50,pos_hint = {"center_x": 0.5, "center_y":0.5})
        return img
ImageApp().run()