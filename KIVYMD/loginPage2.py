from kivymd.app import MDApp as jbsidis
from kivy.lang import Builder as jbsidisx


class loginApp(jbsidis):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def build(self):
        return  jbsidisx.load_string(M)
M="""
#:import Window kivy.core.window.Window
Screen:
    bg_color: (1,1,1,.3)
    highlight_color1jbsidis: [0,0,0,0]
    highlight_color2jbsidis: (0,0,0,.3)
    canvas.before:
        Color:
            rgba: [1,1,1,1]
        Rectangle:
            size: self.size
            pos: self.pos
            source: "logo.png"
    FloatLayout:
        MDIconButton:
            size_hint: .4, .05
            pos_hint: {"center_x": .1, "top": .975}
            text: "Back"
            icon: 'chevron-left'
            markup: True
        TextInput:
            id: email_jbsidis
            hint_text_color: [0,0,0, 1]
            foreground_color: [1,1,1,1]
            hint_text: "Email"
            background_color: [0,0,0,0]
            background_image: ""
            background_normal: ""
            background_active: ""
            multiline: False
            size_hint: .7 ,.1 #.06
            pos_hint: {'center_x':.5, 'center_y':.8} #'center_y':.8
            canvas.before:
                Color:
                    rgba: root.highlight_color2jbsidis if root.ids.email_jbsidis.focused else [1,1,1,.5]
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: 10,
        FloatLayout:
            MDIconButton:
                text: "[u]Reset password[/u]"
                icon: 'email-send-outline'
                markup: True
                color: Window.clearcolor
                opposite_colors: True
                pos_hint: {'center_x':.8, 'center_y':.8}    
        TextInput:
            id: password_jbsidis
            hint_text: "Password"
            foreground_color: [1,1,1,1]
            background_color: [0,0,0,0]
            background_image: ""
            background_normal: ""
            background_active: ""
            multiline: False
            password: True
            size_hint: .7 ,.1 #.06
            pos_hint: {'center_x':.5, 'center_y':.65}
            canvas.before:
                Color:
                    rgba: root.highlight_color2jbsidis if root.ids.password_jbsidis.focused else [1,1,1,.5]
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: 10,
        FloatLayout:
            MDIconButton:
                icon: 'lock-outline'
                markup: True
                color: Window.clearcolor
                opposite_colors: True
                pos_hint: {'center_x':.8, 'center_y':.65}
        MDIconButton:
            id: jbsidis_s
            text: "[u]Reset password[/u]"
            icon: 'lock-open-outline'
            markup: True
            color: Window.clearcolor
            pos: password_jbsidis.pos[0]+password_jbsidis.size[0], password_jbsidis.pos[1]+dp(4)
            pos_x: password_jbsidis.pos[0]
            opposite_colors: True
        MDRaisedButton:
            id: jbsidis_i
            text: "Sign In"
            pos_hint: {"center_x": .5, "top": .5}
        MDRaisedButton:
            id: button_jbsidis
            text: "Sign up"
            size_hint: .2 ,.05
            pos_hint: {"right": .85, "center_y": .1}
            opacity: 0
            disabled: True
            bg_color: (0,0,0,1)
            color: [0,0,0,1] 
"""
loginApp().run()