import webbrowser
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
from crypto import decrypt
import os
# Глобальные переменные
outputtext = ''
weblink = ''
togglflag = True
togglcrypt = False
elements = ['']
leb = Label(text=outputtext, size_hint_y=None, height='48dp', font_size='24dp')


class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = ('vertical')
        # Adding camera to UI
        self.cam = Camera(play=True, resolution=(1280, 720))
        self.add_widget(self.cam)

        # UI Buttons
        self.stopbut = ToggleButton(text='Camera: ON', state='down', size_hint_y=None, height='48dp', on_press=self.change_state)
        self.cyphbut = ToggleButton(text='Encryption: OFF', size_hint_y=None, height='48dp', on_press=self.toggle_crypto)

        self.add_widget(self.stopbut)
        self.add_widget(self.cyphbut)

        # Screen refresh rate
        Clock.schedule_interval(self.update, 1.0 / 30)

    def update(self, dt):
        # if self.cam.texture:
        #     print("We got texture!")  # Checking whether the cam is working
        global weblink, elements
        # Creating texture
        texture = self.cam.texture
        size = texture.size
        pixels = texture.pixels

        # Checking whether we got pixels
        if not pixels:
            print("Error: Null pixels!")
            return

        # Reorganize using NumPy
        frame = np.frombuffer(pixels, dtype=np.uint8).reshape(size[1], size[0], 4)  # (H, W, 4) - RGBA
        # Convert to BGR
        frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB)
        frame = cv2.flip(frame, 1)
        # Decoding QR-codes
        qrcodes = decode(frame)
        for qrcode in qrcodes:
            # x, y, w, h = qrcode.rect  # For displaying text above QR
            # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            data = qrcode.data.decode("utf-8")
            # cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            leb.text = data

            # Decoding encrypted data and organizing it in list
            if togglcrypt == True:
                data = decrypt(data)
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
            weblink = data
            self.change_screen()


    def change_state(self, *args):
        # Stopping and running camera
        global togglflag
        if togglflag:
            self.stopbut.text = 'Camera: OFF'
            self.cam.play = False
        else:
            self.stopbut.text = 'Camera: ON'
            self.cam.play = True
        togglflag = not togglflag

    def toggle_crypto(self, *args):
        global togglcrypt
        if togglcrypt == False:
            togglcrypt = True
            self.cyphbut.text = 'Encryption: ON'
        else:
            togglcrypt = False
            self.cyphbut.text = 'Encryption: OFF'
    def change_screen(self, *args):
        # Opening another screen after scanning
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
        # Opening clear links in browser
        html_filename = "index.html"
        with open(html_filename, 'w+') as f:
            f.write(weblink)
            f.close()
        if togglcrypt == False:
            webbrowser.open(weblink)
        else: # Opening encrypted text in the app
            leb1 = Label(text='Name: ' + elements[0], size_hint_y=None, height='48dp', font_size='24dp')
            leb2 = Label(text='Processor: ' + elements[1], size_hint_y=None, height='48dp', font_size='24dp')
            leb3 = Label(text='Display: ' + elements[2], size_hint_y=None, height='48dp', font_size='24dp')
            leb4 = Label(text='RAM: ' + elements[3], size_hint_y=None, height='48dp', font_size='24dp')
            leb5 = Label(text='Size of HDD: ' + elements[4], size_hint_y=None, height='48dp', font_size='24dp')
            leb6 = Label(text='Power: ' + elements[5], size_hint_y=None, height='48dp', font_size='24dp')

            self.add_widget(leb1)
            self.add_widget(leb2)
            self.add_widget(leb3)
            self.add_widget(leb4)
            self.add_widget(leb5)
            self.add_widget(leb6)



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
