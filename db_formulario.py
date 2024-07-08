from db_connection import FormularioTemplate
from markupsafe import Markup

def creat_form_line (user, game, type):
    formulario = {}
    form = FormularioTemplate.query.filter_by(form_user=user, form_game=game, form_game_type=type).order_by(FormularioTemplate.form_id).all()
    for row in form:
        line = f'<{row.form_type} '
        if row.form_name != None:
            line = f'{line} name={row.form_name} '
        if row.form_class != None:
            line = f'{line} class={row.form_class} '
        if row.form_value != None:
            line = f'{line} value="{row.form_value}" '
        
        line=f'{line}>'
        if row.form_descript != None:
            line = f'{line}{row.form_descript}'
        if row.form_end != None:
            line = f'{line}<{row.form_end}>'

        formulario[row.form_id] = Markup(line)
        

    return(formulario)

def create_select_form(user,game,type,cuidx):
    formulario = {}
    form = FormularioTemplate.query.filter_by(form_user=user, form_game=game, form_game_type=type).order_by(FormularioTemplate.form_id).all()