# Import library
import qrcode

# Data to be encoded
data = 'https://www.linkedin.com/in/herilshah/'# Write the information or your website

# Encoding data using make() function
img = qrcode.make(data)

#Saving as an image
img.save('MyQRCode1.png')