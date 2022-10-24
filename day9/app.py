from registration import signUp, signIn, resetPassword, deleteAccount
from registration import data

signUp("test", "password")


print(signIn("test", "password"))

resetPassword("test", "new_password")

deleteAccount("user1")

