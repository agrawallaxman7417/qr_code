import qrcode # type: ignore

data="https://www.youtube.com/watch?v=cKEf8H9cQGM&list=PLwO5-rumi8A4J7h4Fm92TEC00gfZUk7ls"

qr=qrcode.QRCode(version=1)
error_correction=qrcode.constants.ERROR_CORRECT_L,
box_size=10
boarder=4
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_colour="white")
img.save("qrcode_your_youtube.png")