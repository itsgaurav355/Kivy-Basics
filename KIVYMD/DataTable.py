from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.datatables import MDDataTable

class DataTableApp(MDApp):
    def build(self):
        layout = MDAnchorLayout()
        mytable=MDDataTable(
            size_hint = (0.7,0.6),
            check = True,
            use_pagination=True,
            column_data=[("No.",dp(30)),
            ("Price",dp(30)),
            ("Name",dp(60))],
            row_data=[
                ("1","250","Veg Momos"),
                ("2","300","Burger"),
                ("3","300","Biryani"),
                ("4","300","Biryani"),
                ("5","300","Biryani"),
                ("6","300","Biryani"),
                ("7","300","Biryani"),
                ("8","300","Biryani"),
                ("9","300","Biryani"),
                ("10","300","Biryani"),
            ]
        )
        layout.add_widget(mytable)
        return layout


DataTableApp().run()