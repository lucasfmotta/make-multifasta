#!/usr/bin/python3

import os

directorio = os.listdir(os.curdir)
fastas = []
for file in directorio:
	if file.endswith('.FASTA'):
		fastas.append(file)

if not fastas:
	print('No .FASTA files found')
	quit()

multifasta = open('multiFasta.FASTA', 'a')
for file in fastas:
	fasta = open(file)
	for line in fasta:
		line = line.rstrip()
		multifasta.write(line)
		multifasta.write('\n')
	fasta.close()
multifasta.close()
