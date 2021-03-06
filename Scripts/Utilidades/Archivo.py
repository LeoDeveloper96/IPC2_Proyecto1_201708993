import os
import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET
from Scripts.Estructuras.ListaEnlazadaSimple.PatronScript import Patron
from Scripts.Estructuras.ListaEnlazadaSimple.PisoScript import Piso
from Scripts.Estructuras.ListaEnlazadaSimple.ListaEnlazadaScript import ListaEnlazada


def cargarArchivo(self):
    root = tk.Tk()
    root.withdraw()
    ruta = os.getcwd() + "\\Archivos prueba"
    nombre_archivo = filedialog.askopenfilename(initialdir=ruta, title="Seleccionar un archivo",
                                                filetypes=(("texto", "*.xml"), ("todos", "*.*")))
    try:
        with open(nombre_archivo, "r", encoding="utf8"):
            arbol = ET.parse(nombre_archivo, parser=ET.XMLParser(encoding='iso-8859-5'))
            raiz = arbol.getroot()
            pisos = raiz.findall('piso')
            for piso in pisos:
                patrones = ListaEnlazada()
                nombre_piso = piso.attrib['nombre']
                r = piso.find('R').text
                c = piso.find('C').text
                f = piso.find('F').text
                s = piso.find('S').text
                et_patrones = piso.find('patrones').findall('patron')
                for patron in et_patrones:
                    codigo = patron.attrib['codigo']
                    patron = patron.text
                    patrones.append(Patron(codigo, patron))
                self.lista_pisos.append(Piso(nombre_piso, r, c, f, s, patrones))
                a = 1
    except FileNotFoundError:
        print("archivo no encontrado")


def crearArchivo(self, nombre):

    ruta = tk.filedialog.askdirectory()
    ruta += "\\" + nombre
    try:
        with open(ruta, 'w') as f:
            f.write(self.instrucciones)
    except FileNotFoundError:
        print("No existe el directorio")