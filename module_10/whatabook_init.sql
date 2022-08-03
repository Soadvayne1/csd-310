'''
Jeremy Johnson
8/3/2022
CYBR410
Assignment 10.3
'''

drop user 'whatabook_user'@'localhost';

create user 'whatabook_user'@'localhost' identified with mysql_native_password by 'MySQL8IsGreat!';

grant all privileges on whatabook.* to 'whatabook_user'@'localhost';

alter table wishlist drop foreign key fk_book;
alter table wishlist drop foreign key fk_user;

drop table if exists store;
drop table if exists book;
drop table if exists wishlist;
drop table if exists user;

create table store (
store_id int not null auto_increment,
locale varchar(500) not null, 
primary key(store_id)
);

create table book (
book_id int not null auto_increment,
book_name varchar(200) not null,
author varchar(200) not null,
details varchar(500) not null,
primary key (book_id)
);

create table user (
user_id int not null auto_increment,
first_name varchar(75) not null,
last_name varchar(75) not null,
primary key (user_id)
);

create table wishlist (
wishlist_id int not null auto_increment,
user_id int not null, 
book_id int not null,
primary key (wishlist_id),
constraint fk_book
foreign key (book_id)
	references book(book_id),
constraint fk_user
foreign key (user_id)
 	references user(user_id)
);

insert into store(locale)
 	values('72 Eileen Dr, Bloomfield Hills, MI 48302');

insert into book(book_name, author, details)
 	values('Book 3: Return of the Son of Book 2', 'H.G. Bookenstuff', 'The final chapter of the Book series.');

insert into book(book_name, author, details)
 	values('Book to the Footure', 'A. Penname', 'A bad Back to the Future parody.');

insert into book(book_name, author, details)
 	values('Almost Made Me Drop My Croissant: A Tragedy', 'O.H. Naw', 'The tale of a man who almost dropped his croissant.');

insert into book(book_name, author, details)
 	values('Tremors XIII', 'D. Hasselhoff', 'The book that keeps on...tremoring?.');

insert into book(book_name, author, details)
 	values('Vincent and the Pretty Big Strawberry', 'Judge Johanson', 'A pure infringement and James and the Giant Peach.');

insert into book(book_name, author, details)
 	values('Mario: The Rise and Fall of a Plumber', 'I.P. Freely', 'A tale of a plumber who went to far.');

insert into book(book_name, author, details)
 	values('Skulk Vs. Shor: Beginning of the Endgame', 'Not Stanley', 'A graphic novel where Skulk meets Shor in glorius battle.');

insert into book(book_name, author, details)
 	values('Gary Blotter and the Wizards Rock ', 'R.U. Serious', 'The first adventure in the magical Gary Blotter series.');

insert into book(book_name, author, details)
 	values('Animal Burial Ground', 'Esteban Emperor', 'A thrilling tale about a burial ground that makes zombies or something.');


insert into user(first_name, last_name)
 	values('Bob', 'Dobalina');

insert into user(first_name, last_name)
 	values('Screamin', 'Stephens');

insert into user(first_name, last_name)
 	values('Schmoozin', 'VanHoosen');

insert into wishlist(user_id, book_id)
 	values((select user_id from user where first_name = 'Bob'),(select book_id from book where book_name = 'Tremors XIII'));

insert into wishlist(user_id, book_id)
 	values((select user_id from user where first_name = 'Screamin'),(select book_id from book where book_name = 'Animal Burial Ground'));

insert into wishlist(user_id, book_id)
 	values((select user_id from user where first_name = 'Schmoozin'),(select book_id from book where book_name = 'Almost Made Me Drop My Croissant: A Tragedy'));
