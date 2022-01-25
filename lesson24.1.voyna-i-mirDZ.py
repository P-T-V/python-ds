import zipfile
import collections


def unzip(archive):
    zfile = zipfile.ZipFile(archive, 'r')
    for i_file_name in zfile.namelist():
        zfile.extract(i_file_name)
    zfile.close()


def freq_sorted_dict(file_name):
    letters_dict = dict()
    if file_name.endswith('.zip'):
        unzip(file_name)
        file_name = ''.join((file_name[:-3], 'txt'))
    txt_file = open(file_name, 'r', encoding='utf-8')
    for i_line in txt_file:
        for j_symbol in i_line:
            if j_symbol.isalpha():
                if j_symbol not in letters_dict:  # Формируем словарь
                    letters_dict[j_symbol] = 0
                letters_dict[j_symbol] += 1
    sorted_values = sorted(letters_dict.values())
    sorted_dict = collections.OrderedDict()
    for i_value in sorted_values:
        for j_key in letters_dict.keys():
            if letters_dict[j_key] == i_value:
                sorted_dict[j_key] = letters_dict[j_key]
    txt_file.close()
    return sorted_dict


file_name = 'voyna-i-mir.zip'
stats = freq_sorted_dict(file_name)
print("+{:-^19}+".format('+'))
print("|{: ^9}|{: ^9}|".format('буква', 'частота'))
print("+{:-^19}+".format('+'))
for char, count in stats.items():
    print("|{: ^9}|{: ^9}|".format(char, count))
print("+{:-^19}+".format('+'))
