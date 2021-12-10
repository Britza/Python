import gi
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio


class Aplication(Gtk.Window):

    def __init__(self):
        super().__init__(title="Layout Glade")
        self.set_border_width(5)

        noteBook = Gtk.Notebook()
        self.add(noteBook)

        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        noteBook.append_page(caixaV, Gtk.Label(label="Xeral"))

        caixaV1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        noteBook.append_page(caixaV1, Gtk.Label(label="Empaquetado"))

        caixaV2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        noteBook.append_page(caixaV2, Gtk.Label(label="Comun"))

        caixaV3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        noteBook.append_page(caixaV3, Gtk.Label(label="Sinais"))


        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)

        lblId = Gtk.Label(label="ID: ")
        self.GtkId = Gtk.Entry()

        caixaH.pack_start(lblId, False, False, 0)
        caixaH.pack_start(self.GtkId, True, True, 0)
        caixaV.pack_start(caixaH, True, True, 0)

        lblApariencia = Gtk.Label()
        lblApariencia.set_markup("<b>Apariencia</b>")
        lblApariencia.props.xalign=0
        caixaV.pack_start(lblApariencia, True, True, 0)

        rede = Gtk.Grid()
        caixaV.pack_start(rede, True, True, 0)
        lblEtiqueta = Gtk.Label()
        lblEtiqueta.set_markup("<i>Etiqueta</i>")
        rede.add(lblEtiqueta)
        caixa = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        txvEtiqueta = Gtk.TextView()
        txvEtiqueta.set_size_request(300,50)
        caixa.pack_start(txvEtiqueta, True, True, 0)
        btnEditarEtiqueta = Gtk.Button()
        btnEditarEtiqueta.connect("clicked", self.on_btn_EditarEtiqueta_clicked)
        imaxe = Gtk.Image.new_from_icon_name("preferences-other", Gtk.IconSize.BUTTON)
        btnEditarEtiqueta.set_image(imaxe)
        caixa.pack_start(btnEditarEtiqueta, True, False, 0)
        rede.attach_next_to(caixa, lblEtiqueta, Gtk.PositionType.RIGHT, 3, 2)

        rbtAtributos = Gtk.RadioButton(label="Atributos")
        rede.attach(rbtAtributos, 0, 2, 1, 1)
        btnEditarAtributos = Gtk.Button(label="editar Atributos")
        rede.attach_next_to(btnEditarAtributos, rbtAtributos, Gtk.PositionType.RIGHT, 3, 1)

        rbtUsarMarcado = Gtk.RadioButton(label="Usar marcado")
        rede.attach(rbtUsarMarcado, 0, 3, 2, 1)

        rbtPatron = Gtk.RadioButton(label="Patron")
        rede.attach(rbtPatron, 0, 4, 1, 1)
        txtPatron = Gtk.Entry()
        rede.attach(txtPatron, 2, 4, 2, 1)


        lblBehaviour= Gtk.Label()
        lblBehaviour.set_markup("<b>Label Behaviour</b>")
        lblBehaviour.props.xalign = 0
        caixaV.pack_start(lblBehaviour, True, True, 0)

        rede2 = Gtk.Grid()
        caixaV.pack_start(rede2, True, True, 0)
        rbtSeleccionable = Gtk.CheckButton(label="Seleccionable")
        rede2.attach(rbtSeleccionable, 0, 2, 1, 1)
        rbtEnlaces = Gtk.CheckButton(label="Seguir los enlaces visitados")
        rede2.attach_next_to(rbtEnlaces, rbtSeleccionable, Gtk.PositionType.RIGHT, 3, 1)
        rbtSubrayado = Gtk.CheckButton(label="Utilizar Subrayado")
        rede2.attach(rbtSubrayado, 0, 3, 1, 1)
        txtComportamentoEtiqueta = Gtk.Entry()
        rede2.attach_next_to(txtComportamentoEtiqueta, rbtSubrayado, Gtk.PositionType.RIGHT, 1, 1)

        builder = Gtk.Builder()
        builder.add_from_file("Cadro.glade")
        caixaGlade = builder.get_object("caixaGlade")
        caixaV.pack_start(caixaGlade, True, True, 0)

        sinais = {"on_cmdElipsis_changed": self.on_cmdElipsis_changed}
        builder.connect_signals(sinais)
        caixaV.pack_start(caixaGlade, True, True, 0)

        cmdElipsis = builder.get_object("cmdElipsis")
        cmdElipsis.append_text("Start")
        cmdElipsis.append_text("Midle")
        cmdElipsis.append_text("End")

        self.add(caixaV)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_cmdElipsis_changed(self, control):
            self.GtkId.set_text(control.get_active_text())

    def on_btn_EditarEtiqueta_clicked(self, boton):
            self.GtkId.set_text("Boton pulsado")


if __name__ == "__main__":
    Aplication()
    Gtk.main()
