DROP TABLE formulario_option_template;

CREATE TABLE formulario_option_template (
    option_id int NOT NULL AUTO_INCREMENT,
    option_cuidx varchar(255) DEFAULT NULL,
    option_idx int DEFAULT NULL,
    option_status varchar(255) DEFAULT NULL,
    option_descript varchar(2000) DEFAULT NULL,
    option_value VARCHAR(255) DEFAULT NULL,
    option_text VARCHAR(255) DEFAULT NULL,
    option_disabled VARCHAR(255) DEFAULT NULL,
    option_selected VARCHAR(255) DEFAULT NULL,
    option_label VARCHAR(255) DEFAULT NULL,
    option_class VARCHAR(255) DEFAULT NULL,
    option_name VARCHAR(255) DEFAULT NULL,
    option_style VARCHAR(255) DEFAULT NULL,
    option_title VARCHAR(255) DEFAULT NULL,
    option_aria_label VARCHAR(255) DEFAULT NULL,
    option_aria_hidden VARCHAR(255) DEFAULT NULL,
    option_onclick varchar(2000) DEFAULT NULL,
    option_python_code varchar(2000) DEFAULT NULL,
    option_complement varchar(255) DEFAULT NULL,
    option_game varchar(255) DEFAULT NULL,
    option_game_type varchar(255) DEFAULT NULL,
    PRIMARY KEY (option_id)
);

/*
-- Query: select * from formulario_option_template
-- Date: 2024-08-07 21:10
*/
INSERT INTO formulario_option_template (option_id,option_cuidx,option_idx,option_status,option_descript,option_class,option_name,option_value,option_python_code,option_game,option_game_type) VALUES (1,'optiondifficultgame',1,'valid','Fácil',NULL,NULL,'Easy','{% if info.GameDifficulty == \"Easy\" %}selected{% endif %}','vrising','game');
INSERT INTO formulario_option_template (option_id,option_cuidx,option_idx,option_status,option_descript,option_class,option_name,option_value,option_python_code,option_game,option_game_type) VALUES (2,'optiondifficultgame',2,'valid','Normal',NULL,NULL,'Normal','{% if info.GameDifficulty == \"Normal\" %}selected{% endif %}','vrising','game');
INSERT INTO formulario_option_template (option_id,option_cuidx,option_idx,option_status,option_descript,option_class,option_name,option_value,option_python_code,option_game,option_game_type) VALUES (3,'optiondifficultgame',3,'valid','Dificil',NULL,NULL,'Hard','{% if info.GameDifficulty == \"Hard\" %}selected{% endif %}','vrising','game');
INSERT INTO formulario_option_template (option_id,option_cuidx,option_idx,option_status,option_descript,option_class,option_name,option_value,option_python_code,option_game,option_game_type) VALUES (4,'optiontypegame',1,'valid','PvE',NULL,NULL,'PvE','{% if info.GameModeType == \"PvE\" %}selected{% endif %}','vrising','game');
INSERT INTO formulario_option_template (option_id,option_cuidx,option_idx,option_status,option_descript,option_class,option_name,option_value,option_python_code,option_game,option_game_type) VALUES (5,'optiontypegame',2,'valid','PvP',NULL,NULL,'PvP','{% if info.GameModeType == \"PvP\" %}selected{% endif %}','vrising','game');
INSERT INTO formulario_option_template (option_id,option_cuidx,option_idx,option_status,option_descript,option_class,option_name,option_value,option_python_code,option_game,option_game_type) VALUES (6,'optiondamagecastle',1,'valid','Sempre',NULL,NULL,'Always','{% if info.CastleDamageMode == \"Always\" %}selected{% endif %}','vrising','game');
INSERT INTO formulario_option_template (option_id,option_cuidx,option_idx,option_status,option_descript,option_class,option_name,option_value,option_python_code,option_game,option_game_type) VALUES (7,'optiondamagecastle',2,'valid','Nunca',NULL,NULL,'Never','{% if info.CastleDamageMode == \"Never\" %}selected{% endif %}','vrising','game');
INSERT INTO formulario_option_template (option_id,option_cuidx,option_idx,option_status,option_descript,option_class,option_name,option_value,option_python_code,option_game,option_game_type) VALUES (8,'optiondamagecastle',3,'valid','Tempo Restrito',NULL,NULL,'TimeRestricted','{% if info.CastleDamageMode == \"TimeRestricted\" %}selected{% endif %}','vrising','game');
INSERT INTO formulario_option_template (option_id,option_cuidx,option_idx,option_status,option_descript,option_class,option_name,option_value,option_python_code,option_game,option_game_type) VALUES (9,'optiondamageplayer',1,'valid','Sempre',NULL,NULL,'Always','{% if info.PlayerDamageMode == \"Always\" %}selected{% endif %}','vrising','game');
INSERT INTO formulario_option_template (option_id,option_cuidx,option_idx,option_status,option_descript,option_class,option_name,option_value,option_python_code,option_game,option_game_type) VALUES (10,'optiondamageplayer',2,'valid','Tempo Restrito',NULL,NULL,'TimeRestricted','{% if info.PlayerDamageMode == \"TimeRestricted\" %}selected{% endif %}','vrising','game');
INSERT INTO formulario_option_template (option_id,option_cuidx,option_idx,option_status,option_descript,option_class,option_name,option_value,option_python_code,option_game,option_game_type) VALUES (11,'optioncastleheartdamagemode',1,'valid','Por Tempo',NULL,NULL,'CanBeDestroyedOnlyWhenDecaying','{% if info.CastleHeartDamageMode == \"CanBeDestroyedOnlyWhenDecaying\" %}selected{% endif %}','vrising','game');
INSERT INTO formulario_option_template (option_id,option_cuidx,option_idx,option_status,option_descript,option_class,option_name,option_value,option_python_code,option_game,option_game_type) VALUES (13,'optioncastleheartdamagemode',2,'valid','Por Players',NULL,NULL,'CanBeDestroyedByPlayers','{% if info.CastleHeartDamageMode == \"CanBeDestroyedByPlayers\" %}selected{% endif %}','vrising','game');
INSERT INTO formulario_option_template (option_id,option_cuidx,option_idx,option_status,option_descript,option_class,option_name,option_value,option_python_code,option_game,option_game_type) VALUES (14,'optioncastleheartdamagemode',3,'valid','Aprendido ou Destruido',NULL,NULL,'CanBeSeizedOrDestroyedByPlayers','{% if info.CastleHeartDamageMode == \"CanBeSeizedOrDestroyedByPlayers\" %}selected{% endif %}','vrising','game');
INSERT INTO formulario_option_template (option_id,option_cuidx,option_idx,option_status,option_descript,option_class,option_name,option_value,option_python_code,option_game,option_game_type) VALUES (15,'optiondeathcontainerpermission',1,'valid','Qualquer',NULL,NULL,'Anyone','{% if info.DeathContainerPermission == \"Anyone\" %}selected{% endif %}','vrising','game');
INSERT INTO formulario_option_template (option_id,option_cuidx,option_idx,option_status,option_descript,option_class,option_name,option_value,option_python_code,option_game,option_game_type) VALUES (16,'optiondeathcontainerpermission',2,'valid','Mebros do Clã',NULL,NULL,'ClanMembers','{% if info.DeathContainerPermission == \"ClanMembers\" %}selected{% endif %}','vrising','game');

commit;