import pymysql


db_host = 'db-cym-gr8.cjqq0o4aioah.us-east-1.rds.amazonaws.com'
db_user = 'johan'
db_password = 'Capsula-0a**'
db_name = 'db_users'


def connectionSQL():
    try:
        connection = pymysql.connect(
            host = db_host,
            user = db_user,
            password = db_password,
            database = db_name
            )
        print('Succesfull connection to DB')
        return connection
    except Exception as err:
        print("Error connecting to DB", err)
        
def insert_records(id, name, lastname, birthday):
    query = 'INSERT INTO users (id,name, lastname, birthday) VALUES ('+id+',"'+name+'","'+lastname+'","'+birthday+'")'
    try:
        connection = connectionSQL()
        if connection != None:
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            print("User added")
        else:
            print("Error in the connection")
    except Exception as err:
        print ("Error creating the user", err)
        
        
def consult_records(id):
    query = "SELECT * FROM users WHERE id = " + str(id)
    try:
        connection = connectionSQL()
        cursor = connection.cursor()
        if connection != None:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        else:
            print("Error in the connection")
            return None
    except Exception as err:
        print ("Error consulting the user " + id, err)
        return None