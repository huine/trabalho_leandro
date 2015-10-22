--sequence id_usuario
CREATE SEQUENCE id_usuario_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 29000000
  START 4
  CACHE 1;
ALTER TABLE id_usuario_seq
  OWNER TO postgres;


--sequence tipo_usuario
CREATE SEQUENCE tipo_usuario_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 2900000
  START 3
  CACHE 1;
ALTER TABLE tipo_usuario_seq
  OWNER TO postgres;


-- sequence lista
CREATE SEQUENCE id_lista_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 2900000
  START 1
  CACHE 1;
ALTER TABLE id_lista_seq
  OWNER TO postgres;


--tabela tipo usuario
CREATE TABLE tipo_usuarios
(
  id_tipo_usuario integer NOT NULL DEFAULT nextval('tipo_usuario_seq'::regclass),
  descricao character varying(100),
  CONSTRAINT tipo_usuarios_pkey PRIMARY KEY (id_tipo_usuario)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE tipo_usuarios
  OWNER TO postgres;
GRANT ALL ON TABLE tipo_usuarios TO postgres;


-- tabela usuario
CREATE TABLE usuarios
(
  id_usuario integer NOT NULL DEFAULT nextval('id_usuario_seq'::regclass),
  email character varying(100) NOT NULL,
  senha character varying(40) NOT NULL,
  id_tipo_usuario smallint NOT NULL,
  data_insercao timestamp without time zone DEFAULT now(),
  CONSTRAINT usuarios_pkey PRIMARY KEY (id_usuario),
  CONSTRAINT tipo_usuario FOREIGN KEY (id_tipo_usuario)
      REFERENCES tipo_usuarios (id_tipo_usuario) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE usuarios
  OWNER TO postgres;
GRANT ALL ON TABLE usuarios TO postgres;



--tabela listas
CREATE TABLE listas
(
  id_lista integer NOT NULL DEFAULT nextval('id_lista_seq'::regclass),
  id_usuario integer NOT NULL,
  titulo character varying(200) NOT NULL,
  data_insercao timestamp without time zone DEFAULT now(),
  CONSTRAINT listas_pkey PRIMARY KEY (id_lista),
  CONSTRAINT id_usuario_fk FOREIGN KEY (id_usuario)
      REFERENCES usuarios (id_usuario) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE listas
  OWNER TO postgres;
GRANT ALL ON TABLE listas TO postgres;