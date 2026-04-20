import os
import sys

# هذا السطر يمنع Kivy من محاولة تشغيل الواجهة أثناء البناء
if os.environ.get('GITHUB_ACTIONS'):
    print("GitHub Actions environment detected. Skipping UI initialization.")
else:
    # هذا الكود سيعمل فقط عندما تشغل البرنامج على جهازك في الورشة
    from kivymd.app import MDApp
    from kivymd.uix.label import MDLabel
    from kivy.lang import Builder
    import sqlite3

    KV = '''
MDFloatLayout:
    MDLabel:
        text: "نظام إدارة ورشة الألمنيوم"
        halign: "center"
        pos_hint: {"center_y": .8}
    '''

    class WorkshopApp(MDApp):
        def build(self):
            return Builder.load_string(KV)

    if __name__ == "__main__":
        WorkshopApp().run()
        
