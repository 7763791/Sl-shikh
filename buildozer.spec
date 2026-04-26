[app]

# (str) Title of your application
title = WorkshopMasterPro

# (str) Package name
package.name = workshopmaster

# (str) Package domain (needed for android/ios packaging)
package.domain = org.workshop

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let include_exts be empty to include all files)
source.include_exts = py,png,jpg,kv,db

# (str) Application versioning
version = 1.0

# (list) Application requirements
requirements = python3,kivy

# (bool) Accept the Android SDK license
# هذا هو السطر الجوهري لحل مشكلتك
android.accept_sdk_license = True

# (str) Presplash of the application
#fullscreen = 0
orientation = portrait

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Warning when user is trying to run buildozer as root
warn_on_root = 1

# (int) Android API to use
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (str) Android architecture
android.arch = arm64-v8a
