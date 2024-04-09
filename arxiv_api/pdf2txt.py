import pdfplumber

name = "2404.02831v1.Empowering_Biomedical_Discovery_with_AI_Agents"
pdf_path = f"PDF/{name}.pdf"
txt_path = f"TXT/{name}.txt"
# Open the PDF file using pdfplumber
with pdfplumber.open(pdf_path) as pdf:
    full_text = ''
    # Iterate over each page in the PDF
    for page in pdf.pages:
        # Extract text from the current page
        text = page.extract_text()
        # Check if text was found on the page
        if text:
            # Append extracted text to the accumulator with a newline
            full_text += text + '\n'

# Write the accumulated text to a TXT file
with open(txt_path, 'w', encoding='utf-8') as txt_file:
    txt_file.write(full_text)