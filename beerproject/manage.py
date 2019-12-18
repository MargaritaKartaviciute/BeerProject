#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import csv
import datetime
#
# import mysql.connector
# from pymysql import NULL

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beerproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

# def categories(mycursor, mydb):
#     data = read_categories_data()
#     stmt = "SHOW TABLES LIKE 'categories'"
#     mycursor.execute(stmt)
#     result = mycursor.fetchone()
#     if result is None:
#         mycursor.execute("CREATE TABLE categories (id INT(11) NOT NULL AUTO_INCREMENT,cat_name VARCHAR(255), last_mod date NOT NULL, PRIMARY KEY (id) )")
#
#     stmt = "SELECT * FROM categories"
#     mycursor.execute(stmt)
#     rows = mycursor.fetchall()
#     if len(rows) == 0:
#         sql = "INSERT INTO categories (cat_name, last_mod) VALUES (%s, %s)"
#         for dict in data:
#             val = (dict['cat_name'],  datetime.datetime.strptime(dict['last_mod'][:-4], '%Y-%m-%d %H:%M:%S'))
#             mycursor.execute(sql, val)
#         mydb.commit()
#
# def breweries(mycursor, mydb):
#     data = read_breweries_data()
#     stmt = "SHOW TABLES LIKE 'breweries'"
#     mycursor.execute(stmt)
#     result = mycursor.fetchone()
#     if result is None:
#         mycursor.execute("CREATE TABLE breweries (id INT(11) NOT NULL,name VARCHAR(255), address1 VARCHAR(255) NULL, address2 VARCHAR(255) NULL, city VARCHAR(255) NULL, PRIMARY KEY (id))")
#
#     stmt = "SELECT * FROM breweries"
#     mycursor.execute(stmt)
#     rows = mycursor.fetchall()
#     if len(rows) == 0:
#         sql = "INSERT INTO breweries (id, name, address1, address2, city) VALUES (%s, %s, %s, %s, %s)"
#         for dict in data:
#             val = (dict['id'], dict['name'], dict['address1'], dict['address2'],  dict['city'])
#             mycursor.execute(sql, val)
#         mydb.commit()
#
# def styles(mycursor, mydb):
#     data = read_styles_data()
#     stmt = "SHOW TABLES LIKE 'styles'"
#     mycursor.execute(stmt)
#     result = mycursor.fetchone()
#     if result is None:
#         mycursor.execute("CREATE TABLE styles (id INT(11) NOT NULL AUTO_INCREMENT,cat_id INT(255), style_name VARCHAR(255) NOT NULL, last_mod date NOT NULL, PRIMARY KEY (id), FOREIGN KEY (cat_id) REFERENCES categories(id) )")
#
#     stmt = "SELECT * FROM styles"
#     mycursor.execute(stmt)
#     rows = mycursor.fetchall()
#     if len(rows) == 0:
#         sql = "INSERT INTO styles (cat_id, style_name, last_mod) VALUES (%s, %s, %s)"
#         for dict in data:
#             val = (dict['cat_id'], dict['style_name'], datetime.datetime.strptime(dict['last_mod'][:-4], '%Y-%m-%d %H:%M:%S'))
#             mycursor.execute(sql, val)
#         mydb.commit()
#
# def geocodes(mycursor, mydb):
#     data = read_geocodes_data()
#     stmt = "SHOW TABLES LIKE 'geocodes'"
#     mycursor.execute(stmt)
#     result = mycursor.fetchone()
#     if result is None:
#         mycursor.execute("CREATE TABLE geocodes (id INT(11) NOT NULL,brewery_id INT(11) NOT NULL, latitude FLOAT (20) NOT NULL, longitude FLOAT (20) NOT NULL, accuracy VARCHAR(255) NOT NULL, PRIMARY KEY (id), FOREIGN KEY (brewery_id) REFERENCES breweries(id))")
#
#     stmt = "SELECT * FROM geocodes"
#     mycursor.execute(stmt)
#     rows = mycursor.fetchall()
#     if len(rows) == 0:
#         sql = "INSERT INTO geocodes (id, brewery_id, latitude, longitude, accuracy) VALUES (%s, %s, %s, %s, %s)"
#
#         for dict in data:
#             val = dict['brewery_id']
#             mycursor.execute("SELECT * FROM breweries WHERE id = %s", (val,))
#             rows = mycursor.fetchall()
#             if len(rows) != 0:
#                 val = (dict['id'], dict['brewery_id'], dict['latitude'], dict['longitude'], dict['accuracy'])
#                 mycursor.execute(sql, val)
#         mydb.commit()
#
# def beers(mycursor, mydb):
#     data = read_beers_data()
#     stmt = "SHOW TABLES LIKE 'beers'"
#     mycursor.execute(stmt)
#     result = mycursor.fetchone()
#     if result is None:
#         mycursor.execute("CREATE TABLE beers (id INT(11) NOT NULL,brewery_id INT(11) NOT NULL, name VARCHAR (255) NOT NULL, PRIMARY KEY (id), FOREIGN KEY (brewery_id) REFERENCES breweries(id))")
#
#     stmt = "SELECT * FROM beers"
#     mycursor.execute(stmt)
#     rows = mycursor.fetchall()
#     if len(rows) == 0:
#         sql = "INSERT INTO beers (id, brewery_id, name) VALUES (%s, %s, %s)"
#         for dict in data:
#             val = (dict['id'], dict['brewery_id'], dict['name'])
#             mycursor.execute(sql, val)
#         mydb.commit()
#
# def read_categories_data():
#     DATA_SRC = 'breweries/static/categories.csv'
#
#     data = []
#     with open(DATA_SRC, 'r') as f:
#         next(f)
#         reader = csv.reader(f, delimiter=',')
#         for row in reader:
#
#             if len(row) != 3:
#                 continue
#
#             thisdict = {
#                 "cat_name": row[1],
#                 "last_mod": row[2]
#             }
#             data.append(thisdict)
#
#     return data
#
# def read_styles_data():
#     DATA_SRC = 'breweries/static/styles.csv'
#
#     data = []
#     with open(DATA_SRC, 'r') as f:
#         next(f)
#         reader = csv.reader(f, delimiter=',')
#         for row in reader:
#
#             if len(row) != 4:
#                 continue
#
#             thisdict = {
#                 "cat_id": row[1],
#                 "style_name": row[2],
#                 "last_mod": row[3]
#             }
#             data.append(thisdict)
#
#     return data
#
# def read_breweries_data():
#     DATA_SRC = 'breweries/static/breweries.csv'
#
#     data = []
#     with open(DATA_SRC, 'r') as f:
#         next(f)
#         reader = csv.reader(f, delimiter=',')
#         for row in reader:
#
#             if len(row) != 14:
#                 continue
#
#             thisdict = {
#                 "id": row[0],
#                 "name": row[1],
#                 "address1": row[2],
#                 "address2": row[3],
#                 "city": row[4]
#             }
#             data.append(thisdict)
#
#     return data
#
# def read_geocodes_data():
#     DATA_SRC = 'breweries/static/geocodes.csv'
#
#     data = []
#     with open(DATA_SRC, 'r') as f:
#         next(f)
#         reader = csv.reader(f, delimiter=',')
#         for row in reader:
#
#             if len(row) != 5:
#                 continue
#
#             thisdict = {
#                 "id": row[0],
#                 "brewery_id": row[1],
#                 "latitude": row[2],
#                 "longitude": row[3],
#                 "accuracy": row[4]
#             }
#             data.append(thisdict)
#     return data
#
# def read_beers_data():
#     DATA_SRC = 'breweries/static/beers.csv'
#
#     data = []
#     with open(DATA_SRC, 'r') as f:
#         next(f)
#         reader = csv.reader(f, delimiter=',')
#         for row in reader:
#
#             if len(row) != 13:
#                 continue
#
#             thisdict = {
#                 "id": row[0],
#                 "brewery_id": row[1],
#                 "name": row[2]
#             }
#             data.append(thisdict)
#
#     return data
#
#
# def convert():
#     mydb = mysql.connector.connect(
#         host="",
#         user="user",
#         database='beerproject',
#         passwd="password"
#     )
#     mycursor = mydb.cursor()
#     categories(mycursor, mydb)
#     styles(mycursor, mydb)
#     breweries(mycursor, mydb)
#     geocodes(mycursor, mydb)
#     beers(mycursor, mydb)


if __name__ == '__main__':
    # convert()
    main()




