import os
os.system("pip install pyqrcode && pip install pypng")
import pyqrcode
import png

site = "htttp://www.learnwithdeveshsharma.blogspot.com"

qr_code = pyqrcode.create(site)
qr_code.png("qr_code.png")
