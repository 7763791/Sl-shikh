[app]
title = WorkshopApp
package.name = workshopapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
version = 0.1

# إضافة pillow ضرورية جداً لتشغيل KivyMD ومعالجة الصور
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow

orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.3.0
fullscreen = 0

# إعدادات الأندرويد المتوافقة مع سجلاتك
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# التأكد من إضافة ملف الخط Cairo-Regular.ttf
android.add_assets = Cairo-Regular.ttf

[buildozer]
log_level = 2
warn_on_root = 1
