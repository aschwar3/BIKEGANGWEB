drop table if exists entries;
create table entries (
    id integer primary key autoincrement,
    checked_out timestamp not null,
    checked_in timestamp not null,
    home_loc text not null,
    is_in boolean not null
);