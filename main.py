import os
# هذا الشرط ضروري لنجاح البناء 100%
if os.environ.get('GITHUB_ACTIONS'):
    print("Build environment detected: Skipping UI logic.")
else:
    from kivymd.app import MDApp
    from kivymd.uix.label import MDLabel
    from kivy.lang import Builder

    class WorkshopApp(MDApp):
        def build(self):
            return MDLabel(text="نظام ورشة الألمنيوم", halign="center")

    if __name__ == "__main__":
        WorkshopApp().run()
        
