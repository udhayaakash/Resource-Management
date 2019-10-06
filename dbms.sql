create database dbms_pro;
use dbms_pro;


create table DATE7(date_id varchar(20) NOT NULL,start_date date,end_date date,primary key(date_id));

create table NAME7(name_id varchar(20),first_name varchar(20),last_name varchar(20),primary key(name_id));

create table CONTACT7(c_id varchar(20),phone1 numeric(10,0),phone2 numeric(10,0),emailid varchar(20),primary key(c_id));

create table PROJECT7(p_id varchar(20),proj_name varchar(20),priority numeric(3,0),date_id varchar(20),total_skill varchar(20),primary key(p_id),foreign key(date_id) references DATE7(date_id));

create table RESOURCE7(r_id varchar(20),reso_name varchar(20),quantity numeric(10,0),primary key(r_id));

create table employee(eid varchar(20),pid varchar(20),rid varchar(20),name_id varchar(20),c_id varchar(20),dob date,
doj date,city varchar(20),skill varchar(20),reso_needed varchar(20),available numeric(1,0),primary key(eid),foreign key(pid) references PROJECT7(p_id), foreign key(rid) references 
RESOURCE7(r_id),foreign key(name_id) references NAME7(name_id), foreign key(c_id) references CONTACT7(c_id));


insert into employee values('4',null,null,'n4','c4','1992-10-12','2014-10-03','mumbai','10','arduino_board',5);

