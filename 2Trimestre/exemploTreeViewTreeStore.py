import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio
from gi.repository.GdkPixbuf import Pixbuf


class Aplication(Gtk.Window):
    def __init__(self):
        super().__init__(title="Exemplo Tree View Tre Store")
        self.set_border_width(5)

        modelo = Gtk.TreeStore(str, int, str)

        for avo in range (5):
            punteiroAvo = modelo.append(None, ['Avó', avo, "Sen datos"])
            for pai in range (4):
                punteiroPai = modelo.append(punteiroAvo, ['Pai', pai, "Lexítimo"])
                for fillo in range (6):
                    modelo.append(punteiroPai, ['Fillo', fillo, "Lexítimo"])

        trvArboreXenealoxico = Gtk.TreeView(modelo)
        trvColumna = Gtk.TreeViewColumn('Parentesco')
        trvArboreXenealoxico.append_column(trvColumna)
        celda = Gtk.CellRendererText()
        celda.set_property("editable", True)
        trvColumna.pack_start(celda, True)
        trvColumna.add_attribute(celda, "text", 0)
        trvColumna = Gtk.TreeViewColumn('Orde')
        trvArboreXenealoxico.append_column(trvColumna)
        celda = Gtk.CellRendererText()
        trvColumna.pack_start(celda, True)
        trvColumna.add_attribute(celda, "text", 1)

        tipoParentesco = Gtk.ListStore(str)
        tipoParentesco.append(["Sen datos"])
        tipoParentesco.append(["Lexítimo"])
        tipoParentesco.append(["Bastardo"])

        celdaCombo = Gtk.CellRendererCombo()
        celdaCombo.set_property("editable", True)
        celdaCombo.set_property("model", tipoParentesco)
        celdaCombo.set_property("text-column", 0)
        celdaCombo.set_property("has-entry", False)
        celdaCombo.connect("edited", self.on_combo_changed, modelo)
        trvColumnaCombo = Gtk.TreeViewColumn("Combo", celdaCombo, text=2)
        trvArboreXenealoxico.append_column(trvColumnaCombo)

        self.add(trvArboreXenealoxico)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()


    def on_combo_changed(self, control, fila, texto, modelo):
        modelo[fila][2] = texto


if __name__ == "__main__":
    Aplication()
    Gtk.main()