-- insert usuarios
insert into usuarios (email,senha,id_tipo_usuario) values ('gabrielgisoldi@gmail.com','18500b9a277d16369248674d5be0e42babc09579:*:8974ff0bc1a34590a77c3b9ded083a2c',1),('rafael.zulli0@gmail.com','a01108b425643bc8e22ee7d3443909b61a613c5e:*:74755a9a7150484d8e00eba95ecc8d11',1),('gabrielgisoldi@hotmail.com','f61d7f4dac026b77c0a24c53656eff41b3e9c0fb:*:586fcb9f0fbb47d69d9fb88fe8b60ee0',3),('developers@agenda.com','270248772b3238d484e3e9a5ecc53f1d3c5485b0:*:9974ad50d264424e80d7e2467bc5045f',2);

-- insert tipo_usuarios
insert into tipo_usuarios (descricao) values ('administrador'), ('grupo'), ('comum');

-- insert niveis prioridade
insert into nivel_prioridade (nivel) values ('Sem Urgencia'),('Razoavel'),('Urgente');
