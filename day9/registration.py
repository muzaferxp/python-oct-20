data = [
        {
           "username" : "user1",
           "password" : "password1"
           },
    ]

#create
def signUp(username , password):
    #create new user account
    data.append({
                "username" : username, 
                 "password": password
                })
    print("==========ACCOUNT CREATED SUCCESSFULLY:", username)


#read
def signIn(username, password):
    #read the data from database to check if the username and password is correct
    isUserFound = False
    
    for user in data:
        if user['username'] == username:
            if user['password'] == password:
                isUserFound = True
                print("==========LOGGED IN SUCCESSFULLY:", username)

                break
            
    return isUserFound
                

#update
def resetPassword(username, newPassword):    #or changePassword
    #updating the password of user
    print("==========RESET PASSWORD:", username)

    for user in data:
        if user['username'] == username:
            user['password'] = newPassword
            


#delete
def deleteAccount(username):
    #delete user account
    global data
    temp = []
    
    print("==========DELETING USER:", username)
    for user in data:
        if user['username'] != username:
            temp.append(user)
            
    data = temp
    print(data)
    