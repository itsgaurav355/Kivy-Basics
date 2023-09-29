from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.clearcolor=(1,1,1,1)
Window.size=(330,520)

class InputApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical",spacing=20,padding="250px")

        self.email = TextInput(text = "Enter Your E-mail ")
        self.password = TextInput(text="Enter Your Password ")
        self.btn1 = Button(text="LOG IN",on_press=self.submission)
        
        layout.add_widget(self.email)
        layout.add_widget(self.password)
        layout.add_widget(self.btn1)
       
        return layout

    def submission(self,obj):
        print(f"Your Email : {self.email.text}")
        print(f"Your Password : {self.password.text}")

        

InputApp().run()