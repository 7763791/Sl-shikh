from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivy.core.text import LabelBase
import sqlite3

# تسجيل الخط العربي
LabelBase.register(name="Cairo", fn_regular="Cairo-Regular.ttf")

KV = '''
MDScreen:
    MDBoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 15
        
        MDLabel:
            text: "نظام الورشة المتكامل"
            halign: "center"
            font_name: "Cairo"
            font_style: "H5"
            
        MDTextField:
            id: sale_item
            hint_text: "اسم الصنف"
        MDTextField:
            id: sale_qty
            hint_text: "الكمية"
            input_filter: "int"
        MDRaisedButton:
            text: "تسجيل مبيعات وخصم من المخزن"
            pos_hint: {"center_x": .5}
            on_release: app.record_sale()
            
        MDLabel:
            text: "المهندس/ طه غراب"
            halign: "right"
            font_name: "Cairo"
            font_size: "14sp"
            theme_text_color: "Hint"

class WorkshopApp(MDApp):
    def build(self):
        self.conn = sqlite3.connect('workshop_final_db.db')
        self.conn.execute('CREATE TABLE IF NOT EXISTS inv (item TEXT PRIMARY KEY, qty INTEGER)')
        return Builder.load_string(KV)

    def record_sale(self):
        item = self.root.ids.sale_item.text
        qty = self.root.ids.sale_qty.text
        if item and qty:
            cursor = self.conn.cursor()
            cursor.execute("UPDATE inv SET qty = qty - ? WHERE item = ?", (int(qty), item))
            self.conn.commit()
            print("تم الخصم بنجاح")

if __name__ == "__main__":
    WorkshopApp().run()
