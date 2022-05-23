import pandas as pd
import uuid
import sqlite3 as sq
import os

# DIKARENAKAN MENGGUNAKAN metode nama_model.objects.create
# TIDAK BISA MAKA TERPAKSA MENGGUNAKAN LANGSUNG INJECT SQL
# KEDALAM DATABASE (TIDAK DISARANKAN. DIPERUNTUKAN HANYA UNTUK UJI COBA SAJA)


dnegara = pd.read_excel('negara.xlsx', sheet_name='negara')
conn = sq.connect('db.sqlite3')

with open ('dumdum.txt', 'w') as dumdum:
	for iid, data in zip(range(dnegara.shape[0]), dnegara.itertuples()):
		command_sql = """ INSERT INTO MajuJayaApp_data_negara VALUES( {}, "{}", "{}", {} );""".format(
				iid+1,
				uuid.uuid4(),
				data.Country,
				True,
			)
		conn.execute(command_sql)

conn.commit()
conn.close()
os.system('dumdum.txt')
print('selesai..')