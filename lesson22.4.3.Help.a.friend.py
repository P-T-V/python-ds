# Если в списке встретился словарь, то оставляем его.
# Если в списке встретилась строка, то из неё нужно сделать словарь и положить его в итоговый список,
# например  “abc” → {“abc”: “abc”}.
# С числами нужно сделать то же самое, что и со строками.
# Всё остальное выкидываем из нашего списка

def create_dict(element, template=None):
    if isinstance(element, dict):
        return element
    if isinstance(element, int) or isinstance(element, float) or isinstance(element, str):
        template = dict()
        template[element] = element
    return template


def data_preparation(old_list):
    new_list = []
    for i_element in old_list:
        if create_dict(i_element):
            new_list.append(create_dict(i_element))
    return new_list


data = ['sad', {'sds': 23}, {43}, [12, 42, 1], 2323, 2.5]
data = data_preparation(data)
print(data)
