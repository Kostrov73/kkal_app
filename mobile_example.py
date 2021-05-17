from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen

from  instructions import *
from scrollLabel import * 

class FirstScr(Screen):
    def __init__(self,name='first'):
        super().__init__(name=name)
        lay1=BoxLayout(orientation='vertical')
        layh1=BoxLayout(size_hint=(1,.1))
        layh2=BoxLayout(size_hint=(1,.1))
        label_n=Label(text="Ваше имя: ")
        label_age=Label(text="Введите Ваш возраст: ")
        scl = ScrollLabel(ltext=txt_instruction,pos_hint={'center_y':.5})
        self.name_val=TextInput(text='', multiline=False, size_hint=(.75,.9), pos_hint={"top":1,'center_x':.5})
        self.age_val=TextInput(text='', multiline=False, size_hint=(.75,.9), pos_hint={"top":1,'center_x':.5})
        btn=Button(text="Продолжить",size_hint=(.33,.23), pos_hint={'top':0.5, 'center_x':.5})
        btn.on_press=self.next
        layh1.add_widget(label_n)
        layh2.add_widget(label_age)
        layh1.add_widget(self.name_val)
        layh2.add_widget(self.age_val)
        lay1.add_widget(scl)
        lay1.add_widget(layh1)
        lay1.add_widget(layh2)
        lay1.add_widget(btn)
        self.add_widget(lay1)

    def next(self):
        self.manager.current='second'


        
class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        lay1=BoxLayout(orientation='vertical')
        lay2=BoxLayout(size_hint=(1,.1))
        scrl=ScrollLabel(txt_test1,)
        label=Label(text='Введите результат:')
        self.ti=TextInput(text='', multiline=False, size_hint=(.75,.9), pos_hint={"top":1,'center_x':.5})
        btn=Button(text="Продолжить",size_hint=(.33,.23), pos_hint={'top':0.5, 'center_x':.5})
        btn.on_press=self.next
        lay2.add_widget(label)
        lay2.add_widget(self.ti)
        lay1.add_widget(scrl)
        lay1.add_widget(lay2)
        lay1.add_widget(btn)
        self.add_widget(lay1)

    def next(self):
        self.manager.current='third'

class ThirdScr(Screen):
    def __init__(self, name='third'):
        super().__init__(name=name)
        
class FourthScr(Screen):
    def __init__(self, name='fourth'):
        super().__init__(name=name)


class FivethScr(Screen):
    def __init__(self, name='fiveth'):
        super().__init__(name=name)


class SixthScr(Screen):
    def __init__(self, name='sixth'):
        super().__init__(name=name)
        




class MainScr(Screen):
    def __init__(self,name='main'):
        super().__init__(name=name)
        
        

class MyApp(App):
    def build(self):
        sm=ScreenManager()
        #sm.add_widget(MainScr(name='main'))
        sm.add_widget(FirstScr(name='first'))
        sm.add_widget(SecondScr(name='second'))
        sm.add_widget(ThirdScr(name='third'))
        sm.add_widget(FourthScr(name='fourth'))
        sm.add_widget(FivethScr(name='fiveth'))
        sm.add_widget(SixthScr(name='sixth'))
        return sm


MyApp().run()