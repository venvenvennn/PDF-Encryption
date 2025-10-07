import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
import io

st.title("🔐 PDF Encryption App")

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])


# Enter password
password = st.text_input("Enter a password to encrypt the PDF", type="password")

# Encrypt and download
if uploaded_file and password:
    reader = PdfReader(uploaded_file)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt(password)

    # Save to buffer
    output_buffer = io.BytesIO()
    writer.write(output_buffer)
    output_buffer.seek(0)

    st.success("✅ PDF encrypted successfully!")

 
    st.download_button(
        label="📥 Download Encrypted PDF",
        data=output_buffer,
        file_name=uploaded_file.name,
        mime="application/pdf"

    )

    