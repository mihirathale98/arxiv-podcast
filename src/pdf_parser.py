import PyPDF2

def parse_pdf(pdf_file_path):

    content = ""
    try:
        with open(pdf_file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            print('Parsed PDF')
            for page in pdf_reader.pages:
                content += page.extract_text() 

        return content

    except FileNotFoundError:
        raise FileNotFoundError
    except Exception as e:
        raise e