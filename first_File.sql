create database mca_b2;
use mca_b2;
select * from 50_startups;
CREATE TABLE DEPARTMENT (
 DID INT PRIMARY KEY ,
    DNAME VARCHAR(20)
);
INSERT INTO department VALUES
(1, 'DEVELOPER'),
(2, 'HR'),
(3, 'SALES'),
(4, 'FINANCE'),
(5, 'SUPPORT');

CREATE TABLE EMPLOYEE (
 EID INT PRIMARY KEY ,
    ENAME VARCHAR(20) NOT NULL ,
    SALARY INT CHECK(SALARY > 0 ),
    DESIGNATION VARCHAR(20) NOT NULL ,
    D_ID INT ,
 foreign key(D_ID) REFERENCES DEPARTMENT(DID)
    ON UPDATE CASCADE 
    ON DELETE CASCADE 
);

INSERT INTO employee VALUES
(1, 'VISHAKHA', 10000, 'DA', 1),
(2, 'CHITRALI', 40000, 'RECRUITER', 2),
(3, 'SAYALI', 100000, 'MARKETING', 3),
(4, 'HARSHDA', 20000, 'JAVA', 1),
(5, 'GAYATRI', 10000, 'EDITOR', 3),
(6, 'YASHSAVI', 40000, 'TESTER', 4),
(7, 'PRAVEEN', 80000, 'DA', 2),
(8, 'HARSH', 90000, 'BA', 4),
(9, 'SNEHAL', 25000, 'INTERN', NULL);

# Inner Join 
-- Emp name with department names. 
select e.EID , e.ENAME , d.DNAME from 
employee e inner join department d on 
e.D_ID = d.DID;

-- find emp with dname who is having salary less than 40k
select e.EID , e.ENAME,e.SALARY , d.DNAME from 
employee e inner join department d on 
e.D_ID = d.DID where salary < 40000;

#Left Join 
-- find emp with dname also find out the emp who doesnt belong to any dept.
select e.eid , e.ename,e.salary,d.dname from
employee e left join department d on 
e.d_id = d.did;

#self join => table gets connected with itself. 
-- find emp who is working in same dept 
select e1.eid,e1.ename,e1.DESIGNATION from employee e1 join 
employee e2 on e1.eid <> e2.eid and e1.DESIGNATION = e2.DESIGNATION 
order by e1.DESIGNATION;

#Sub-query 
-- maximum salary 
select max(salary) from employee; -- 100000

-- maximum salary with emp name,id etc.
select * from employee where
 salary = (select max(salary) from employee);
 
-- 2nd highest salaried emp 
select max(salary) from employee where
 salary < (select max(salary) from employee);

-- 3rd highest salaried emp 
select max(salary) from employee where
salary < (select max(salary) from employee where salary <
(select max(salary) from employee));



















CREATE TABLE Vehicle (
vehicle_id INT PRIMARY KEY,
vehicle_name VARCHAR(30),
price INT,
fuel_type VARCHAR(20),
color VARCHAR(20),
number_of_tyres INT
);

INSERT INTO Vehicle VALUES
(1, 'Honda City', 1200000, 'Petrol', 'White', 4),
(2, 'Swift', 800000, 'Petrol', 'Red', 4),
(3, 'Creta', 1500000, 'Diesel', 'Black', 4),
(4, 'Royal Enfield', 220000, 'Petrol', 'Black', 2),
(5, 'Activa', 90000, 'Petrol', 'Grey', 2),
(6, 'KTM Duke', 280000, 'Petrol', 'Orange', 2),
(7, 'Tata Truck', 2500000, 'Diesel', 'Blue', 10),
(8, 'Ashok Leyland Truck', 3000000, 'Diesel', 'White', 12),
(9, 'Volvo Bus', 4500000, 'Diesel', 'Red', 6),
(10, 'Mini Bus', 1800000, 'Diesel', 'Yellow', 6),
(11, 'Auto Rickshaw', 350000, 'CNG', 'Green', 3),
(12, 'Eeco Van', 600000, 'CNG', 'White', 4),
(13, 'Bolero', 1100000, 'Diesel', 'Silver', 4),
(14, 'Scorpio', 1600000, 'Diesel', 'Black', 4),
(15, 'BMW Car', 5500000, 'Petrol', 'Blue', 4),
(16, 'Audi Car', 6000000, 'Petrol', 'White', 4),
(17, 'Tractor', 900000, 'Diesel', 'Green', 4),
(18, 'School Bus', 3200000, 'Diesel', 'Yellow', 6),
(19, 'Pickup Truck', 1400000, 'Diesel', 'Grey', 4),
(20, 'Electric Car', 1800000, 'Electric', 'White', 4);
--  stored procedure 
-- by syntax 
-- delimiter //
-- create procedure sp1()
-- BEGIN
-- 	-- Query 
-- END //

-- delimiter ;

-- delimiter //
-- create procedure pro1()
-- begin
-- select * from vehicle;
-- select * from employee;
-- end //

-- delimiter ;

-- call pro1();
-- call auto_pro();
call in_para(5);
call in_para(1);

call out_para(@mprice);
select @mprice as max_price;
-- task1 : create a sp and calculate the count of cars by their fuel type.
 
-- count the no of cars by their colors. using inout parameter 
set @cnt = "grey";
call inout_para(@cnt);
select @cnt as total_count_by_colors;
 
-- CREATE DEFINER=`root`@`localhost` PROCEDURE `in_para`(in n int)
-- BEGIN
-- select * from vehicle limit n;
-- END

-- out para 
-- REATE DEFINER=`root`@`localhost` PROCEDURE `out_para`(out mprice int)
-- BEGIN
-- select max(price) into mprice from vehicle;
-- END

-- in out para 
-- CREATE DEFINER=`root`@`localhost` PROCEDURE `inout_para`(inout cnt varchar(20))
-- BEGIN
-- select count(vehicle_id) into cnt from vehicle where 
-- color = cnt;
-- END













