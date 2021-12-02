from sqlite3.dbapi2 import Cursor
from PyQt5.QtWidgets import QInputDialog, QComboBox, QMainWindow, QApplication, QTableWidgetItem
from PyQt5 import uic
import sqlite3

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("agendaf.ui", self)
        self.editar.clicked.connect(self.on_editar)
        self.eliminar.clicked.connect(self.on_eliminar)
        self.guardar.clicked.connect(self.on_guardar)
        self.cargar.clicked.connect(self.on_cargar)
        self.conexion = sqlite3.connect("agenda.db")
        self.cursor = self.conexion.cursor()
        
        self.tabla.setColumnCount(9)
        self.tabla.setHorizontalHeaderLabels(("ID", "Nombre", "Apellido", "E-mail", "Dirección", "Teléfono", "Fecha de nacimiento", "Altura", "Peso", "ID"))
        self.filas = 0
        
             
        
    def on_editar(self):
        texto_item = self.tabla.currentItem().text()
        indess = self.tabla.currentRow()
        index = indess + 1
        columna = self.tabla.currentColumn()
        if self.tabla.currentColumn()==1:
            nuevo_nombre, ok = QInputDialog.getText(self, "Editar", "Ingrese el texto", text = texto_item)
            if ok:
                self.tabla.currentItem().setText(nuevo_nombre)
                self.cursor.execute("UPDATE contactos SET nombres='"+nuevo_nombre+"' WHERE id = '"+str(index)+"'")
                self.conexion.commit()
        elif self.tabla.currentColumn()==2:
            nuevo_nombre, ok = QInputDialog.getText(self, "Editar", "Ingrese el texto", text = texto_item)
            if ok:
                self.tabla.currentItem().setText(nuevo_nombre)
                self.cursor.execute("UPDATE contactos SET apellido='"+nuevo_nombre+"' WHERE id = '"+str(index)+"'")
                self.conexion.commit()
        elif self.tabla.currentColumn()==3:
            nuevo_nombre, ok = QInputDialog.getText(self, "Editar", "Ingrese el texto", text = texto_item)
            if ok:
                self.tabla.currentItem().setText(nuevo_nombre)
                self.cursor.execute("UPDATE contactos SET email='"+nuevo_nombre+"' WHERE id = '"+str(index)+"'")
                self.conexion.commit()
        elif self.tabla.currentColumn()==4:
            nuevo_nombre, ok = QInputDialog.getText(self, "Editar", "Ingrese el texto", text = texto_item)
            if ok:
                self.tabla.currentItem().setText(nuevo_nombre)
                self.cursor.execute("UPDATE contactos SET telefono='"+nuevo_nombre+"' WHERE id = '"+str(index)+"'")
                self.conexion.commit()
        elif self.tabla.currentColumn()==5:
            nuevo_nombre, ok = QInputDialog.getText(self, "Editar", "Ingrese el texto", text = texto_item)
            if ok:
                self.tabla.currentItem().setText(nuevo_nombre)
                self.cursor.execute("UPDATE contactos SET direccion='"+nuevo_nombre+"' WHERE id = '"+str(index)+"'")
                self.conexion.commit()
        elif self.tabla.currentColumn()==6:
            nuevo_nombre, ok = QInputDialog.getText(self, "Editar", "Ingrese el texto", text = texto_item)
            if ok:
                self.tabla.currentItem().setText(nuevo_nombre)
                self.cursor.execute("UPDATE contactos SET fecha_de_nacimiento='"+nuevo_nombre+"' WHERE id = '"+str(index)+"'")
                self.conexion.commit()
        elif self.tabla.currentColumn()==7:
            nuevo_nombre, ok = QInputDialog.getText(self, "Editar", "Ingrese el texto", text = texto_item)
            if ok:
                self.tabla.currentItem().setText(nuevo_nombre)
                self.cursor.execute("UPDATE contactos SET altura='"+nuevo_nombre+"' WHERE id = '"+str(index)+"'")
                self.conexion.commit()
        elif self.tabla.currentColumn()==8:
            nuevo_nombre, ok = QInputDialog.getText(self, "Editar", "Ingrese el texto", text = texto_item)
            if ok:
                self.tabla.currentItem().setText(nuevo_nombre)
                self.cursor.execute("UPDATE contactos SET peso='"+nuevo_nombre+"' WHERE id = '"+str(index)+"'")
                self.conexion.commit()
        

        
    def on_cargar(self):
        self.cursor.execute("select * from contactos")
        contactos = self.cursor.fetchall()
        
        for usuario in contactos:
            fila = contactos.index(usuario)
            self.tabla.insertRow(fila)
            self.tabla.setItem(fila, 0, QTableWidgetItem(str(usuario[0])))
            self.tabla.setItem(fila, 1, QTableWidgetItem(str(usuario[1])))
            self.tabla.setItem(fila, 2, QTableWidgetItem(str(usuario[2])))
            self.tabla.setItem(fila, 3, QTableWidgetItem(str(usuario[3])))
            self.tabla.setItem(fila, 4, QTableWidgetItem(str(usuario[4])))
            self.tabla.setItem(fila, 5, QTableWidgetItem(str(usuario[5])))
            self.tabla.setItem(fila, 6, QTableWidgetItem(str(usuario[6])))
            self.tabla.setItem(fila, 7, QTableWidgetItem(str(usuario[7])))
            self.tabla.setItem(fila, 8, QTableWidgetItem(str(usuario[8])))
            
            
                
    def on_guardar(self):
        filass = self.filas + 1
        fila = self.filas
        self.tabla.insertRow(fila)
        aidi = filass
        
        self.tabla.setItem(fila, 0, QTableWidgetItem(str(aidi)))
        nombre = self.nombre.text()
        self.tabla.setItem(fila, 1, QTableWidgetItem(nombre))
        apellido = self.apellido.text()
        self.tabla.setItem(fila, 2, QTableWidgetItem(apellido))
        email = self.email.text()
        self.tabla.setItem(fila, 3, QTableWidgetItem(email))
        direccion = self.direccion.text()
        self.tabla.setItem(fila, 4, QTableWidgetItem(direccion))
        telefono = self.telefono.text()
        self.tabla.setItem(fila, 5, QTableWidgetItem(telefono))
        fechadenacimiento = self.fechadenacimiento.text()
        self.tabla.setItem(fila, 6, QTableWidgetItem(fechadenacimiento))
        altura = self.altura.text()
        self.tabla.setItem(fila, 7, QTableWidgetItem(altura))
        peso = self.peso.text()
        self.tabla.setItem(fila, 8, QTableWidgetItem(peso))
        
        self.filas = self.filas + 1
        
        nombre = self.nombre.text()
        apellido = self.apellido.text()
        email = self.email.text()
        telefono = self.telefono.text()
        direccion = self.direccion.text()
        fechadenacimiento = self.fechadenacimiento.text()
        altura = self.altura.text()
        peso = self.peso.text()
        
        self.cursor.execute("INSERT INTO contactos(id, nombres, apellidos, email, telefono, direccion, fecha_de_nacimiento, altura, peso) VALUES ('"+str(aidi)+"','"+nombre+"','"+apellido+"','"+email+"','"+telefono+"','"+direccion+"','"+fechadenacimiento+"','"+altura+"','"+peso+"')")
        self.conexion.commit()
        
                
    def on_eliminar(self): 
        indess = self.tabla.currentRow()
        index = indess + 1
        self.cursor.execute("DELETE from contactos WHERE id="+ str(index))
        self.conexion.commit()
        print(index)
        
        self.tabla.removeRow(self.tabla.currentRow())
        

app = QApplication([])

win = MiVentana()
win.show()

app.exec_()


