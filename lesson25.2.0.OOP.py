class User:
    user_name = 'Admin'
    password = 'Qwerty'
    is_banned = False


user_1 = User()  # Instance of the User class
user_2 = User()
user_2.user_name = 'Tom'
print(user_1.user_name, user_2.user_name)
User.user_name = 'Noname'
print(user_1.user_name, user_2.user_name)
