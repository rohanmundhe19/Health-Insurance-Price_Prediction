import mysql.connector
from mysql.connector import Error, MySQLConnection
import config

def insert_query(args):
    conn = MySQLConnection(**config.DB_PARAM)
    cursor = conn.cursor()
    try:
        
        
        insert_query = """ INSERT INTO user_data (age,gender,bmi,children,smoker,region,charges)
                            values (%s,%s,%s,%s,%s,%s,%s)"""
        cursor.execute(insert_query,args)

        if cursor.lastrowid:
            print(f"last rowid = {cursor.lastrowid}")
        else:
            print(f"NO id found")
        
        conn.commit()

    except Error as error:
        print(error) 

    finally:
        cursor.close()
        conn.close()



if __name__ == "__main__":
    user_data = (36, 'female', 24, 1, 'yes', 'southeast', 20071.92)
    insert_query(user_data)
