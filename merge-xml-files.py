#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Det här skriptet slår ihop alla xml-filer i samma mapp som skriptet ligger.

import csv
import glob

# Hämta in alla xml-filer i mappen
files = glob.glob("*.xml")
print files

# Definiera vad output-filen ska heta
outFile = "output.xml"

# Töm output-filen på innehåll
fclear = open(outFile,"w")
fclear.write("")
fout = open(outFile,"a")

# Skriv en första rad med ett samlande xml-objekt 
fout.write("<data>")

# Loop alla xml-filerna
for fileName in files:
	f = open(fileName)
	# Loopa varje rad i xml-filen och skriv motsvarande rad till output-filen
	for line in f:
		fout.write(line)
	f.close() # not really needed

# Avsluta xml-filen
fout.write("</data>")
fout.close()
