INSERT INTO listas(
             id_usuario, titulo, data_insercao)
VALUES ( 
	 <dtml-sqlvar id_usuario type="int">,  <dtml-sqlvar titulo type="string">,  NOW());