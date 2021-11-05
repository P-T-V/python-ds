data = dict()
# some activities before this string
print(data.get('server'))

data['server'] = {
    "host": "127.0.0.1",
    "port": "10"
}

# some activities before this string
if data.get('configuration', {}).get('ssh', {}).get('login', {}):
    print('Login already exists in the structure')
print(data.get('configuration', {}).get('ssh', {}).get('login', {}))

data['configuration'] = {
    'ssh': {
        'access': 'true',
        'login': 'Ivan',
        'password': 'qwerty'
    }
}
print()
print(data)
print(data['server']['port'])
data['configuration']['ssh']['login'] = 'Vova'
print(data['configuration']['ssh']['login'])
print()
for i_value in data.values():
    for j_key in i_value:
        print(j_key, i_value[j_key])
