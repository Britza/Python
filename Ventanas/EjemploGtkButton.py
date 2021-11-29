import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplication(Gtk.Window):

    def __init__(self):
        super().__init__(title="Ex de uso de Gtk.Button")

        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.add(caixaH)

        # btnBoton = Gtk.Button(label="Etiqueta")
        # btnBoton = Gtk.Button.new_with_label("Etiqueta")
        btnBotonAbrir = Gtk.Button.new_with_mnemonic("_Abrir")
        btnBotonAbrir.connect("clicked", self.on_btnBotonAbrir_clicked)
        caixaH.pack_start(btnBotonAbrir, True, True, 0)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_btnBotonAbrir_clicked(self, boton):
        print("O boton 'Abrir' foi pulsado")


if __name__ == "__main__":
    Aplication()
    Gtk.main()
