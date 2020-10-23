from Ventana import *
import sys, var, events


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_VentPrincipal()
        var.ui.setupUi(self)
        '''
        CONEXION CON LOS EVENTOS
        '''
        '''
        BOTONES
        '''
        var.ui.btlAceptar.clicked.connect(events.Eventos.Saludo)
        var.ui.btlSalir.clicked.connect(events.Eventos.Salida)
        '''
        TOOLBAR
        '''
        var.ui.actionSalir.triggered.connect(events.Eventos.Salida)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec_())


