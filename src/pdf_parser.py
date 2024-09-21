import PyPDF2

def parse_pdf(pdf_file_path):

    content = {}
    try:
        with open(pdf_file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            print('Parsed PDF')
            for i, page in enumerate(pdf_reader.pages):
                content[i] = {'page_text': page.extract_text()}
        return content

    except FileNotFoundError:
        raise FileNotFoundError
    except Exception as e:
        raise e