

def greetUser(name, hour):
    if hour >= 4 and hour <= 12 :
        print("Hi Good morning, welcome", name)
    
    elif hour > 12 and hour < 16:
        print("Hi Good afternoon, welcome", name)
        
    elif hour > 16 and hour < 20:
        print("Hi Good evening, welcome", name)
        
    elif hour >= 20 or hour <= 4:
        print("Hi Good night, welcome", name)   
    
    
greetUser("Adam", 20)
    