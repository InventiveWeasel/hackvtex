# import cv2 and pyzbar for qr read and decode
from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2

# Import QR Code library
import qrcode


class QRCodeManager:
    def __init__(self):
        self.qrCodeReader = qrcode.QRCode(
                            version = 1,
                            error_correction = qrcode.constants.ERROR_CORRECT_H,
                            box_size = 10,
                            border = 4,
                            )

    def createQR(description):
        # The data that you want to store

        # Add data
        qr.add_data(description)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image()

        # Save it somewhere, change the extension as needed:
        # img.save("image.png")
        # img.save("image.bmp")
        # img.save("image.jpeg")
        img.save("image.png")

    def decodeQR(self, im) : 
      # Find barcodes and QR codes
      decodedObjects = pyzbar.decode(im)
     
      # Print results
      for obj in decodedObjects:
        print('Type : ', obj.type)
        print('Data : ', obj.data,'\n')
         
      return decodedObjects
     
     
    # Display barcode and QR code location  
    def displayQR(self, im, decodedObjects):
     
      # Loop over all decoded objects
      for decodedObject in decodedObjects: 
        points = decodedObject.polygon
     
        # If the points do not form a quad, find convex hull
        if len(points) > 4 : 
          hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
          hull = list(map(tuple, np.squeeze(hull)))
        else : 
          hull = points;
         
        # Number of points in the convex hull
        n = len(hull)
     
        # Draw the convext hull
        for j in range(0,n):
          cv2.line(im, hull[j], hull[ (j+1) % n], (255,0,0), 3)
     
      # Display results 
      cv2.imshow("Results", im);
      cv2.waitKey(0);

    def readQR(self):
        cam = cv2.VideoCapture(0)
        cv2.namedWindow("test")
        img_counter = 0

        while True:
            ret, frame = cam.read()
            cv2.imshow("test", frame)
            if not ret:
                break
            k = cv2.waitKey(1)

            if k%256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k%256 == 32:
                # SPACE pressed
                img_name = "temp_qr.png".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                im = cv2.imread("temp_qr.png")
                dec = self.decodeQR(im)
                self.displayQR(im, dec)
                img_counter += 1
        cam.release()
        cv2.destroyAllWindows()
        
        return int(dec[0].data)


#10.11.3.45:8080/hackathon/index.php?codigo=1000
