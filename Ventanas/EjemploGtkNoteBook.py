import gi
import GridConBotons

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplication(Gtk.Window):

    def __init__(self):
        super().__init__(title="Ex de uso de Gtk.Grid")
        self.set_border_width(5)

        cartafol = Gtk.Notebook()

        paxina1 = Gtk.Box()
        paxina1.set_border_width(10)
        paxina1.add(Gtk.Label(label="Páxina principal!"))
        cartafol.append_page(paxina1, Gtk.Label(label="Identificador da páxina1"))

        paxina2 = Gtk.Box()
        paxina2.set_border_width(10)
        paxina2.add(Gtk.Label(label="Páxina con imaxe na lapela"))
        cartafol.append_page(paxina2, Gtk.Image.new_from_icon_name("help-about", Gtk.IconSize.MENU))

        caixaConBotons = GridConBotons.CaixaDeBotons()
        caixaConBotons.set_border_width(10)
        cartafol.append_page(caixaConBotons, Gtk.Label(label="Grid con botóns"))

        self.add(cartafol)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    Aplication()
    Gtk.main()