import json


def get_all():
    with open('candidates.json', 'r') as candidates:
        return json.load(candidates)


def get_by_pk(pk):
    return get_all()[pk - 1]


def get_by_skill(skill_name):
    return [i for i in get_all() if skill_name.lower() in i['skills'].lower()]

def main_page(list_condidate):
    str_ = ''
    for i in range(len(list_condidate)):
        str_ +=  f'''
        Имя кандидата - {list_condidate[i]['name']}
        Позиция кандидата - {list_condidate[i]['position']}
        Навыки - {list_condidate[i]['skills']}
        '''
    return f'<pre>{str_}</pre>'

