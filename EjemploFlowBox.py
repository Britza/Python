import gi
import GridConBotons

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio


class Aplication(Gtk.Window):

    def __init__(self):
        super().__init__(title="Ex de uso de Flow Box")
        self.set_border_width(5)
        self.set_default_size(300, 250)

        cabeceira = Gtk.HeaderBar(title="Flow Box")
        cabeceira.set_subtitle("Con cabeceira HeaderBar")
        cabeceira.props.show_close_button = True
        self.set_titlebar(cabeceira)

        boton = Gtk.Button()
        icono = Gio.ThemedIcon(name="mail-send-receive-symbolic")
        imaxe = Gtk.Image.new_from_gicon(icono, Gtk.IconSize.BUTTON)
        boton.add(imaxe)
        cabeceira.pack_end(boton)

        caixa = Gtk.Box(orientation= Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(caixa.get_style_context(), "linked")

        boton2 = Gtk.Button()
        boton2.add(
            Gtk.Arrow(arrow_type=Gtk.ArrowType.LEFT, shadow_type=Gtk.ShadowType.NONE)
        )
        caixa.add(boton2)

        boton3 = Gtk.Button.new_from_icon_name("pan-end-symbolic", Gtk.IconSize.MENU)
        caixa.add(boton3)
        cabeceira.pack_start(caixa)


        flowBox = Gtk.FlowBox()
        flowBox.set_valign(Gtk.Align.START)
        flowBox.set_max_children_per_line(30)
        flowBox.set_selection_mode(Gtk.SelectionMode.NONE)

        for n in range(50):
            cadro = GridConBotons.CaixaDeBotons()
            flowBox.add(cadro)

        barras = Gtk.ScrolledWindow()
        barras.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)

        barras.add(flowBox)
        self.add(barras)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    Aplication()
    Gtk.main()
