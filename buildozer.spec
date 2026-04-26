[app]
title = Workshop Master Pro
package.name = workshopmaster
package.domain = org.workshop

source.dir = .
source.include_exts = py,png,jpg,kv,db

version = 1.0

orientation = portrait
fullscreen = 0

# ✔ أهم جزء
requirements = python3,kivy,sqlite3

# لو عندك خطأ عربي لاحقاً (اختياري)
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1

# Android settings
android.api = 33
android.minapi = 21
android.ndk = 25b
android.arch = arm64-v8a
