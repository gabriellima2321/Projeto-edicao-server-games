DROP TABLE formulario_ul_template;

CREATE TABLE formulario_ul_template (
    ul_id int NOT NULL AUTO_INCREMENT,
    ul_cuidx varchar(255) DEFAULT NULL,
    ul_idx int DEFAULT NULL, 
    ul_status varchar(255) DEFAULT NULL,
    ul_descript varchar(2000) DEFAULT NULL,
    ul_class VARCHAR(255) DEFAULT NULL,
    ul_style VARCHAR(255) DEFAULT NULL,
    ul_title VARCHAR(255) DEFAULT NULL,
    ul_dir VARCHAR(255) DEFAULT NULL,
    ul_lang VARCHAR(255) DEFAULT NULL,
    ul_role VARCHAR(255) DEFAULT NULL,
    ul_aria_label VARCHAR(255) DEFAULT NULL,
    ul_aria_hidden VARCHAR(255) DEFAULT NULL,
    ul_python_code varchar(2000) DEFAULT NULL,
    ul_complement varchar(255) DEFAULT NULL,
    ul_game varchar(255) DEFAULT NULL,
    ul_game_type varchar(255) DEFAULT NULL,
    PRIMARY KEY (ul_id)
);