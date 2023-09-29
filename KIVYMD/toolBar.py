from kivymd.app import MDApp
from kivy.lang.builder import Builder

KV="""
MDBoxLayout:
    orientation:"vertical"
    MDTopAppBar:
        title:"Let's Connect"
        left_action_items:[["menu",lambda x:x]]
        right_action_items:[["clock"],["git"],["github"]]
        elevation:17

    MDBottomAppBar:
        MDTopAppBar:
            title: "Let's Connect"
            icon: "play"
            type: "bottom"
            left_action_items:[["menu"]]
            # on_action_button: app.callback(self.icon)

    MDLabel:
        text: "Profile Here"
        halign : "center"


"""


class ToolBarApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

ToolBarApp().run()
        