SELECT
    senha
FROM
    usuarios
WHERE
<dtml-if id_usuario>
    id_usuario = <dtml-sqlvar id_usuario type="int">
</dtml-if>
<dtml-if email>
    email LIKE <dtml-sqlvar email type="string">
</dtml-if>;
