CREATE TABLE Book (
	id int primary key,
	title varchar,
	pages int,
	author varchar,
	price float
);

ALTER TABLE Book ADD COLUMN realease_year int