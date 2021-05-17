from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config

class Scr1(Screen):
    def __init__(self,name='first'):
        super().__init__(name=name)
        l1=BoxLayout(orientation="vertical")
        label=Label(text='[size=20][b]Hello[/b][/size]')
        label2=Label(text="Калькулятор")
        btn=Button(text="Начать")
        l1.add_widget(label)
        l1.add_widget(label2)
        l1.add_widget(btn)
        self.add_widget(l1)
        btn.on_press=self.next

    def next(self):
        self.manager.current='second'

class Scr2(Screen):
    def __init__(self,name='second'):
        super().__init__(name=name)
        l1=BoxLayout(orientation="vertical")
        label=Label(text='[size=20][b]Hello[/b][/size]')
        label2=Label(text="Калькулятор")
        btn=Button(text="Начать")
        l1.add_widget(label)
        l1.add_widget(label2)
        l1.add_widget(btn)
        self.add_widget(l1)
        btn.on_press=self.next

    def next(self):
        self.manager.current='second'


class MyApp(App):
    def build(self):
        sm=ScreenManager()
        sm.add_widget(Scr1(name="first"))
        sm.add_widget(Scr2(name="second"))
        
        return sm


MyApp().run()