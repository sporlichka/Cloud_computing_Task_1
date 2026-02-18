
import pypdf
import os

pdf_path = r'c:\Users\Данис\Desktop\antigravity-task-1\Activ_Kcell_Formatted_RUS_FS_12m_2024_Consolidated_signed.pdf'
output_path = r'c:\Users\Данис\Desktop\antigravity-task-1\extracted_text.txt'

try:
    reader = pypdf.PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    
    print(f"Text extracted to {output_path}")

except Exception as e:
    print(f"Error extracting text: {e}")
