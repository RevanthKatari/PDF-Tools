import os
from PyPDF2 import PdfMerger
import streamlit as st

def combine_pdfs(root_folder):
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)
        
        # Check if the item in the root folder is a directory
        if os.path.isdir(folder_path):
            pdf_files = [file for file in os.listdir(folder_path) if file.endswith('.pdf')]
            
            # Sort PDF files by name or modification time
            pdf_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))
            
            if pdf_files:
                merger = PdfMerger()
                for pdf_file in pdf_files:
                    pdf_file_path = os.path.join(folder_path, pdf_file)
                    merger.append(pdf_file_path)
                
                # Combine PDFs
                output_pdf_name = f"{folder_name}.pdf"
                output_pdf_path = os.path.join(root_folder, output_pdf_name)
                merger.write(output_pdf_path)
                merger.close()
                st.write(f"Combined PDF created for {folder_name}")

# Streamlit UI
st.title("PDF Merger Web App")
root_folder = st.text_input("Enter the root folder path:")

if st.button("Combine PDFs"):
    if os.path.exists(root_folder):
        combine_pdfs(root_folder)
        st.success("PDFs combined successfully!")
    else:
        st.error("Invalid folder path. Please enter a valid path.")
