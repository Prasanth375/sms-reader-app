[app]
# (str) Title of your application
title = MyApp

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.myname

# (str) Source code where the main.py live (relative)
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements (comma separated)
requirements = python3,kivy

# (list) Supported orientations
orientation = portrait

# (str) Presplash & icon (uncomment to use)
# presplash.filename = %(source.dir)s/data/presplash.png
# icon.filename = %(source.dir)s/data/icon.png

# (bool) Fullscreen on Android
fullscreen = 0

# (list) Android permissions (uncomment if needed)
# android.permissions = INTERNET

[buildozer]
# (str) Path to Android SDK/NDK will be auto-managed by Buildozer.
# You can set android.sdk_path or android.ndk_path here if required.
log_level = 2
