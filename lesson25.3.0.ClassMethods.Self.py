class User:
    user_name = 'Admin'
    password = 'Qwerty'
    is_banned = False
    friends = []

    def print_info(self):
        print('Name: {}\nPassword: {}\nBan status: {}'.format(
            self.user_name, self.password, self.is_banned
        ))


    def add_friend(self, friend):
        if isinstance(friend, User):
            self.friends.append(friend.user_name)
        else:
            self.friends.append(friend)


user_1 = User()  # Instance of the User class
user_2 = User()
user_2.user_name = 'Tom'
User.user_name = 'Noname'
user_1.print_info()
user_1.add_friend('Bob')
print(user_1.friends)
user_1.add_friend(user_2)
print(user_1.friends)
