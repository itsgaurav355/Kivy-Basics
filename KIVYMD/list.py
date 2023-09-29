from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.list import MDList,OneLineListItem,TwoLineListItem,OneLineAvatarIconListItem
from kivymd.uix.scrollview import MDScrollView

class ListApp(MDApp):
    def build(self):
        gaurav=["Gaurav","Aditi","Jay","Sammit","Shreyas","Munde","Bibin","Geeta","Sejal","Ancial"]
        view =MDScrollView()
        mylist =MDList()
        i=1
        for j in gaurav:
        # item = OneLineListItem(text=f"Item {i}")
            item = TwoLineListItem(text=f"{j}", secondary_text=f"Item {i}")
            mylist.add_widget(item)
            
            i=i+1
    
        view.add_widget(mylist)
        
        return view

    


ListApp().run()