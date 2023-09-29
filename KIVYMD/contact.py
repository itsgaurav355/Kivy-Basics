from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.list import MDList,OneLineListItem,OneLineIconListItem,OneLineAvatarIconListItem

prop="""
MDScrollView:
    MDList:
        id:mylist
        # OneLineListItem:
        #     text:"Account Details"
        # OneLineIconListItem: 
        #     IconLeftWidget:
        #         icon:"instagram"

"""

class ContactApp(MDApp):
    def build(self):
        bldr = Builder.load_string(prop)
        return bldr

    def on_start(self):
        gaurav=["Gaurav","Aditi","Jay","Sammit","Shreyas","Munde","Bibin","Geeta","Sejal","Ancial"]
        for i in gaurav:
            self.root.ids.mylist.add_widget(
                OneLineListItem(text=f"{i}")
            )

ContactApp().run()