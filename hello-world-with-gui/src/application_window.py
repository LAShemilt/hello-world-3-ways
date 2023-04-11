import gi
gi.require_version('Gtk', '4.0')
gi.require_version("Gdk","4.0")
from gi.repository import Gtk, Gdk
class AppWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs,
        default_height=230,
            default_width=500,)

        self.box= Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        
        self.box2=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box3=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box4=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.set_child(self.box)
        self.box.append(self.box2)
        self.box.append(self.box3)
        self.box.append(self.box4)
    
        

        self.button = Gtk.Button(label="Hello")
        self.box2.append(self.button)

        self.button.connect('clicked', self.hello)

        self.name_entry = Gtk.Entry()
        self.box3.append(self.name_entry)


    def hello(self, button):
        self._name = self.name_entry.get_text()
        if self._name:
           self.name_box=Gtk.Label(label=f"Hello {self._name}")
        else:
            self.name_box= Gtk.Label(label="Hello world")
        self.box4.append(self.name_box)













