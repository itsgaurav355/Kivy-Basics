from kivymd.app import MDApp
from kivy.lang import Builder


KV = """
MDFloatLayout:
    MDCard:
        size_hint: .45, .8
        pos_hint: {"center_x": .5, "center_y": .5}
        Carousel:
            id: slide
            MDFloatLayout:
                MDTextField:
                    hint_text: "First Name"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .48}
                MDTextField:
                    hint_text: "Last Name"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .36}
                MDRaisedButton:
                    text: "NEXT"
                    size_hint_x: .8
                    pos_hint: {"center_x" .5, "center_y": .2}
                    on_release: app.next()
             MDFloatLayout:
                MDTextField:
                    hint_text: "Email Address"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .48}
                MDTextField:
                    hint_text: "Phone number"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .36}
                MDRaisedButton:
                    text: "PREVIOUS"
                    size_hint_x: .39
                    pos_hint: {"center_x" .3, "center_y": .2}
                    on_release: app.previous1()
                MDRaisedButton:
                    text: "NEXT"
                    size_hint_x: .39
                    pos_hint: {"center_x" .7, "center_y": .2}
                    on_release: app.next1()
             MDFloatLayout:
                MDTextField:
                    hint_text: "Password"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .48}
                    password: True
                MDTextField:
                    hint_text: "Confirm Password"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .36}
                    password: True
                MDRaisedButton:
                    text: "PREVIOUS"
                    size_hint_x: .39
                    pos_hint: {"center_x" .3, "center_y": .2}
                    on_release: app.previous1()
                MDRaisedButton:
                    text: "SUBMIT"
                    size_hint_x: .39
                    pos_hint: {"center_x" .7, "center_y": .2}
    MDLabel:
        text: "SignUp Form"
        bold: True
        pos_hint: {"center_x": .88, "center_y": .8}
        font_style: "H4"
    MDLabel:
        id: Name
        text: "Name"
        pos_hint: {"center_x": .888, "center_y": .7}
        font_style: "H6"
        theme_text_color: "Custom"
    MDIconButton:
        id: name
        icon: "numeric-1-circle"
        pos_hint: {"center_x: .34, "center_y": .65}
        user_font_size: "35sp"
        theme_text_color: "Custom"
    MDProgressBar:
        id: progress
        size_hint_x: .1
        pos_hint: {"center_x": .42, "center_y": .65}
    MDLabel:
        id: Contact
        text: "Contact"
        pos_hint: {"center_x": .958, "center_y": .7}
        font_style: "H6"
        theme_text_color: "Custom"
    MDIconButton:
        id: contact
        icon: "numeric-2-circle"
        pos_hint: {"center_x: .5, "center_y": .65}
        user_font_size: "35sp"
        theme_text_color: "Custom"
    MDProgressBar:
        id: progress1
        size_hint_x: .1
        pos_hint: {"center_x": .58, "center_y": .65}
    MDLabel:
        id: Submit
        text: "Submit"
        pos_hint: {"center_x": 1.12, "center_y": .7}
        font_style: "H6"
        theme_text_color: "Custom" 
    MDIconButton:
        id: submit
        icon: "numeric-3-circle"
        pos_hint: {"center_x: .66, "center_y": .65}
        user_font_size: "35sp"
        theme_text_color: "Custom"
              
"""


class ProjectApp(MDApp):

    def build(self):
        kv = Builder.load_string(KV)
        return kv

    def next(self):
        self.root.ids.slide.load_next(mode="next")
        self.root.ids.Name.text_color = self.theme_cls.primary_color
        self.root.ids.progress.value = 100
        self.root.ids.name.text_color = self.theme_cls.primary_color
        self.root.ids.name.icon = "check-decagram"

    def next1(self):
        self.root.ids.slide.load_next(mode="next")
        self.root.ids.Contact.text_color = self.theme_cls.primary_color
        self.root.ids.progress1.value = 100
        self.root.ids.contact.text_color = self.theme_cls.primary_color
        self.root.ids.contact.icon = "check-decagram"

    def previous(self):
        self.root.ids.slide.load_previous()
        self.root.ids.name.text_color = 0, 0, 0, 1
        self.root.ids.Name.text_color = 0, 0, 0, 1
        self.root.ids.progress.value = 0
        self.root.ids.name.icon = "numeric-1-circle"

    def previous1(self):
        self.root.ids.slide.load_previous()
        self.root.ids.contact.text_color = 0, 0, 0, 1
        self.root.ids.Contact.text_color = 0, 0, 0, 1
        self.root.ids.progress1.value = 0
        self.root.ids.contact.icon = "numeric-2-circle"


if __name__ == "_main_":
    ProjectApp().run()
    