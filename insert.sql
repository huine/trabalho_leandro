-- insert usuarios
insert into usuarios (email,senha,id_tipo_usuario) values ('gabrielgisoldi@gmail.com','1e536bdb71098aa3e6fed796efcd890ac746cb6b',1),('rafael.zulli0@gmail.com','601f1889667efaebb33b8c12572835da3f027f78',1),('gabrielgisoldi@hotmail.com','7c4a8d09ca3762af61e59520943dc26494f8941b',3),('developers@agenda.com','f7c3bc1d808e04732adf679965ccc34ca7ae3441',2);

-- insert tipo_usuarios
insert into tipo_usuarios (descricao) values ('administrador'), ('grupo'), ('comum');

-- insert niveis prioridade
insert into nivel_prioridade (nivel) values ('Sem Urgencia'),('Razoavel'),('Urgente');
