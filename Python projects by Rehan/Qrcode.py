import qrcode
new  = qrcode.make("https://www.cricbuzz.com/")
new.save("cricbuzz.jpg")