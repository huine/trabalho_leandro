SELECT 
	id_evento, id_lista, titulo_evento, data_inicio, data_fim, hora_inicio, 
    	hora_fim, descricao, stamp, prioridade, id_usuario_criador, local_evento,
    	TO_CHAR(data_inicio,'DD/Mon/YY') AS data_inicio_form,
		TO_CHAR(data_fim,'DD/Mon/YY') AS data_fim_form,
		TO_CHAR(hora_inicio,'HH24:MI') AS hora_inicio_form,
		TO_CHAR(hora_fim,'HH24:MI') AS hora_fim_form	
    	
FROM 
  eventos
WHERE 

<dtml-if id_evento>
    id_evento = <dtml-sqlvar id_evento type="int">
</dtml-if>

<dtml-if id_lista>
    id_lista = <dtml-sqlvar id_lista type="int">
</dtml-if>

ORDER BY data_fim ASC;

