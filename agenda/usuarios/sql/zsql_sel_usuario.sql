SELECT
    *
FROM
    usuarios
WHERE
<dtml-if email>
    email LIKE <dtml-sqlvar email type="int">
<dtml-else>
    id_usuario = <dtml-sqlvar id_usuario type="int">
</dtml-if>;
