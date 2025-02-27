import qrcode


# Give the data
data='I am sudarshan khatri'

#create the qrcode
img=qrcode.make(data)

img.save('Projects\myqr.png')


