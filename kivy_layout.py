from kivy.app import App
from kivy.lang import Builder

class convert_m_km(App):
    def build(self):
            self.title = "Convert Miles to Kilometres"
            self.root = Builder.load_file('kivy_layout.kv')
            return self.root
    def something(self):
        pass




convert_m_km().run()