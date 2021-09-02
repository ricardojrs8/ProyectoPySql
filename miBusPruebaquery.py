# Importamos el módulo
import sqlite3
import csv
import pandas as pd
import numpy as np

conexion = sqlite3.connect("mibus.db")
cursor   = conexion.cursor()

#1.	¿Cuántas transacciones se realizan por cada hora? (mostrar las 24 horas)
def fecha_transaccion(conexion):

    sql1 = "SELECT fecha_transaccion FROM transacciones WHERE fecha_transaccion LIKE '01/26/2018 01:%';"
    sql2 = "SELECT fecha_transaccion FROM transacciones WHERE fecha_transaccion LIKE '01/26/2018 02:%';"
    sql3 = "SELECT fecha_transaccion FROM transacciones WHERE fecha_transaccion LIKE '01/26/2018 03:%';"
    sql4 = "SELECT fecha_transaccion FROM transacciones WHERE fecha_transaccion LIKE '01/26/2018 04:%';"
    sql5 = "SELECT fecha_transaccion FROM transacciones WHERE fecha_transaccion LIKE '01/26/2018 05:%';"
    sql6 = "SELECT fecha_transaccion FROM transacciones WHERE fecha_transaccion LIKE '01/26/2018 06:%';"
    sql7 = "SELECT fecha_transaccion FROM transacciones WHERE fecha_transaccion LIKE '01/26/2018 07:%';"
    sql8 = "SELECT fecha_transaccion FROM transacciones WHERE fecha_transaccion LIKE '01/26/2018 08:%';"
    sql9 = "SELECT fecha_transaccion FROM transacciones WHERE fecha_transaccion LIKE '01/26/2018 09:%';"
    sql10 = "SELECT fecha_transaccion FROM transacciones WHERE fecha_transaccion LIKE '01/26/2018 10:%';"
    sql11 = "SELECT fecha_transaccion FROM transacciones WHERE fecha_transaccion LIKE '01/26/2018 11:%';"
    sql12 = "SELECT fecha_transaccion FROM transacciones WHERE fecha_transaccion LIKE '01/26/2018 12:%';"
    
    ##PM
    
    sql13 = "SELECT fecha_transaccion FROM transacciones WHERE fecha_transaccion LIKE '01/26/2018 13:%';"
    sql14 = "SELECT fecha_transaccion FROM transacciones WHERE fecha_transaccion LIKE '01/26/2018 14:%';"
    sql15 = "SELECT fecha_transaccion FROM transacciones WHERE fecha_transaccion LIKE '01/26/2018 15:%';"
    sql16 = "SELECT fecha_transaccion FROM transacciones WHERE fecha_transaccion LIKE '01/26/2018 16:%';"
    sql17 = "SELECT fecha_transaccion FROM transacciones WHERE fecha_transaccion LIKE '01/26/2018 17:%';"
    sql18 = "SELECT fecha_transaccion FROM transacciones WHERE fecha_transaccion LIKE '01/26/2018 18:%';"
    sql19 = "SELECT fecha_transaccion FROM transacciones WHERE fecha_transaccion LIKE '01/26/2018 19:%';"
    sql20 = "SELECT fecha_transaccion FROM transacciones WHERE fecha_transaccion LIKE '01/26/2018 20:%';"
    sql21 = "SELECT fecha_transaccion FROM transacciones WHERE fecha_transaccion LIKE '01/26/2018 21:%';"
    sql22 = "SELECT fecha_transaccion FROM transacciones WHERE fecha_transaccion LIKE '01/26/2018 22:%';"
    sql23 = "SELECT fecha_transaccion FROM transacciones WHERE fecha_transaccion LIKE '01/26/2018 23:%';"
    sql24 = "SELECT fecha_transaccion FROM transacciones WHERE fecha_transaccion LIKE '01/26/2018 24:%';"
    
    
    cursor1 = conexion.cursor()
    cursor1.execute(sql1)
    cursor2 = conexion.cursor()
    cursor2.execute(sql2)
    cursor3 = conexion.cursor()
    cursor3.execute(sql3)
    cursor4 = conexion.cursor()
    cursor4.execute(sql4)
    cursor5 = conexion.cursor()
    cursor5.execute(sql5)
    cursor6 = conexion.cursor()
    cursor6.execute(sql6)
    cursor7 = conexion.cursor()
    cursor7.execute(sql7)
    cursor8 = conexion.cursor()
    cursor8.execute(sql8)
    cursor9 = conexion.cursor()
    cursor9.execute(sql9)
    cursor10 = conexion.cursor()
    cursor10.execute(sql10)
    cursor11 = conexion.cursor()
    cursor11.execute(sql11)
    cursor12 = conexion.cursor()
    cursor12.execute(sql12)

    ###Pm

    cursor13 = conexion.cursor()
    cursor13.execute(sql13)
    cursor14 = conexion.cursor()
    cursor14.execute(sql14)
    cursor15 = conexion.cursor()
    cursor15.execute(sql15)
    cursor16 = conexion.cursor()
    cursor16.execute(sql16)
    cursor17 = conexion.cursor()
    cursor17.execute(sql17)
    cursor18 = conexion.cursor()
    cursor18.execute(sql18)
    cursor19 = conexion.cursor()
    cursor19.execute(sql19)
    cursor20 = conexion.cursor()
    cursor20.execute(sql20)
    cursor21 = conexion.cursor()
    cursor21.execute(sql21)
    cursor22 = conexion.cursor()
    cursor22.execute(sql22)
    cursor23 = conexion.cursor()
    cursor23.execute(sql23)
    cursor24 = conexion.cursor()
    cursor24.execute(sql24)
    
    registros1 = cursor1.fetchall()
    registros2 = cursor2.fetchall()
    registros3 = cursor3.fetchall()
    registros4 = cursor4.fetchall()
    registros5 = cursor5.fetchall()
    registros6 = cursor6.fetchall()
    registros7 = cursor7.fetchall()
    registros8 = cursor8.fetchall()
    registros9 = cursor9.fetchall()
    registros10 = cursor10.fetchall()
    registros11 = cursor11.fetchall()
    registros12 = cursor12.fetchall()

    ##PM
    registros13 = cursor13.fetchall()
    registros14 = cursor14.fetchall()
    registros15 = cursor15.fetchall()
    registros16 = cursor16.fetchall()
    registros17 = cursor17.fetchall()
    registros18 = cursor18.fetchall()
    registros19 = cursor19.fetchall()
    registros20 = cursor20.fetchall()
    registros21 = cursor21.fetchall()
    registros22 = cursor22.fetchall()
    registros23 = cursor23.fetchall()
    registros24 = cursor24.fetchall()

    

    registro1 = len(registros1)
    registro2 = len(registros2)
    registro3 = len(registros3)
    registro4 = len(registros4)
    registro5 = len(registros5)
    registro6 = len(registros6)
    registro7 = len(registros7)
    registro8 = len(registros8)
    registro9 = len(registros9)
    registro10 = len(registros10)
    registro11 = len(registros11)
    registro12 = len(registros12)
    registro13 = len(registros13)
    registro14 = len(registros14)
    registro15 = len(registros15)
    registro16 = len(registros16)
    registro17 = len(registros17)
    registro18 = len(registros18)
    registro19 = len(registros19)
    registro20 = len(registros20)
    registro21 = len(registros21)
    registro22 = len(registros22)
    registro23 = len(registros23)
    registro24 = len(registros24)

    listados =[registro1,registro2,registro3,registro4,registro5,registro6,registro7,registro8,registro9,registro10,registro11,registro12,registro13,registro14,registro15,registro16,registro17,registro18,registro19,registro20,registro21,registro22,registro23,registro24]
    arr = np.array(listados)

    ##print(arr)

    print("")
    print("------ MAÑANA ------ "+'\n')
    print(registro1, "Transaciones a las 1 del 01/26/2018")
    print(len(registros2), "Transaciones a las 2 del 01/26/2018")
    print(len(registros3), "Transaciones a las 3 del 01/26/2018")
    print(len(registros4), "Transaciones a las 4 del 01/26/2018")
    print(len(registros5), "Transaciones a las 5 del 01/26/2018")
    print(len(registros6), "Transaciones a las 6 del 01/26/2018")
    print(len(registros7), "Transaciones a las 7 del 01/26/2018")
    print(len(registros8), "Transaciones a las 8 del 01/26/2018")
    print(len(registros9), "Transaciones a las 9 del 01/26/2018")
    print(len(registros10),"Transaciones a las 10 del 01/26/2018")
    print(len(registros11),"Transaciones a las 11 del 01/26/2018"+'\n')


    ##PM 

    print("------ TARDE ------ "+'\n')

    print(len(registros12), "Transaciones a las 12md del 01/26/2018")
    print(len(registros13), "Transaciones a las 13pm del 01/26/2018")
    print(len(registros14), "Transaciones a las 14 del 01/26/2018")
    print(len(registros15), "Transaciones a las 15 del 01/26/2018")
    print(len(registros16), "Transaciones a las 16 del 01/26/2018")
    print(len(registros17), "Transaciones a las 17 del 01/26/2018")
    print(len(registros18), "Transaciones a las 18 del 01/26/2018")
    print(len(registros19), "Transaciones a las 19 del 01/26/2018")
    print(len(registros20), "Transaciones a las 20 del 01/26/2018")
    print(len(registros21), "Transaciones a las 21 del 01/26/2018")
    print(len(registros22), "Transaciones a las 22 del 01/26/2018")
    print(len(registros23), "Transaciones a las 23 del 01/26/2018")
    print(len(registros24), "Transaciones a las 24 del 01/26/2018")

    df1=pd.DataFrame(arr)
    df1.reset_index().to_csv('pregun1.csv', header=True, index=False)


def bus_max_30(conexion):
    sql1 = "SELECT bus FROM transacciones WHERE bus = 411"
    sql2 = "SELECT bus FROM transacciones WHERE bus = 1010"
    sql3 = "SELECT bus FROM transacciones WHERE bus = 131"
    sql4 = "SELECT bus FROM transacciones WHERE bus = 1064"


  
    cursor1 = conexion.cursor()
    cursor1.execute(sql1)
    registros1 = cursor1.fetchall()
    cursor2 = conexion.cursor()
    cursor2.execute(sql2)
    registros2 = cursor2.fetchall()
    cursor3 = conexion.cursor()
    cursor3.execute(sql3)
    registros3 = cursor3.fetchall()
    cursor4 = conexion.cursor()
    cursor4.execute(sql4)
    registros4 = cursor4.fetchall()


    print(len(registros1).real, "bus 411");
    listados = ['registros1','registros2','registros3','registros4']
    print(max(listados))
 

fecha_transaccion(conexion)
#bus_max_30(conexion)

# Guardamos los cambios haciendo un commit
conexion.commit()
conexion.close()
