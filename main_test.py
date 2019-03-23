from qrtest import QRCodeManager
from connections import ConnectionManager

DESC_SERVER_URL = "http://10.11.3.45:8080/hackathon/index.php"

man = QRCodeManager()
prodCode = man.readQR()
#im = cv2.imread("temp_qr.png")
#dec = man.decodeQR(im)
#man.displayQR(im, dec)
CM = ConnectionManager(DESC_SERVER_URL)
desc = CM.getDescription(prodCode)
print("descricao: "+ desc)