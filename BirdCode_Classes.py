# ===================================== BirdCode Classes =======================================
from Sites_Classes import *
from Markers import *

class Accipiter_trivirgatus():

	def __init__(self):

		self.scientific_name = 'Accipiter trivirgatus'
		self.presence = False
		self.sites_present = ['Chengdu']


	def Image_display(self):

		for i, value in enumerate(Sites):

			if value.name in self.sites_present:

				print('Done')



Accipiter_trivirgatus_00 = Accipiter_trivirgatus()

turn_species = [Accipiter_trivirgatus_00]



