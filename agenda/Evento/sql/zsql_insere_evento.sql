INSERT INTO eventos(
            id_lista, titulo_evento, data_inicio, data_fim, hora_inicio, 
            hora_fim, descricao, stamp, prioridade, id_usuario_criador, local_evento)
    VALUES (
    <dtml-sqlvar id_lista type="int">,
    <dtml-sqlvar titulo_evento type="string">,
    <dtml-sqlvar data_inicio type="string">,
    <dtml-sqlvar data_fim type="string">,
    '00:00:00','00:00:00',
    <dtml-sqlvar descricao type="string">,
    NOW(),
    <dtml-sqlvar prioridade type="int">,
    <dtml-sqlvar id_usuario_criador type="int">,
    <dtml-sqlvar local_evento type="string">);
