use MyDatabase
---create table Pratice(sno int identity(1,1) primary key,sname char(500),age int);
insert into Pratice values('deena',17);

/*Select commands select column1,colunm2 from TableName*/
select sno,sname from Pratice;
select distinct sname from Pratice;
select *from Pratice where age>=18

---order clause select *from TableName order by ColunmName ASC|DESC
select *from Pratice order by sname DESC
select *from Pratice order by sname ASC,sno DESC;

---Logical operators And,or,Not
select *from Pratice where age>18 and sname like 'h%'
---like is used to return start letter with H%
select *from Pratice where age>18 or sname like 's%'
select *from Pratice where not age>18
select *from Pratice where not sname like 'H%'
---combination of and,or
select *from Pratice where age>=18 and (sname like 'h%' or sname like 'E%')

---insert operation
insert into Pratice (sname) values('santhosh')
insert into Pratice values('sam',26)

---update operation (update null value)
update Pratice set age  = 20,sname = 'pragadeesh' where sno = 9
update Pratice set sname = 'Prasanth' where sno = 12

---Delete operation
delete Pratice where sno = 11
select *from Pratice
---NULL Values(blank record)
select *from Pratice where age is null
select *from Pratice where age is not null

---Top,Limit-MSSql

select top 3 *from Pratice
select top 50 PERCENT *from Pratice

---aggegate Function min(),max(),count(),sum(),avg()

select min(age) as Minimum_Age from Pratice
select max(age) as Maximum_Age from Pratice
select count(*) as Total_Rows from Pratice
select count(age) as without_Null from Pratice
select count(distinct sname) as [without duplicate],sname from Pratice group by sname
select sum(age*10) as [Total sum] from Pratice
select avg(sno) as [Total sum // No.of.Elements]from Pratice

/*Alias(as) is used to give name for colunms if we use aggegate function
it returns only the answer without colunm name*/ 
--- if we use space between one and other word we can use array[]

---Like operator % ,_ start end contain 
select *from Pratice
--start 
select *from Pratice where sname like 'H%'
--end
select *from Pratice where sname like '%n'
--contain
select *from Pratice where sname like '%r%'
--start,end
select *from Pratice where sname like 'h%n'
--underscore To take praticular word
select *from Pratice where sname like 'j_ga_'
---start with s and that word contain atleast length 3
select *from Pratice where sname like 's%__'
---The second letter should start with a
select *from Pratice where sname like '_a%'
---return The word can start either j,h,c
select *from Pratice where sname like '[jhc]%'
---return word a-z
select *from Pratice where sname like '[a-f]%'

---In Between
use MyDatabase
select *from Pratice where sname in (select sname from Pratice_2)
select *from Pratice where sname not in (select sname from Pratice_2)
---between
select *from Pratice where age between 19 and 24
select *from Pratice where age between 18 and 22 and sno in (1,2,3)

---Alias
use MyDatabase
select * from Pratice_2 as P2 where P2.id in (1,2,3,4)

/*Joins (combine rows from two or more tables based on one related colunms)
inner join,left join,right join,full join
*/

---Inner Join (select common values)
select *from Pratice inner join Pratice_2 on Pratice.sname =Pratice_2.sname

---Left Join(select all record from left table common record from right)
select Pratice.sname,Pratice.age,Pratice_2.sname,Pratice_2.Age from Pratice left Join Pratice_2 on Pratice.sname = Pratice_2.sname

---Right Join(select all record from Right table common record from lrft)
---using Alias as TableName
select P2.sname,P2.Age,P1.sname,P1.age from Pratice as P1 right Join Pratice_2 as P2 on P1.sname = P2.sname


---Full Join (select all record from Both Tables.order goes from left to right)
select *from Pratice_2 full join Pratice on Pratice.sname = Pratice_2.sname
select *from Pratice full join Pratice_2 on Pratice.sname = Pratice_2.sname

---Using More Than One table
select*from ((Pratice inner join Pratice_2 on Pratice.sname = Pratice_2.sname)inner join Pratice_3 on Pratice.sname = Pratice_3.sname) 

---union union all(combine two select statement)
--rules:only use same colunms and same data type
select sname from Pratice_2 union select sname from Pratice_3
select sname from Pratice_2 union all select sname from Pratice_3
select 'Pratice_2' as Type ,sname from Pratice_2 union select 'Pratice_3',sname from Pratice_3

---group by (combine same no of rows like 'find the number of sname in Pratice table') 
select *from Pratice
select count(sno) from Pratice as [count of names]
select count(sno) as [count of names],sname from Pratice group by sname

---having clause(it is used with group by clause)having==where we cannot use where either in group by and aggregate functions
select count(sno) as [Having],sname from Pratice group by sname having count(sno)>=2

---exists
use MyDatabase
select id,sname from Pratice_2 where exists(select ID,sname from Pratice_3 where Pratice_2.sname = Pratice_3.sname)
---Any,all
select sname from Pratice_2 where sname = any (select sname from Pratice)
---All
select sname from Pratice_2 where sname = all (select sname from Pratice where sname like 's%')

---select into(copies the table into newtable)
select *into Customer from Pratice_2
select *from Customer
select *into NewTable from Pratice_3 where 1=0
select *from NewTable

---case(if the first condition is true it return the value)
select id,sname,Age,
case
when Age<=20 then 'Your Age in under 20'
else 'Your Age is above 20'
end as Test from Pratice_2;

---stored Procedure
create procedure 
selecttable 
as select *from Pratice 
go;

exec selecttable

create procedure Tablee @sname nvarchar(30) as select *from Pratice where sname=@sname 
exec Tablee @sname='Hemanth'

create procedure T as select *from Pratice where sname like 'h%'
exec T

---alter 

alter table Customer Add Phone int
---Add new column it stores null values
alter table Customer Drop column Phone
---Drop column delete the column
exec sp_rename 'Customer.Age','Age_of_Std','column'
---sp_rename rename the column name
select *from Customer



select distinct(Age) from Customer
select *from Customer order by Age Desc
select * from Customer where sname like '%h%' and Age>=20
select *from Customer where sname like 'h%' or Age>=20
select *from Customer where not sname like '%h%'

select *from Pratice where age is null
select top 50 percent *from Pratice