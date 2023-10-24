import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="",database="welcome")
print(mydb)

# cursor() method allows python code to execute database command
crsr=mydb.cursor()

# create database

# crsr.execute("create database welcome")
# print("database created")

crsr.execute('use welcome')
# create table

# crsr.execute("create table good(id int primary key auto_increment,name varchar(34),place varchar(34))")
# print("table created")

# insert values to a table

# a="insert into good(name,place)values(%s,%s)"
# b=[("anu","goa"),("manu","chennai"),("akhila","dubai")]
# crsr.executemany(a,b)
# mydb.commit()
# print("values inserted")

# display values in a table

# crsr.execute("select *from good")
# c=crsr.fetchall()
# for i in c:
#     print(i)

# update table

# crsr.execute("update good set name='gouri' where id=5")
# mydb.commit()
# print("updated")

# delete table

# crsr.execute("delete from good where place='dubai'")
# mydb.commit()
# print("deleted")

# drop table
# crsr.execute("drop table good")
# print("droped")

# drop database
crsr.execute("drop database welcome")
print("drop database")

