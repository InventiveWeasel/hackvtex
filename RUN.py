from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.lang import Builder


class CustDrop(DropDown):
    def __init__(self, **kwargs):
        super(CustDrop, self).__init__( **kwargs)
        self.select('')


kv_str = Builder.load_string('''
#:import os os


BoxLayout:
    orientation: 'vertical'
    BoxLayout:
        canvas.before:
            Rectangle:
                pos: self.pos
                size: self.size
            Color:
                rgb: (1,1,1)
        size_hint_y:1

        Button:
            id: btn
            text: 'test'
            on_release: dropdown.open(self)
            #size_hint_y: None
            #height: '48dp'  


        CustDrop:

            id: dropdown

            Button:
                text: 'Run another script'
                size_hint_y: None
                height: '48dp'
                on_release: os.system("python main_test.py")

        Label:
            size_hint_x: 4

    Label:
        size_hint_y: 9

''')


class ExampleApp(App):
    def build(self):
        return kv_str

if __name__ =='__main__':
    ExampleApp().run()
