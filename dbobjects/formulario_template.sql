DROP TABLE formulario_template;

CREATE TABLE formulario_template (
  form_id int NOT NULL AUTO_INCREMENT,
  form_module_use varchar(500) DEFAULT NULL,
  form_cuidx varchar(255) DEFAULT NULL,
  form_idx int DEFAULT NULL,
  form_status varchar(255) DEFAULT NULL,
  form_descript varchar(2000) DEFAULT NULL,
  form_connection_cuidx varchar(255) DEFAULT NULL,
  form_type varchar(255) DEFAULT NULL,
  form_game varchar(255) DEFAULT NULL,
  form_game_type varchar(255) DEFAULT NULL,
  PRIMARY KEY (form_id)
);

/*
-- Query: select * from formulariotemplate
-- Date: 2024-07-23 13:53
*/
INSERT INTO  formulario_template(form_id,form_module_use,form_cuidx,form_idx,form_status,form_descript,form_connection_cuidx,form_type,form_game,form_game_type) VALUES (1,'v_rsing_server_config','formnameserver',1,'valid','Nome','lidifficultgame','list','vrising','game');
INSERT INTO  formulario_template(form_id,form_module_use,form_cuidx,form_idx,form_status,form_descript,form_connection_cuidx,form_type,form_game,form_game_type) VALUES (3,'v_rsing_server_config','formdescriptserver',1,'valid','Descrição','ligamemodetype','list','vrising','game');
INSERT INTO  formulario_template(form_id,form_module_use,form_cuidx,form_idx,form_status,form_descript,form_connection_cuidx,form_type,form_game,form_game_type) VALUES (4,'v_rsing_server_config','formplayernumserver',1,'valid','Numero Maximo de Players','licastledamagemode','list','vrising','game');
INSERT INTO  formulario_template(form_id,form_module_use,form_cuidx,form_idx,form_status,form_descript,form_connection_cuidx,form_type,form_game,form_game_type) VALUES (5,'v_rsing_server_config','formadminnumserver',1,'valid','Numero Maximo de ADM','liplayerdamagemode','list','vrising','game');
INSERT INTO  formulario_template(form_id,form_module_use,form_cuidx,form_idx,form_status,form_descript,form_connection_cuidx,form_type,form_game,form_game_type) VALUES (6,'v_rsing_server_config','formfpsserver',1,'valid','FPS do servidor','licastleheartdamagemode','list','vrising','game');
INSERT INTO  formulario_template(form_id,form_module_use,form_cuidx,form_idx,form_status,form_descript,form_connection_cuidx,form_type,form_game,form_game_type) VALUES (7,'v_rsing_server_config','formsavenameserver',1,'valid','Save Name','lideathcontainerpermission','list','vrising','game');

COMMIT;