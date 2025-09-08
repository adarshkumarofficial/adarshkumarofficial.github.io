import os

i=1
for file in os.listdir(os.getcwd()):
    if file.endswith(".jpg"):
        os.rename(file, f"{i}.jpg")
        i+=1