site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_key(structure, key):
    if key in structure:
        return structure[key]
    for sub_structure in structure.values():
        if isinstance(sub_structure, dict):
            result = find_key(sub_structure, key)
            if result:
                break
    else:
        result = None
    return result


user_key = input('Какой ключ ищем?: ')
value = find_key(site, user_key)
if value:
    print(value)
else:
    print('Такого ключа в структуре сайта нет.')
