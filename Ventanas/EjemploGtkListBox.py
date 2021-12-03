import gi
import GridConBotons

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class ListBoxRowConDatos(Gtk.ListBoxRow):
    def __init__(self, palabra):
        super().__init__()
        self.palabra = palabra
        self.add(Gtk.Label(label=palabra))


class Aplication(Gtk.Window):

    def __init__(self):
        super().__init__(title="Ex de uso de Stack e StackSwitcher")
        self.set_border_width(5)

        caixaExterna = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(caixaExterna)

        listBox = Gtk.ListBox()
        listBox.set_selection_mode(Gtk.SelectionMode.NONE)
        caixaExterna.pack_start(listBox, True, True, 0)

        fila = Gtk.ListBoxRow()
        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        fila.add(caixaH)
        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        caixaH.pack_start(caixaV, True, True, 0)
        etiqueta1 = Gtk.Label(label="Data e hora automática", xalign=0)
        etiqueta2 = Gtk.Label(label="Require acceso a interrede2", xalign=0)
        caixaV.pack_start(etiqueta1, True, True, 0)
        caixaV.pack_start(etiqueta2, True, True, 0)

        conmutador = Gtk.Switch()
        conmutador.props.valign = Gtk.Align.CENTER
        caixaH.pack_start(conmutador, False, True, 0)

        listBox.add(fila)

        fila2 = Gtk.ListBoxRow()
        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        fila2.add(caixaH)
        etiqueta = Gtk.Label(label="Permitir actualizacións automáticas", xalign=0)
        chkActualizacions = Gtk.CheckButton()
        caixaH.pack_start(etiqueta, True, True, 0)
        caixaH.pack_start(chkActualizacions, False, True, 0)

        listBox.add(fila2)

        fila3 = Gtk.ListBoxRow()
        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        fila3.add(caixaH)
        lblFormatoData = Gtk.Label(label="Formato data", xalign=0)
        cmbFormatoData = Gtk.ComboBoxText()
        cmbFormatoData.insert(0, "0", "24-hour")
        cmbFormatoData.insert(1, "1", "AM/PM")
        caixaH.pack_start(lblFormatoData, True, True, 0)
        caixaH.pack_start(cmbFormatoData, False, True, 0)

        listBox.add(fila3)


        listBox2 = Gtk.ListBox()
        elementos = "Esta é unha ListBox ordeada para mostra".split()
        for elemento in elementos:
            listBox2.add(ListBoxRowConDatos(elemento))

        def ordear(fila1, fila2, palabra, notify_destroy):
            return fila1.palabra.lower() > fila2.palabra.lower()

        def filtrar(fila, datos, notify_destroy):
            return False if fila.palabra == "ListBox" else True

        listBox2.set_sort_func(ordear, None, False)
        listBox2.set_filter_func(filtrar, None, False)
        listBox2.connect("row_activated", self.on_row_activated)

        caixaExterna.pack_start(listBox2, True, True, 0)
        listBox2.show_all()

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_row_activated(listBox, fila):
        print(fila.palabra)


if __name__ == "__main__":
    Aplication()
    Gtk.main()
