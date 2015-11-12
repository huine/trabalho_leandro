SELECT id_lista, id_usuario, titulo, data_insercao
  FROM listas
  WHERE 
<dtml-if id_usuario>
    id_usuario = <dtml-sqlvar id_usuario type="int">
    <dtml-if id_lista>
    	AND
    </dtml-if>
</dtml-if>

<dtml-if id_lista>
    id_lista = <dtml-sqlvar id_lista type="int">
</dtml-if>;