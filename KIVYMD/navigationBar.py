from kivymd.app import MDApp
from kivy.lang.builder import Builder

kv = """
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#03012b"
    text_color: "#fcfcfc"
    icon_color: "#fcfcfc"
    ripple_color : "aquamarine"
    selected_color : "#fcfcfc"

<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#fcfcfc"
    icon_color: "#fcfcfc"
    focus_behavior: False
    selected_color : "#fcfcfc"
    no_ripple_effect:True

MDScreen:

    MDNavigationLayout:

        MDScreenManager:

            MDScreen:

                MDTopAppBar:
                    title : "Let's Connect"
                    elevation: 4 
                    pos_hint:{"top":1}
                    md_bg_color: "#03012b"
                    specific_text_coolor: "#fcfcfc"
                    left_action_items : [["menu",lambda x: nav_drawer.set_state("open")]]

        MDNavigationDrawer:
            id:nav_drawer
            radius : (0,16,16,0)

            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    title : "Gaurav"
                    title_color: "#fcfcfc"
                    text:"Comapany Name"
                    spacing:"4dp"
                    padding: "12dp","10dp",0,"56dp"
                    Image:
                        id:profile-img
                        source: "logo.png"
                        
                
                    

                MDNavigationDrawerLabel:
                    text: "Mail"

                DrawerClickableItem:
                    icon:"send"
                    right_text: "+99"
                    right_text_color: "#fcfcfc"
                    text:"Connect"
                
                DrawerClickableItem:
                    icon: "message"
                    text: "Chats"

                MDNavigationDrawerDivider:

                MDNavigationDrawerLabel:
                    text: "Company Name"

                DrawerLabelItem:
                    icon: "information-outline"
                    text: "About Us"

                DrawerLabelItem:
                    icon: "information-outline"
                    text: "established in 1987"

""" 
class NavBarApp(MDApp):
    def build(self):

        self.theme_cls.theme_style="Dark"
        b= Builder.load_string(kv)
        return b


NavBarApp().run()