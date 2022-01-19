import gi
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplication(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Exemplo TreeViewSeleccion")
        self.set_border_width(5)
        self.set_default_size(400, 200)
        programas = Gtk.ListStore(str, int, str)
        programas.append(["FireFox", 1960, "C++"])
        programas.append(["Eclipse", 1999, "Java"])
        programas.append(["AndroidEstudio", 2000, "Kotling"])
        programas.append(["VirtualBox", 2001, "Java"])
        programas.append(["VisualEstudio", 2005, "PHP"])
        programas.append(["Chrome", 2022, "C"])
        programas.append(["Netbeans", 1998, "Java"])

        grid = Gtk.Grid()
        grid.set_column_homogeneous(True)
        grid.set_row_homogeneous(True)
        tvrVistaProgramas = Gtk.TreeView(model=programas)
        for i, tituloColumna in enumerate(["Software", "Ano", "Linguaxe de programación"]):
            celda = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn(tituloColumna, celda, text=i)
            tvrVistaProgramas.append_column(columna)

        scroll = Gtk.ScrolledWindow()
        scroll.set_vexpand(True)
        grid.attach(scroll, 0, 0, 2, 3)
        scroll.add(tvrVistaProgramas)

        seleccion = tvrVistaProgramas.get_selection()
        seleccion.connect("changed", self.on_tvrVistaProgramacion_changed)

        lblPrograma = Gtk.Label(label="Programa")
        lblAno = Gtk.Label(label="Ano")
        lblLinguaxe = Gtk.Label(label="Linguaxe")

        self.txtPrograma = Gtk.Entry()
        self.txtAno = Gtk.Entry()
        self.txtLinguaxe = Gtk.Entry()

        self.btnModificar = Gtk.Button(label="Modificar")
        self.btnModificar.connect("clicked", self.on_btnModificar_clicked, seleccion)
        self.btnModificar.set_sensitive(False)
        grid.attach_next_to(lblPrograma, scroll, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(self.txtPrograma, lblPrograma, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(lblAno, lblPrograma, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(self.txtAno, lblAno, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(lblLinguaxe, lblAno, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(self.txtLinguaxe, lblLinguaxe, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(self.btnModificar, scroll, Gtk.PositionType.BOTTOM, 4, 1)
        self.add(grid)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_tvrVistaProgramacion_changed(self, selec):
        modelo, punteiro = selec.get_selected()
        self.txtPrograma.set_text(modelo[punteiro][0])
        self.txtAno.set_text(str(modelo[punteiro][1]))
        self.txtLinguaxe.set_text(modelo[punteiro][2])
        self.btnModificar.set_sensitive(True)

    def on_btnModificar_clicked(self, boton, seleccion):
        modelo, fila = seleccion.get_selected()
        modelo[fila][0] = self.txtPrograma.get_text()
        modelo[fila][1] = int(self.txtAno.get_text())
        modelo[fila][2] = self.txtLinguaxe.get_text()
        self.btnModificar.set_sensitive(False)


if __name__ == "__main__":
    Aplication()
    Gtk.main()