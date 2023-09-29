from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

class DialogueApp(MDApp):
    def build(self):
        close_btn = MDFlatButton(text="Nope",on_release=self.close_dialog)
        more_btn = MDFlatButton(text="Yes")
        self.dialog = MDDialog(title="Exit",text="Do you want to Exit ? ",size_hint=(0.7,1),buttons = [close_btn,more_btn])
        self.dialog.open()
        
    def close_dialog(self,obj):
        self.dialog.dismiss()
        



    

DialogueApp().run()
