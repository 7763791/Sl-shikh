[app]
title = Workshop Master
package.name = workshopmaster
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db
version = 1.0
requirements = python3,kivy,kivymd,sqlite3
orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# إعدادات أندرويد لضمان قبول التراخيص وعدم القفز للإصدار 37 غير المستقر
android.sdk = 33
android.build_tools_version = 33.0.1
android.ndk = 25b
android.api = 33
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
