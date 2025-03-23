[app]
title = QR
package.name = qr
package.domain = org.qr
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,html
version = 0.1
requirements = python3,kivy,opencv,pyzbar,numpy, python-for-android
orientation = landscape
android.permissions = CAMERA, INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, QUERY_ALL_PACKAGES
android.api = 30
android.minapi = 24
android.ndk = 25b
android.arch = arm64-v8a
p4a.branch = master
p4a.fork = kivy
p4a.local_recipes = 

android.gradle_dependencies = com.android.support:support-v4:28.0.0
p4a.bootstrap = sdl2 
android.whitelist =
# Ускорение рендеринга и компиляции
android.ndk_api = 24
android.allow_backup = False

# Убираем отладочные логи в релизе
log_level = 2
