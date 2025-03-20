import pyodbc

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=172.16.0.41;DATABASE=DW_TEXNEO_HOMOLOG;UID=ext.lizardti.01;PWD=rzQUB%YjT&pSg6')

print("db connected")