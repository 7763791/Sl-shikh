from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import sqlite3


# ================= قاعدة البيانات =================
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

    c.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        item TEXT,
        qty INTEGER,
        profit REAL,
        total_sell REAL DEFAULT 0
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS archive (
        name TEXT,
        details TEXT,
        tw REAL,
        th REAL,
        tm2 REAL,
        tcash REAL
    )
    """)

    conn.commit()
    conn.close()


# ================= شاشة رئيسية =================
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # عنوان
        layout.add_widget(Label(
            text="نظام الورشة المتكامل",
            font_size=24,
            size_hint_y=None,
            height=60
        ))

        # الحقوق
        layout.add_widget(Label(
            text="إعداد / طه غراب",
            font_size=10,
            size_hint_y=None,
            height=25
        ))

        # سعر المتر
        self.price = TextInput(
            hint_text="سعر متر الألمنيوم",
            multiline=False,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(self.price)

        # أزرار النظام (نفس فكرتك)
        layout.add_widget(Button(text="المخزون"))
        layout.add_widget(Button(text="المبيعات"))
        layout.add_widget(Button(text="جدول المقاسات"))
        layout.add_widget(Button(text="الأرباح"))
        layout.add_widget(Button(text="أرشيف العملاء"))

        self.add_widget(layout)


# ================= التطبيق =================
class WorkshopApp(App):
    def build(self):
        init_db()

        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main"))

        return sm


if __name__ == "__main__":
    WorkshopApp().run()
