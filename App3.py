import streamlit as st
import fitz  # PyMuPDF

# Set up the title and instructions
st.title("PDF Content Viewer")
st.write("Upload a PDF file to extract and display its text content.")

# File uploader widget
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Open the uploaded PDF file
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        content = ""
        # Extract text from each page
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            content += page.get_text()

    # Display the extracted text
    if content.strip():
        st.text_area("PDF Content:", content, height=400)
    else:
        st.error("No readable text found in the PDF.")
