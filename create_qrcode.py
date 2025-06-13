import qrcode

image = qrcode.make("https://docs.google.com/spreadsheets/d/1Cb3yKTzCae8Oq_3WMLXybHXyXRCzn7uvU5___jJjD3o/edit?gid=0#gid=0")
image.save("qrcode.png", "PNG")