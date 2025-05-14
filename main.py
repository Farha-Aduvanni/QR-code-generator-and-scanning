import streamlit as st
import qrcode
from io import BytesIO
#QR code generation function
def generate_qr_code(data):
    qr=qrcode.QRCode(version=3,box_size=8,border=4)
    qr.add_data(data)
    qr.make(fit=True)
    qr_img=qr.make_image(fill='black',back_color='white')

    buffer=BytesIO()
    qr_img.save(buffer,fromat='PNG')
    buffer.seek(0)
    return buffer
st.title("QR Code generation APP")
inp=st.text_input("Enter text or URL")
if st.button("Generate"):
    if inp:
        qr_image=generate_qr_code(inp)
        st.image(qr_image,caption="This is the generated qr code")
        st.download_button(label="Download",data=qr_image,file_name='qr_code.png',mime='image/png')
    else:
        st.warning("Please enter the input text")


    