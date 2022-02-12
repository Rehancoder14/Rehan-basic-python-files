words = ["donkey","idiot", "stupid","crazy", "unworthymoron"]
with open("rs.txt", "r") as f:
    content = f.read()



for word in words:
    content1 = content.replace("donkey","#$%#$#$")
    with open("rs.txt", "w") as f:
        f.write(content1)



