drop table if exists airlines;
create table airlines
(
    id int,
    name text,
    iata char(2),
    icao char(3),
    country text,
    active boolean,

    primary key (id)
);

drop table if exists airports;
create table airports
(
    id int,
    name text,
    city text,
    country text,
    iata char(3),
    icao char(4),
    latitude float,
    longitude float,

    primary key (id)
);

drop table if exists routes;
create table routes
(
    airline_id int,
    from_airport_id int,
    to_airport_id int,
    equipment char(3),

    primary key (airline_id, from_airport_id, to_airport_id)
);
