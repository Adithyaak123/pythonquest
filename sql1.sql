#to create database
create database student;

# to use database
use student;

# delete database
drop database student;

# to create table
create table adithya(id int,name varchar(20),age int);

# to delete table 
drop table adithya;

# to display databases
show databases;

# insert values to a table
insert into adithya values(1,'ammu',23);
insert into adithya values(2,'pavithra',21),(3,'minnu',13);
insert into adithya(id,name,age)values(4,'sruthi',45);

# display values of a table
select *from adithya;
select id,name from adithya;

# to use condition - where clause
select name from adithya where age=13;

# update table
update adithya set name='jiya' where id=1;

# delete column of a table
delete from adithya where id=4;