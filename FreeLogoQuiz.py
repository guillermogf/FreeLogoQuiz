#!/usr/bin/python
# coding: utf-8

import pygtk
pygtk.require("2.0")
import gtk

from commands import getoutput
from os import system
user = getoutput("logname")

#Archivos con la configuración
if getoutput("ls ~/.freelogoquiz") == "ls: no se puede acceder a /home/" + user + "/.freelogoquiz: No existe el archivo o el directorio":
	system("mkdir ~/.freelogoquiz")
if getoutput("ls ~/.freelogoquiz") == "":
	system("echo \"0\" >> ~/.freelogoquiz/nivel1")
	system("echo \"0\" >> ~/.freelogoquiz/nivel2")
	system("echo \"0\" >> ~/.freelogoquiz/nivel3")
	system("echo \"0\" >> ~/.freelogoquiz/nivel4")

completados1 = system("cat ~/.freelogoquiz/nivel1")
completados2 = system("cat ~/.freelogoquiz/nivel2")
completados3 = system("cat ~/.freelogoquiz/nivel3")
completados4 = system("cat ~/.freelogoquiz/nivel4")


class Menu:
	def delete_event(self, widget, event, data=None):
		gtk.main_quit()
		return False

	def volver(self, widget):
		self.window.destroy()
		self.__init__()

	def volver2(self, widget, nivel):
		self.vboxLogo.destroy()
		self.nivel(self.nivel, nivel)

	def delete_event(self, widget, event, data=None):
		gtk.main_quit()
		return False

	def mensaje(self, mensaje):
		dialogo = gtk.MessageDialog(parent=None, flags=0, buttons=gtk.BUTTONS_OK)
		dialogo.set_title("Mensaje")
		label = gtk.Label(mensaje)
		dialogo.vbox.pack_start(label, True, True, 0)
		dialogo.show_all()
		dialogo.run()
		dialogo.destroy()

	def enter_callback(self, widget, entry, respuesta, nivel):
		entry_text = entry.get_text()
		entry_text = entry_text.lower()
		if entry_text in respuesta:
			self.mensaje("¡Correcto!")
		else:
			self.mensaje("¡Incorrecto!")

	def pistas(self, widget, pista1, pista2, pista3, pista4):
		dialogo = gtk.MessageDialog(parent=None, flags=0, buttons=gtk.BUTTONS_OK)
		dialogo.set_title("Pistas")
		label1 = gtk.Label(pista1)
		dialogo.vbox.pack_start(label1)
		label2 = gtk.Label(pista2)
		dialogo.vbox.pack_start(label2)
		label3 = gtk.Label(pista3)
		dialogo.vbox.pack_start(label3)
		label4 = gtk.Label(pista4)
		dialogo.vbox.pack_start(label4)
		dialogo.show_all()
		dialogo.run()
		dialogo.destroy()

	def logo(self, widget, nivel, logo):
		self.scrollNivel.destroy()
		self.tableNivel.destroy()

		if nivel == 1:
			path = "logos/Grandes/Level1"
			if logo == 1:
				respuesta = "openoffice"
				pista1 = "1. Suite ofimática libre (licencia Apache 2.0)"
				pista2 = "2. Proyecto iniciado por Sun Microsystems"
				pista3 = "3. Proyecto donado por Oracle a la Apache Foundation"
				pista4 = "4. La comunidad inició un proyecto paralelo independiente en 2010"
			elif logo == 2:
				respuesta = "wikipedia"
				pista1 = "1. Enciclopedia creada por Jimbo Wales en 2001"
				pista2 = "2. Inicialemente llamado Nupedia"
				pista3 = "3. Mantenido por una amplia comunidad"
				pista4 = "4. Contenido publicado bajo licencias Creative Commons"
			elif logo == 3:
				respuesta = "libreoffice"
				pista1 = "1. Suite ofimática libre (GNU LGPL)"
				pista2 = "2. Escisión de otro proyecto producida en 2010"
				pista3 = "3. Soporta el formato OpenDocument, entre otros"
				pista4 = "4. Son seis los programas que la forman"
			elif logo == 4:
				respuesta = "vlc"
				pista1 = "1. Reproductor multimedia libre (GNU GPL)"
				pista2 = "2. Desarrollado por VideoLAN"
				pista3 = "3. Proyecto iniciado en 1996 y liberado en 2001"
				pista4 = "4. Recientemente se ha publicado versión para Android"
			elif logo == 5:
				respuesta = "chromium"
				pista1 = "1. Navegador libre (licencia BSD)"
				pista2 = "2. Desarrollado a partir del código fuente del navegador Chrome liberado por Google"
				pista3 = "3. Es multiplataforma"
				pista4 = "4. Programado en C++ y ensamblador"
			elif logo == 6:
				respuesta = "kde"
				pista1 = "1. Entorno de escritorio libre (GNU GPL, GNU LGPL, licencia BSD,...)"
				pista2 = "2. Utiliza Qt para las interfaces gráficas"
				pista3 = "3. Iniciado en 1996 para sistemas Unix"
				pista4 = "4. Las mascotas del proyecto son Konqui (actual) y Kandalf "
			elif logo == 7:
				respuesta = "creative commons"
				pista1 = "1. Licencias publicadas y defendidas por la fundación homónima"
				pista2 = "2. Licencias principalmente utilizadas en textos y gráficos"
				pista3 = "3. Usadas por Wikipedia"
				pista4 = "4. El único requisito que comparten todas es indicar el autor"
			elif logo == 8:
				respuesta = "linux", "tux"
				pista1 = "1. Kernel libre (GNU GPL)"
				pista2 = "2. Kernel basado en Unix"
				pista3 = "3. Desarrollado por Linus Torvarlds desde 1991"
				pista4 = "4. Es el núcleo que usan más distribuciones libres"
			elif logo == 9:
				respuesta = "android"
				pista1 = "1. Sistema Operativo libre (licencia Apache y GNU GPL)"
				pista2 = "2. Desarrollado por un grupo de empresas lideradas por Google"
				pista3 = "3. Iniciado en 2005"
				pista4 = "4. La mascota es Andy"
			elif logo == 10:
				respuesta = "ubuntu"
				pista1 = "1. Distribución GNU/Linux libre (GNU GPL)"
				pista2 = "2. Desarrollado por Canonical"
				pista3 = "3. Se publica una nueva versión cada seis meses."
				pista4 = "4. Distribución GNU/Linux más popular"
			elif logo == 11:
				respuesta = "gnu"
				pista1 = "1. Proyecto creado con el objetivo de crear un SO completamente libre"
				pista2 = "2. Proyecto iniciado por Richard Stallman en 1983"
				pista3 = "3. Basado en la arquitectura de Unix"
				pista4 = "4. Se creó la licencia GPL para asegurar la libertad de los usuarios"
			elif logo == 12:
				respuesta = "audacity"
				pista1 = "1. Editor y grabador de audio libre (GNU GPL)"
				pista2 = "2. Creado en 1999 y publicado el 2000"
				pista3 = "3. Gran soporte de formatos"
				pista4 = "4. Aplicación de su tipo más popular en sistemas Linux"
			elif logo == 13:
				respuesta = "calibre"
				pista1 = "1. Gestor de libros electrónicos libres (GNU GPL)"
				pista2 = "2. Programado en C y python y usa la biblioteca Qt"
				pista3 = "3. Proyecto iniciado en 2006"
				pista4 = "4. Es multiplataforma"
			elif logo == 14:
				respuesta = "gimp"
				pista1 = "1. Editor de imágenes libre (GNU GPL)"
				pista2 = "2. Es parte del proyecto GNU"
				pista3 = "3. GTK fue creado inicialmente para este programa"
				pista4 = "4. Wilber es la mascota desde 1997"
			elif logo == 15:
				respuesta = "inkscape"
				pista1 = "1. Editor de gráficos vectoriales libre (GNU GPL)7"
				pista2 = "2. Utiliza el formato SVG y permite la exportación e importación de otros"
				pista3 = "3. Iniciado en 2006"
				pista4 = "4. Multiplataforma"
			elif logo == 16:
				respuesta = "gnome"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 17:
				respuesta = "fedora"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 18:
				respuesta = "fsf"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 19:
				respuesta = "thunderbird"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 20:
				respuesta = "firefox"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""

		elif nivel == 2:
			path = "logos/Grandes/Level2"
			if logo == 1:
				respuesta = "gparted"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 2:
				respuesta = "blender"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 3:
				respuesta = "bugzilla"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 4:
				respuesta = "redhat"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 5:
				respuesta = "scribus"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 6:
				respuesta = "python"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 7:
				respuesta = "banshee"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 8:
				respuesta = "debian"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 9:
				respuesta = "gentoo"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 10:
				respuesta = "wikimedia foundation", "fundación wikimedia", "wikimedia"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 11:
				respuesta = "amarok"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 12:
				respuesta = "k3b"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 13:
				respuesta = "apache"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 14:
				respuesta = "java"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 15:
				respuesta = "mozilla foundation", "fundación mozilla", "mozilla"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 16:
				respuesta = "kubuntu"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 17:
				respuesta = "totem"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 18:
				respuesta = "amsn"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 19:
				respuesta = "unity"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 20:
				respuesta = "wikicommons"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""

		elif nivel == 3:
			path = "logos/Grandes/Level3"
			if logo == 1:
				respuesta = "gpl"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 2:
				respuesta = "gcc"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 3:
				respuesta = "linuxmint"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 4:
				respuesta = "0ad"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 5:
				respuesta = "assault cube"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 6:
				respuesta = "epiphany"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 7:
				respuesta = "archlinux"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 8:
				respuesta = "emacs"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 9:
				respuesta = "frozenbubble"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 10:
				respuesta = "nautilus"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 11:
				respuesta = "mediawiki"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 12:
				respuesta = "xubuntu"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 13:
				respuesta = "slackware"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 14:
				respuesta = "opensuse"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 15:
				respuesta = "mandriva"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 16:
				respuesta = "deluge"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 17:
				respuesta = "lxde"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 18:
				respuesta = "rhythmbox"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 19:
				respuesta = "compiz"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 20:
				respuesta = "canonical"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""

		elif nivel == 4:
			path = "logos/Grandes/Level4"
			if logo == 1:
				respuesta = "kdenlive"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 2:
				respuesta = "lgpl"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 3:
				respuesta = "savannah"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 4:
				respuesta = "xfce"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 5:
				respuesta = "big buck bunny"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 6:
				respuesta = "sun microsystems"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 7:
				respuesta = "warmux"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 8:
				respuesta = "centos"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 9:
				respuesta = "ffmpeg"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 10:
				respuesta = "cheese"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 11:
				respuesta = "cinelerra"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 12:
				respuesta = "kate"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 13:
				respuesta = "php"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 14:
				respuesta = "gnome subtitles"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 15:
				respuesta = "enlightenment"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 16:
				respuesta = "open solaris"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 17:
				respuesta = "gedit"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 18:
				respuesta = "lubuntu"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 19:
				respuesta = "openarena"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""
			elif logo == 20:
				respuesta = "slackware", "slackware mascot", "mascota slackware"
				pista1 = ""
				pista2 = ""
				pista3 = ""
				pista4 = ""

		#Creando la tabla
		self.vboxLogo = gtk.VBox()
		self.vboxLogo.show()
		self.window.add(self.vboxLogo)

		#Cargando la imagen
		self.image = gtk.Image()
		self.image.set_from_file("logos/Grandes/Level" + str(nivel) + "/" + str(logo) + ".png")
		self.image.show()
		self.vboxLogo.pack_start(self.image)

		self.hboxLogo = gtk.HBox()
		self.hboxLogo.show()
		self.vboxLogo.pack_start(self.hboxLogo, True, False, 0)

		self.entry = gtk.Entry()
		self.entry.connect("activate", self.enter_callback, self.entry, respuesta, nivel)
		self.entry.show()
		self.hboxLogo.pack_start(self.entry, True, True, 0)

		self.pistasButton = gtk.Button("Pistas")
		self.pistasButton.show()
		self.hboxLogo.pack_start(self.pistasButton, False, False, 0)
		self.pistasButton.connect("clicked", self.pistas, pista1, pista2, pista3, pista4)

		#Botones para volver
		self.hboxLogo2 = gtk.HBox()
		self.hboxLogo2.show()
		self.vboxLogo.pack_start(self.hboxLogo2, True, False, 0)

		self.atrasLogo = gtk.Button("Volver al menú principal")
		self.atrasLogo.show()
		self.hboxLogo2.pack_start(self.atrasLogo, True, True, 0)
		self.atrasLogo.connect("clicked", self.volver)

		self.atrasLogo2 = gtk.Button("Volver al nivel " + str(nivel))
		self.atrasLogo2.show()
		self.hboxLogo2.pack_start(self.atrasLogo2, True, True, 0)
		self.atrasLogo2.connect("clicked", self.volver2, nivel)

	def nivel(self, widget, nivel):
		#Determinando el nivel y las imágenes
		if nivel == 1:
			path = "logos/Pequeños/Level1/"
		elif nivel == 2:
			path = "logos/Pequeños/Level2/"
		elif nivel == 3:
			path = "logos/Pequeños/Level3/"
		elif nivel == 4:
			path = "logos/Pequeños/Level4/"

		self.window.set_title("FreeLogoQuiz - Nivel" + str(nivel))

		#Destuir los widgets que ya no se usan
		self.scroll.destroy()
		self.table.destroy()

		#Scroll
		self.scrollNivel = gtk.ScrolledWindow()
		self.scrollNivel.set_border_width(0)
		self.scrollNivel.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)
		self.window.add(self.scrollNivel)

		#Table
		self.tableNivel = gtk.Table(4, 6, False)
		self.tableNivel.set_row_spacings(10)
		self.tableNivel.set_col_spacings(10)

		self.scrollNivel.add_with_viewport(self.tableNivel)
		self.scrollNivel.show()
		self.tableNivel.show()

		#Cargando las imágenes
		self.image1 = gtk.Image()
		self.image1.set_from_file(path + "1.png")
		self.image1.show()
		self.button = gtk.Button()
		self.button.add(self.image1)
		self.button.show()
		self.tableNivel.attach(self.button, 0, 1, 0, 1)
		self.button.connect("clicked", self.logo, nivel, 1)

		self.image2 = gtk.Image()
		self.image2.set_from_file(path + "2.png")
		self.image2.show()
		self.button2 = gtk.Button()
		self.button2.add(self.image2)
		self.button2.show()
		self.tableNivel.attach(self.button2, 1, 2, 0, 1)
		self.button2.connect("clicked", self.logo, nivel, 2)

		self.image3 = gtk.Image()
		self.image3.set_from_file(path + "3.png")
		self.image3.show()
		self.button3 = gtk.Button()
		self.button3.add(self.image3)
		self.button3.show()
		self.tableNivel.attach(self.button3, 2, 3, 0, 1)
		self.button3.connect("clicked", self.logo, nivel, 3)

		self.image4 = gtk.Image()
		self.image4.set_from_file(path + "4.png")
		self.image4.show()
		self.button4 = gtk.Button()
		self.button4.add(self.image4)
		self.button4.show()
		self.tableNivel.attach(self.button4, 3, 4, 0, 1)
		self.button4.connect("clicked", self.logo, nivel, 4)

		self.image5 = gtk.Image()
		self.image5.set_from_file(path + "5.png")
		self.image5.show()
		self.button5 = gtk.Button()
		self.button5.add(self.image5)
		self.button5.show()
		self.tableNivel.attach(self.button5, 0, 1, 1, 2)
		self.button5.connect("clicked", self.logo, nivel, 5)

		self.image6 = gtk.Image()
		self.image6.set_from_file(path + "6.png")
		self.image6.show()
		self.button6 = gtk.Button()
		self.button6.add(self.image6)
		self.button6.show()
		self.tableNivel.attach(self.button6, 1, 2, 1, 2)
		self.button6.connect("clicked", self.logo, nivel, 6)

		self.image7 = gtk.Image()
		self.image7.set_from_file(path + "7.png")
		self.image7.show()
		self.button7 = gtk.Button()
		self.button7.add(self.image7)
		self.button7.show()
		self.tableNivel.attach(self.button7, 2, 3, 1, 2)
		self.button.connect("clicked", self.logo, nivel, 7)

		self.image8 = gtk.Image()
		self.image8.set_from_file(path + "8.png")
		self.image8.show()
		self.button8 = gtk.Button()
		self.button8.add(self.image8)
		self.button8.show()
		self.tableNivel.attach(self.button8, 3, 4, 1, 2)
		self.button8.connect("clicked", self.logo, nivel, 8)

		self.image9 = gtk.Image()
		self.image9.set_from_file(path + "9.png")
		self.image9.show()
		self.button9 = gtk.Button()
		self.button9.add(self.image9)
		self.button9.show()
		self.tableNivel.attach(self.button9, 0, 1, 2, 3)
		self.button9.connect("clicked", self.logo, nivel, 9)

		self.image10 = gtk.Image()
		self.image10.set_from_file(path + "10.png")
		self.image10.show()
		self.button10 = gtk.Button()
		self.button10.add(self.image10)
		self.button10.show()
		self.tableNivel.attach(self.button10, 1, 2, 2, 3)
		self.button10.connect("clicked", self.logo, nivel, 10)

		self.image11 = gtk.Image()
		self.image11.set_from_file(path + "11.png")
		self.image11.show()
		self.button11 = gtk.Button()
		self.button11.add(self.image11)
		self.button11.show()
		self.tableNivel.attach(self.button11, 2, 3, 2, 3)
		self.button11.connect("clicked", self.logo, nivel, 11)

		self.image12 = gtk.Image()
		self.image12.set_from_file(path + "12.png")
		self.image12.show()
		self.button12 = gtk.Button()
		self.button12.add(self.image12)
		self.button12.show()
		self.tableNivel.attach(self.button12, 3, 4, 2, 3)
		self.button12.connect("clicked", self.logo, nivel, 12)

		self.image13 = gtk.Image()
		self.image13.set_from_file(path + "13.png")
		self.image13.show()
		self.button13 = gtk.Button()
		self.button13.add(self.image13)
		self.button13.show()
		self.tableNivel.attach(self.button13, 0, 1, 3, 4)
		self.button13.connect("clicked", self.logo, nivel, 13)

		self.image14 = gtk.Image()
		self.image14.set_from_file(path + "14.png")
		self.image14.show()
		self.button14 = gtk.Button()
		self.button14.add(self.image14)
		self.button14.show()
		self.tableNivel.attach(self.button14, 1, 2, 3, 4)
		self.button14.connect("clicked", self.logo, nivel, 14)

		self.image15 = gtk.Image()
		self.image15.set_from_file(path + "15.png")
		self.image15.show()
		self.button15 = gtk.Button()
		self.button15.add(self.image15)
		self.button15.show()
		self.tableNivel.attach(self.button15, 2, 3, 3, 4)
		self.button15.connect("clicked", self.logo, nivel, 15)

		self.image16 = gtk.Image()
		self.image16.set_from_file(path + "16.png")
		self.image16.show()
		self.button16 = gtk.Button()
		self.button16.add(self.image16)
		self.button16.show()
		self.tableNivel.attach(self.button16, 3, 4, 3, 4)
		self.button16.connect("clicked", self.logo, nivel, 16)

		self.image17 = gtk.Image()
		self.image17.set_from_file(path + "17.png")
		self.image17.show()
		self.button17 = gtk.Button()
		self.button17.add(self.image17)
		self.button17.show()
		self.tableNivel.attach(self.button17, 0, 1, 4, 5)
		self.button17.connect("clicked", self.logo, nivel, 17)

		self.image18 = gtk.Image()
		self.image18.set_from_file(path + "18.png")
		self.image18.show()
		self.button18 = gtk.Button()
		self.button18.add(self.image18)
		self.button18.show()
		self.tableNivel.attach(self.button18, 1, 2, 4, 5)
		self.button18.connect("clicked", self.logo, nivel, 18)

		self.image19 = gtk.Image()
		self.image19.set_from_file(path + "19.png")
		self.image19.show()
		self.button19 = gtk.Button()
		self.button19.add(self.image19)
		self.button19.show()
		self.tableNivel.attach(self.button19, 2, 3, 4, 5)
		self.button19.connect("clicked", self.logo, nivel, 19)

		self.image20 = gtk.Image()
		self.image20.set_from_file(path + "20.png")
		self.image20.show()
		self.button20 = gtk.Button()
		self.button20.add(self.image20)
		self.button20.show()
		self.tableNivel.attach(self.button20, 3, 4, 4, 5)
		self.button20.connect("clicked", self.logo, nivel, 20)

		#Botón atrás
		self.atras = gtk.Button("Volver a selección de niveles")
		self.atras.show()
		self.tableNivel.attach(self.atras, 2, 4, 5, 6)
		self.atras.connect("clicked", self.volver)


	def __init__(self):
		self.window = gtk.Window()
		self.window.connect("delete_event", self.delete_event)
		self.window.set_title("FreeLogoQuiz")
		self.window.set_border_width(7)
		self.window.set_default_size(800,550)
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.show()

		#Scroll
		self.scroll = gtk.ScrolledWindow()
		self.scroll.set_border_width(0)
		self.scroll.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)
		self.window.add(self.scroll)

		#Table
		self.table = gtk.Table(1, 4, False)
		self.table.set_row_spacings(10)
		self.table.set_col_spacings(0)

		self.scroll.add_with_viewport(self.table)
		self.scroll.show()
		self.table.show()

		#Botones de niveles
		#Level1
		self.level1 = gtk.Button("Nivel 1\nLogos " + str(completados1) + "/20")
		self.level1.connect("clicked", self.nivel, 1)

		self.mapa1 = self.level1.get_colormap() 
		self.color1 = self.mapa1.alloc_color("#008000")
		self.style1 = self.level1.get_style().copy()
		self.style1.bg[gtk.STATE_NORMAL] = self.color1
		self.level1.set_style(self.style1)

		self.mapa1b = self.level1.get_colormap()
		self.color1b = self.mapa1b.alloc_color("#239023")
		self.style1b = self.level1.get_style().copy()
		self.style1b.bg[gtk.STATE_PRELIGHT] = self.color1b
		self.level1.set_style(self.style1b)

		self.mapa1c = self.level1.get_colormap()
		self.style1c = self.level1.get_style().copy()
		self.style1c.bg[gtk.STATE_ACTIVE] = self.color1b
		self.level1.set_style(self.style1c)

		self.level1.show()
		self.table.attach(self.level1, 0, 1, 0, 1)

		#Level2
		self.level2 = gtk.Button("Nivel 2\nLogos " + str(completados2) + "/20")
		self.level2.connect("clicked", self.nivel, 2)

		self.mapa2 = self.level2.get_colormap()
		self.color2 = self.mapa2.alloc_color("#1d64bc")
		self.style2 = self.level2.get_style().copy()
		self.style2.bg[gtk.STATE_NORMAL] = self.color2
		self.level2.set_style(self.style2)

		self.mapa2b = self.level2.get_colormap()
		self.color2b = self.mapa2b.alloc_color("#3372c0")
		self.style2b = self.level2.get_style().copy()
		self.style2b.bg[gtk.STATE_PRELIGHT] = self.color2b
		self.level2.set_style(self.style2b)

		self.mapa2c = self.level2.get_colormap()
		self.style2c = self.level2.get_style().copy()
		self.style2c.bg[gtk.STATE_ACTIVE] = self.color2b
		self.level2.set_style(self.style2c)

		self.level2.show()
		self.table.attach(self.level2, 0, 1, 1, 2)

		#Level3
		self.level3 = gtk.Button("Nivel 3\nLogos " + str(completados3) + "/20")
		self.level3.connect("clicked", self.nivel, 3)

		self.mapa3 = self.level3.get_colormap()
		self.color3 = self.mapa3.alloc_color("#ffd200")
		self.style3 = self.level3.get_style().copy()
		self.style3.bg[gtk.STATE_NORMAL] = self.color3
		self.level3.set_style(self.style3)

		self.mapa3b = self.level3.get_colormap()
		self.color3b = self.mapa3b.alloc_color("#fdd418")
		self.style3b = self.level3.get_style().copy()
		self.style3b.bg[gtk.STATE_PRELIGHT] = self.color3b
		self.level3.set_style(self.style3b)

		self.mapa3c = self.level3.get_colormap()
		self.style3c = self.level3.get_style().copy()
		self.style3c.bg[gtk.STATE_ACTIVE] = self.color3b
		self.level3.set_style(self.style3c)

		self.level3.show()
		self.table.attach(self.level3, 0, 1, 2, 3)

		#Level4
		self.level4 = gtk.Button("Nivel 4\n Logos " + str(completados4) + "/20")
		self.level4.connect("clicked", self.nivel, 4)

		self.mapa4 = self.level4.get_colormap()
		self.color4 = self.mapa4.alloc_color("#ea0d0d")
		self.style4 = self.level4.get_style().copy()
		self.style4.bg[gtk.STATE_NORMAL] = self.color4
		self.level4.set_style(self.style4)

		self.mapa4b = self.level4.get_colormap()
		self.color4b = self.mapa4b.alloc_color("#ea2424")
		self.style4b = self.level4.get_style().copy()
		self.style4b.bg[gtk.STATE_PRELIGHT] = self.color4b
		self.level4.set_style(self.style4b)

		self.mapa4c = self.level4.get_colormap()
		self.style4c = self.level4.get_style().copy()
		self.style4c.bg[gtk.STATE_ACTIVE] = self.color4b
		self.level4.set_style(self.style4c)

		self.level4.show()
		self.table.attach(self.level4, 0, 1, 3, 4)


def main():
	gtk.main()
	return 0

if __name__ == "__main__":
	Menu()
	main()
