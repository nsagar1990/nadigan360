import os
import datetime
import traceback
from datetime import *

class Backup:
	def __init__(self):
		self.name = "backup"
		self.created_time = datetime.now()
		self.two_days_older = datetime.now() - timedelta(days=2)
		self.messages	= []

	def create_backup(self):
		try:
			#2015-02-16 03:12:41.852419
			timestamp = datetime.strftime(self.created_time, "%d_%m_%y_%H_%M_%s")
			print timestamp
			cmd = "mysqldump NADIGAN > NADIGAN_%s.sql" %timestamp
			status = os.popen(cmd)

			del_cmd = "%s_*" %datetime.strftime(self.two_days_older, "%d_%m_%y")
			print del_cmd
			status 	= os.popen(cmd)

		except:
			print traceback.format_exc()


if __name__ == "__main__":
	Backup().create_backup()
