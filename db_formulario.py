from db_connection import FormulariooptionTemplate,FormularioTemplate,FormularioSelectTemplate,FormulariolistTemplate,FormularioinputTemplate
from markupsafe import Markup

def creat_form_line (user, game, type):
    formulario = {}
    form = FormularioTemplate.query.filter_by(form_user=user, form_game=game, form_game_type=type).order_by(FormularioTemplate.form_idx).all()
    #form = FormularioTemplate.query.order_by(FormularioTemplate.form_idx).all()
    for row in form:
        if row.form_type == 'list':
            line = create_list_form(game,type,row.form_connection_cuidx)

        formulario[row.form_id] = Markup(line)

    return(formulario)

def create_list_form(game,type,cuidx):
    form = FormulariolistTemplate.query.filter_by(list_cuidx=cuidx, list_game=game, list_game_type=type, list_status='valid').order_by(FormulariolistTemplate.list_idx).all()
    list_line = ''
    for row in form:
        list_line = list_line + f'<li> '
        if row.list_descript != None:
           list_line = list_line + f'{row.list_descript} '

        if row.list_type_connection == 'select':
            list_line = list_line + create_select_form(game,type,row.list_connection_key)
        if row.list_type_connection == 'input':
            list_line = list_line + create_input_form(game,type,row.list_connection_key)
        if row.list_type_connection == 'barline':
            None
        
        list_line = list_line + f'</li>'
    
    return list_line


def create_select_form(game,type,list_connection_key):
    select_form = FormularioSelectTemplate.query.filter_by(select_cuidx=list_connection_key, select_game=game, select_game_type=type, select_status='valid').order_by(FormularioSelectTemplate.select_idx).all()
    line_select = ''
    for row in select_form:
        line_select = line_select + f'<select '
        if row.select_name != None:
            line_select = line_select + f'id="{row.select_name}" name="{row.select_name}" '
        if row.select_class != None:
            line_select = line_select + f'class="{row.select_class}" '
        if row.select_value != None:
            line_select = line_select + f'value="{row.select_value}" '
        if row.select_python_code != None:
            line_select = line_select + f'{row.select_python_code}'
        
        line_select = line_select + f'>'
        line_select = line_select + create_option_form(game,type,row.select_option_cuidx)
        line_select = line_select + f'</select>'
    
    return line_select


def create_option_form(game,type,option_cuidx):
    option_form = FormulariooptionTemplate.query.filter_by(option_cuidx=option_cuidx, option_game=game, option_game_type=type, option_status='valid').order_by(FormulariooptionTemplate.option_idx).all()
    line_option = ''
    for row in option_form:
        line_option = line_option + f'<option '

        if row.option_name != None:
            line_option = line_option + f'id="{row.option_name}" name="{row.option_name}" '
        if row.option_class != None:
            line_option = line_option + f'class="{row.option_class}" '
        if row.option_value != None:
            line_option = line_option + f'value="{row.option_value}" '
        if row.option_python_code != None:
            line_option = line_option + f'{row.option_python_code} '
        
        line_option = line_option + f'>'
        if row.option_descript != None:
            line_option = line_option + f'{row.option_descript}'

        line_option = line_option + f'</option>'

    return line_option

# https://clips.twitch.tv/PoisedBillowingWoodpeckerVoteYea-MOHjHVXRy4-Q6KO3

def create_input_form(game,type,list_connection_key):
    input_form = FormularioinputTemplate.query.filter_by(input_cuidx=list_connection_key, input_game=game, input_game_type=type, input_status='valid').order_by(FormularioinputTemplate.input_idx).all()
    for row in input_form:
        line_input = line_input + f'<input '
        if row.input_name != None:
            line_input = line_input + f'id="{row.input_name}" name="{row.input_name}" '
        
        if row.input_type is not None:
            line_input += f'type="{row.input_type}" '
    
        if row.input_value is not None:
            line_input += f'value="{row.input_value}" '
        
        if row.input_placeholder is not None:
            line_input += f'placeholder="{row.input_placeholder}" '
        
        if row.input_class is not None:
            line_input += f'class="{row.input_class}" '
        
        if row.input_id is not None:
            line_input += f'id="{row.input_id}" '
        
        if row.input_disabled is not None:
            line_input += 'disabled '
        
        if row.input_readonly is not None:
            line_input += 'readonly '
        
        if row.input_required is not None:
            line_input += 'required '
        
        if row.input_maxlength is not None:
            line_input += f'maxlength="{row.input_maxlength}" '
        
        if row.input_min is not None:
            line_input += f'min="{row.input_min}" '
        
        if row.input_max is not None:
            line_input += f'max="{row.input_max}" '
        
        if row.input_pattern is not None:
            line_input += f'pattern="{row.input_pattern}" '
        
        if row.input_size is not None:
            line_input += f'size="{row.input_size}" '
        
        if row.input_autocomplete is not None:
            line_input += f'autocomplete="{row.input_autocomplete}" '
        
        if row.input_autofocus is not None:
            line_input += 'autofocus '

        if row.input_onclick != None:
            line_input = line_input + f'onclick="{row.input_onclick}" '
        if row.input_python_code != None:
            line_input = line_input + f'{row.input_python_code} '
        if row.input_complement != None:
            line_input = line_input + f'{row.input_complement} '
        
        line_input = line_input + f'>'
    
    return line_input