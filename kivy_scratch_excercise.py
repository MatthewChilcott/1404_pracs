from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934

class convert_m_km(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('kivy_layout.kv')
        return self.root

    def handle_calculate(self):
        valid_value = self.get_validated_input()
        result = valid_value * MILES_TO_KM
        self.root.ids.output_text.text = str(result)

    def handle_increment(self, change_value):
        increment_value = self.get_validated_input() + change_value
        self.root.ids.input_text.text = str(increment_value)

    def get_validated_input(self):
        try:
            check_value = float(self.root.ids.input_text.text)
            return check_value
        except ValueError:
            return 0


convert_m_km().run()
