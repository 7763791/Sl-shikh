[app]
title = WorkshopApp
package.name = workshopapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
version = 0.1

# إضافة pillow ضرورية جداً لتشغيل KivyMD بدون مشاكل
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow

orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.3.0
fullscreen = 0

# إعدادات الأندرويد (متوافقة مع سجلات الخطأ السابقة)
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# إضافة الخط Cairo-Regular.ttf كمورد أساسي
android.add_assets = Cairo-Regular.ttf

[buildozer]
log_level = 2
warn_on_root = 1
