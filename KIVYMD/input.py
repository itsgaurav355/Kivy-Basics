from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField

class InputApp(MDApp):
    def build(self):
        layout = MDBoxLayout(orientation="vertical",spacing=10,padding=250)
        
        email = MDTextField(text="Email or Phone No",pos_hint={"center_x":0.5,"center_y":0.5})
        password = MDTextField(text="Enter your Password",pos_hint={"center_x":0.5,"center_y":0.5})
        btn = MDRectangleFlatButton(text="LogIn",pos_hint={"center_x":0.5,"center_y":0.5})
        
        layout.add_widget(email)
        layout.add_widget(password)
        layout.add_widget(btn)

        return  layout

InputApp().run()
        