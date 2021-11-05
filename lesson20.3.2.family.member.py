family_member = {
    "name": "Jane",
    "surname": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "name": "Alice",
            "age": 6
        },
        {
            "name": "Bob",
            "age": 8
        }
    ]
}
# Noname
# print(family_member.get('children')[1].get('name'))
if family_member.get('children')[1].get('name') == "Bob":
    print(family_member.get('children')[1].get('name'))
if family_member.get('children')[1].get('name') != "Rob":
    print('Noname')
print(family_member.get('children', {})[1].get('name', {}) == "Rob")
