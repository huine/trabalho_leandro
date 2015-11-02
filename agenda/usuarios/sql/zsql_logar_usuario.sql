UPDATE 
    usuarios
SET
    logado = TRUE,
    ip_login = <dtml-sqlvar ip_login type="string">
WHERE
    id_usuario = <dtml-sqlvar id_usuario type="int">;

INSERT INTO
    login(ip_login, hash_login, id_usuario_login)
VALUES
    (<dtml-sqlvar ip_login type="string">, <dtml-sqlvar hash type="string">, <dtml-sqlvar id_usuario type="int">);
