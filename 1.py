import qrcode

url="https://drive.google.com/file/d/1ydnuLvUlkFcjMt9HI7y9n2lnkT4PxP4M/view?usp=sharing"

qrcode.make(url).save("master.qrcode.png")

print("QR Code 已存成 qrcode.png")