import os

# هذا الجزء يضمن نجاح البناء في GitHub Actions دون أخطاء الواجهة
if os.environ.get('GITHUB_ACTIONS'):
    print("GitHub Actions environment detected. Building APK only...")
else:
    # الكود الذي سيظهر لك عند فتح التطبيق في هاتفك
    from kivymd.app import MDApp
    from kivymd.uix.label import MDLabel
    from kivy.lang import Builder

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
        
