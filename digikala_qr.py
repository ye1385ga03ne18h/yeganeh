import qrcode

# لینک سایت دیجی‌کالا
link = "https://www.digikala.com"

# ساخت QR Code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

qr.add_data(link)
qr.make(fit=True)

# تبدیل QR Code به تصویر
img = qr.make_image(fill_color="black", back_color="white")

# ذخیره تصویر
img.save("digikala_qr.png")

print("QR Code created successfully!")
print("Saved as digikala_qr.png")
