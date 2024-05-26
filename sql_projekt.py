'''
import os
print(os.getcwd())
'''
import psycopg2
import pandas as pd



DBNAME = 'skillfactory'
USER = 'skillfactory'
PASSWORD = 'cCkxxLVrDE8EbvjueeMedPKt'
HOST = '84.201.134.129'
PORT = 5432

connection = psycopg2.connect(
   dbname=DBNAME, # название базы к которой надо подключиться 
   user=USER, # имя польователя СУБД
   host=HOST, # адрес по которому надо подключиться
   password=PASSWORD, # пароль
   port=PORT # порт к которому надо подключиться. 5432 по умолчанию
)
# код запроса 
n = 10
query = f'''select * 
            from sql.pokemon
            limit {n}
            '''
# выполнение запроса
df = pd.read_sql_query(query, connection)
print(df)
# необходимо закрыть соединение после окончания работы
connection.close()
