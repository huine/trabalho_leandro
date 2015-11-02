UPDATE 
    usuarios
SET
    logado = FALSE,
    ip_login = NULL
WHERE
    id_usuario = <dtml-sqlvar id_usuario type="int">;
