import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.core.window import Window
import subprocess
import time
from threading import Thread, Event

kivy.require('2.0.0')

class MacroApp(App):
    def build(self):
        self.press_interval = 1.0  # Valor padrão para o intervalo de pressão (1 segundo)
        
        Window.size = (250, 400)
        # Layout para organizar os widgets
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Título informativo
        label = Label(text="Macro App", font_size=20, size_hint=(1, 0.1), color=(1, 1, 1, 1))

        # Botões para pressionar cada tecla repetidamente
        self.q_button = Button(text="Pressionar Q Repetidamente", font_size=20, size_hint=(1, 0.1), background_normal='', background_color=(0.4, 0.7, 0.2, 1))
        self.q_button.bind(on_press=self.press_q_repeatedly)

        self.w_button = Button(text="Pressionar W Repetidamente", font_size=20, size_hint=(1, 0.1), background_normal='', background_color=(0.4, 0.7, 0.2, 1))
        self.w_button.bind(on_press=self.press_w_repeatedly)

        self.e_button = Button(text="Pressionar E Repetidamente", font_size=20, size_hint=(1, 0.1), background_normal='', background_color=(0.4, 0.7, 0.2, 1))
        self.e_button.bind(on_press=self.press_e_repeatedly)

        # Stop buttons for each key
        self.stop_q_button = Button(text="Parar Q", font_size=20, size_hint=(1, 0.1), background_normal='', background_color=(0.7, 0.2, 0.2, 1), disabled=True)
        self.stop_q_button.bind(on_press=self.stop_q)

        self.stop_w_button = Button(text="Parar W", font_size=20, size_hint=(1, 0.1), background_normal='', background_color=(0.7, 0.2, 0.2, 1), disabled=True)
        self.stop_w_button.bind(on_press=self.stop_w)

        self.stop_e_button = Button(text="Parar E", font_size=20, size_hint=(1, 0.1), background_normal='', background_color=(0.7, 0.2, 0.2, 1), disabled=True)
        self.stop_e_button.bind(on_press=self.stop_e)

        # Slider para ajustar a velocidade do aperto das teclas
        self.speed_slider = Slider(min=0.1, max=10.0, value=0.5, step=0.1, size_hint=(1, 0.1))
        self.speed_slider.bind(value=self.on_slider_value_change)

        # Adiciona todos os widgets ao layout
        layout.add_widget(label)
        layout.add_widget(self.q_button)
        layout.add_widget(self.stop_q_button)
        layout.add_widget(self.w_button)
        layout.add_widget(self.stop_w_button)
        layout.add_widget(self.e_button)
        layout.add_widget(self.stop_e_button)
        layout.add_widget(self.speed_slider)

        return layout

    def on_slider_value_change(self, instance, value):
        # Ajusta o intervalo de pressionamento de forma inversa
        # Ajuste o valor máximo para tornar o intervalo menor, resultando em pressionamentos mais rápidos
        self.press_interval = max(0.01, 1 / value)  # Definindo o mínimo intervalo como 0.01 segundos
        print(f"Intervalo de pressões ajustado para: {self.press_interval} segundos.")

    def press_q_repeatedly(self, instance):
        self.stop_q_button.disabled = False
        if not hasattr(self, 'q_event'):
            self.q_event = Event()
            self.q_thread = Thread(target=self.press_q_continuously)
            self.q_thread.start()

    def press_q_continuously(self):
        ahk_path = r"C:\Program Files\AutoHotkey\UX\AutoHotkeyUX.exe"
        script_path = r"C:\Users\Anderson\Documents\Nova pasta\key_macro.ahk"  # Caminho do script AHK
        while not self.q_event.is_set():
            subprocess.run([ahk_path, script_path, "q", str(int(self.press_interval * 1000))])
            time.sleep(self.press_interval)

    def stop_q(self, instance):
        self.q_event.set()
        self.stop_q_button.disabled = True
        print("Parou de pressionar Q.")

    def press_w_repeatedly(self, instance):
        self.stop_w_button.disabled = False
        if not hasattr(self, 'w_event'):
            self.w_event = Event()
            self.w_thread = Thread(target=self.press_w_continuously)
            self.w_thread.start()

    def press_w_continuously(self):
        ahk_path = r"C:\Program Files\AutoHotkey\UX\AutoHotkeyUX.exe"
        script_path = "key_macro.ahk"
        while not self.w_event.is_set():
            subprocess.run([ahk_path, script_path, "w", str(int(self.press_interval * 1000))])
            time.sleep(self.press_interval)

    def stop_w(self, instance):
        self.w_event.set()
        self.stop_w_button.disabled = True
        print("Parou de pressionar W.")

    def press_e_repeatedly(self, instance):
        self.stop_e_button.disabled = False
        if not hasattr(self, 'e_event'):
            self.e_event = Event()
            self.e_thread = Thread(target=self.press_e_continuously)
            self.e_thread.start()

    def press_e_continuously(self):
        ahk_path = r"C:\Program Files\AutoHotkey\UX\AutoHotkeyUX.exe"
        script_path = "key_macro.ahk"
        while not self.e_event.is_set():
            subprocess.run([ahk_path, script_path, "e", str(int(self.press_interval * 1000))])
            time.sleep(self.press_interval)

    def stop_e(self, instance):
        self.e_event.set()
        self.stop_e_button.disabled = True
        print("Parou de pressionar E.")

if __name__ == '__main__':
    MacroApp().run()
