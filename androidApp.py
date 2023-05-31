
#https://www.techwithtim.net/tutorials/kivy-tutorial/creating-buttons-triggering-events


import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from main import getYoutubeLink,downloadTheSong

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="Enter Youtube URL's to download : "))
        self.urls = TextInput(multiline=True)
        self.inside.add_widget(self.urls)

        self.inside.add_widget(Label(text="Download Progress : "))
        self.lastName = TextInput(multiline=False)
        self.inside.add_widget(self.lastName)

        self.inside.add_widget(Label(text="User Information Box : "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.download = Button(text="Click To Download", font_size=40)
        self.download.bind(on_press=self.pressed)
        self.add_widget(self.download)

    def pressed(self, instance):
        urls = self.urls.text
        last = self.lastName.text
        email = self.email.text

        print("Entered URL's:", urls, "Last Name:", last, "Email:", email)
        yt = getYoutubeLink(urls)
        downloadTheSong(yt)

        self.urls.text = ""
        self.lastName.text = ""
        self.email.text = ""

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()