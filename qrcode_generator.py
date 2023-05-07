import qrcode


def generate_qrcode(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color=(98, 229, 218))
    img.save(str(input('Enter file name: ')) + '.png')


text_to_qrcode = input('Enter text to convert: ')
generate_qrcode(text_to_qrcode)
