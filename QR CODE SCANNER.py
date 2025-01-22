import qrcode
from PIL import Image


def generate_upi_qr(upi_id, recipient_name, file_prefix):
    try:
        
        upi_url = f'upi://pay?pa={upi_id}&pn={recipient_name}'

    
        qr = qrcode.QRCode(
            version=1,  
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(upi_url)
        qr.make(fit=True)

     
        qr_img = qr.make_image(fill_color="black", back_color="white")
        file_name = f"{file_prefix}_qr.png"
        qr_img.save(file_name)
        print(f"{file_prefix.capitalize()} QR code saved as {file_name}")

        qr_img.show()

    except Exception as e:
        print(f"Error generating QR code for {file_prefix}: {e}")

# Taking UPI ID and recipient name as input
upi_id = "example@upi"  # Replace with a valid UPI ID
recipient_name = "John Doe"  # Replace with a recipient name


if not upi_id or not recipient_name:
    print("UPI ID and recipient name are required!")
else:
    #  To Generate QR codes for different payment apps
    generate_upi_qr(upi_id, recipient_name, "phonepe")
    generate_upi_qr(upi_id, recipient_name, "paytm")
    generate_upi_qr(upi_id, recipient_name, "google_pay")
