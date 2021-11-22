import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

'''
fiestra = Gtk.Window()
fiestra.connect("destroy",Gtk.main_quit)
fiestra.show_all()'''


class Aplication(Gtk.Window):

    def __init__(self):
        super().__init__(title="Ex de uso de Gtk.Label")

        # wndFiestra = Gtk.Window()
        # wndFiestra.set_title("Exemplo de uso de Gtk.Label")
        self.cont = 0
        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        caixaV_dereita = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        caixaV_esquerda = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        caixaH.pack_start(caixaV_esquerda, True, True, 0)
        caixaH.pack_start(caixaV_dereita, True, True, 0)

        self.etiqueta = Gtk.Label(label="Etiqueta normal")
        caixaV_esquerda.pack_start(self.etiqueta, True, True, 0)

        etiqueta2 = Gtk.Label(label="Etiqueta con texto xustificado a esquerda. \nCon multiples liñas.")
        etiqueta2.set_justify(Gtk.Justification.RIGHT)
        caixaV_esquerda.pack_start(etiqueta2, True, True, 0)

        etiqueta3 = Gtk.Label(label="En este caso e etiqueta line-wraped. Esta "
                                    "o texto non nos coller no ancho "
                                    "poño varias cadeas de texto "
                                    "que van a ser unidas. \n"
                                    "Isto permite múltiples parágrafos e engade "
                                    "bastantes    espazos extra")
        etiqueta3.set_line_wrap(True)
        etiqueta3.set_max_width_chars(32)
        caixaV_dereita.pack_start(etiqueta3, True, True, 0)

        etiqueta4 = Gtk.Label(label="En este caso e etiqueta line-wraped. Esta "
                                    "o texto non nos coller no ancho "
                                    "poño varias cadeas de texto "
                                    "que van a ser unidas. \n"
                                    "Isto permite múltiples parágrafos e engade "
                                    "bastantes    espazos extra.\n"
                                    "Parragrafo extra longo para facer máis "
                                    "Texto")
        etiqueta4.set_line_wrap(True)
        etiqueta4.set_justify(Gtk.Justification.FILL)
        etiqueta4.set_max_width_chars(32)
        caixaV_dereita.pack_start(etiqueta4, True, True, 0)

        etiqueta5 = Gtk.Label()
        etiqueta5.set_markup("O texto pode ter <small>pequeno</small>, <big>grande</big>,"
                             "<b>negriña</b>, <i>cursiva</i>, e apuntar cara a "
                             '<a href="http://www.gtk.org"'
                             'title="pulsa para saber mais"> interrede</a>')

        etiqueta5.set_line_wrap(True)
        etiqueta5.set_max_width_chars(48)
        caixaV_dereita.pack_start(etiqueta5, True, True, 0)

        etiqueta6 = Gtk.Label.new_with_mnemonic("_Press Alt + P para seleccionar o boton dereito")
        etiqueta6.set_selectable(True)
        caixaV_dereita.pack_start(etiqueta6, True, True, 0)

        boton = Gtk.Button(label="Pulsa...")
        etiqueta6.set_mnemonic_widget(boton)
        boton.connect("clicked", self.botonFuncionable)
        caixaV_dereita.pack_start(boton, True, True, 0)

        self.add(caixaH)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()



    def botonFuncionable(self,boton):

        self.cont += 1
        self.etiqueta.set_text("Boton pulsado " + str(self.cont))

    def otraManeraBoton(self, boton,etiq):
        self.cont +=1
        etiq.set_text("Boton pulsado " + str(self.cont))


if __name__ == "__main__":
    Aplication()
    Gtk.main()
