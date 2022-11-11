messages = {
    "hi" : "hello",
    "how are you" : "fine",
    "Day today?" : "Monday"
}

#get reply from messages dict without if else
def bot(key):
    
    key = key.strip()
    if key.lower() in messages:
        key  = key.lower()
        print(messages[key])
    elif key.upper() in messages:
        key  = key.upper()
        print(messages[key])
    elif key in messages:
        print(messages[key])
    else:
        print("Sorry i couldn't understand you")
        
bot(" Hi ")  #hello
bot("Day today?")   #Monday
bot("who are you")   #Sorry i couldn't understand you