text = input(">")

letters = {}
banned = ".,!@#$%^&*()-_+= "

for i in text:
    if i in banned:
        continue
    keys = letters.keys()
    if i not in keys:

        letters[i] = 1
    
    else:
        letters[i] += 1

print(letters)