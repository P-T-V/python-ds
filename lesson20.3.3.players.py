players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

team_a_members = [
    player['name']
    for player in players_dict.values()
    if player['team'] == 'A' and player['status'] == 'Rest'
]
print('Все члены команды из команды А, которые отдыхают:', team_a_members)

team_b_members = [
    player['name']
    for player in players_dict.values()
    if player['team'] == 'B' and player['status'] == 'Training'
]
print('Все члены команды из группы B, которые тренируются:', team_b_members)

team_c_members = [
    player['name']
    for player in players_dict.values()
    if player['team'] == 'C' and player['status'] == 'Travel'
]
print('Все члены команды из команды C, которые путешествуют:', team_c_members)
