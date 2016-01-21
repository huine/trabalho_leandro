INSERT INTO
    info_usuario
    (
        id_usuario,
        sexo,
        dt_nascimento,
        uf,
        cidade,
        rua,
        numero,
        bairro,
        complemento
    )
VALUES
    (
        <dtml-sqlvar id_usuario type="int">,
        <dtml-sqlvar sexo type="int">,
        <dtml-sqlvar dt_nascimento type="string">,
        <dtml-sqlvar uf type="string">,
        <dtml-sqlvar cidade type="string">,
        <dtml-sqlvar rua type="string">,
        <dtml-sqlvar numero type="int">,
        <dtml-sqlvar bairro type="string">,
        <dtml-sqlvar complemento type="string">
    )
RETURNING 1 AS result;
