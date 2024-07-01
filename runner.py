from users.User import User
from users.FreeUser import FreeUser
# from users.PremiumUser import PremiumUser

premium_user = User('robert', 'robert@mail.com')
print(premium_user.posts)
premium_user.add_post('first post')
print(premium_user.posts)


# free_user_bob = FreeUser('bob', 'bob@gmail.com')
# print(free_user_bob)
# free_user_bob.add_post('1st post')
# print(free_user_bob.posts)
# free_user_bob.add_post('2st post')
# print(free_user_bob.posts)
# free_user_bob.add_post('3st post')
# free_user_bob.deleting_post(1)
# print(free_user_bob.posts)
