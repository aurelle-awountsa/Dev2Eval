from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App


class CalculatorForm(BoxLayout):
    number1_input = ObjectProperty()
    number2_input = ObjectProperty()
    add_status = False
    sous_status = False
    mul_status = False
    div_status = False
    result_app = ObjectProperty()

    def on_checkbox_Active_add(self, instance, value):
        if value:
            self.add_status = True

        else:
            print("checkbox add off")
            self.add_status = True
            self.sous_status = False
            self.mul_status = False
            self.div_status = False

    def on_checkbox_Active_sous(self, checkboxInstance, value):
        if value:
            print("Checkbox sous on")
            self.add_status = False
            self.sous_status = True
            self.mul_status = False
            self.div_status = False
        else:
            print("checkbox sous off")
            self.sous_status = False

    def on_checkbox_Active_mul(self, checkboxInstance, value):
        if value:
            print("Checkbox mult on")
            self.add_status = False
            self.sous_status = False
            self.mul_status = True
            self.div_status = False
        else:
            print("checkbox mult off")
            self.mul_status = False

    def on_checkbox_Active_div(self, checkboxInstance, value):
        if value:
            print("Checkbox div on")
            self.add_status = False
            self.sous_status = False
            self.mul_status = False
            self.div_status = True
        else:
            print("checkbox div off")
            self.div_status = False

    def buttonClicked(self, btn):
        global tot
        try:
            if self.add_status:
                print(self.add_status)
                tot = int(self.number1_input.text) + int(self.number2_input.text)

            if self.sous_status:
                tot = int(self.number1_input.text) - int(self.number2_input.text)

            if self.mul_status:
                tot = int(self.number1_input.text) * int(self.number2_input.text)

            if self.div_status:
                tot = int(self.number1_input.text) / int(self.number2_input.text)

            if not self.div_status and not self.add_status and not self.sous_status and not self.mul_status:
                self.result_app.text = "veuillez choisir une operation"

            self.result_app.text = "le résultat est: {}".format(tot)

        except:
            self.result_app.text = "veuillez entrer un chiffre"


class CalculatorApp(App):
    pass


if __name__ == '__main__':
    CalculatorApp().run()
