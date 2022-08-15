create database PLC;
use PLC;
create table horno(
	id mediumint not null auto_increment,
    status_encendido int not null,
    status_trabajando int not null,
    status_enfriamiento int not null,
    status_fail int not null,
    status_puerta int not null,
    temperatura_actual decimal(3,1) not null,
    temperatura_deseada decimal(3,1) not null,
    tipo_carga varchar(80) not null,
    tiempo_deseado decimal(100,1) not null,
    tiempo_actual decimal(100,1) not null,
    lote int not null,
    fecha_encendido varchar(100) not null,
    fecha_inicio varchar(100) not null,
    fecha_fin varchar(100) not null,
    fecha_enfriamiento varchar(100) not null,
    fecha_falla varchar(100),
    primary key(id)
    );
create table tendencias(
    id mediumint not null auto_increment,
    lote int not null,
    temperatura_actual decimal(3,1) not null,
    primary key(id)
);
create table alertas(
    id mediumint not null auto_increment,
    falla int not null,
    fecha_falla varchar(100),
    primary key(id)   
);