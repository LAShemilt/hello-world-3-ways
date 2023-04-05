import gi
gi.require_version('Gtk', '4.0')
gi.require_version("Adw","1")
from gi.repository import Gtk, Adw
class AppWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.box = Gtk.Box()
        self.set_child(self.box)

        self.button = Gtk.Button(label="Hello")
        self.box.append(self.button)