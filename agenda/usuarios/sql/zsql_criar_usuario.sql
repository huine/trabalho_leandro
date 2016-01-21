INSERT INTO
    usuarios(email, senha, nome_usuario)
VALUES
    (
        <dtml-sqlvar email type="string">,
        <dtml-sqlvar senha type="string">,
        <dtml-sqlvar nome_usuario type="string">
    )
RETURNING id_usuario;
