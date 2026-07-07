import pymysql

def db():
    return pymysql.connect(
        host= '127.0.0.1',
        user= 'root',
        password= 'ny2005ny',
        database= 'datateste',
        cursorclass=pymysql.cursors.DictCursor 
    )
