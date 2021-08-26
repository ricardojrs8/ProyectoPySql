# Importamos el módulo
import sqlite3
import csv

conexion = sqlite3.connect('mibus.db')
# Creamos el cursor
cursor = conexion.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS distancias_entre_paradas  " \
    "(rt_id VARCHAR(100), sn INTEGER, stop_cd VARCHAR(100), pattn_detail_id INTEGER, is_active VARCHAR(100), lmt_spd INTEGER, dist INTEGER, topology VARCHAR(100))")
cursor.execute("CREATE TABLE IF NOT EXISTS transacciones " \
    "(fecha_transaccion VARCHAR(100), bus INTEGER, validador INTEGER, tarjeta INTEGER, fecha_registrocle  VARCHAR(100), tarifa_monto INTEGER, c_tipo_transaccion VARCHAR(100), codigo_transacciones INTEGER, fecha_contabilizacion VARCHAR(100))")

archivo = open(r"/Users/ricardoruiz/Desktop/PruebMibus/paattern_detaill.csv")
archivo2 = open(r"/Users/ricardoruiz/Desktop/PruebMibus/transaccionesxx.csv")

filas   = csv.reader(archivo,delimiter=";")
lista = list (filas)

filas2   = csv.reader(archivo2,delimiter=";")
lista2 = list (filas2)

#del (lista[0])
tuplaa = tuple(lista)
tuplaa2 = tuple(lista2)

#insertar

cursor.executemany("INSERT INTO distancias_entre_paradas ('rt_id','sn','stop_cd','pattn_detail_id','is_active','lmt_spd','dist','topology') VALUES (?,?,?,?,?,?,?,?)",tuplaa)
cursor.executemany("INSERT INTO transacciones('fecha_transaccion','bus','validador','tarjeta','fecha_registrocle','tarifa_monto','c_tipo_transaccion','codigo_transacciones','fecha_contabilizacion') VALUES (?,?,?,?,?,?,?,?,?)",tuplaa2)

# Guardamos los cambios haciendo un commit
conexion.commit()
conexion.close()



