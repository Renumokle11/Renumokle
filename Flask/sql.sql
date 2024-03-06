CREATE DATABASE IF NOT EXISTS geeklogin DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE geeklogin;
-- Table for storing personal details
 
CREATE TABLE IF NOT EXISTS personal_details(
    id int(11) NOT NULL AUTO_INCREMENT,
    username varchar(50) NOT NULL,
    password varchar(25) NOT NULL,
    email varchar(40) NOT NULL,
    name varchar(223),
    phone_number varchar(20) NOT NULL,
    emp_id varchar(20),
    emp_name varchar(100),
    company_name varchar(100),
    designation varchar(50),
    date_of_joining datetime,
    street varchar(100),
    society varchar(100),
    landmark varchar(100),
    city varchar(50),
    state varchar(50),
    pincode varchar(10),

    PRIMARY KEY (id)
); 
use geeklogin;

ALTER TABLE personal_details
MODIFY password VARCHAR(25) NOT NULL,
MODIFY email VARCHAR(40) NOT NULL ;
select * from personal_details;
use geeklogin;
SELECT * FROM  kyc_details;
 
 CREATE TABLE IF NOT EXISTS kyc_details(
    user_id int,
    adharcard_number varchar(20) NOT NULL,
    pancard_number varchar(20) NOT NULL,
    PRIMARY KEY (user_id),
    FOREIGN KEY (user_id) REFERENCES personal_details(id)
);

ALTER TABLE personal_details CHANGE phone_number phonenumber VARCHAR(20);





