
import qrcode

# 連結
url = "https://drive.google.com/file/d/11bbmOJ1zPmRhQ_VW1rOpdCTxvLZ9vxez/view?usp=drive_link"

# 生成 QR Code
img = qrcode.make(url)

# 儲存圖片
img.save("qrcode.png")


