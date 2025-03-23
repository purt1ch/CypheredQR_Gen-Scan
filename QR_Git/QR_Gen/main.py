from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.camera import Camera
import numpy as np
import cv2
from pyzbar.pyzbar import decode
import webbrowser
from crypto import decrypt
# Глобальные переменные
outputtext = ''
weblink = ''
leb = Label(text=outputtext, size_hint_y=None, height='48dp', font_size='12dp')
togglflag = True
togglcrypt = False


class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = ('vertical')

        # Добавляем камеру в UI
        self.cam = Camera(play=True, resolution=(1920, 720))
        self.add_widget(self.cam)

        # Кнопки управления
        self.stopbut = ToggleButton(text='Съёмка', state='down', size_hint_y=None, height='48dp', on_press=self.change_state)
        self.cyphbut = ToggleButton(text='Шифрование Выключено', size_hint_y=None, height='48dp', on_press=self.toggle_crypto)

        self.add_widget(self.stopbut)
        self.add_widget(self.cyphbut)

        # Запускаем обновление кадров
        Clock.schedule_interval(self.update, 1.0 / 30)

    def update(self, dt):
        # if self.cam.texture:
        #     print("Текстура получена!")  # Проверка работы
        global weblink
        # Создаем новую текстуру
        texture = self.cam.texture
        size = texture.size
        pixels = texture.pixels

        # Проверяем, есть ли пиксели
        if not pixels:
            print("Ошибка: Пустые пиксели!")
            return

        # Преобразуем в NumPy
        frame = np.frombuffer(pixels, dtype=np.uint8).reshape(size[1], size[0], 4)  # (H, W, 4) - RGBA
        # Конвертируем в BGR
        frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB)
        frame = cv2.flip(frame, 1)
        # Декодируем штрих-коды
        barcodes = decode(frame)
        for barcode in barcodes:
            # x, y, w, h = barcode.rect  Для отображения текста над QR
            # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            data = barcode.data.decode("utf-8")
            # cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            if togglcrypt == True:
                data = decrypt(data)
                leb.text = data
                elements = ['']
                n = 0
                for i in data:
                    if i != ';':
                        elements[n] += i
                    else:
                        elements.append('')
                        n += 1
                        continue
                print(elements)
                data = f'<center> <table border="1" width="350" height="240"> <font size="+4">{elements[0]}</font></td><tr> <td align="centre"><h2>G8</td> <td><h2>{elements[1]}</td> <td><h2>(1920x1080)</td> </tr> <tr> <td><h2>{elements[2]}</td> <td><h2>{elements[3]}</td> <td><h2>{elements[4]}</td> </tr> <tr> <td><h2>SSD</td> <td><h2>{elements[5]}</td> <td><h2>FPR</td></h2> </tr></table> </center>'
            weblink = data
            self.change_screen()


    def change_state(self, *args):
        """Остановка и запуск камеры"""
        global togglflag
        if togglflag:
            self.stopbut.text = 'Съёмка'
            self.cam.play = False
        else:
            self.stopbut.text = 'Пауза'
            self.cam.play = True
        togglflag = not togglflag

    def toggle_crypto(self, *args):
        global togglcrypt
        if togglcrypt == False:
            togglcrypt = True
            self.cyphbut.text = 'Шифрование Включено'
        else:
            togglcrypt = False
            self.cyphbut.text = 'Шифрование Выключено'
    def change_screen(self, *args):
        """Переход на второй экран после сканирования"""
        main_app.sm.current = 'second'


class SecondScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.lab1 = Label(text='Output: ', size_hint_y=None, height='48dp', font_size='45dp')
        self.but1 = Button(text='Open in Web Browser', on_press=self.open_browser, size_hint_y=None, height='48dp')

        self.add_widget(self.lab1)
        self.add_widget(leb)
        self.add_widget(self.but1)

    def open_browser(self, *args):
        """Открытие ссылки в браузере"""
        with open('index.html', 'w+') as f:
            f.write(weblink)
            f.close()
        webbrowser.open('index.html')


class TestApp(App):
    def build(self):
        self.sm = ScreenManager()

        self.mainsc = MainScreen()
        scrn = Screen(name='main')
        scrn.add_widget(self.mainsc)
        self.sm.add_widget(scrn)

        self.secondsc = SecondScreen()
        scrn = Screen(name='second')
        scrn.add_widget(self.secondsc)
        self.sm.add_widget(scrn)

        return self.sm


if __name__ == '__main__':
    main_app = TestApp()
    main_app.run()
