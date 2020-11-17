from instabot import Bot
from time import sleep
import user_id_pass

bot = Bot()
bot.login(username=user_id_pass.USERNAME, password=user_id_pass.PASSWORD)
non_followers = set(bot.following) - set(bot.followers)

# Fetches only around 99 IDs or until the max no. of requests is reached.
def list_of_non_followers():
  i=0
  for user_id in non_followers:
    print("{} : {}".format(i, bot.get_username_from_user_id(user_id)))
    i+=1

# YT Video method to unfollow non_followers.
def unfollow_unfollowers():
  i=0
  for non_follower in non_followers:
    if i==50:
      break
    try:
      bot.unfollow(non_follower)
      sleep(2)
      i+=1
    except Exception as e:
      print(e)
      sleep(4)

# List of exceptions - Stuo.in
list_of_exceptions = []

# My function to unfollow non followers except some exceptions (celebs or other accounts).
def unfollow_them():
  people_to_unfollow = non_followers - set(list_of_exceptions)
  if len(people_to_unfollow) >=70:
    print("\n**********\nInstagram unfollow limit exceeded, so halting the request else your ID can be banned.\n**********\n")
  else:
    try:
      bot.unfollow_users(people_to_unfollow)
    except Exception as e:
      print(e)
      print("\n**********\nSome error occurred. Please retry after sometime.\n**********\n")


# ********** All function calls **********
list_of_non_followers()
# unfollow_them()


# Update for the above code :-
# using unfollow_them() function blocks the unfollow action on IG after 16 unfollows although enough time (around 1.5 hrs) was given to the code.
