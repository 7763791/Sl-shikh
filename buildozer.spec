[app]
title = Workshop Master
package.name = workshopmaster
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db
version = 1.0
requirements = python3,kivy==2.3.0,kivymd==1.2.0,sqlite3,cython==0.29.33
orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# إجبار النظام على إصدارات مستقرة (هذا هو الحل الجذري لفشل الترخيص)
android.sdk = 33
android.build_tools_version = 33.0.1
android.ndk = 25b
android.api = 33
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
