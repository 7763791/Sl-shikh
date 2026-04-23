[app]
# (str) Title of your application
title = Workshop Master
# (str) Package name
package.name = workshopmaster
# (str) Package domain (needed for android/ios packaging)
package.domain = org.test
# (str) Source code where the main.py live
source.dir = .
# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,db
# (str) Application versioning (method 1)
version = 1.0
# (list) Application requirements
requirements = python3,kivy,kivymd,sqlite3
# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait
# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0
# (list) Permissions
android.permissions = INTERNET

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2
# (int) Display build warnings
warn_on_root = 1
