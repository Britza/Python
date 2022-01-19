import gi
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplication(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Exemplo TreeView filtrado e ordeado")
        self.set_border_width(5)
        self.set_default_size(400, 200)

        self.filtro_actual_linguaxe = "None"

        programas = Gtk.ListStore(str, int, str)
        programas.append(["FireFox", 1960, "C++"])
        programas.append(["Eclipse", 1999, "Java"])
        programas.append(["VirtualBox", 2001, "Java"])
        programas.append(["Bazaar", 2005, "Python"])
        programas.append(["Chrome", 2002, "C++"])
        programas.append(["GCC", 1997, "C"])
        programas.append(["Kernel Linux", 1991, "C"])
        programas.append(["Sphinx", 2003, "Python"])

        grid = Gtk.Grid()
        grid.set_column_homogeneous(True)
        grid.set_row_homogeneous(True)

        self.filtroLinguaxe = programas.filter_new()
        self.filtroLinguaxe.set_visible_func(self.filtro_linguaxe)

        tvrVistaProgramas = Gtk.TreeView(model=programas)
        for i, tituloColumna in enumerate(["Software", "Ano", "Linguaxe de programación"]):
            celda = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn(tituloColumna, celda, text=i)
            tvrVistaProgramas.append_column(columna)
            if i==1:
                columna.set_sort_column_id(1)

        programas.set_sort_func(1, self.ordear_por_ano, None)

        scroll = Gtk.ScrolledWindow()
        scroll.set_vexpand(True)
        grid.attach(scroll, 0, 0, 5, 3)
        scroll.add(tvrVistaProgramas)

        filtroJava = Gtk.Button(label="Java")
        filtroC = Gtk.Button(label="C")
        filtroCMaisMais = Gtk.Button(label="C++")
        filtroPython = Gtk.Button(label="Python")
        senFiltro = Gtk.Button(label="None")

        filtroJava.connect("clicked", self.on_botonSeleccion_clicked)
        filtroC.connect("clicked", self.on_botonSeleccion_clicked)
        filtroCMaisMais.connect("clicked", self.on_botonSeleccion_clicked)
        filtroPython.connect("clicked", self.on_botonSeleccion_clicked)
        senFiltro.connect("clicked", self.on_botonSeleccion_clicked)

        grid.attach_next_to(filtroJava, scroll, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(filtroC, filtroJava, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(filtroCMaisMais, filtroC, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(filtroPython, filtroCMaisMais, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(senFiltro, filtroPython, Gtk.PositionType.RIGHT, 1, 1)

        self.add(grid)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_botonSeleccion_clicked(self, boton):
        self.filtro_actual_linguaxe = boton.get_label()
        self.filtroLinguaxe.refilter()

    def filtro_linguaxe(self, modelo, fila, datos):
        if self.filtro_actual_linguaxe == "None":
            return True
        else:
            return modelo[fila][2] == self.filtro_actual_linguaxe

    def ordear_por_ano(self, modelo, fila1, fila2, datos_usuario):
        columna, _ = modelo.get_sort_column_id()
        ano1 = modelo.get_value(fila1, columna)
        ano2 = modelo[fila2][columna]
        if ano1 < ano2:
            return -1
        elif ano1 == ano2:
            return 0
        else:
            return 1


if __name__ == "__main__":
    Aplication()
    Gtk.main()
