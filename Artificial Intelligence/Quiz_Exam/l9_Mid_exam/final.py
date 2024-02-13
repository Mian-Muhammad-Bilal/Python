class User:
    user_friends = set()  # set other users (friends)

    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        print(f"User {self.user_name} is created successfully.\n")

    def display(self):
        print(
            f"Displaying the User information:\nUser id: {self.user_id} user name: {self.name_name} friends: {self.user_friends}")


class UserNetwork(User):
    def add_new_user(self, user_id, user_name, user_friends):
        User.__init__(self, user_id, user_name, user_friends)

    def add_connection(self):
        user1 = input(("Give the name of the user1:"))
        # user2=input(("Give the name of the user2:"))
        User.user_friends.append(user1)

    def Display(self):
        print(
            f"Displaying the User information:\nUser id: {User.user_id} user name: {User.name_name} friends: {User.user_friends}")


class UserAnalysis(User):
    def find_most_connected_users(self):
        usr = 0
        newusr = 1
        for users in range(len(User.user_friends)):
            if newusr < usr:
                usr = len(users.user_friends)
        return newusr

    def no_connection_user(self):
        newusr = 1
        for users in range(len(User.user_friends)):
            if newusr == 0:
                return newusr

    def store_analysis(self, analysis):

        with open('text.txt', 'a') as f:
            f.write(analysis)


class FriendRecommendation(User):
    def recommend_friend(self):
        for friends in User.user_friends:
            if friends in User.friends:
                rec = User.user_friends
                print("The recommendation is ", rec)


def mnue():
    print("1) Create User.")
    print("2) Create connection between Users.")
    print("3) Display User information.")
    print("4) Display entire network.")
    print("5) Find user with most friends/connections")
    print("6) Find user with zero friends/connections")
    print("7) Store the analysis")
    print("8) Give recommendations")
    print("9) Exit")


def main():
    mnue()

    choise = int(input('Select your option:'))

    if choise == 1:
        userid = input(("Enter user id:"))
        usrname = input(("Enter user name:"))
        user1 = UserNetwork(userid, usrname)
    elif choise == 2:
        user1.add_connection()

    # elif choise == 3:
    # elif choise == 4:
    # elif choise == 5:
    # elif choise == 6:
    # elif choise == 7:
    # elif choise == 8:
    # elif choise == 9:
    # else


if __name__ == '__main__':
    main()
