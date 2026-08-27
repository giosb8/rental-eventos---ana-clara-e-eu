create table equipamento(
	id serial primary key,
	marca varchar (100)not null,
	modelo varchar(100) not null,
	categoria varchar(100) not null,
	potencial varchar(100) not null,
	material varchar(100) not null ,
	peso float not null,
	dimensoes decimal (10,2),
	cor varchar (100) not null,
	quantidade int not null
);

create table funcionario(
	id serial primary key,
	nome varchar(50)not null,
	email varchar(80)not null,
	senha varchar(50)not null
);

create table registro(
	id serial primary key,
	cliente_responsavel varchar(100),
	data_movimentacao timestamp not null,
	tipo_movimentacao varchar (100),
	quantidade int,
	funcionario_id int, foreign key (funcionario_id) references funcionario(id),
	equipamento_id int, foreign key (equipamento_id) references equipamento(id)
);