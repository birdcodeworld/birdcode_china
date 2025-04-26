# ========================= Sites Classes ==========================================

import psycopg2


class Point():

	def __init__(self):

		self.description = 'Locality'
		self.ecoregion_location = ''

	def db_connection(self, code):

		self.miConexion_point = psycopg2.connect(host = 'bctc8tdlqly4cpe3dj0b-postgresql.services.clever-cloud.com', port = 50013, 
		user = 'uylah5thtah6mgce6pcu', dbname = 'bctc8tdlqly4cpe3dj0b', password = 'W4IDeZIuZSOKKxRqzXhjFsiu1WFcYT')
		self.miCursor_point = self.miConexion_point.cursor()
		self.myProvince = '''select eco_name from ecoregions_china, birding_sites_china 
		where st_intersects(ecoregions_china.geom, birding_sites_china.geom) and birding_sites_china.id = (%s);'''

		self.dlt12 = (int(code), )

		self.miCursor_point.execute(self.myProvince, self.dlt12)
		self.myProvince_results = self.miCursor_point.fetchall()
		
		return self.myProvince_results[0][0]

		self.miConexion_point.commit()
		self.miConexion_point.close()



class Chengdu(Point):

	def __init__(self):

		self.code = 0
		self.name = 'Chengdu'
		self.name_zh = '成都植物园'
		self.latitude = 30.764904
		self.longitude = 104.1285
		self.richness = 115
		self.gbif_records = 1084




class Tangjiahe():

	def __init__(self):

		self.name = 'Tangjiahe'
		self.name_zh = '唐家河国家级自然保护区'
		self.latitude = 32.60294
		self.longitude = 104.788284
		self.richness = 302
		self.gbif_records = 6615


class Gonggangling():

	def __init__(self):

		self.name = 'Gonggangling'
		self.name_zh = '弓杠岭'
		self.latitude = 33.050507
		self.longitude = 103.731224
		self.richness = 193
		self.gbif_records = 2076


class Zoige():

	def __init__(self):

		self.name = 'Zoigê'
		self.name_zh = '若尔盖县 请用更详细的热点'
		self.latitude = 33.577633
		self.longitude = 102.96273
		self.richness = 281
		self.gbif_records = 2314


class Mengbishan():

	def __init__(self):

		self.name = 'Mengbishan'
		self.name_zh = '梦笔山'
		self.latitude = 31.716778
		self.longitude = 102.29581
		self.richness = 198
		self.gbif_records = 3442


class Balangshan():

	def __init__(self):

		self.name = 'Balangshan'
		self.name_zh = '巴郎山'
		self.latitude = 30.878435
		self.longitude = 102.94677
		self.richness = 295
		self.gbif_records = 7800


class Labahe():

	def __init__(self):

		self.name = 'Labahe'
		self.name_zh = '喇叭河自然保护区'
		self.latitude = 30.186972
		self.longitude = 102.43161
		self.richness = 249
		self.gbif_records = 3604


class Longcanggou():

	def __init__(self):

		self.name = 'Longcanggou'
		self.name_zh = '龙苍沟'
		self.latitude = 29.618834
		self.longitude = 102.890785
		self.richness = 306
		self.gbif_records = 13330




Chengdu_00 = Chengdu()
#print(Chengdu_00.db_connection('1'))
Tangjiahe_00 = Tangjiahe()
Gonggangling_00 = Gonggangling()
Zoige_00 = Zoige()
Mengbishan_00 = Mengbishan()
Balangshan_00 = Balangshan()
Labahe_00 = Labahe()
Longcanggou_00 = Longcanggou()


Sites = [Chengdu_00, Tangjiahe_00, Gonggangling_00, Zoige_00, Mengbishan_00, Balangshan_00, Labahe_00, Longcanggou_00]
Route1 = [[30.8080854, 104.1500728], [30.9206707, 104.2339539], [31.0125197, 104.3026184], [31.2030004, 104.4372010],
[31.4212284, 104.5745301], [31.6849526, 104.6835089], [31.9596719, 104.7906256], [32.1691553, 104.8071051],
[32.4569893, 104.7906256], [32.6028766, 104.8510504]]