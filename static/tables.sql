
--create database family;

--use family;

create table member(
	id 			int(11) 		NOT NULL auto_increment primary key,
	name		varchar(100)	NOT NULL 			   ,--姓名
	create_time	date        						   ,--添加时间	
	isDelete	int   								   ,--是否被删除
	field1		varchar(100)						   ,--冗余字段
	field2		varchar(100)						   ,--冗余字段
	field3		varchar(100)						    --冗余字段
);

create table  fee_record(
	id  			int(11)			NOT NULL auto_increment primary key,
	fee        	 	DECIMAL(5,2)	NOT null 			   ,---消费金额	
	fee_type		INT(3)								   ,---消费类型	
	discription		varchar(500)	                       ,---消费描述
	member_id		INT(11)								   ,---支付成员ID
	consume_time	date  								   ,---消费时间
	create_time		date    							   ,---条目创建时间(入库时间)
	isFinish		int(2)								   ,--是否已经结算过	
	field1			varchar(100)						   ,---冗余字段
	field2			varchar(100)						   ,---冗余字段
	field3			varchar(100)							--冗余字段	

)

create table lottery(
	id 				int(11)			NOT NULL auto_increment	primary key,
	title			varchar(100)	NOT NULL,
	redball			varchar(100)	NOT null,
	blueball		varchar(100)	NOT NULL,
	lottery_date	varchar(100)			,
	create_time 	date 			

)