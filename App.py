from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar


class ConverterApp(MDApp):
    def flip(self):
        if self.state == 0:
            self.state = 1
            self.toolbar.title = "Decimal to Binary"
            self.input.text = "Enter a decimal number"
            self.label.text = ""
            self.converted.text = ""

        else:
            self.state = 0
            self.toolbar.title = "Binary to Decimal"
            self.input.text = "Enter a binary number"
            self.label.text = ""
            self.converted.text = ""

    def convert(self, args):
        try:
            if "." not in self.input.text:
                if self.state == 0:
                    val = int(self.input.text, 2)
                    self.label.text = "in decimal is-"
                    self.converted.text = str(val)

                else:
                    val = bin(int(self.input.text))[2:]
                    self.label.text = "in binary is-"
                    self.converted.text = val

            else:

                # if the input value is in fraction
                whole, fract = self.input.text.split(".")

                if self.state == 0:

                    whole = int(whole, 2)

                    floating = 0

                    for idx, digit in enumerate(fract):
                        floating += int(digit)*2**(-(idx+1))

                    self.label.text = "in decimal is- "
                    self.converted.text = str(whole+floating)

                else:

                    # convert decimal to binary
                    decimal_places = 10
                    whole = bin(int(whole))[2:]
                    fract = float("0."+fract)

                    floating = []
                    for i in range(decimal_places):
                        if fract*2 < 1:
                            floating.append("0")
                            fract *= 2

                        elif fract*2 > 1:
                            floating.append("1")
                            fract = fract*2-1

                        elif fract*2 == 1.0:
                            floating.append("1")
                            break

                    self.label.text = "in binary is- "
                    self.converted.text = whole+"."+"".join(floating)

        except ValueError:
            # if the user-provided value is invalid
            self.converted.text = ""
            if self.state == 0:
                # binary to decimal
                self.label.text = "please enter a valid binary number"
            else:
                # decimal to binary
                self.label.text = "please enter a valid decimal number"

    def build(self):
        self.theme_cls.primary_palette = "Purple"
        self.state = 0
        screen = MDScreen()

        self.toolbar = MDToolbar(title="Binary to Decimal Conversion")
        self.toolbar.pos_hint = {'top': 1}
        self.toolbar.right_action_items = [
            ["rotate-3d-variant", lambda x:self.flip()]]
        screen.add_widget(self.toolbar)

        # Image-
        screen.add_widget(Image(
            source="Desktop - 1.png",
            pos_hint={"center_x": 0.5, "center_y": 0.7}

        ))

        # collect user input-

        self.input = MDTextField(
            text="Enter the binary number",
            halign="center",
            size_hint=(0.8, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            font_size=25

        )

        screen.add_widget(self.input)

        # labels-

        self.label = MDLabel(

            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.35},
            theme_text_color="Secondary"

        )

        self.converted = MDLabel(

            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            theme_text_color="Primary",
            font_style="H5"
        )

        screen.add_widget(self.label)
        screen.add_widget(self.converted)

        # convert button-

        screen.add_widget(MDFillRoundFlatButton(
            text="Convert",
            font_size=18,
            pos_hint={"center_x": 0.5, "center_y": 0.15},
            on_press=self.convert
        ))
        return screen


if __name__ == '__main__':
    ConverterApp().run()
