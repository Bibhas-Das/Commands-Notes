import sys
import qrcode
from PIL import Image

def generate_qr_code(text):
    # Create a QR Code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1 is the smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # Size of each box in the QR code grid
        border=4,  # Thickness of the border (minimum is 4)
    )
    qr.add_data(text)
    qr.make(fit=True)

    # Generate the image
    image = qr.make_image(fill_color="black", back_color="white")
    return image

def main():
    # Check for command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <text>")
        sys.exit(1)

    text = sys.argv[1]

    # Generate and display the QR code
    image = generate_qr_code(text)
    image.show()

if __name__ == "__main__":
    main()
