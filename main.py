from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import sqlite3


def init_db():
    conn = sqlite3.connect("workshop.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS inv (
        item TEXT,
        qty INTEGER,
        buy REAL,
        sell REAL
    )
    """)

    conn.commit()
    conn.close()


class MainUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)

        self.add_widget(Label(
            text="نظام الورشة المتكامل",
            font_size=24,
            size_hint_y=None,
            height=60
        ))

        self.add_widget(Label(
            text="إعداد / طه غراب",
            font_size=12,
            size_hint_y=None,
            height=30
        ))

        self.price = TextInput(
            hint_text="سعر متر الألمنيوم",
            multiline=False,
            size_hint_y=None,
            height=50
        )
        self.add_widget(self.price)

        self.add_widget(Button(text="المخزون"))
        self.add_widget(Button(text="المبيعات"))
        self.add_widget(Button(text="المقاسات"))
        self.add_widget(Button(text="الأرباح"))
        self.add_widget(Button(text="الأرشيف"))


class WorkshopApp(App):
    def build(self):
        init_db()
        return MainUI()


if __name__ == "__main__":
    WorkshopApp().run()
