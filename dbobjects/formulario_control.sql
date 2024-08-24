DROP TABLE formulario_control_center;

CREATE TABLE formulario_control_center (
  form_control_id int NOT NULL AUTO_INCREMENT,
  form_control_user varchar(500) DEFAULT NULL,
  form_control_idx int DEFAULT NULL,
  form_control_status varchar(255) DEFAULT NULL,
  form_control_descript varchar(2000) DEFAULT NULL,
  form_control_connection_cuidx varchar(255) DEFAULT NULL,
  form_control_oppenig varchar(2000) DEFAULT NULL,
  form_control_end varchar(2000) DEFAULT NULL,
  form_control_game varchar(255) DEFAULT NULL,
  form_control_game_type varchar(255) DEFAULT NULL,
  PRIMARY KEY (form_control_id)
);

/*
-- Query: select * from formulario_control_center
-- Date: 2024-07-23 14:24
*/
INSERT INTO  formulario_control_center (form_control_id,form_control_user,form_control_idx,form_control_status,form_control_descript,form_control_connection_cuidx,form_control_oppenig,form_control_end,form_control_game,form_control_game_type) VALUES (1,'admin',1,'valid','Configurações de Servidor - VRISING','v_rsing_server_config','<div class=\"mod-category\"><h3>Configurações de Servidor</h3><ul>','</ul></div>','vrising','server');
