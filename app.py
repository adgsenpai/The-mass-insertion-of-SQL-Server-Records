import sqlserver
import time
connectionstring = 'Driver={ODBC Driver 17 for SQL Server};Server=(local);Database=ADGSTUDIOS;Trusted_Connection=yes;'
db = sqlserver.adgsqlserver(connectionstring)

path = r'C:\Users\adgru\Code\The-mass-insertion-of-SQL-Server-Records-algorithm\datasets\babynames.csv'
start = time.time()
print('Creating table')
db.CreateCSVTable(path)
print('Table created')
print('Time taken to create table: ', time.time() - start)
print('inserting data')
db.InsertCSVData(path)
print('Data inserted')
datatime = time.time() 
print('Time taken to insert data: ', datatime - start)
end = time.time()
# print time in seconds
print('Total time taken: ', end - start)
