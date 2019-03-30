from random import randint
import os
from math import ceil

argent=1000
continuer=True
print('vous commencer avec {0} euros'.format(argent))

while continuer:
	nombre=-1
	
	#on verifie que le nombre saisi correspond a ce qui a ete demande
	while nombre<0 or nombre>50:
		nombre=input("Choisissez un nombre entre 0 et 50 : ")
		try:
			nombre=int(nombre)
		except ValueError:
			print("vous n'avez pas saisi de nombre")
			nombre=-1
			continue	
		if nombre<0:
			print('ce nombre est negatif')
		if nombre>50:
			print('ce nombre est trop grand')

	mise=0
	#meme verification pour la mise
	while mise<=0 or mise>argent:
		mise=input("taper le montant de votre mise: ")
		try:
			mise=int(mise)
		except ValueError:
			print("vous n'avez pas saisi de nombre")
			mise=-1
			continue
		if mise<=0:
			print('vous devez miser une somme minimum de 1 euro')
		if mise>argent:
			print("vous n'avez pas assez d argent")

	#on tire le numero de la roulette
	nombre_machine=randint(0,50)
	#ou nombre_machine=randrange(50)
	print("le numero gagnant est le {0}".format(nombre_machine))
	
	"""
    couleur_machine=''
	if nombre%2==0:
		couleur='rouge'
	else:
		couleur='noir'

	#on verifie la couleur du nombre de la roulette
	if nombre_machine%2==0:
		couleur_machine='rouge'
	else:
		couleur_machine='noir'
		"""
	
	if nombre==nombre_machine:
		mise=mise*3
		print('bravo vous avez gagne {0}'. format(mise))
		argent+=mise
	elif nombre%2==nombre_machine%2:
		mise=ceil(mise*0.5)
		print('vous avez gagne {0}'. format(mise))
		argent+=mise
	else:
		print('vous avez perdu votre mise')
		argent-=mise

	if argent<=0:
		print("vous etes ruine!")
		continuer=False
	else:
		print("vous avez a present {0}". format(argent))
		quitter=raw_input("souhaitez vous quitter le casino (o/n): ")
		if quitter=="o" or quitter=="O":
			print('vous quittez le casino avec {0}'. format(argent))
			continuer= False
		

os.system("pause")