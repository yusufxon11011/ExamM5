import threading
import pdfkit

def convert_to_pdf(url, html_filename, config):
    pdfkit.from_url(url, html_filename, configuration=config)

path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"

config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

threads = []

for i in range(1, 20):
    url = 'https://tilshunos.com/omonims/?page=2' + str(i)
    pdf_filename = "omonimlar/" + str(i) + ".pdf"
    operation = threading.Thread(target=convert_to_pdf, args=(url, pdf_filename, config))
    threads.append(operation)
    operation.start()

for operation in threads:
    operation.join()
