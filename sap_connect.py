from hdbcli import dbapi

conn = dbapi.connect(
    address='sap-s4h-s01.moscow.terralink', 
    port=30015, 
    user='PROSKURIND',
    password='Resident4')

cursor = conn.cursor()

print(conn)
print(cursor)



# gпримеры рабочих запросов
#sql_command = "SELECT BISMT FROM ABAPS417.MARA WHERE MANDT=500"
sql_command = "SELECT COLUMN_NAME, DATA_TYPE_NAME FROM SYS.TABLE_COLUMNS WHERE TABLE_NAME = 'MARA' ORDER BY POSITION; "
#sql_command = "SELECT COLUMN_NAME, DATA_TYPE_NAME, IS_NULLABLE FROM SYS.TABLE_COLUMNS WHERE TABLE_NAME = 'MARA' AND IS_NULLABLE = 'TRUE' ORDER BY POSITION; "
cursor.execute(sql_command)

rows = cursor.fetchall()



for row in rows:
    for col in row:
        print ("%s" % col, end=" |0_0| ")
        
    print ("  ")


    #print ("  ")
    #print ("  ")
    #print ("  ")
    #print ("  ")


cursor.close()
conn.close()