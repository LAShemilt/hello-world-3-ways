import gi
gi.require_version('Gtk', '4.0')
gi.require_version("Gdk", "4.0")
from gi.repository import Gtk, Gdk
from .application_window import AppWindow



class HelloApp(Gtk.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.appwindow = AppWindow(application=app)
        self.appwindow.present()

