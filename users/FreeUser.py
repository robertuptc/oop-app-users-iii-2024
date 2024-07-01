from users.User import User

class FreeUser(User):

    def __init__(self, name, email):
        super().__init__(name, email)
        # User.posts[self.name] = [post]


    def add_post(self, message):
        if len((User.posts[self.name])) == 2:
            print("You have exceeded the post limit")
        else:
            if self.name in User.posts.keys():
                User.posts[self.name].append(message)
            else:
                User.posts[self.name] = [message]