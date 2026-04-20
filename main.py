import os
import sqlite3
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivy.core.window import Window

# 1. إعدادات تجنب مشاكل كرت الشاشة على السيرفر
os.environ['KIVY_NO_ARGS'] = '1'

# 2. تصميم الواجهة (KV Language)
KV = '''
MDFloatLayout:
    MDLabel:
        id: title_label
        text: "نظام إدارة ورشة الألمنيوم"
        halign: "center"
        pos_hint: {"center_y": .8}
    
    MDTextField:
        id: sale_item
        hint_text: "اسم القطعة"
        size_hint_x: .8
        pos_hint: {"center_x": .5, "center_y": .6}
        
    MDTextField:
        id: sale_qty
        hint_text: "الكمية"
        size_hint_x: .8
        pos_hint: {"center_x": .5, "center_y": .5}
        input_filter: "int"
        
    MDRaisedButton:
        text: "تسجيل المبيعات"
        pos_hint: {"center_x": .5, "center_y": .3}
        on_release: app.record_sale()
'''

class WorkshopApp(MDApp):
    def build(self):
        # 3. إعداد قاعدة البيانات
        self.conn = sqlite3.connect('workshop.db')
        self.conn.execute('CREATE TABLE IF NOT EXISTS inv (item TEXT, qty INTEGER)')
        self.conn.commit()
        return Builder.load_string(KV)

    def record_sale(self):
        item = self.root.ids.sale_item.text
        qty = self.root.ids.sale_qty.text
        if item and qty:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO inv (item, qty) VALUES (?, ?)", (item, int(qty)))
            self.conn.commit()
            print("تم تسجيل المبيعات بنجاح")

if __name__ == "__main__":
    WorkshopApp().run()
    
