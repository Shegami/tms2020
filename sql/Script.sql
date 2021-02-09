create table Book (
	id int primary key,
	title varchar,
	pages int,
	author varchar,
	price float
);

ALTER TABLE Book ADD COLUMN realease_year int

insert into Book (id, title, pages, author, price, realease_year) values 
(1, 'Matrix', 132, 'Richard', 752.5, 2009),
(2, 'Matrix Two', 133, 'Richard', 861, 2010),
(3, 'Matrix Three', 134, 'Richard', 932, 2011),
(4, 'Matrix Four', 135, 'Richard', 978.3, 2012),
(5, 'Matrix Five', 136, 'Richard', 1000, 2013);
